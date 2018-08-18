<template>
  <div>
    <h1>Peladas Login</h1>


    <h3>Seja Bem vindo  {{user}}</h3>
    <h3>email: {{userEmail}}</h3>
  </div>
</template>

<script>
    export  default {

      computed:{

        user(){
        	const { name} = this.$store.state.user;

        	return	`o Usuario logado é ${name}`
        },
        userEmail(){
          const {email} = this.$store.state.user;
          return `O emai é ${email}`
        },
        userName(){
            return this.$store.state.user.name

        },

      }



    }


</script>
