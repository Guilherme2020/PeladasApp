<template>
  <v-toolbar style="margin-top: 5%;" dark color="red">
    <!--<v-spacer></v-spacer>-->
    <v-toolbar-title style="margin: 33%;text-transform: uppercase" class="white--text">
      PeladasApp
    </v-toolbar-title>
    <v-toolbar-items>

        <v-btn dark color="red" >
          <router-link style="color:white; text-decoration: none;"  :to="{ path: '/auth/login'  }" exact>LOGIN       </router-link>

        </v-btn>
      <v-btn  dark color="red" >Cadastrar </v-btn>
      <v-btn dark color="red" >Link </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>
