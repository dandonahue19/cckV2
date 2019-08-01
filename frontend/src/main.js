import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@fortawesome/fontawesome-free/css/all.css'
import axios from "axios"

Vue.config.productionTip = false

const instance = axios.create({
  baseURL: 'http://localhost:8000'
});

// const instanceUserApi = axios.create({
//   baseURL: 'https://userapi.com'
// });

// instanceUserApi.defaults.headers.common["Authorization"] =
//   "Token" + localStorage.getItem("authToken");

Vue.prototype.$http = instance;
// Vue.prototype.$httpUserApi = instanceUserApi;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')