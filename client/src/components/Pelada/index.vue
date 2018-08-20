<template>
      <v-app id="inspire">
        <my-header></my-header>

        <div style="margin-top: 5%">
          <h1>Detalhes da Sua Pelada</h1>

          <!--{{sucess_data}}-->

          <h2>Nome: {{peladaUserId.nome}}</h2>
          <!--<h1>{{getIdRouter}}</h1>-->
        </div>

        <h1>Jogadores Da sua pelada</h1>

        <!--<div style="margin: 200px">-->
            <!--<th>id</th>-->
            <!--<th>nome</th>-->
            <!--<th>nota</th>-->

            <!--<tr v-for="peladaUse of peladaUserId.jogadores">-->
              <!--<td>{{peladaUse.id}}</td>-->
              <!--<td>{{peladaUse.nome}}</td>-->
              <!--<td>{{peladaUse.rating}}</td>-->
            <!--</tr>-->
        <!--</div>-->

        <v-container  fluid
                      grid-list-md
                      fill-height>
          <v-data-table  :headers="headers" :items="peladaUserId.jogadores">
            <template slot="items" slot-scope="props">
              <td>{{props.item.id}}</td>
              <td>{{props.item.nome}}</td>
              <!--<td>{{props.item.rating}}</td>-->
              <!--<my-star   v-bind:star-size="30"  active-color="red" v-model="dados.raiting"></my-star>-->
              <td>
                <my-star v-bind:read-only=true v-bind:show-rating=false	  v-bind:star-size="20"  active-color="red" v-model="props.item.rating"></my-star>

              </td>
              <td>{{props.item.created_at | date}}</td>
              <td>{{props.item.pelada}}</td>
              <td class="justify-center layout px-0">
                <v-btn @click="edit(props.item)" icon>
                  <v-icon small>edit</v-icon>
                </v-btn>
                <v-btn @click="remove(props.item)" icon>
                  <v-icon small>delete</v-icon>
                </v-btn>
              </td>
            </template>
          </v-data-table>
        </v-container>

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
    import Star  from 'vue-star-rating'

    const endpoint = 'http://127.0.0.1:8000/api/user-peladas/';

    const endpointPelada = 'http://127.0.0.1:8000/api/pelada/';
    export default {
      components:{
        "my-header": Header, "my-star": Star


      },
      props:['id'],
      computed:{
          getIdRouter:function(){
            if(this.id != null){
              return this.id
            }
          }
      },
      data () {
        return{
          sucess_data: response,
          peladaUserId:[],
          headers: [
            {text: 'ID', value: 'id', align: 'left'},
            {text: 'Nome', value: 'nome', align: 'left'},
            {text: 'Avaliação', value: 'rating', align: 'left'},
            {text: 'Cadastrado em', value: 'created_at', align: 'left'},
            {text: 'Pelada', value: 'pelada'},
            {text: 'Actions', sortable: false, align: 'left'}
          ],
          pelada: {
            "id": 1,
            "jogadores": [
              {
                "id": 1,
                "nome": "Willian",
                "rating": 4,
                "created_at": "2018-06-30T15:01:07.229883-03:00",
                "pelada": 1
              },
              {
                "id": 2,
                "nome": "Neymar",
                "rating": 4,
                "created_at": "2018-06-30T15:01:07.569465-03:00",
                "pelada": 1
              },
              {
                "id": 3,
                "nome": "Cristiano Ronaldo",
                "rating": 4,
                "created_at": "2018-06-30T15:01:07.886579-03:00",
                "pelada": 1
              },
              {
                "id": 4,
                "nome": "Messi",
                "rating": 4,
                "created_at": "2018-06-30T15:01:08.212083-03:00",
                "pelada": 1
              },
              {
                "id": 5,
                "nome": "Neuer",
                "rating": 4,
                "created_at": "2018-06-30T15:01:08.568027-03:00",
                "pelada": 1
              },
              {
                "id": 6,
                "nome": "Buffon",
                "rating": 4,
                "created_at": "2018-06-30T15:01:08.956278-03:00",
                "pelada": 1
              },
              {
                "id": 7,
                "nome": "Casemiro",
                "rating": 4,
                "created_at": "2018-06-30T15:01:09.274931-03:00",
                "pelada": 1
              },
              {
                "id": 8,
                "nome": "Marcelo",
                "rating": 4,
                "created_at": "2018-06-30T15:01:09.566529-03:00",
                "pelada": 1
              },
              {
                "id": 9,
                "nome": "Rogerio Ceni",
                "rating": 4,
                "created_at": "2018-06-30T15:01:09.863201-03:00",
                "pelada": 1
              },
              {
                "id": 10,
                "nome": "Kane",
                "rating": 4,
                "created_at": "2018-06-30T15:01:10.151604-03:00",
                "pelada": 1
              },
              {
                "id": 13,
                "nome": "Gui",
                "rating": 2,
                "created_at": "2018-08-19T15:47:47.366892-03:00",
                "pelada": 1
              },
              {
                "id": 14,
                "nome": "Eu",
                "rating": 2,
                "created_at": "2018-08-19T15:54:10.542812-03:00",
                "pelada": 1
              },
              {
                "id": 15,
                "nome": "Gui",
                "rating": 5,
                "created_at": "2018-08-19T16:01:06.885722-03:00",
                "pelada": 1
              },
              {
                "id": 16,
                "nome": "gui",
                "rating": 5,
                "created_at": "2018-08-19T16:07:32.299903-03:00",
                "pelada": 1
              },
              {
                "id": 17,
                "nome": "yyy",
                "rating": 5,
                "created_at": "2018-08-19T16:18:04.776367-03:00",
                "pelada": 1
              },
              {
                "id": 18,
                "nome": "elielda",
                "rating": 1,
                "created_at": "2018-08-19T17:01:19.438562-03:00",
                "pelada": 1
              },
              {
                "id": 19,
                "nome": "eliane2",
                "rating": 2,
                "created_at": "2018-08-19T17:07:29.801309-03:00",
                "pelada": 1
              },
              {
                "id": 20,
                "nome": "Yuri",
                "rating": 5,
                "created_at": "2018-08-19T17:50:30.527663-03:00",
                "pelada": 1
              },
              {
                "id": 21,
                "nome": "Joao",
                "rating": 5,
                "created_at": "2018-08-19T17:54:21.120028-03:00",
                "pelada": 1
              },
              {
                "id": 22,
                "nome": "eu",
                "rating": 5,
                "created_at": "2018-08-19T18:03:02.230280-03:00",
                "pelada": 1
              }
            ],
            "dono": {
              "username": "dono1",
              "email": "dono1@dono1.com"
            },
            "nome": "PELADA 1"
          }

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
          },
        edit(item){
          alert(`Edit ${item.nome}`)
        },
        remove(item){
          alert(`Remove ${item.nome}`)
        }
      },
      filters: {
        date(v){
          const date = new Date(v);
          const d = date.getDate();
          const m = date.getMonth() + 1;
          const y = date.getFullYear();
          return `${d < 10 ? '0' + d : d}/${m < 10 ? '0' + m : m}/${y}`
        }

      },
      created(){
        // const id = sessionStorage.getItem("id");
        const token_export = sessionStorage.getItem("token");
        let authe = {
          headers: {
            Authorization:'Token '+ token_export
          }

        };
        axios.get(`${endpointPelada}${this.getIdRouter}`,{headers:authe.headers })
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
