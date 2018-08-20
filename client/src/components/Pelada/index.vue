<template>
      <v-app id="inspire">
        <my-header></my-header>

        <div style="margin-top: 5%">
          <h1>Detalhes da Sua Pelada</h1>

          <!--{{sucess_data}}-->

          <h2>Nome: {{peladaUserId.nome}}</h2>

        </div>

        <h1>Jogadores Da sua pelada</h1>

        <div style="margin: 200px">
            <th>id</th>
            <th>nome</th>
            <th>nota</th>

            <tr v-for="peladaUse of peladaUserId.jogadores">
              <td>{{peladaUse.id}}</td>
              <td>{{peladaUse.nome}}</td>
              <td>{{peladaUse.rating}}</td>
            </tr>
        </div>

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
                @click="createdPlayer()"
              >
                add
              </v-icon>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-app>


</template>
<script>
    import response from './form/add-player'

    import Header from "../home/header/header"
    import axios from 'axios';
    import router from '../../router/index'
    const endpoint = 'http://127.0.0.1:8000/api/user-peladas/';

    const endpointPelada = 'http://127.0.0.1:8000/api/pelada/';
    export default {
      components:{
        "my-header": Header
      },
      data () {
        return{
          sucess_data: response,
          peladaUserId:[]
        }
      },
      methods:{

          createdPlayer(){
            const id = this.peladaUserId.id;
            router.push(
              {
                path: '/pelada/'+id+'/jogador-add'

              }
            )
          }
      },
      created(){
        const id = sessionStorage.getItem("id");
        const token_export = sessionStorage.getItem("token");
        let authe = {
          headers: {
            Authorization:'Token '+ token_export
          }

        };
        axios.get(`${endpointPelada}${id}`,{headers:authe.headers })
          .then((response)=>{
            console.log(response.data);

            this.peladaUserId = response.data;
          });
      }

    }
</script>
<style scoped>
  #inspire{

  }
</style>
