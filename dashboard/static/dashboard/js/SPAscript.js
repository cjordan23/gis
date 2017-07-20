// script.js

    // create the module and name it scotchApp
    var fleetMgmt = angular.module('fleetMgmt', ['ngRoute']);
    // configure our routes
        app.config(function($routeProvider){
          $routeProvider
          .when("/",{
            templateUrl :"index.html"
          })
          .when("#/daftarDriver",{
            templateUrl :"daftarDriver.html"
          });
        });
