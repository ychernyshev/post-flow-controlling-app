import { createApp } from 'vue'
import axios from 'axios'
import './style.css'
import App from './App.vue'

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
});

const app = createApp(App)
app.provide('api', api)
app.mount('#app')
