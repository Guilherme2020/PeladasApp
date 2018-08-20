<template>
  <v-toolbar style="margin-top: 5%;" dark color="white">
    <!--<v-spacer></v-spacer>-->
    <v-toolbar-title style="margin:35%;text-transform: uppercase" class="red--text">
      PeladasApp
    </v-toolbar-title>
    <v-toolbar-items>

      <v-btn dark color="white" >
        <router-link style="color:red; text-decoration: none;"  :to="{ path: '/peladas'  }" exact>Pagina Inicial</router-link>

      </v-btn>
      <v-btn  dark color="white" style="color:red" >Cadastrar </v-btn>

    </v-toolbar-items>
  </v-toolbar>
</template>

<style>

</style>

<script>

</script>
