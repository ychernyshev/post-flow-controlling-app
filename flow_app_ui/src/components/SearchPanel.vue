<script setup>
import { ref } from 'vue'
import axios from 'axios'

// простий debounce
function debounce(fn, delay) {
  let timeout
  return (...args) => {
    clearTimeout(timeout)
    timeout = setTimeout(() => fn(...args), delay)
  }
}

const query = ref('')
const results = ref([])

async function search() {
  if (query.value.length > 2) {
    const response = await axios.get(`/api/search/?q=${query.value}`)
    results.value = response.data
  } else {
    results.value = []
  }
}

// створюємо задебоунсений варіант
const debouncedSearch = debounce(search, 300)
</script>

<template>
  <input v-model="query" class="form-control form-control-dark w-100 rounded-0 border-0" type="search" @input="debouncedSearch" placeholder="Пошук..." aria-label="Search">
  <div class="navbar-nav">
    <!--    <div class="nav-item text-nowrap">-->
    <!--      <a class="nav-link px-3" href="#">Sign out</a>-->
    <!--    </div>-->
  </div>
  <ul>
    <li v-for="item in results" :key="item.id">{{ item.name }}</li>
  </ul>
</template>

<style scoped>

</style>