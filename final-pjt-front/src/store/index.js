import router from '@/router'
import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000/'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    communityArticles: [],
    token: null,
  },
  getters: {
  },
  mutations: {
    CREATE_COMMUNITY_ARTICLE(state, data) {
      state.communityArticles.push(data)
    },
    DELETE_COMMUNITY_ARTICLE(state, data) {
      const index = state.communityArticles.indexOf(data)
      state.communityArticles.splice(index, 1)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'CommunityView' })
    }
  },
  actions: {
    createCommunityArticle(context, data) {
      context.commit('CREATE_COMMUNITY_ARTICLE', data)
    },
    deleteCommunityArticle(context, data) {
      context.commit('DELETE_COMMUNITY_ARTICLE', data)
    },
    // 회원가입
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    // 로그인
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
    }
  },
  modules: {
  }
})
