import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import store from './store/store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios,axios);
// axios 改写为 Vue 的原型属性
Vue.prototype.$axios = axios

// 引入过滤器
// import * as currency from './api/filter.js'
// Object.keys(currency).forEach(key=>{
//   Vue.filter(key, currency[key])
// })

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
