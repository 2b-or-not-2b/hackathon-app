var API_URL = 'http://45.55.34.6/api/';

angular.module('starter.services', [])

.factory('Chats', function($q) {
  // NOT USING BUT TOO LAZY TO ERASE
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var chats = [];
  return {
    all: function() {
      return chats;
    },
    remove: function(chat) {
      chats.splice(chats.indexOf(chat), 1);
    },
    get: function(chatId) {
      for (var i = 0; i < chats.length; i++) {
        if (chats[i].id === parseInt(chatId)) {
          return chats[i];
        }
      }
      return null;
    }
  };
})

//-------------------------------------------------------------
// Our stuff
//-------------------------------------------------------------

.factory('HashFeeds', function($q, $http) {
  // Might use a resource here that returns a JSON array

    var domain;
    var url = window.location.href;
    if (url.indexOf("://") > -1) {
      domain = url.split('/')[2];
    }
    else {
      domain = url.split('/')[0];
    }
    domain = domain.split(':')[0];

  var myhashs = [
    {
        id: 69,
        tag_name: '#js_open_source_library',
        title: 'Support this great project!!!',
        desc: 'AniJS was created two years ago .....',
        video: '',
        image: 'img/rock_band.jpg',
        supporters: [],
        rewards: [],
        raised_money: 456.80,
        share_url: 'http://somethingcool.com',
        min_price: 10,
        name: 'Perry Governor',
        lastText: 'Look at my mukluks!',
        face: 'img/perry.png'
      }
  ];
  return {
    all: function() {
      console.log('Receiving the hash here ;)');
      var defer = $q.defer();
      if (1) {
        //defer.resolve(hashfeeds);
        $http.get(API_URL + 'cashtag').then(function (response) {
          var hashfeeds_response = response.data.cash_tags;
          defer.resolve(hashfeeds_response);
        }, function (error) {
          console.log('error');
        })

      } else {
        defer.reject();
      }
      return defer.promise;
    },
    allMyHashs: function(){
      var defer = $q.defer();
      if (1) {
        defer.resolve(myhashs);
      } else {
        defer.reject();
      }
      return defer.promise;
    },
    remove: function(chat) {
      hashfeeds.splice(hashfeeds.indexOf(hashfeed), 1);
    },
    get: function(chatId) {
      for (var i = 0; i < hashfeeds.length; i++) {
        if (hashfeeds[i].id === parseInt(chatId)) {
          return hashfeeds[i];
        }
      }
      return null;
    },
    create: function(hash){
      console.log('Receiving the hash here ;)');
      var defer = $q.defer();
      var share_url = undefined;
      var domain;
      if (url.indexOf("://") > -1) {
        domain = url.split('/')[2];
      }
      else {
        domain = url.split('/')[0];
      }
      domain = domain.split(':')[0];

      if (1) {
        hash.image = 'img/rock_band.jpg';
        hash.tag_name = '#support_my_band';
        hash.share_url = 'http://' + domain + '/' + hash.tag_name;
        hash.desc = 'Guys, if you like this music, support us';
        hash.share_url= 'http://something.funny.com';
        hash.raised_money = 0;
        hash.supporters = [1];
        hash.emmbeded_code = '<div class="fb-like" data-href="https://developers.facebook.com/docs/plugins/" data-layout="standard" data-action="like" data-show-faces="true" data-share="true"></div>';

        defer.resolve(hash);
      } else {
        defer.reject();
      }
      return defer.promise;
    },
    pledge: function(){
      var defer = $q.defer();
      if (1) {
        defer.resolve({});
      } else {
        defer.reject();
      }
      return defer.promise;
    },
    getBasic: function(chatId) {
      var basic = {
        tag_name: '',
        title: '',
        desc: '',
        video: '',
        image: '',
        supporters: [],
        rewards: [],
        min_price: 0,
        share_url: '',
        username: '',
        name: '',
        face: ''
      };
      return basic;
    },
  };
})

.factory('Friends', function() {
// NOT USING BUT TOO LAZY TO ERASE
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var friends = [];

  return {
    all: function() {
      return friends;
    },
    remove: function(chat) {
      friends.splice(friends.indexOf(hashfeed), 1);
    },
    get: function(chatId) {
      for (var i = 0; i < friends.length; i++) {
        if (friends[i].id === parseInt(chatId)) {
          return friends[i];
        }
      }
      return null;
    },
    getBasic: function(chatId) {
      var basic = {
        tag_name: '',
        title: '',
        desc: '',
        video: '',
        image: '',
        supporters: [],
        rewards: [],
        min_price: 0,
        share_url: '',
        username: '',
        name: '',
        face: ''
      };
      return basic;
    },
  };
})

.factory('CurrentUser', function($q) {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var user = {
    id: 60,
    username: 'cody',
    name: 'Cody Greene',
    lastText: 'Hey, it\'s me',
    face: 'img/cody.jpg'
  };

  return {
    all: function() {
      return user;
    },
    remove: function() {
    },
    get: function() {
      var defer = $q.defer();
      if (1) {
        defer.resolve(user);
      } else {
        defer.reject();
      }
      return defer.promise;
    },
    getBasic: function() {},
  };
});
