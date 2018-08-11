import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/home/Index'
// import Login from '@/components/login/Index'
Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    // {path: '/login',component:Login, titulo:'Login'},
    { path: '', component: Home, titulo: 'Home'},

    // { path: '*', redirect: '/' }


  ]
})
