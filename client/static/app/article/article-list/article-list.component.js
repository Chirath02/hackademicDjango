/**
 * Created by chirath on 3/11/16.
 */
'use strict';

angular.module('articleList').
    component('articleList', {
        templateUrl: 'static/app/article/article-list/article-list.template.html',
        controller: function ($scope) {
            $scope.name = 'Chirath';
        }
});
