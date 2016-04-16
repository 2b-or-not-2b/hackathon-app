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

.controller('HashFeedCtrl', function($scope, HashFeeds,$timeout) {
  $scope.hashfeeds = HashFeeds.all();
  $scope.doRefresh = function(){
    $timeout(function(){
      $scope.$broadcast('scroll.refreshComplete');
    }, 2000);
    return;
  };
  $scope.remove = function(hashfeed) {
    HashFeeds.remove(hashfeed);
  };
})

.controller('HashFeedDetailCtrl', function($scope, $stateParams, HashFeeds) {
  $scope.hash = HashFeeds.get($stateParams.hashfeedId);
  $scope.ui = {
    showPledgeOptions: 0
  };
  $scope.pledgeAction = function(){
    // HashFeeds.pledge(hash).then(function(data){
    //   console.log(data);
    //   if(data){

    //   }
    //   // $scope.hash = data;
    //   // $scope.ui.showDetail = 1;
    // });
    $scope.ui.showPledgeOptions = 1;
  }
})

.controller('HashCreateCtrl', function($scope, $stateParams, HashFeeds, Friends, CurrentUser, $rootScope) {
  // $scope.hashfeed = HashFeeds.get($stateParams.hashfeedId);

  init();
  var unbindListenerStart = $rootScope.$on('$stateChangeStart', function (event, toState) {
    unbindListenerStart();
    init();
  });

  function init(){
    $scope.hash = HashFeeds.getBasic();
    $scope.hash = HashFeeds.getBasic();
    $scope.friends = Friends.all();
    $scope.user = CurrentUser.get();
    $scope.ui = {
      showDetail: 0
    };
  }

  console.log('Here!!!');

  $scope.createAction = function(){
    var hash = $scope.hash;
    HashFeeds.create(hash).then(function(data){
      console.log('Somehitng else');
      console.log(data);
      $scope.hash = data;
      $scope.ui.showDetail = 1;
    });
    // Call the service create the card and then going
    // to the new url
  }
});
