import mammoth
from bs4 import BeautifulSoup
import pprint
from yaml import load, dump

SEP = " " * 4


def get_city_image(city):
    city = city.capitalize()
    images = {
        "Lyon": "/imgs/photos/villes/lyon3.jpg",
        "Lille": "/imgs/photos/villes/lille.jpg",
        "Paris": "/imgs/photos/villes/paris3.jpg",
    }
    if city not in images:
        print(f"{SEP*2}Unknown city: {city}")
    return images.get(city, "")


class Node:
    def __init__(self, title=None):
        self.title = title
        self.content = None
        self.children = []

    def add_child(self, title):
        self.children.append(Node(title))

    def get_child(self, title):
        for c in self.children:
            if c.title == title:
                return c

        print(f"{SEP}unknown child: {title}")
        return Node()

    def add_content(self, element):
        if element.name in ("h1", "h2", "h3", "p"):
            self.content = element.text
        elif element.name == "ul":
            self.content = [e.text for e in element.children]
        else:
            raise TypeError(f"unknown name: {element.name}")

    def __hash__(self):
        return hash(self.title)

    def __iter__(self):
        yield from self.children

    def __repr__(self):
        children = ""
        if self.children:
            children = f"> {self.children}"
        return f"\n{self.title}: {self.content} {children}"


def parse_file(fname):
    tree = Node()
    last_h1 = None
    last_h2 = None
    last_h3 = None

    with open(fname, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value  # The generated HTML
        messages = result.messages  # Any messages, such as warnings during conversion
        soup = BeautifulSoup(html, "html.parser")

        for element in soup:
            if element.name == "h1":
                last_h1 = element.text
                last_h2, last_h3 = None, None
                tree.add_child(element.text)
                continue
            if element.name == "h2":
                last_h2 = element.text
                last_h3 = None
                tree.get_child(last_h1).add_child(element.text)
            if element.name == "h3":
                last_h3 = element.text
                tree.get_child(last_h1).get_child(last_h2).add_child(element.text)

            if last_h3:
                if element.name == "p":
                    tree.get_child(last_h1).get_child(last_h2).add_child("free_text")
                    tree.get_child(last_h1).get_child(last_h2).get_child(
                        "free_text"
                    ).add_content(element)

                else:
                    tree.get_child(last_h1).get_child(last_h2).get_child(
                        last_h3
                    ).add_content(element)
            elif last_h2:
                tree.get_child(last_h1).get_child(last_h2).add_content(element)
            elif last_h1:
                tree.get_child(last_h1).add_content(element)
            else:
                print(f"{SEP}???")
    return tree


def prepare_output_programme(tree):
    sections = []
    for section in tree.get_child("Plan de formation / programme"):
        free_text = ""
        elements = []
        for element in section:
            subelements = []
            if isinstance(element.content, list):
                for subelement in element.content:
                    subelements.append(subelement)
            if element.title == "free_text":
                free_text = element.content
                continue

            res = {"title": element.title}
            if subelements:
                res["subelements"] = subelements
            elements.append(res)
        res = {"title": section.title, "elements": elements}
        if free_text:
            res["free_text"] = free_text
        sections.append(res)
    return sections


def prepare_output_title(tree):
    key = "Titre"
    return tree.get_child(key).content


def prepare_output_description(tree):
    key = "Description (10 lignes max)"
    return tree.get_child(key).content


def prepare_output_identifier(tree):
    key = "Identifiant technique"
    return tree.get_child(key).content


def prepare_output_domaines(tree):
    key = "Domaine"
    return tree.get_child(key).content


def prepare_output_subdomain(tree):
    key = "Sous-domaine"
    return tree.get_child(key).content


def prepare_output_url(tree):
    key = "Url"
    return tree.get_child(key).content


def prepare_output_weight(tree):
    key = "Ordre dans la page"
    return tree.get_child(key).content


def prepare_output_catchphrase(tree):
    key = "Catch phrase (2 lignes max)"
    return tree.get_child(key).content


def prepare_output_duration(tree):
    key = "Durée"
    return tree.get_child(key).content


def prepare_output_equilibre(tree):
    key = "Équilibre théorie / pratique"
    return tree.get_child(key).content


def prepare_output_pricing(tree):
    key = "Tarifs"
    return tree.get_child(key).content


def prepare_output_objectifs(tree):
    key = "Objectifs pédagogiques"
    return tree.get_child(key).content


def prepare_output_prerequis(tree):
    key = "Prérequis"
    content = tree.get_child(key).content
    if isinstance(content, str):
        content = [content]
    return content


def prepare_output_publics(tree):
    key = "Public visé / participants"
    return tree.get_child(key).content


def prepare_output_sessions(tree):
    key = "Prochaines sessions"
    sessions = []
    for session in tree.get_child(key).children:
        sessions.append(
            {
                "city": session.title,
                "date": session.content,
                "image": get_city_image(session.title),
            }
        )
    return sessions


def preprare_output_draft(tree):
    key = "Contenu validé"
    content = tree.get_child(key).content
    return content not in ("oui", "Oui")


def prepare_output(tree, fname_output):
    frontmatter_data = {
        "title": prepare_output_title(tree),
        "draft": preprare_output_draft(tree),
        "identifier": prepare_output_identifier(tree),
        "domaines": prepare_output_domaines(tree),
        "subdomain": prepare_output_subdomain(tree),
        "url": prepare_output_url(tree),
        "weight": prepare_output_weight(tree),
        "catchphrase": prepare_output_catchphrase(tree),
        "duration": prepare_output_duration(tree),
        "equilibre": prepare_output_equilibre(tree),
        "pricing": prepare_output_pricing(tree),
        "objectifs": prepare_output_objectifs(tree),
        "prerequis": prepare_output_prerequis(tree),
        "publics": prepare_output_publics(tree),
        "programme": prepare_output_programme(tree),
        "sessions": prepare_output_sessions(tree),
    }
    description = prepare_output_description(tree)

    content_file = open(fname_output, "w")
    frontmatter = dump(
        frontmatter_data,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    content_file.write(f"---\n{frontmatter}\n---\n\n{description}\n")


def convert_all():
    names = [
        (
            "./content_google_doc/datascience/01_SQL Pratique.docx",
            "./content/formations/datascience/sql_pratique.md",
        ),
        (
            "./content_google_doc/developpement/01_Initiation à la Programmation avec Python .docx",
            "./content/formations/developpement/python/python_debutant.md",
        ),
        (
            "./content_google_doc/developpement/02_Python objet.docx",
            "./content/formations/developpement/python/python_objet.md",
        ),
        (
            "./content_google_doc/developpement/03_Python avancé.docx",
            "./content/formations/developpement/python/python_avance.md",
        ),
        (
            "./content_google_doc/developpement/04_Python idiomatique.docx",
            "./content/formations/developpement/python/python_idiomatique.md",
        ),
        (
            "./content_google_doc/developpement/05_Programmation concurrente en python.docx",
            "./content/formations/developpement/python/python_concurrence.md",
        ),
        (
            "./content_google_doc/developpement/06_Clean code en Python et gestion de code legacy.docx",
            "./content/formations/developpement/python/python_clean_code.md",
        ),
        (
            "./content_google_doc/developpement/07_Distribuer son code python.docx",
            "./content/formations/developpement/python/python_distribution.md",
        ),
    ]

    identifiers = []
    for input, output in names:
        print(f"Converting {input.split('/')[-1]} -> {output.split('/')[-1]}")
        tree = parse_file(input)
        identifiers.append(prepare_output_identifier(tree))
        prepare_output(tree, output)
        print(f"done")
    print(identifiers)


if __name__ == "__main__":
    convert_all()
