// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from './store'
import Vuex from 'vuex'
import SessionStorage from './services/session-storage'


Vue.use(VueAxios, axios);
Vue.use(Vuetify);
Vue.config.productionTip = false;
Vue.use(Vuex);
/* eslint-disable no-new */

// Vue.http.headers.common['Access-Control-Allow-Origin'] = true;
// axios.http.headers.common['Access-Control-Allow-Origin'] = '*';
window.axios = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*'
};
new Vue({

  store,
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
