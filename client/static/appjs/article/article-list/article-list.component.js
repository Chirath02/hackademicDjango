/**
 * Created by chirath on 6/19/16.
 */

angular.module('hackademicApp').component('articleList', {
    templateUrl: 'static/appjs/article/article-list/article-list.template.html',
    controller:
        function angularListController() {
            this.articles = [{
                title: "Hello World",
                content: "A \"Hello, world!\" program is often used to introduce beginning o"
            },
                {
                    title: "Hello World",
                    content: "A \"Hello, world!\" program is "
                }];
        }
});

