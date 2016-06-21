/**
 * Created by chirath on 6/21/16.
 */

angular.module('hackademicApp').component('articleDetail', {
    template: 'TBD: Detail view for <span>{{$ctrl.articleId}}</span>',
    controller: function articleDetailController($routeParams) {
        this.articleId = $routeParams.articleId;
    }
});