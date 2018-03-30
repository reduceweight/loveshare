<template lang="html">
  <div class="g-container">
    <new-header></new-header>
    <div class="container main-container ">
      <div class="col-md-9 topics-index main-col">
          <div class="panel panel-default">
              <div class="panel-heading">
                <ul class="list-inline topic-filter">
                  <li class="popover-with-html" v-for="item in categoryList" @click="getArticleByUser(item.fields.title)"><a class="active">{{item.fields.title}}</a></li>
                </ul>
                <div class="clearfix"></div>
              </div>
              <div class="jscroll">
                <div class="jscroll-inner">
                  <div class="panel-body remove-padding-horizontal">
                    <ul class="list-group row topic-list">
                      <li class="list-group-item" v-for="item in articleList">
                        <a class="reply_count_area hidden-xs pull-right" href="https://laravel-china.org/topics/7657/laravel-tutorial-series-third-the-first-edition-of-the-laravel-tutorial-advanced-architecture-api-server">
                          <div class="count_set">
                            <span class="count_of_votes" title="投票数">
                               202
                            </span>

                            <span class="count_seperator">/</span>
                            <span class="count_of_replies" title="回复数">
                               88
                            </span>
                            <span class="count_seperator">/</span>
                            <span class="count_of_visits" title="查看数">
                               20.3k
                            </span>
                            <span class="count_seperator">|</span>
                            <abbr title="2018-03-29 10:10:53" class="timeago">{{item.fields.pub_date}}</abbr>
                           </div>
                        </a>
                        <div class="avatar pull-left">
                          <a href="https://laravel-china.org/users/1" title="Summer">
                            <img class="media-object img-thumbnail avatar avatar-middle" alt="Summer" src="https://lccdn.phphub.org/uploads/avatars/1_1479342408.png?imageView2/1/w/100/h/100">
                          </a>
                        </div>
                        <div class="infos">
                          <div class="media-heading">
                            <span class="hidden-xs label label-warning">置顶{{item.fields.author}}</span>
                            <a href="https://laravel-china.org/topics/7657/laravel-tutorial-series-third-the-first-edition-of-the-laravel-tutorial-advanced-architecture-api-server" title="Laravel 教程系列书第三本《Laravel 教程实战高级 - 构架 API 服务器》">
                               {{item.fields.title}}
                            </a>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
          </div>
      </div>
      <div class="clearfix"></div>
    </div>
  </div>
</template>
<script>
import NewHeader from '../components/NewHeader'
import $ from 'jquery'
export default {
  data () {
    return {
      recommends: [],
      categoryList: [],
      articleList: []
    }
  },
  components: {
    NewHeader
  },
  created () {
    var self = this
    // $.getJSON('/api/getCategoryList', function (data) {
    //    self.categoryList = data.list
    // })

    self.$http.get('http://127.0.0.1:8000/api/getCategoryList')
      .then(function (response) {
        self.categoryList = response.data.list
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  mounted () {

  },
   methods: {
    getArticleByUser: function (title) {
      var self = this
      // $.get('/api/getArticleList',{'title':title}, function (data) {
      //    self.articleList = data.list
      // })
      self.$http.get('list/api/getArticleList', {
        params: {
          title: title
        }
      })
      .then(function (response) {
        self.articleList = response.data.list
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style lang="css" scoped>
.container {
  width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}
.container:before,
.container:after {
  content: " ";
  display: table;
}
.container:after {
  clear: both;
}
.main-container {
  padding-bottom: 228px;
}
.topics-index {
  float: left;
  width: 880px;
}
.panel {
  margin-bottom: 20px;
  background-color: #fff;
  border: 1px solid #dde2e8;
}
.panel-heading {
  padding: 8px 15px;
  color: #333;
  background-color: #fff;
  border-bottom: 1px solid #eeeeee;
  border-top-right-radius: 3px;
  border-top-left-radius: 3px;
}
.topics-index .topic-filter {
  margin-top: 8px;
  margin-left: 0px;
  margin-bottom: 3px;
  color: #d0d0d0;
  font-size: 12px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
.topics-index .topic-filter li {
  margin-right: 8px;
}
.topics-index .topic-filter a {
  color: #8b8a8a;
  text-decoration: none;
  font-size: 14px;
  padding: 1px 4px;
  line-height: 18px;
}
.topics-index .topic-filter a.active {
  border-bottom: 2px solid #fbbd08;
}
.panel-body {
  padding: 15px;
}
.panel-body:before,
.panel-body:after {
  content: " ";
  display: table;
}
.panel-body:after {
  clear: both;
}
.remove-padding-horizontal {
  padding-bottom: 0px;
  padding-top: 0px;
}
.row {
  margin-left: -15px;
  margin-right: -15px;
}
.row:before,
.row:after {
  content: " ";
  display: table;
}
.row:after {
  clear: both;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 4px;
  border-top-left-radius: 4px;
}
.topic-list .list-group-item {
  height: 58px;
  padding: 0px 15px;
  border: none;
  margin-bottom: 0px;
  border-bottom: 1px solid #f2f2f2;
}
.pull-left {
  float: left !important;
}
.pull-right {
  float: right !important;
}
.reply_count_area {
  width: 200px;
  display: inline-block;
  text-align: right;
  float: left;
  line-height: 2em;
  margin-top: 18px;
}
.topic-list a, .topic-list a:focus, .topic-list a:hover {
  color: #555;
}
#wrap .avatar {
  padding: 3px;
  margin: 2px 0 0;
  border-radius: 50%;
}
.topic-list .list-group-item .avatar.avatar-middle {
  display: block;
  width: 44px;
  height: 44px;
  margin: 2px 0 0;
  padding: 3px;
  line-height: 1.42857143;
  border-radius: 50%;
  background-color: #fff;
  border: 1px solid #ddd;
  -webkit-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
}
.topics-index .topic-list .media-heading {
  font-size: 15px;
  padding-top: 18px;
  padding-left: 8px;
  white-space: nowrap;
  overflow: hidden;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
  z-index: 10;
}
.label-warning {
  background-color: #f0ad4e;
}
.topic-list .media-heading .label {
  position: relative;
  top: -1px;
  font-size: 12px;
  font-weight: normal;
}
.topics-index .topic-list .infos .media-heading a {
  display: inline-block;
  width: 100%;
  padding-left: 2px;
}
.topic-list a,
.topic-list a:focus,
.topic-list a:hover {
  color: #555;
}
.topics-index .topic-list .infos .media-heading a:visited {
  color: #a2a2a2;
}
</style>
