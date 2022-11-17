import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    communityArticles: [
      
    ],
    foodsArticles: [

    ]
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
    CREATE_FOODS_ARTICLE(state, data) {
      state.foodsArticles.push(data)
    },
    DELETE_FOODS_ARTICLE(state, data) {
      const index = state.foodsArticles.indexOf(data)
      state.foodsArticles.splice(index, 1)
    }
  },
  actions: {
    createCommunityArticle(context, data) {
      context.commit('CREATE_COMMUNITY_ARTICLE', data)
    },
    deleteCommunityArticle(context, data) {
      context.commit('DELETE_COMMUNITY_ARTICLE', data)
    },
    createFoodsArticle(context, data) {
      context.commit('CREATE_FOODS_ARTICLE', data)
    },
    deleteFoodsArticle(context, data) {
      context.commit('DELETE_FOODS_ARTICLE', data)
    }
  },
  modules: {
  }
})
