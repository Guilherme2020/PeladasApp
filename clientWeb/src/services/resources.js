import Vue from 'vue';
import axios from 'axios';

import interceptor from './interceptors'
// require('./interceptors')
export class Token {
  static acessToken(username,password){
    const headers = {
      'Content-Type': 'application/json',
    };
    return  axios.post('http://127.0.0.1:8000/api/login',{username,password},{headers:headers});
  }
}
const USER  = ''
