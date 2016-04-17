var API_URL = 'http://45.55.34.6/api/';
//var API_URL = 'http://localhost:8000/api/';

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

.controller('HashFeedCtrl', function($scope, HashFeeds,$timeout, $stateParams, $state) {
  $scope.hashfeeds = [];
  HashFeeds.all().then(function(data){
    $scope.hashfeeds = data;
  });

    console.log('tag name: ' + $stateParams.tag_name);
    if ($stateParams.tag_name) {
    var looking_for_tag = '#' + $stateParams.tag_name.trim();
    var matching_cashtag;
    for (var i = 0; i < $scope.hashfeeds.length; i++) {
      var cashtag = $scope.hashfeeds[i];
      if (cashtag.tag_name.trim() == looking_for_tag ||
        ('#' + cashtag.tag_name.trim()) == looking_for_tag) {
          matching_cashtag = cashtag;
        break
      }
    }

    $state.go('tab.hashfeed-detail', {'hashfeedId': cashtag.id});
  }

  $scope.doRefresh = function(){
    HashFeeds.all().then(function(data){
      $scope.hashfeeds = data;
      $scope.$broadcast('scroll.refreshComplete');
    });
  };
  $scope.remove = function(hashfeed) {
    HashFeeds.remove(hashfeed);
  };
})

.controller('HashFeedDetailCtrl', function($scope, $stateParams, HashFeeds,$timeout, $ionicHistory, $ionicLoading, $http) {
    $scope.priceChosen = 25;
    $scope.hash = HashFeeds.get($stateParams.hashfeedId);
  $scope.ui = {
    pledgeCustomPriceAmount: null,
    showPledgeOptions: 0,
    showThanks: 0,
    pledgeAmount: 0,
    pledgeOptions: [
      {price: 10, selected: 0},
      {price: 25, selected: 1},
      {price: 50, selected: 0},
      {price: 100, selected: 0},
    ]
  };

  $scope.pledgeOptionAction = function(pledgeOption){
    for (var i = 0; i < $scope.ui.pledgeOptions.length; i++) {
      $scope.ui.pledgeOptions[i].selected = 0;
    };
    pledgeOption.selected = 1;
    $scope.priceChosen = pledgeOption.price;
  };

    $scope.pledgeCustomPrice = function() {
      var amount = parseInt($scope.ui.pledgeCustomPriceAmount);
      if (!!amount || amount <= 0) {
        $scope.priceChosen = amount;
      } else {
        $scope.priceChosen = undefined;
      }
    };

  $scope.pledgeAction = function(){
    var hash = $scope.hash;
    if($scope.ui.showPledgeOptions){
      if (!$scope.priceChosen) {
        $ionicLoading.show({
          template: 'Please select an amount.',
          hideOnStateChange: true,
          duration: 2500
        });
        return;
      }
      //TODO: sent info to the servers
      HashFeeds.pledge(hash).then(function(data){
        console.log(data);
        if(data){
          $ionicLoading.show({
             template: 'Sending Payment',
             hideOnStateChange: true,
             duration: 4000
          });
          $http.get(API_URL + 'pay?amount=' + $scope.priceChosen + '&cashtag_id=' + hash.id).then(
            function(response) {
              $scope.ui.showThanks = 1;
              console.log(response);
              hash.raised_money = response.data.raised_money;
              $timeout(function(){$ionicHistory.goBack(-1)}, 1000);
            },
            function(error) {
              console.log(error);
              $ionicLoading.show({
                template: 'An Error Occured.',
                hideOnStateChange: true,
                duration: 2000
              });
            }
          );
        }
        // $scope.hash = data;
        // $scope.ui.showDetail = 1;
      });
    } else {
      $scope.ui.showPledgeOptions = 1;
    }
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
    $scope.user = {};
    CurrentUser.get().then(function(data){
      $scope.user = data;
    });
    $scope.ui = {
      showDetail: 0,
      showShare: 0
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
    // Changin
  }

  $scope.showShareAction = function(){
    if($scope.ui.showShare){
      $scope.ui.showShare = 0;
    } else{
      $scope.ui.showShare = 1;
    }
  }
})

.controller('HashSearchCtrl', function($scope, HashFeeds,$timeout) {
  $scope.hashfeeds = [];
  HashFeeds.all().then(function(data){
    $scope.hashfeeds = data;
  });
  $scope.query = {}
  $scope.queryBy = '$'
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

.controller('MyHashsCtrl', function($scope, HashFeeds,$timeout) {
  $scope.hashfeeds = [];
  HashFeeds.allMyHashs().then(function(data){
    $scope.hashfeeds = data;
  });
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



;
