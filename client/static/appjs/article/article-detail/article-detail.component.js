/**
 * Created by chirath on 6/21/16.
 */

angular.module('hackademicApp').component('articleDetail', {
    templateUrl: 'static/appjs/article/article-detail/article-detail.template.html',
    controller: ['$http', '$routeParams',
        function articleDetailController($http, $routeParams) {
            var self = this;

            $http.get('/article/' + $routeParams.articleId + '.json').then(function(response) {
                self.article = response.data;
            });
    }]
});