/**
 * Created by chirath on 6/19/16.
 */

angular.module('articleList').component('articleList', {
    templateUrl: 'static/appjs/article/article-list/article-list.template.html',
    controller: ['Article',
        function ArticleListController(Article) {
            this.article = Article.query();
        }
    ]
});
