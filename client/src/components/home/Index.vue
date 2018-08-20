<template>
  <v-app id="inspire">
    <header-user ></header-user>

    <v-content>
      <div style="margin-top: 5%">

        <h3>Seja Bem vindo:  <span>{{ user }}</span></h3>
        <h3>email: {{ email }}  </h3>
      </div>
      <div style="margin-top: 5%">
        <h2>Minhas Peladas</h2>

      </div>
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
            v-for="pelada of peladaUser"
            :key="pelada.nome"
          >
            <!--:src="prato.image"-->
            <router-link>

            </router-link>
            <v-card  hover >

              <v-toolbar dark color="red">
                <v-toolbar-title>Nome-Pelada: {{pelada.nome}} </v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-media
                  src="https://conteudo.imguol.com.br/c/esporte/6c/2017/09/06/neymar-e-mbappe-se-encontram-pela-primeira-vez-em-treino-do-psg-1504716753721_615x300.jpg"
                  height="200px"
              >

              </v-card-media>
              <v-card-text>
                <span class="headline black--text">Id: {{pelada.id}}</span>
              </v-card-text>
              <v-card-text>
                <span class="headline black--text">Dono: {{pelada.dono}}</span>
              </v-card-text>
              <v-card-text>
                <span class=" headline black--text">Limite de Gols: {{pelada.configuracao.limite_gols}} </span>

              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon
                    @click="peladaId(pelada.id)"
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

  </v-app>




    <!--<div style="margin-top: 40px" >-->
       <!--<ul  style="list-style: none" v-for="pelada of peladaUser" >-->

         <!--<li>Username: {{pelada.dono.username}}</li>-->
         <!--<li>Email: {{pelada.dono.email}}</li>-->
         <!--<li>Nome da Pelada: {{pelada.nome}}</li>-->
         <!--<li>Tipo Configuracao: {{pelada.configuracao}}</li>-->

       <!--</ul>-->
    <!--</div>-->

    <!--<div style="margin-top: 40px" >-->

    <!--</div>-->
    <!--<li>id: {{peladaUserId.id}}</li>-->
    <!--<li>nome pelada: {{peladaUserId.nome}}</li>-->
    <!--</div>-->

  <!--</div>-->
</template>

<!--<v-app id="inspire">-->
  <!--<my-header></my-header>-->

  <!--<v-content style="margin-top: 10%">-->
    <!--<h1>Peladas Publicas </h1>-->

    <!--<v-container-->
      <!--fluid-->
      <!--grid-list-md-->
      <!--fill-height-->
    <!--&gt;-->
      <!--<v-layout-->

        <!--row wrap-->
      <!--&gt;-->
        <!--<v-flex-->
          <!--xs12 sm4 md5-->
          <!--v-for="pelada of peladas"-->

        <!--&gt;-->

          <!--<v-card    class="elevation-12">-->
            <!--<v-toolbar dark color="red">-->
              <!--<v-toolbar-title>Nome: {{ pelada.nome}}.</v-toolbar-title>-->
              <!--<v-spacer></v-spacer>-->


            <!--</v-toolbar>-->
            <!--<v-card-text>-->
              <!--<span class="headline black&#45;&#45;text">Dono:</span> {{pelada.dono.username}}-->
            <!--</v-card-text>-->
            <!--<v-card-text>-->
              <!--<span class=" headline black&#45;&#45;text">email :</span> {{pelada.dono.email}}-->

            <!--</v-card-text>-->
          <!--</v-card>-->

        <!--</v-flex>-->
      <!--</v-layout>-->
    <!--</v-container>-->
  <!--</v-content>-->
<!--</v-app>-->



<script>
  import axios from 'axios'
  import token from "../../services/token";
  import Header from './header/header';
  import store from '@/store'
  import {mapState} from 'vuex'
  import router from '../../router/index'
  // import {store} from '../../store'
  const endpoint = 'http://127.0.0.1:8000/api/user-peladas/';

  const endpointPelada = 'http://127.0.0.1:8000/api/pelada/';



  export  default {

    components: {
      'header-user' : Header
    },
    data () {
      return {
        peladaUser:[],
        pelada: '',
        peladaUserId:[],
        cards: [
          { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
        ]
      }
    },
      computed:{
        ...mapState({
            user: state => state.user.name,
            email: state => state.user.email
        }),
        // user(){
        // 	const {name} = this.$store.state.user;
        //
        // 	return	`${name}`
        // },
        // userEmail(){
        //   const {email} = this.$store.state.user;
        //   return `${email}`
        // },
        userName(){
            return this.store.state.user.name

        },

      },
      methods:{

          peladaId(id){
            // const id = this.peladaUser[1].id;
            // alert(JSON.stringify(id));
            router.push(
              {
                path: `/pelada/`+id
              }
            )

          }
      },
      mounted(){
          const token_export = sessionStorage.getItem("token");
          let authe = {
            headers: {
              Authorization:'Token '+ token_export
            }

           };

          axios.get(endpoint,{ headers: authe.headers })
            .then((response)=>{
                console.log(response.data);
                    this.peladaUser = response.data
            });


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
