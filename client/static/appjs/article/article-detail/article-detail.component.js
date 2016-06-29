/**
 * Created by chirath on 6/21/16.
 */

angular.module('phoneDetail').component('articleDetail', {
    templateUrl: 'static/appjs/article/article-detail/article-detail.template.html',
    controller: ['$routeParams', 'Article',
        function ArticleDetailController($routeParams, Article) {
            var self = this;


            self.article = Article.get({articleId: $routeParams.articleId}, function(article) {

            });
    }]
});
