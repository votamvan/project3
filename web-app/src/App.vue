<template>
  <div id="app" class="full-bg">
    
    <div class="hero__logo">
    </div>
    <MainApp/>
  </div>
  
</template>

<script>
import MainApp from './components/MainApp.vue'
import './assets/css/style.css'

export default {
  name: 'App',
  components: {
    MainApp
  }
}
</script>
<link rel="stylesheet"  href="https://pro.fontawesome.com/releases/v5.2.0/css/all.css" type="text/css" media="all">
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
