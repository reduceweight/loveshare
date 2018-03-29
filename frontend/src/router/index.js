import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

const routes = [
  {
    path: '/',
    name: 'index',
    component: (resolve) => require(['@/pages/index'], resolve)
  },
  {
    path: '/home',
    name: 'home',
    component: (resolve) => require(['@/pages/home'], resolve)
  },
  {
    path: '/article',
    name: 'article',
    component: (resolve) => require(['@/pages/article'], resolve)
  }
]
export default routes
