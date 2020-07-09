import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    tasksList: []
  },
  getters: {
    tasksListGetter: state => {
      return state.tasksList
    },
  },
  mutations: {
    setTasksList: (state, TasksList) => (state.tasksList = TasksList),
  },
  actions: {
    getTasksList ({ commit }) {
      axios.get(`http://127.0.0.1:4000/tasks`)
      .then(response => {
        commit('setTasksList', response.data)
      })
      .catch(e => {
        this.errors.push(e)
      })
    }
  }
})
