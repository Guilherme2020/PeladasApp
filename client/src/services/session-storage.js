export default {

  set(key,value){
      window.sessionStorage[key] = value;
      return window.sessionStorage[key];
  },
  get(key, defaultValue){
      return window.sessionStorage[key] || defaultValue;
  },
  remove(key){
    return window.sessionStorage.removeItem(key);
  },

  setUsername(key,value){
    window.sessionStorage[key] = value;
    return window.sessionStorage[key];

  },
  getUsername(key){
      return window.sessionStorage[key]
  },
  setUserEmail(key,value){
      window.sessionStorage[key]  = value;
      return window.sessionStorage[key];
  },
  getUserEmail(key){
      return window.sessionStorage[key]
  },

  setObject(key,value){
    window.sessionStorage[key] = JSON.stringify(value);
    return this.getObject(key);
  },

  getObject(key){
    return JSON.parse(window.sessionStorage[key] || null);
  }

};
