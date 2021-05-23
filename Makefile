GDOC_FOLDER=./content_google_doc

all: sync-google-drive convert runserver

runserver: clean
	hugo server -d out

clean:
	rm -rf out 

sync-google-drive:
	rclone copy remote:OhCeCours/Formations/datascience ${GDOC_FOLDER}/datascience --drive-export-formats docx
	rclone copy remote:OhCeCours/Formations/developpement ${GDOC_FOLDER}/developpement --drive-export-formats docx
	rclone copy remote:OhCeCours/Formations/devops ${GDOC_FOLDER}/devops --drive-export-formats docx

convert:
	python converter.py