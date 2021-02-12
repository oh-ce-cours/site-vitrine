module.exports = {
    plugins: {
        // 'cssnano': {
        //     preset: 'default',
        // },
        '@fullhuman/postcss-purgecss': {
            content: ['./themes/**/*.html', './themes/**/*.js'],
            whitelist: ["flex-control-nav", "flex-control-paging", "fslider",]
        },
    }
};