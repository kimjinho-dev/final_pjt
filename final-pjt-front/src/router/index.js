import Vue from 'vue'
import VueRouter from 'vue-router'
import MoviesView from '../views/Movies/MoviesView.vue'
import FoodsView from '../views/Foods/FoodsView.vue'
import CommunityView from '../views/Community/CommunityView.vue'

Vue.use(VueRouter)

const routes = [
 {
  path: '/movies',
  name: 'movies',
  component: MoviesView
 },
 {
  path: '/community',
  name: 'community',
  component: CommunityView
 },
 {
  path: '/foods',
  name: 'foods',
  component: FoodsView
 },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
