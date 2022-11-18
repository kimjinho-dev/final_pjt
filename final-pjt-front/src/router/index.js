import Vue from 'vue'
import VueRouter from 'vue-router'
import MoviesView from '../views/Movies/MoviesView.vue'
import CommunityView from '../views/Community/CommunityView.vue'
import Create_C_Article from '../views/Community/Create_C_Article.vue'

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
    path: '/community/createarticle',
    name: 'createcommunityarticle',
    component: Create_C_Article
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
