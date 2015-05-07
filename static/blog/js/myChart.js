/**
 * Created by RaPoSpectre on 15/5/7.
 */

var chartApp = angular.module("chartApp", []);
chartApp.controller("chartController", function ($scope, $http) {
    $scope.req_http = function (para) {
        if (para == 0) {
            alert("木有啦");
            return null;
        }
        var url = $scope.req_type() + '?page=' + para;
        $http.get(url).success(function (response) {
            $scope.blogs = response.body.blog_list;
            $scope.pagination = response.body.pagination;
        });
    };
    var url = $scope.req_type();
    $http.get(url).success(function (response) {
        $scope.blogs = response.body.blog_list;
        $scope.pagination = response.body.pagination;
    });
});