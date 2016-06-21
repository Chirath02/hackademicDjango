/**
 * Created by chirath on 6/19/16.
 */

angular.module('hackademicApp').component('articleList', {
    templateUrl: 'static/appjs/article/article-list/article-list.template.html',
    controller:
        function articleListController() {
            this.articles = [
                {
                    title: 'Nexus S',
                    content: 'Fast just got faster with Nexus S.'
                }, {
                    title: 'Motorola XOOM™ with Wi-Fi',
                    content: 'The Next, Next Generation tablet.'
                }, {
                    title: 'MOTOROLA XOOM™',
                    content: 'The Next, Next Generation tablet.'
                }
            ];
        }
});


