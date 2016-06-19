/**
 * Created by chirath on 6/19/16.
 */

angular.module('hackademicApp').config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
        $locationProvider.hashPrefix('!');

        $routeProvider.when('/articles', {
            template: '<article-list></article-list>'
        }).
        otherwise('/articles');
    }
]);
