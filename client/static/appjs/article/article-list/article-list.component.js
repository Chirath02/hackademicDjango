/**
 * Created by chirath on 6/19/16.
 */

angular.module('phoneList').component('phoneList', {
    templateUrl: 'article-list/article-list.template.html',
    controller: ['Article',
        function articleListController(Articles) {
            this.articles = Articles.query();
        }
    ]
});