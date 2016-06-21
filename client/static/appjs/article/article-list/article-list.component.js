/**
 * Created by chirath on 6/19/16.
 */

angular.module('hackademicApp').component('articleList', {
    templateUrl: 'static/appjs/article/article-list/article-list.template.html',
    controller:
        function articleListController($http) {
            var self = this;
            $http.get('http://127.0.0.1:8000/article.json').then(function(response) {
                self.articles = response.data.results;
            })
        }
});


