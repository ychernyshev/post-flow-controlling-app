import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Dashboard.vue'

const routes = [
    { path: '/', name: 'home', component: HomeView },
    { path: '/add_entry', name: 'about', component: () => import('../views/AddEntry.vue') },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
