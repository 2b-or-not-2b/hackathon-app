angular.module('starter.services', [])

.factory('Chats', function($q) {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var chats = [{
    id: 0,
    name: 'Ben Sparrow',
    lastText: 'You on your way?',
    face: 'img/ben.png'
  }, {
    id: 1,
    name: 'Max Lynx',
    lastText: 'Hey, it\'s me',
    face: 'img/max.png'
  }, {
    id: 2,
    name: 'Adam Bradleyson',
    lastText: 'I should buy a boat',
    face: 'img/adam.jpg'
  }, {
    id: 3,
    name: 'Perry Governor',
    lastText: 'Look at my mukluks!',
    face: 'img/perry.png'
  }, {
    id: 4,
    name: 'Mike Harrington',
    lastText: 'This is wicked good ice cream.',
    face: 'img/mike.png'
  }];

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

.factory('HashFeeds', function($q) {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var hashfeeds = [{
    id: 0,
    tag_name: '#mywedding',
    title: 'Happy forever!!!',
    desc: 'Hi friends, we are happy to announce our wedding...',
    video: '',
    image: 'img/rock_band.jpg',
    supporters: [1, 3],
    rewards: [],
    raised_money: 456.80,
    share_url: 'http://somethingcool.com',
    min_price: 0,
    name: 'Max Lynx',
    lastText: 'Hey, it\'s me',
    face: 'img/max.png'
  }, {
    id: 1,
    tag_name: '#buildNe2S_april_rent',
    title: 'Monthly Rent Ready',
    desc: 'Dear home renters, you can pay your monthly...',
    video: '',
    image: 'img/rock_band.jpg',
    supporters: [],
    rewards: [],
    raised_money: 456.80,
    share_url: 'http://somethingcool.com',
    min_price: 0,
    share_url: '',
    username: 'ben',
    name: 'Ben Sparrow',
    face: 'img/ben.png'
  }, {
    id: 2,
    tag_name: '#garage_sale_brickell',
    title: 'Brickell garage sale',
    desc: 'Use this hash if you want to purchase something here...',
    video: '',
    image: 'img/rock_band.jpg',
    supporters: [],
    rewards: [],
    raised_money: 456.80,
    share_url: 'http://somethingcool.com',
    min_price: 0,
    name: 'Adam Bradleyson',
    lastText: 'I should buy a boat',
    face: 'img/adam.jpg'
  }, {
    id: 3,
    tag_name: '#big_party_miami2016',
    title: 'Just be fun with us :) ;)',
    desc: 'Hi guys, we are hosting a big stuff here, Free beers included, the minimal support is just 10 box.',
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
  }, {
    id: 4,
    tag_name: '#help_emily_baby',
    title: 'Help us please?',
    desc: 'Our cute Emily is so sick, and unfurtunately, we cannot afford the payments',
    video: '',
    image: 'img/rock_band.jpg',
    supporters: [],
    rewards: [],
    raised_money: 456.80,
    share_url: 'http://somethingcool.com',
    min_price: 0,
    name: 'Mike Harrington',
    lastText: 'This is wicked good ice cream.',
    face: 'img/mike.png'
  },
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
      return hashfeeds;
    },

    allMyHashs: function(){
      return myhashs;
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
      if (1) {
        hash.image = 'img/rock_band.jpg';
        hash.tag_name = '#support_my_band';
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
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var friends = [{
    id: 0,
    username: 'max',
    name: 'Max Lynx',
    lastText: 'Hey, it\'s me',
    face: 'img/max.png'
  }, {
    id: 1,
    username: 'ben',
    name: 'Ben Sparrow',
    lastText: 'Hey, it\'s me',
    face: 'img/ben.png'
  }, {
    id: 2,
    username: 'adam',
    name: 'Adam Bradleyson',
    lastText: 'I should buy a boat',
    face: 'img/adam.jpg'
  }, {
    id: 3,
    username: 'perry',
    name: 'Perry Governor',
    lastText: 'Look at my mukluks!',
    face: 'img/perry.png'
  }, {
    id: 4,
    username: 'mike',
    name: 'Mike Harrington',
    lastText: 'This is wicked good ice cream.',
    face: 'img/mike.png'
  }];

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

.factory('CurrentUser', function() {
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
      return user;
    },
    getBasic: function() {},
  };
})

//TODO: We are not using it
.factory('ShareHash', function($q) {
  return {
    share: function(hash) {
      var defer = $q.defer();
      if (1) {
        hash.share_url = 'http://aquinama.com';
        defer.resolve(hash);
      } else {
        defer.reject();
      }
      return defer.promise;
    },
  };
})

;
