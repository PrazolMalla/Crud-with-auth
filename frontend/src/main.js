import './assets/main.css'
import './index.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'vue-toast-notification/dist/theme-bootstrap.css'
import Vue3Toastify from 'vue3-toastify'
const app = createApp(App)
app.use(router, Vue3Toastify)

app.mount('#app')
