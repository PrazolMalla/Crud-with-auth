import './assets/main.css'
import './index.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'vue-toast-notification/dist/theme-bootstrap.css'
import Vue3Toastify from 'vue3-toastify'
import store from './store'
const app = createApp(App)
app.use(store)
app.use(router)
app.use(Vue3Toastify, {
  autoClose: 3000
})

app.mount('#app')
