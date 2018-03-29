<template>
  <div role="navigation" class="navbar navbar-default topnav">
    <div class="container">
      <div class="navbar-header">
        <a href="/" class="navbar-brand">
          <img src="../../static/common/logo.png" alt="Love Share" width="148px">
        </a>
      </div>

      <div id="top-navbar-collapse" class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <li class=""><a href="https://laravel-china.org/topics">社区</a></li>
          <li class=""><a href="https://laravel-china.org/categories/10">头条</a></li>
          <li class=""><a href="https://laravel-china.org/categories/4">公告</a></li>
          <li>
            <a class="no-pjax" href="https://laravel-china.org/courses">教程</a>
          </li>
          <li class="nav-docs hidden-sm"><a href="https://laravel-china.org/docs">文档</a></li>
          <li class=""><a href="https://laravel-china.org/categories/12">翻译</a></li>
        </ul>

        <div class="navbar-right">
          <form method="GET" action="https://laravel-china.org/search" accept-charset="UTF-8"
                class="navbar-form navbar-left hidden-sm hidden-md" style="display: none">
            <div class="form-group">
              <input class="form-control search-input mac-style" placeholder="搜索" name="q" type="text" value="">
            </div>
          </form>

          <ul class="nav navbar-nav github-login">
            <a href="https://laravel-china.org/auth/login" class="btn btn-default login-btn no-pjax">
              <i class="fa fa-user"></i>
              登 录
            </a>
            <a href="https://laravel-china.org/auth/register" class="btn btn-default login-btn no-pjax">
              <i class="fa fa-user-plus"></i>
              注 册
            </a>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data () {
      return {
          items: []   /* 定义一个空数组数据items */
      }
  },
  created () {

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

.navbar {
    margin-bottom: 20px;
}

.navbar-default {
  height: 56px;
  border: none;
  border-color: #e7e7e7;
  background-color: #fff;
  -webkit-box-shadow: 0px 1px 11px 2px rgba(42, 42, 42, 0.1);
  box-shadow: 0px 1px 11px 2px rgba(42, 42, 42, 0.1);
  border-top: 4px solid #f46660;
}

.navbar:before,
.navbar:after {
  content: " ";
  display: table;
}

.navbar:after {
  clear: both;
}

.navbar-header {
  float: left;
}

.navbar-brand {
  float: left;
  padding: 15px 15px;
  font-size: 18px;
  line-height: 20px;
  height: 38px;
}

.navbar-nav {
    float: left;
    margin: 0;
}

.navbar-nav > li {
  float: left;
}

.navbar-nav > li > a {
  padding-top: 15px;
  padding-bottom: 15px;
}

.topnav .nav > li > a {
  float: none;
  position: relative;
  display: block;
  padding: 15px 15px 9px;
  line-height: 28px;
  color: inherit;
  text-decoration: none;
}

.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:focus,
.navbar-default .navbar-nav > .active > a:hover {
  color: #555;
  background-color: rgba(0, 0, 0, 0.03);
}

.navbar-right {
  float: right;
  margin-right: 0;
}

.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 14px;
  line-height: 1.42857143;
  border-radius: 4px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.btn:focus,
.btn.focus,
.btn:active:focus,
.btn:active.focus,
.btn.active:focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}

.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}

.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}

.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}

.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e5e5;
  border-color: #8c8c8c;
}

.btn-default:hover {
  color: #333;
  background-color: #e6e5e5;
  border-color: #adadad;
}

.btn-default:active,
.btn-default.active,
.open > .btn-default.dropdown-toggle {
  color: #333;
  background-color: #e6e5e5;
  border-color: #adadad;
}

.topnav .btn {
  margin-top: 7px;
  font-size: 13px;
  padding: 5px 12px;
  border-radius: 2px;
}

.topnav .navbar-form {
  padding: 0px 20px;
  margin-top: 7px;
  margin-bottom: 4px;
}


</style>
