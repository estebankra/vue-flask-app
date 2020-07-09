<template>
  <b-row>
    <b-col cols=3 v-for="task in tasksListGetter" :key="task.id">
        <b-card :title=task.name class="mb-2" >
          <b-card-text>
            {{ task.detail }}
          </b-card-text>
          <b-button href="#" size="sm" variant="primary"><b-icon-pencil></b-icon-pencil></b-button> |
          <b-button href="#" size="sm" variant="danger"><b-icon-trash></b-icon-trash></b-button>
        </b-card>
    </b-col>
  </b-row>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'TasksList',
  computed: {
    ...mapGetters(['tasksListGetter']),
  }
}
</script>