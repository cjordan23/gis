var app = angular.module('loginApp',['ngRoute']);

app.config(function($routeProvider){
    $routeProvider
        .when('/',{
            templateUrl: 'login.html'
        })
        .when('/index',{
            templateUrl: 'index.html'
        })
        .otherwise({
            redirectTo: '/'
        });
});

app.controller('loginCtrl', function($scope, $location){
    $scope.su6bmit = function(){
        var uname = $scope.username;
        var pword = $scope.password;
        if($scope.username == 'admin' && $scope.password =='admin'){
            $location.path('/index');
        }
    };
});