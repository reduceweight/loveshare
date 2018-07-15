<template lang="html">
  <div class="container">
    <div class="m-balloon z-soaring"></div>
    <div id="language-switcher" class="cloud cloud-1">
      <router-link to="/home">首页</router-link>
    </div>
    <header>
      <div id="ribbon">
          <div class="subtitle date">3.15</div>
          <div class="title bride">Love</div>
          <div class="title groom">Share</div>
          <div class="subtitle year">2018</div>
      </div>
    </header>
    <div id="zone-beginning" class="moment first">
        &nbsp;
        <p class="scroll-hint">Scroll down</p>
        <p class="right"><strong>Hey!</strong>Nobody had the slightest idea what it would be like, when it all started...</p>
    </div>
    <div class="clouding cloud-1 cloud" id="cloud-0" style="top: 400px; margin-left: -450px;">
      <a href="/">说说</a>
    </div>
    <div class="clouding cloud-3 cloud" id="cloud-1" style="top: 500px; margin-left: 320px;">
      <a href="/">日志</a>
    </div>
    <div class="clouding cloud-bird cloud" id="cloud-2" style="top: 400px; margin-left: 450px;"></div>
    <div class="clouding cloud-2 cloud" id="cloud-3" style="top: 900px; margin-left: -320px;">
      <a href="/">游记</a>
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

<style lang="css">
body {
  background: #a7d3db; /* Old browsers */
  /* IE9 SVG, needs conditional override of 'filter' to 'none' */
  background: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/Pgo8c3ZnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgdmlld0JveD0iMCAwIDEgMSIgcHJlc2VydmVBc3BlY3RSYXRpbz0ibm9uZSI+CiAgPGxpbmVhckdyYWRpZW50IGlkPSJncmFkLXVjZ2ctZ2VuZXJhdGVkIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjAlIiB5MT0iMCUiIHgyPSIwJSIgeTI9IjEwMCUiPgogICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iI2E3ZDNkYiIgc3RvcC1vcGFjaXR5PSIxIi8+CiAgICA8c3RvcCBvZmZzZXQ9Ijg4JSIgc3RvcC1jb2xvcj0iI2NmZGRjOSIgc3RvcC1vcGFjaXR5PSIxIi8+CiAgICA8c3RvcCBvZmZzZXQ9Ijk0JSIgc3RvcC1jb2xvcj0iI2UyZTNjZSIgc3RvcC1vcGFjaXR5PSIxIi8+CiAgICA8c3RvcCBvZmZzZXQ9IjEwMCUiIHN0b3AtY29sb3I9IiNmY2VhYmQiIHN0b3Atb3BhY2l0eT0iMSIvPgogIDwvbGluZWFyR3JhZGllbnQ+CiAgPHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjEiIGhlaWdodD0iMSIgZmlsbD0idXJsKCNncmFkLXVjZ2ctZ2VuZXJhdGVkKSIgLz4KPC9zdmc+);
  background: -moz-linear-gradient(top,  #a7d3db 0%, #cfddc9 88%, #e2e3ce 94%, #fceabd 100%); /* FF3.6+ */
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#a7d3db), color-stop(88%,#cfddc9), color-stop(94%,#e2e3ce), color-stop(100%,#fceabd)); /* Chrome,Safari4+ */
  background: -webkit-linear-gradient(top,  #a7d3db 0%,#cfddc9 88%,#e2e3ce 94%,#fceabd 100%); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(top,  #a7d3db 0%,#cfddc9 88%,#e2e3ce 94%,#fceabd 100%); /* Opera 11.10+ */
  background: -ms-linear-gradient(top,  #a7d3db 0%,#cfddc9 88%,#e2e3ce 94%,#fceabd 100%); /* IE10+ */
  background: linear-gradient(to bottom,  #a7d3db 0%,#cfddc9 88%,#e2e3ce 94%,#fceabd 100%); /* W3C */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#a7d3db', endColorstr='#fceabd',GradientType=0 ); /* IE6-8 */
}
.m-balloon {
  position: fixed;
  left: 50%;
  margin-left: -304px;
  margin-top: -190px;
  width: 609px;
  height: 940px;
  background: url(/static/images/indexView/balloon.png) no-repeat center top;
  z-index: 100;
}
header {
    top: 110px;
    position: relative;
    height: 255px;
    background: url('/static/images/indexView/ribbon.png') center no-repeat;
    z-index: 100;
}
header #ribbon {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    width: 960px;
    padding-left: 30px;
    padding-right: 30px;
    height: 100%;
}
header div {
    position: absolute;
    text-shadow: 0px 1px 0px #ffffff;
}
header .title {
    font-family: "Sreda", "Georgia", "Times New Roman", serif;
    font-size: 3.7em;
    color: #8E6454;
    top: 45px;
}
header .subtitle {
    font-family: "Georgia", serif;
    font-size: 2.2em;
    color: #9B7664;
    top: 130px;
}
header .date {
    left: 110px;
}
header .year {
    right: 120px;
}
header .bride {
    left: 270px;
    -webkit-transform: rotate(353deg);
    -moz-transform: rotate(353deg);
    -o-transform: rotate(353deg);
    transform: rotate(353deg);
    writing-mode: lr-tb;
}

header .groom {
    right: 0%;
    margin-right: 230px;
    -webkit-transform: rotate(7deg);
    -moz-transform: rotate(7deg);
    -o-transform: rotate(7deg);
    transform: rotate(7deg);
    writing-mode: lr-tb;
}
#language-switcher {
  position: absolute;
  top: 60px;
  left: 50%;
  margin-left: 340px;
  text-align: center;
  vertical-align: middle;
  padding-top: 25px;
  height: 32px;
}
#language-switcher a, #language-switcher a:visited, #language-switcher a:active {
    color: #A3A5A5;
    font-size: 0.8em;
    text-decoration: none;
    padding: 0 10px;
}
#language-switcher a:hover {
    color: #83CFCB;
}
.moment {
    position: relative;
    width: 960px;
    margin-left: auto;
    margin-right: auto;
    height: 750px;
}
.moment.first {
    margin-top: 250px;
}
.moment p {
    position: absolute;
    width: 250px;
    top: 20%;
    z-index: 10;
    color: #666;
}
.moment p.scroll-hint {
    color: #FAFDFC;
    font-size: 20px;
    font-family: "Sreda", "Georgia", "Times New Roman", serif;
    background: url('/static/images/indexView/arrow.png') right 0px no-repeat;
    padding-right: 17px;
    width: 100px;
    animation: drumming-up 0.8s linear infinite;
    -o-animation: drumming-up 0.8s linear infinite;
    -webkit-animation: drumming-up 0.8s linear infinite;
    -moz-animation: drumming-up 0.8s linear infinite;
}
.moment p strong {
    font-family: "Sreda", "Georgia", "Times New Roman", serif;
    margin-top: 150px;
    margin-bottom: 13px;
    font-size: 1.5em;
    line-height: 1em;
    font-weight: 300;
    display: block;
    color: #F26A47;
}
.moment p.right {
    right: 0px;
}
.clouding {
    animation: cloud 5s linear infinite;
    -webkit-animation: cloud 5s linear infinite;
    -moz-animation: cloud 5s linear infinite;
    -o-animation: cloud 5s linear infinite;
}
.z-soaring {
    animation-name: soar;
    animation-duration: 4s;
    animation-iteration-count: infinite;
    animation-timing-function: ease-in-out;
    -webkit-animation-name: soar;
    -webkit-animation-duration: 4s;
    -webkit-animation-iteration-count: infinite;
    -webkit-animation-timing-function: ease-in-out;
    -moz-animation-name: soar;
    -moz-animation-duration: 4s;
    -moz-animation-iteration-count: infinite;
    -moz-animation-timing-function: ease-in-out;
    z-index: 30;
}
.cloud {
    left: 50%;
    position: absolute;
    z-index: 0;
    background-image: url('/static/images/indexView/clouds.png');
    background-repeat: no-repeat;
}
.cloud-1 {
    width: 143px;
    height: 57px;
    background-position: 0px 0px;
}
.cloud-2 {
    width: 156px;
    height: 64px;
    background-position: 0px -57px;
}
.cloud-3 {
    width: 308px;
    height: 87px;
    background-position: 0px -121px;
}
.cloud-bird {
    width: 48px;
    height: 32px;
    background: url('/static/images/indexView/bird.png');
}
@keyframes soar {
  50% {
    transform: translate(0, -7px);
  }
}

@-webkit-keyframes soar {
  50% {
    -webkit-transform: translate(0, -7px);
  }
}

@-moz-keyframes soar {
  50% {
    -moz-transform: translate(0, -7px);
  }
}
</style>
