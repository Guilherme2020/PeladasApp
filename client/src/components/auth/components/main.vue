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
                <v-tooltip bottom>

                  <span>Source</span>
                </v-tooltip>
                <v-tooltip right>
                  <v-btn slot="activator" icon large href="https://codepen.io/johnjleider/pen/wyYVVj" target="_blank">
                    <v-icon large>mdi-codepen</v-icon>
                  </v-btn>
                  <span>Codepen</span>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field prepend-icon="person" name="login" label="Login" type="text"></v-text-field>
                  <v-text-field id="password" prepend-icon="lock" name="password" label="Password" type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-content>
      <h1>Area Publica </h1>
      <v-container fluid fill-height>
        <v-layout >
          <v-flex xs12 sm8 md4>
            <div>
            <v-card  class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Peladas.</v-toolbar-title>
                <v-spacer></v-spacer>


              </v-toolbar>
              <v-card-text>
                {{peladas.nome}}
              </v-card-text>
            </v-card>
            </div>
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
        peladas: []
      }
    },

    mounted (){
      axios.get(url).then( response => (this.peladas = response.data))


    },

  }
</script>

<style lang="css">
  #inspire{
    margin-top: -60px ;
  }
</style>
