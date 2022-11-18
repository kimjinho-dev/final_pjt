import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'
// import createPersistedState from 'vuex-persistedstate'
// import router from '@/router'

Vue.use(Vuex)

// const API_URL = 'http://127.0.0.1:8000/'

export default new Vuex.Store({
  plugins: [
    // createPersistedState()
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
  },
  actions: {
    createCommunityArticle(context, data) {
      context.commit('CREATE_COMMUNITY_ARTICLE', data)
    },
    deleteCommunityArticle(context, data) {
      context.commit('DELETE_COMMUNITY_ARTICLE', data)
    },
  },
  modules: {
  }
})
