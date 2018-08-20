<template>
    <v-app id="inspire">
      <v-toolbar dark color="white">
        <v-spacer></v-spacer>
        <v-toolbar-title  style="margin: 43%" class= "red--text">Adicionar Jogador</v-toolbar-title>

      </v-toolbar>
      <!--<div style="margin-top: 10%">-->
        <!--<h1>Adicionar Jogador</h1>-->

      <!--</div>-->
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
          <v-form v-model="valid">
            <v-text-field
              v-model="dados.name"
              :rules="nameRules"
              :counter="10"
              label="Name"
              required
            ></v-text-field>
            <!--<v-text-field-->
              <!--v-model="dados.raiting"-->
              <!--:rules="raitingRules"-->
              <!--label="Raiting"-->
              <!--required-->
            <!--&gt;</v-text-field>-->

            <my-star   v-bind:star-size="30"  active-color="red" v-model="dados.raiting"></my-star>

          </v-form>
           <v-btn
             dark color="red"
             style="color:white"
             @click="postData()"

           >
             Adicionar
           </v-btn>

          </v-flex>
        </v-layout>
      </v-container>
    </v-app>

</template>
<script>
  import axios from 'axios'
  import router from '../../../router/index'
  import Star  from 'vue-star-rating'
  const  endpointAddJogador = 'http://127.0.0.1:8000/api/jogadores/';
  export const response = this.sucess;
  export default {
    components:{
      "my-star": Star
    },
    data: () => ({
      valid: false,
      select: null,
      sucess: '',
      items: [

      ],
      dados:{
        name: '',
        raiting: '',
      },

      nameRules: [
        v => !!v || 'Name this player required',
        v => v.length <= 10 || 'Name must be less than 10 characters'
      ],
      raitingRules: [
        v => !!v || 'Raiting is Required',
        v => v.valueOf() <= 5 || 'Raiting ultrapassou'
        // v => /.+@.+/.test(v) || 'E-mail must be valid'
      ]
    }),
    created(){

    },
    methods:{
      postData(){
          const id = sessionStorage.getItem("id");

          const token_export = sessionStorage.getItem("token");
          const authe = {
            headers: {

              Authorization:'Token '+ token_export
            }

          };
          const  data = {
              "nome": this.dados.name,
              "rating": this.dados.raiting,
              "pelada": sessionStorage.getItem("id")
          };
          axios.post("http://127.0.0.1:8000/api/jogadores/",data,{headers:authe.headers})
            .then((response)=>{
                console.log(response);
                this.sucess = response.status;
                router.push(
                {
                  path: '/pelada/'+id

                }
              )
            })
            .catch(err =>{
                console.log(err.message)
          })

      },
    }
  }
</script>
<style>

</style>
