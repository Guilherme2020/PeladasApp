
<template>
  <v-app id="inspire">

    <my-header></my-header>

    <v-content style="margin-top: 5%">
      <h1> Configurações </h1>

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
            v-for="configuracao of configuracaoList"

          >

            <v-card    hover>
              <v-toolbar dark color="red">
                <v-toolbar-title>Nome: {{ configuracao.id}}.</v-toolbar-title>
                <v-spacer></v-spacer>


              </v-toolbar>
              <v-card-text>
                <span class="headline black--text">Tempos: {{configuracao.tempos}}</span>
              </v-card-text>
              <v-card-text>
                <span class="headline black--text">Tempo de duração:</span> <h2>{{configuracao.tempo_duracao}} </h2>
              </v-card-text>
              <v-card-text>
                <span class="headline black--text">Limite de Gol:</span> <h2>{{configuracao.limite_gols}} </h2>
              </v-card-text>
              <v-card-text>
                <span class="headline black--text">quantidade de _jogadores:</span> <h2>{{configuracao.qtd_jogadores}} </h2>
              </v-card-text>
              <v-card-text>
                <span class="headline black--text">Tipo Sorteio:</span> <h2>{{configuracao.tipo_sorteio}} </h2>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon

                  >
                    visibility
                  </v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon>edit</v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon>delete</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>

          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <v-layout row wrap>
      <v-flex xs12 sm12 md6>
        <v-btn
          absolute
          dark
          fab
          bottom
          right
          color="red"
        >
          <v-icon
          >
            add
          </v-icon>
        </v-btn>
      </v-flex>
    </v-layout>

  </v-app>


</template>

<style scoped>
  #inspire{
    margin-top: -68px ;
  }
</style>

<script>
  import Header from './header/header'
  import axios from 'axios'
  const endpoint = 'http://127.0.0.1:8000/api/configuracao/';
  export default {
    components:{
      'my-header': Header

    },

    data(){
      return{
         configuracaoList : []
      }
    },

    created(){

      const token_export = sessionStorage.getItem("token");
      let authe = {
        headers: {
          Authorization:'Token '+ token_export
        }

      };

      axios.get(endpoint,{ headers: authe.headers })
        .then((response)=>{
          console.log(response.data);
          this.configuracaoList = response.data
        });

    }


  }

</script>

