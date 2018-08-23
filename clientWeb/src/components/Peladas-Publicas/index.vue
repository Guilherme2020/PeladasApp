<template>
  <v-app id="inspire">
    <my-header></my-header>

    <v-content style="margin-top: 10%">
      <h1>Peladas Publicas </h1>

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
              <v-toolbar dark color="red">
                <v-toolbar-title>Nome: {{ pelada.nome}}.</v-toolbar-title>
                <v-spacer></v-spacer>


              </v-toolbar>
              <v-card-text>
                <span class="headline black--text">Dono_id: {{pelada.dono}}</span>
              </v-card-text>
              <v-card-text>
                <span class="headline black--text">Tempo de duração:</span> <h2>{{pelada.configuracao.limite_gols}} </h2>
              </v-card-text>

            </v-card>

          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>


</template>
<style scoped>
  #inspire{
    margin-top: -68px ;
  }
</style>
<script>
  import axios from 'axios'
  import Header from './header/header'
  const url ='http://127.0.0.1:8000/api/peladas/';
  export default {
    components:{
       'my-header':Header
    },
    data () {
      return {

        peladas: [],
        error:{
          error:false,
          message: ''
        },
      }
    },
    mounted(){
      let authe = {
        headers: {
          'content-type': 'application/json'
        }

      };
      axios.get(url,{headers: authe})

        .then((response) => {
          console.log(response.data);
          this.peladas = response.data;
//           response.data;
        })
    }

  }
</script>
<style>

</style>
