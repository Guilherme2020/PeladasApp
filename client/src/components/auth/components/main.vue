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
                <v-form>
                  <v-text-field prepend-icon="person" v-model="username" name="username" label="Login" type="text"></v-text-field>
                  <v-text-field id="password" prepend-icon="lock"  v-model="password" name="password" label="Password" type="password"></v-text-field>
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

            <v-card   key="pelada.id" class="elevation-12">
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
  const url ='http://127.0.0.1:8000/api/peladas/';

  export default {
    data () {
      return {
        username:'',
        password:'',
        peladas: [],
        login_message: false
      }
    },
    methods:{
      sigin(){
         const endpoint = 'http://127.0.0.1:8000/api/login';
          const headers = {
            'Content-Type': 'application/json',
          };
          const  payload = {
           "username":this.username,
            "password" : this.password
         };
          axios.post(endpoint,payload,{headers:headers})
            .then((response) => {
                console.log(response.data.token);
                localStorage.setItem("token",response.data.token)
            }).catch(err => {
              this.login_message = err
          })
      },
    },
    mounted (){
      axios.get(url)

        .then((response) => {
          console.log(response.data);
          this.peladas = response.data;
//           response.data;
        })
        .catch(error => {
          console.log(error)
        })

    },

  }
</script>

<style lang="css">
  #inspire{
    margin-top: -60px ;
  }
</style>
