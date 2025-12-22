<script setup>
  import {ref, onMounted} from "vue";
  import {useAxios} from "../composables/useAxios.js";

  const apiItems = useAxios('api/postage');

  const items = ref([])

  onMounted(async () => {
    items.value = await apiItems.get()
  })
</script>

<template>
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Entries History</h1>
  </div>
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item }}
    </li>
  </ul>
</template>

<style scoped>

</style>