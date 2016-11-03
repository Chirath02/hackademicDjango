/**
 * Created by chirath on 3/11/16.
 */

'use stricu';

angular.module('hackademic').config(
    function ($routeProvider, $locationProvider){
        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false
        });

        $routeProvider.when("/articles", {
            template: "<article-list></article-list>"
        }).otherwise({
            template: "<article-list></article-list>"
        })
    });