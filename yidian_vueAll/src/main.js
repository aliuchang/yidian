import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Axios from 'axios'


//赋值之前
let getCookie = function (cookie) {
    let reg = /csrftoken=([\w]+)[;]?/g
    return reg.exec(cookie)[1]
}

Axios.interceptors.request.use(
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

Vue.prototype.$axios = Axios


import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
