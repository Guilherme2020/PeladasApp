<script>
  import router from '../../../router/index'

  export default {
    data: () => ({
      types: ['Places to Be', 'Places to See'],
      cards: ['Good', 'Best', 'Finest'],
      socials: [
        {
          icon: 'fab fa-facebook',
          color: 'indigo'
        },
        {
          icon: 'fab fa-linkedin',
          color: 'cyan darken-1'
        },
        {
          icon: 'fab fa-instagram',
          color: 'red lighten-3'
        }
      ]
    }),

    methods: {
      logout(){

          sessionStorage.removeItem("token");
          sessionStorage.removeItem("id");
          sessionStorage.removeItem("username");

          router.push({path: '/auth/login'})

      },
      getImage () {
        const min = 550
        const max = 560

        return Math.floor(Math.random() * (max - min + 1)) + min
      }
    }
  }
</script>

<style scoped>

</style>
<template>

  <v-toolbar dark color="white">
    <v-spacer></v-spacer>
    <v-toolbar-title  style="margin: 30%" class= "red--text">PeladasApp</v-toolbar-title>
    <v-toolbar-items style="margin:10px;">
        <v-btn dark color="white" style="color:red">
          Jogadores
        </v-btn>
        <v-btn dark color="white" style="color:red">
          <router-link style="color:red; text-decoration: none;"  :to="{ path: '/configuracao'  }" exact>Configuracao
          </router-link>

        </v-btn>

      <v-btn
        @click="logout()"
        dark color="white"
        style="color:red">
        Sair

      </v-btn>


    </v-toolbar-items>
  </v-toolbar>

</template>
