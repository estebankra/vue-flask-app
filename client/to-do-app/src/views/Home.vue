<template>
  <b-container>
      <b-jumbotron header="To-Do-App"></b-jumbotron>
      <tasks-list />
  </b-container>
</template>

<script>
import TasksList from '../components/TasksList.vue'

export default {
  name: 'Home',
  components: {
    TasksList
  },
  mounted () {
    this.$store.dispatch('getTasksList')
  }
}
</script>
