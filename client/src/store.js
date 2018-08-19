
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import Token from './services/token'
import SessionStorage from './services/session-storage'
import router from "./router/index";

Vue.use(Vuex);

const  userName =  window.sessionStorage.getItem("username");
const userEmail = window.sessionStorage.getItem("email");
const state = {
  user:{
    name: userName,
    email: userEmail
  },
};

const mutations = {

};

const actions = {

    login(context, {username,password}){
      // const headers = {
      //   'Content-Type': 'application/json',
      // };
      Token.acessToken(username,password)

      // router.push({ name: 'Home' })

      // axios.post('http://127.0.0.1:8000/api/login',{username,password},{headers:headers})
      //   .then((response) => {
      //           if(response.status == 200){
      //             console.log(response.data.token)
      //             console.log(response.data.user_name);
      //             console.log(response.data.user_id);
      //             console.log(response.data.user_email);
      //             router.push({ name: 'Home' })
      //
      //
      //           }
      //   })
      //   .catch(error => {
      //     console.log(error.message)
      //   })

    }
};
export default new Vuex.Store({

  state,
  getters:{

  },
  mutations,
  actions
})


