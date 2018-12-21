// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Routers from './router'
import VueRouter from 'vue-router'
import Util from './libs/util'
import axios from 'axios'
import BaseLayout from './layout'

Vue.use(VueRouter)
Vue.config.productionTip = false
Vue.prototype.$http = axios

// 路由配置
const RouterConfig = {
  // mode: 'history',
  routes: Routers
}

const router = new VueRouter(RouterConfig)

router.beforeEach((to, from, next) => {
  Util.title(to.meta.title)
  next()
})

router.afterEach((to, from, next) => {
  window.scrollTo(0, 0)
})
Vue.component('base-layout', BaseLayout)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
