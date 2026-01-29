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
    // FIRST WE WANT TO CREATE A FUNCTION CALLED initializeStore so we can store things in the local storage of the browser
    initializeStore(state){
      //Checking of the local storage exists with an item called cart and if not we create it
      if(localStorage.getItem('cart')){
          state.cart = JSON.parse(localStorage.getItem('cart'))
      }else{
          // If local storage does not have it we create
          localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
    addToCart(state, item){
     const exists = state.cart.items.filter(i => i.product.id === item.product.id)
     
     if(exists.length){
      exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
     } else {
      state.cart.items.push(item)
     }
     localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  // ACTIONS WOULD BE ASYNCHRONOUS FUNCTION TO CHANGE THE VARIABLE
  actions: {
  },
  modules: {
  }
})
