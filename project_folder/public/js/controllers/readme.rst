=================
Controllers
=================


Do not manipulate DOM in your controllers, this will make your controllers harder for testing and will violate the [Separation of Concerns principle](https://en.wikipedia.org/wiki/Separation_of_concerns). Use directives instead.

* The naming of the controller is done using the controller's functionality (for example shopping cart, homepage, admin panel) and the substring `Ctrl` in the end. The controllers are named UpperCamelCase (`HomePageCtrl`, `ShoppingCartCtrl`, `AdminPanelCtrl`, etc.).
* The controllers should not be defined as globals (no matter AngularJS allows this, it is a bad practice to pollute the global namespace).
* Use array syntax for controller definitions::



    module.controller('MyCtrl', ['dependency1', 'dependency2', ..., 'dependencyn', function (dependency1, dependency2, ..., dependencyn) {
      //...body
    }]);



sing this type of definition avoids problems with minification. You can automatically generate the array definition from standard one using tools like [ng-annotate](https://github.com/olov/ng-annotate) (and grunt task [grunt-ng-annotate](https://github.com/mzgol/grunt-ng-annotate)).
* Use the original names of the controller's dependencies. This will help you produce more readable code::


    module.controller('MyCtrl', ['$scope', function (s) {
      //...body
    }]);


is less readable than::


    module.controller('MyCtrl', ['$scope', function ($scope) {
      //...body
    }]);


This especially applies to a file that has so much code that you'd need to scroll through. This would possibly cause you to forget which variable is tied to which dependency.

* Make the controllers as lean as possible. Abstract commonly used functions into a service.
* Communicate within different controllers using method invocation (possible when children wants to communicate with parent) or `$emit`, `$broadcast` and `$on` methods. The emitted and broadcasted messages should be kept to a minimum.
* Make a list of all messages which are passed using `$emit`, `$broadcast` and manage it carefully because of name collisions and possible bugs.
* When you need to format data encapsulate the formatting logic into a [filter](#filters) and declare it as dependency::


    module.filter('myFormat', function () {
      return function () {
        //body...
      };
    });

    module.controller('MyCtrl', ['$scope', 'myFormatFilter', function ($scope, myFormatFilter) {
      //body...
    }]);

