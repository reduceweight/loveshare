<template lang="html">
<header class="header">
	<h1 class="logo">
			<a href="http://www.shejipi.com/">爱分享</a>
	</h1>
	<div class="feel">
		<a class="feel-tag" href="http://www.shejipi.com/?feel=like">赞</a>
    <a class="feel-tag" href="http://www.shejipi.com/?feel=bud">萌</a>
    <a class="feel-tag" href="http://www.shejipi.com/?feel=ha">哈</a>
    <a class="feel-tag" href="http://www.shejipi.com/?feel=cao">艹</a>
    <a class="feel-tag" href="http://www.shejipi.com/?feel=buy">买</a>
	</div>
	<div class="user">
    <a class="login_button" id="show_login" href="#">登录</a>
  </div><!-- .user -->
	<nav>
		<div class="navico"> </div>
		<div class="nav">
      <ul id="menu-nav" class="menu">
        <li id="menu-item-168537" class="menu-item menu-item-type-custom menu-item-object-custom current-menu-item current_page_item menu-item-home menu-item-168537">
          <a href="http://www.shejipi.com">首页</a><i></i>
        </li>
        <li id="menu-item-97955" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-97955">
          <a href="http://www.shejipi.com/?sort=date&amp;days=all#3">资讯</a><i></i>
        </li>
        <li id="menu-item-121210" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-121210">
          <a target="_blank" href="http://www.shejipi.com/features">专题</a><i></i>
        </li>
        <li id="menu-item-168522" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-168522">
          <a href="#">招聘</a><i></i>
          <ul class="sub-menu">
            <li id="menu-item-153225" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-153225"><a href="http://job.shejipi.com/">职位</a><i></i></li>
            <li id="menu-item-168523" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-168523"><a href="http://job.shejipi.com/?s=&amp;post_type=company">公司</a><i></i></li>
            <li id="menu-item-168524" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-168524"><a target="_blank" href="http://cn.mikecrm.com/gnn8DqU">发布职位</a><i></i></li>
          </ul>
        </li>
      </ul>
    </div>
	</nav>
</header>
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
  .header {
	width: 100%;
	height: 66px;
	position: relative;
	background: #fff;
	z-index: 666;
	border-bottom: 1px solid #e5e5e5;
}

.logo {
	margin: 16px 25px 16px 12px;
	float: left;
}
.logo a {
	display: block;
	height: 33px;
	width: 194px;
	background: url(../../../frontend/static/images/common/logo.png) no-repeat center center;
}
.feel {
	margin: 14px 0 0 0;
	float: left;
}
.feel a {
	margin: 0 0 0 12px;
	float: left;
}
.feel a:hover {
	margin-top: -2px;
}
.feel-tag {
	height: 36px;
	line-height: 36px;
	width: 36px;
	border-radius: 100%;
	display: block;
	text-align: center;
	background: #F8E71C;
	font-size: 20px;
	color: #131418;
	transform: rotate(-28deg);
	-webkit-transform: rotate(-28deg);
	-moz-transform: rotate(-28deg);
}
/* search */

.sch {
	transition: all 0.2s;
	overflow: hidden;
	float: right;
	margin: 19px 10px 0 0;
	background: #f5f5f5;
	width: 27px;
	height: 27px;
	line-height: 27px;
	position: relative;
}
.startsearch {
	width: auto;
}
.sch .s, .sch .go {
	border: none;
	color: #4d4d4d;
	outline: medium;
}
.sch .s {
	display: none;
	background: none;
	line-height: 25px;
	vertical-align: middle;
	font-family: "STXihei", "åŽæ–‡ç»†é»‘", Arial, Helvetica, sans-serif, "Microsoft YaHei", "å¾®è½¯é›…é»‘";
	float: left;
	width: 150px;
	margin: 0 0 0 30px;
}
.startsearch .s {
	display: block;
}
.sch .go {
	display: none;
	position: absolute;
	left: 0;
}
.gobtn {
	display: none;
	width: 24px;
	height: 24px;
	cursor: pointer;
	position: absolute;
	left: 0;
}
.startsearch .gobtn {
	display: block;
}
.ac {
	display: block;
	width: 24px;
	height: 24px;
	cursor: pointer;
	background: #f5f5f5;
}
.ac:before, .gobtn:before {
	content: '';
	margin: 7px 0 0 8px;
	width: 9px;
	height: 9px;
	display: block;
	border: 1px solid #9B9B9B;
	background: rgba(0, 0, 0, 0);
	-webkit-border-radius: 50%;
	-moz-border-radius: 50%;
	border-radius: 50%;
}
.ac:after, .gobtn:after {
	content: '';
	width: 2px;
	position: absolute;
	display: block;
	height: 6px;
	margin: -3px 0 0 18px;
	background: #9B9B9B;
	-webkit-transform: rotate(-45deg);
	-ms-transform: rotate(-45deg);
	transform: rotate(-45deg);
}
.startsearch .ac {
	position: absolute;
	right: 0;
	background: none;
	z-index: 100;
	font-size: 18px;
	font-weight: bold;
	font-style: normal;
	line-height: 24px;
	color: #aaa;
}
.startsearch .ac:before {
	content: 'x';
	margin: 0;
	border: none;
}
.startsearch .ac:after {
	display: none;
}
</style>
