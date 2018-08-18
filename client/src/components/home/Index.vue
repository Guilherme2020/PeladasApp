<template>
  <div>
    <h1>Peladas Login</h1>


    <h3>Seja Bem vindo:  {{user}}</h3>
    <h3>email: {{userEmail}}  </h3>




  </div>
</template>

<script>
  import axios from 'axios'
  import token from "../../services/token";
  const endpoint = 'http://127.0.0.1:8000/api/user-peladas/';

  export  default {
    data () {
      return {
        // user: {
        //   username: 'dono1',
        //   password: 'dono1',
        // },
      }
    },
      computed:{

        user(){
        	const { name} = this.$store.state.user;

        	return	`o Usuario logado é ${name}`
        },
        userEmail(){
          const {email} = this.$store.state.user;
          return `O email é  ${email}`
        },
        userName(){
            return this.$store.state.user.name

        },

      },
      mounted(){

        const token = localStorage.getItem('token');
        const auth = {
          headers: {Authorization:'Token '+ token}
        };
        // axios.post('http://127.0.0.1:8000/movies/', this.form, auth).then((response) => {
        //   router.push({ name: 'movie', params: { id: response.data.id } })
        // }, (err) => {
        //   this.showDismissibleAlert = true
        // })

          const token_export = sessionStorage.getItem("token");
          let authe = {
            headers: {
              Authorization:'Token '+ token_export
            }

          };

          axios.get(endpoint,{ headers: authe.headers }).then((response)=>{
            console.log(response.data)
          })
      }


    }


</script>
