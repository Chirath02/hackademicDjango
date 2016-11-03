/**
 * Created by chirath on 3/11/16.
 */
'use strict';

angular.module('articleDetail').
    component('articleDetail', {
        templateUrl: 'static/app/article/article-detail/article-detail.template.html',
        controller: function ($scope, $http, $routeParams) {
            $http.get('api/article/' + $routeParams.articleId).then(function (response) {
                $scope.article = response.data;
                console.log($routeParams);
            })
        }
    }
);