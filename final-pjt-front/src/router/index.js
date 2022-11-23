import Vue from 'vue'
import VueRouter from 'vue-router'
import MoviesView from '@/views/Movies/MoviesView'
import MovieDetail from '@/views/Movies/MovieDetail'
import MoviesSearchResult from '@/views/Movies/MoviesSearchResult'
import CommunityView from '../views/Community/CommunityView.vue'
import Create_C_Article from '../views/Community/Create_C_Article.vue'
import CommunitySearchResult from '../views/Community/CommunitySearchResult'
import LoginView from '../views/Account/LoginView.vue'
import SignupView from '../views/Account/SignupView.vue'
import ProfileView from '../views/Account/ProfileView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'Movies',
    component: MoviesView
  },
  {
    path: '/movies/:movie_id',
    name: 'movieDetail',
    component: MovieDetail,
  },
  {
    path: '/movies/searchresult/:searchData',
    name: 'searchresult',
    component: MoviesSearchResult,
  },
  {
    path: '/community',
    name: 'Community',
    component: CommunityView
  },
  {
    path: '/community/createarticle',
    name: 'CreateCommunityArticle',
    component: Create_C_Article
  },
  {
    path: '/community/searchresult/:searchData',
    name: 'CommunitySearchResult',
    component: CommunitySearchResult
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
