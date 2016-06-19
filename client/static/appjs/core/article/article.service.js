/**
 * Created by chirath on 6/19/16.
 */

angular.module('core.article').factory('Article', ['$resource',
    function($resource) {
        return $resource('article/:articleId.json', {}, {
            query: {
                method: 'GET',
                params: {articleId: 'article'},
                isArray: true
            }
        })
    }
]);