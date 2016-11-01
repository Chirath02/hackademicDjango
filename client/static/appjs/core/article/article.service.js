/**
 * Created by chirath on 6/19/16.
 */


angular.
module('core.article').
factory('Article',  ['$resource', '$location',
    function($resource, $location) {
        if($location.path() == '/article') {
            return $resource('article', {}, {
                query: {
                    method: 'GET',
                    params: {articleId: 'articles'},
                    isArray: true,
                    transformResponse: function(data) {
                        console.log(data);
                        return angular.fromJson(data);
                    }
                }
            });
        }
        else {
            var response = $resource('article/:articleId', {}, {
                query: {
                    method: 'GET',
                    params: {articleId: 'articles'},
                    isArray: true

                }
            });
            return response;
        }
    }
]);