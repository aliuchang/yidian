import Vue from 'vue'
import App from './App.vue'
import router from './router'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI);

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios);

let getCookie = function (cookie) {
    let reg = /csrftoken=([\w]+)[;]?/g
    return reg.exec(cookie)[1]
}

axios.interceptors.request.use(
  function(config) {
    // 在post请求前统一添加X-CSRFToken的header信息
    let cookie = document.cookie;
    if(cookie && config.method == 'post'){
      config.headers['X-CSRFToken'] = getCookie(cookie);
    }
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// axios 改写为 Vue 的原型属性
Vue.prototype.$axios = axios;

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
