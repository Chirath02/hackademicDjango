/**
 * Created by chirath on 6/19/16.
 */


angular.
module('core.article').
factory('Article',  ['$resource', '$location',
    function($resource, $location) {
        if($location.path() == '/article') {
            return $resource('article.json', {}, {
                query: {
                    method: 'GET',
                    params: {articleId: 'articles'},
                    isArray: true,
                    transformResponse: function(data) {
                        return angular.fromJson(data).results;
                    }
                }
            });
        }
        else {
            var response = $resource('article/:articleId.json', {}, {
                query: {
                    method: 'GET',
                    params: {articleId: 'articles'},
                    isArray: true
                }
            });
            console.log($location.path());
            return response;
        }
    }
]);