<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login Peladas</v-toolbar-title>
                <v-spacer></v-spacer>

              </v-toolbar>
              <v-card-text>
                <div class="" v-if="error.error">
                    {{error.message}}
                </div>
                <v-form>
                  <v-text-field prepend-icon="person" v-model="user.username" name="username" label="Login" type="text"></v-text-field>
                  <v-text-field id="password" prepend-icon="lock"  v-model="user.password" name="password" label="Password" type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn v-on:click.prevent="sigin" color="primary">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-content>
      <h1>Area Publica </h1>

      <v-container
        fluid
        grid-list-md
        fill-height
      >
        <v-layout

          row wrap
          >
          <v-flex
            xs12 sm4 md5
            v-for="pelada of peladas"

          >

            <v-card    class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Nome: {{ pelada.nome}}.</v-toolbar-title>
                <v-spacer></v-spacer>


              </v-toolbar>
              <v-card-text>
                <span class="headline black--text">Dono:</span> {{pelada.dono.username}}
              </v-card-text>
              <v-card-text>
                 <span class=" headline black--text">email :</span> {{pelada.dono.email}}

              </v-card-text>
            </v-card>

          </v-flex>
        </v-layout>
      </v-container>
    </v-content>

  </v-app>
</template>

<script>
  import axios from 'axios'
  // import router from "./router/index";
  const url ='http://127.0.0.1:8000/api/peladas/';

  export default {
    data () {
      return {
        user:{
          username:'',
          password:'',
        },
        error:{
          error:false,
          message: ''
        },
        peladas: [],
        login_message: false,


      }
    },
    methods:{
      sigin(){
         // const endpoint = 'http://127.0.0.1:8000/api/login';
         //  const headers = {
         //    'Content-Type': 'application/json',
         //  };
         //  const  payload = {
         //   "username":this.username,
         //    "password" : this.password
         // };
          // axios.post(endpoint,payload,{headers:headers})
          //   .then((response) => {
          //       console.log(response.data.token);
          //       console.log(response.data.user_name);
          //       console.log(response.data.user_id);
          //       console.log(response.data.user_email);
          //       localStorage.setItem("token",response.data.token);
          //       const  user_name = localStorage.setItem("user_name",response.data.user_name);
          //
          //   }).catch(err => {
          //     this.login_message = err
          // })
          this.$store.dispatch('login',this.user)
            .then((response)=>{

            }).catch((respoonseErr) => {
              console.log(respoonseErr)
            })
            // .catch(responseError => {
            //   this.error.error = true;
            //   if(responseError.status === 404){
            //       this.error.message  = responseError.data.message
            //   }else{
            //       this.error.message = 'login falhou.'
            //   }
            //
            // })

      },
    },
    mounted (){
      axios.get(url)

        .then((response) => {
          console.log(response.data);
          this.peladas = response.data;
//           response.data;
        })

    },

  }
</script>

<style lang="css">
  #inspire{
    margin-top: -60px ;
  }
</style>
