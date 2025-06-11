import { createRouter, createWebHistory } from 'vue-router'
import Links from '../views/Links.vue'
import Home from '../views/Home.vue'


const routes = [
  { path: '/', component: Home },
  { path: '/list', component: Links },


]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
