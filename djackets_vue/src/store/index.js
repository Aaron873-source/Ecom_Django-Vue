import { createStore } from 'vuex'

// WE SET UP Vuex/State here 
export default createStore({
  // STATE IS THE VARIABLES AND INFORMATION 
  state: {
    cart: {
      items:[],
    },
    isAuthenticated: false,
    token: '',
    isLoading: false
  },
  getters: {
  },
  // MUTATIONS IS SYNCHRONOUS MUTATIONS TO THE VARIABLES BECAUSE WE CANNOT JUST CHANGE THEM DIRECTLY
  mutations: {
  },
  // ACTIONS WOULD BE ASYNCHRONOUS FUNCTION TO CHANGE THE VARIABLE
  actions: {
  },
  modules: {
  }
})
