import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Dashboard.vue'

const routes = [
    { path: '/', name: 'home', component: HomeView },
    { path: '/dashboard', name: 'dashboard', component: HomeView },
    { path: '/add_entry', name: 'add_entry', component: () => import('../views/AddEntry.vue') },
    { path: '/edit_entry', name: 'edit_entry', component: () => import('../views/EditEntry.vue') },
    { path: '/entries_history', name: 'entries_history', component: () => import('../views/EntriesHistory.vue') },
    { path: '/search_results', name: 'search_results', component: () => import('../views/SearchResults.vue') },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
