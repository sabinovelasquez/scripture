'use strict';
var app = angular

	.module('app', ['ngAnimate','ui.bootstrap', 'angulartics', 'angulartics.google.analytics', 'firebase'])

  .controller('movieCtrl', function($scope, $firebaseArray) {

    var movies = new Firebase("https://scripture-project.firebaseio.com/raising-arizona");
    $scope.items = $firebaseArray(movies);
    console.log($scope.items);

  })