<script setup>
  import TopNav from "./components/TopNav.vue";
  import SideBar from "./components/SideBar.vue";
</script>

<template>
  <header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
    <TopNav />
  </header>
  <div class="container-fluid">
    <div class="row">
      <SideBar />
      <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">

      </main>
    </div>

    <footer>

    </footer>
  </div>
</template>

<style scoped>
</style>
