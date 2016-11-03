/**
 * Created by chirath on 3/11/16.
 */

'use strict';

angular.module('hackademic').config(
    function config($routeProvider, $locationProvider){
        $locationProvider.hashPrefix('!');

        $routeProvider.when("/article/", {
            template: "<article-list></article-list>"
        }).when("/article/:id/", {
            template: '<article-detail></article-detail>'
        }).otherwise({
            template: "<article-list></article-list>"
        })
    });