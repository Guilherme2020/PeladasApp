import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/home/Index'
import Login from '@/components/auth/components/main'

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [

    {path: '/auth/login',component:Login, titulo:'Login'},
    { path: '/home', name: 'Home',component: Home, titulo: 'Home'},

    // { path: '*', redirect: '/' }


  ]
})
