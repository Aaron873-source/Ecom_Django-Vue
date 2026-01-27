import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// WE NEED TO IMPORT AXIOS INTO THIS JS FILE AND TELL VUE TO USE IT
import axios from 'axios'

// BELOW WE ARE CONNECTING THE BASE URL FOR AXIOS TO BE THE SAME DEVELOPMENT SERVER AS THE ONE WHERE WE RUN THE DJANGO PROJECT WHEN WE RUN THE SERVER
axios.defaults.baseURL = 'http://127.0.0.1:8000/' 

createApp(App).use(store).use(router,axios).mount('#app')
