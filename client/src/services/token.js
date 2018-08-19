import SessionStorage from './session-storage'
import {Token} from './resources'
import router from "../router/index";

export default {

    get token(){
        return SessionStorage.get('token')
    },
    set token(value){
      SessionStorage.set('token',value)
    },
    get userName(){
        return SessionStorage.getUsername('username')
    },
    set userName(value){
        SessionStorage.setUsername('username',value)
    },
    set userEmail(value){
        SessionStorage.setUserEmail('email',value)
    },
    get userEmail(){
        return SessionStorage.getUserEmail('email')
    },
    set userId(value){
      SessionStorage.setUserId('id',value)
    },
    get userId(){
        return SessionStorage.getUserId('id')
    },

    acessToken(username,password){

        return Token.acessToken(username,password).then((response) => {
          this.token = response.data.token;

          console.log(response.data.user_name);

          this.userName = response.data.user_name;

          console.log(response.data.user_email);

          this.userEmail = response.data.user_email;

          this.userId = response.data.user_id;

          console.log(response.data.user_id);
          router.push({ name: 'Home' })

        })
          .catch((responseErr) => {
            console.log(responseErr)


          })
    },
    getAuthorizationHeader(){
      return `Bearer ${this.token}`;
    }

  // axios.post('http://127.0.0.1:8000/api/login',{username,password},{headers:headers})
  //   .then((response) => {
  //           if(response.status == 200){
  //             console.log(response.data.token)
  //             console.log(response.data.user_name);
  //             console.log(response.data.user_id);
  //             console.log(response.data.user_email);
  //             router.push({ name: 'Home' })
  //
  //
  //           }
  //   })
  //   .catch(error => {
  //     console.log(error.message)
  //   })




}
