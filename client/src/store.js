
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

import router from "./router/index";

Vue.use(Vuex);

const state = {

};

const mutations = {

};

const actions = {

    login(context, {username,password}){
      const headers = {
        'Content-Type': 'application/json',
      };

      axios.post('http://127.0.0.1:8000/api/login',{username,password},{headers:headers})
        .then((response) => {
                if(response.status == 200){
                  console.log(response.data.token)
                  console.log(response.data.user_name);
                  console.log(response.data.user_id);
                  console.log(response.data.user_email);
                  // this.$router.push(Home)
                  router.push({ name: 'Home' })
                  // this.$router.push({titulo: 'Home'})


                }
        })
        .catch(error => {
          console.log(error.message)
        })

    }
};
export default new Vuex.Store({

  state,
  getters:{

  },
  mutations,
  actions
})


