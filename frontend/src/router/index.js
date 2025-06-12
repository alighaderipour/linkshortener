import { createRouter, createWebHistory } from 'vue-router'
import Links from '../views/Links.vue'
import Home from '../views/Home.vue'
import NewLinks from '../views/NewLinks.vue'


const routes = [
  { path: '/', component: Home },
  { path: '/list', component: Links },
  { path: '/link/create', component: NewLinks },


]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
