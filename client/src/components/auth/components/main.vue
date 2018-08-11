<template>
  <div >
    <header >
      <h3>SPA Peladas API</h3>
    </header>
    <div >
      <div></div>
      <div >
        <ul >
          <router-link tag="li" :to="{ name: 'auth.signin' }">
            <a>Sign in</a>
          </router-link>
          <router-link tag="li" :to="{ name: 'auth.signup' }">
            <a>Sign up</a>
          </router-link>
        </ul>
      </div>
      <div >
        <router-view></router-view>
      </div>
      <div>



      </div>
    </div>
  </div>
</template>

<script>
  export default {
  }
</script>

<style lang="css">
</style>
