<template>
  <div id="app" class="w-full  h-screen flex flex-col">
    <div v-if="logged">
      <Nav/>
    </div>
    <div class="main-container w-full">
      <RouterView />
    </div>
  </div>
</template>

<script>
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'
import { RouterView } from 'vue-router'
import TailwindComp from './components/TailwindComp.vue'
import { mapGetters } from 'vuex';
import Nav from './components/AppNavBar.vue'
export default {
  components:{
    Nav,
  },
  data() {
  },
  computed: {
    ...mapGetters(['isLoggedIn']),
    logged() {
      return this.isLoggedIn;
    }
    },
  methods:{
    
  }
  
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
