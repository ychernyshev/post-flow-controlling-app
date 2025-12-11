import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Dashboard.vue'

const routes = [
    { path: '/', name: 'home', component: HomeView },
    { path: '/dashboard', name: 'home', component: HomeView },
    { path: '/add_entry', name: 'about', component: () => import('../views/AddEntry.vue') },
    { path: '/edit_entry', name: 'about', component: () => import('../views/EditEntry.vue') },
    { path: '/entries_history', name: 'about', component: () => import('../views/EntriesHistory.vue') },
    { path: '/search_results', name: 'about', component: () => import('../views/SearchResults.vue') },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
