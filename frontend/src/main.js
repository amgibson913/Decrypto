import Vue from 'vue'
import App from './App.vue'
import { io } from 'socket.io-client'
import VueSocketIOExt from 'vue-socket.io-extended'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

const socket = io('https://wyethst.xyz', {
  path: '/decrypto/socket.io'
})

Vue.use(VueSocketIOExt, socket)

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
