import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/home/Index'
import Pelada from '@/components/Pelada/index'
import Login from '@/components/auth/components/main'
import PeladasPublicas from '@/components/Peladas-Publicas/index'
import AddJogador from '@/components/Pelada/form/add-player'
Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {path: '/peladas',component: PeladasPublicas, titulo: 'Peladas'},
    {path: '/auth/login',component:Login, titulo:'Login'},
    { path: '/home', name: 'Home',component: Home, titulo: 'Home'},
    { path: '/pelada/:id',name:'Pelada',component:Pelada, titulo: 'Pelada'},
    {path: '/pelada/:id/jogador-add',name:'AddJogador',component:AddJogador,titulo:'AddJogador'},
    { path: '*', redirect: '/peladas' },
    // {path: "/configuracao",name: "",component:'',titulo:''}


  ]
})
