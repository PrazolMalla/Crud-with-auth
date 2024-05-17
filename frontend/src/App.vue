<template>
  <div id="app" class="w-full">
    <div class="main-container w-full">
      <RouterView />
      <Vue3Toastify />
    </div>
  </div>
</template>

<script>
import Vue3Toastify from 'vue3-toastify'
import NavBar from './components/NavBar.vue'
import { RouterView } from 'vue-router'
import TailwindComp from './components/TailwindComp.vue'

export default {
  data() {}
}
</script>

<style>
@import '/src/assets/base.css';
.btn1 {
  margin: 0.5rem 0 0 0;
  width: 100px;
  height: 40px;
  /* border-radius: 10px; */
  background-color: var(--primary-color);
  border: none;
  color: var(--vt-c-white-soft);
  cursor: pointer;
}

.btn1:hover {
  border: 1px solid var(--primary-color);
  background-color: transparent;
  color: var(--primary-color);
}
</style>
