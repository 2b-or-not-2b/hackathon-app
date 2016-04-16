angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope) {})

.controller('ChatsCtrl', function($scope, Chats) {
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
})

//-------------------------------------------------------------
// Our stuff
//-------------------------------------------------------------

.controller('HashFeedCtrl', function($scope, HashFeeds) {
  $scope.hashfeeds = HashFeeds.all();
  $scope.remove = function(hashfeed) {
    HashFeeds.remove(hashfeed);
  };
})

.controller('HashFeedDetailCtrl', function($scope, $stateParams, HashFeeds) {
  $scope.hashfeed = HashFeeds.get($stateParams.hashfeedId);
})

.controller('HashCreateCtrl', function($scope, $stateParams, HashFeeds, Friends, CurrentUser) {
  // $scope.hashfeed = HashFeeds.get($stateParams.hashfeedId);
  $scope.hash = HashFeeds.getBasic();
  $scope.friends = Friends.all();
  $scope.user = CurrentUser.get();

  $scope.createAction = function(){
    var hash = $scope.hash;
    HashFeeds.create(hash).then(function(data){
      console.log('Somehitng else');
      console.log(data);
    });
    // Call the service create the card and then going
    // to the new url
  }
});
