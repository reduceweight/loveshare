<template lang="html">
  <div class="g-container">
    <home-header></home-header>
    <!--<login></login>-->
    <div style="margin: 524px 0;">
      <button id="j-loadMembers">Ajax 加载所有用户</button>
      <p id="j-memberList"></p>
    </div>
    <div style="margin: 24px 0;">
      <ul>
        <li v-for="item in categoryList" @click="getArticleByUser(item.fields.title)">{{item.fields.title}}</li>
      </ul>
      <table>
        <tr>
          <th>标题</th>
          <th>发表时间</th>
          <th>作者</th>
        </tr>
        <tr v-for="item in articleList">
          <td>{{item.fields.title}}</td>
          <td>{{item.fields.pub_date}}</td>
          <td>{{item.fields.author}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>
<script>
import HomeHeader from '../components/header'   /* 本页面中用到了HomeHeader组件，所以就需要在这里引入一下 */
import Login from '../components/login'
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
    HomeHeader,
    Login
  },
  created () {
    var self = this
    $.getJSON('/api/getCategoryList', function (data) {
       self.categoryList = data.list
    })
  },
  mounted () {
    $('#j-loadMembers').click(function(){
      $.getJSON('/api/show_members', function (data) {
        var html = "<table><tr><th>姓名</th><th>昵称</th><th>性别</th><th>出生日期</th><th>手机号码</th><th>邮箱地址</th>", result = data.list
        for (var i = result.length - 1; i >= 0; i--) {
          var user = result[i].fields
          html += "<tr><td>"+user.name+"</td><td>"+user.nickname+"</td><td>"+user.sex+"</td><td>"+user.birthday+"</td><td>"+user.mobile+"</td><td>"+user.email+"</td></tr>"
        }
        html += "</table>"
        $('#j-memberList').append(html)
      })
    })
  },
   methods: {
    getArticleByUser: function (title) {
      var self = this
      $.get('/api/getArticleList',{'title':title}, function (data) {
         self.articleList = data.list
      })
    }
  }
}
</script>

<style lang="css" scoped>

</style>
