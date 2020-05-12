import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

var Api = require('./apis.js');
let api = new Api();
Vue.prototype.api = api;

var Helper = require('./helper.js');
let helper = new Helper();
Vue.prototype.helper = helper;


Vue.config.productionTip = false

new Vue({
  router:router,
  render: h => h(App),
}).$mount('#app')
