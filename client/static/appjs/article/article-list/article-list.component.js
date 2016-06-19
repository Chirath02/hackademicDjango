/**
 * Created by chirath on 6/19/16.
 */

angular.module('articleList').component('articleList', {
    templateUrl: 'article-list/article-list.template.html',
    controller: ['Article',
        function articleListController(Articles) {
            this.articles = {
                "count": 1,
                "next": null,
                "previous": null,
                "results": [{
                    "id": 1,
                    "created_by": "chirath",
                    "modified_by": "chirath",
                    "title": "Hello World",
                    "content": "A \"Hello, world!\" program is often used to introduce beginning programmers to a programming language. In general, it is simple enough to be understood easily, especially with the guidance of a teacher or a written guide.\r\nIn addition, \"Hello world!\" can be a useful sanity test to make sure that a language's compiler, development environment, and run-time environment are correctly installed.[original research?] Configuring a complete programming toolchain from scratch to the point where even trivial programs can be compiled and run can involve substantial amounts of work. For this reason, a simple program is used first when testing a new tool chain.[citation needed]\r\n\r\nA \"Hello world!\" program running on Sony's PlayStation Portable as a proof of concept.\r\n\"Hello world!\" is also used by computer hackers as a proof of concept that arbitrary code can be executed through an exploit where the system designers did not intend code to be executedâ€”for example, on Sony's PlayStation Portable. This is the first step in using homemade content (\"home brew\") on such a device.\r\n\"Hello, world.\" was used as their first Tweet in 2016 by the previously secretive GCHQ UK communications interception agency.[1][2]",
                    "date_added": "2016-06-18T17:00:05.936475Z",
                    "date_modified": "2016-06-18T17:00:05.936549Z",
                    "ordering": 1,
                    "is_published": true
                }]
            };
        }
    ]
});