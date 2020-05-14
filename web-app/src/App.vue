<template>
  <div id="app">
    
   <div class="container">
     <div class="col-sm-8 col-sm-offset-2">
       <span style="font-size: 90px; color: white; font-weight: 300;">boot</span>
       <span style="font-size: 110px; color: white; font-weight: 300;">U</span>
       <span style="font-size: 90px; color: white; font-weight: 300;">p</span>
     </div>
    </div>
    <MainApp/>
    <div style="padding: 15px;
    font-size: 15px;
    color: rgb(33, 33, 33);
    font-weight: 100;
    float: left;
    background: #ffffffc7;
    border-radius: 0px 0px 15px 0px;">
      <div>
       <span>Professor: Mohamed Abdelrazik</span>
      </div>
      <div>
       <span>Tam Van Vo - 610746</span>
      </div>
      <div>
       <span>Quynh Pham - 610716</span>
      </div>
      <div>
       <span>Samsher Bahadur Rana - 611060</span>
      </div>
      <div>
       <span>Van Vong Tran - 610772</span>
      </div>
      <div>
       <span>Yared Geberetsadik Beyene - 110466</span>
      </div>
    </div>
  </div>
  
</template>

<script>
import './assets/css/style.css'
import MainApp from './components/MainApp.vue'

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
