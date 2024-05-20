import { createStore } from 'vuex'

const store = createStore({
  state: {
    token: null,
    loggedIn: false
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token
      state.loggedIn = !!token
    },
    SET_LOGGED_IN(state, loggedIn) {
      state.loggedIn = loggedIn
    }
  },
  actions: {
    setToken({ commit }, token) {
      commit('SET_TOKEN', token)
    },
    setLoggedIn({ commit }, loggedIn) {
      commit('SET_LOGGED_IN', loggedIn)
    }
  },
  getters: {
    getToken: (state) => state.token,
    isLoggedIn: (state) => state.loggedIn
  }
})

export default store
