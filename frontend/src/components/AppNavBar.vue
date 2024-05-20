<template>
    <nav class="p-4 h-20 border-b-2 border-slate-200">
      <div class="container mx-auto flex justify-between items-center">
        <div class="text-white text-lg font-bold z">
          <RouterLink to="/display">
            <h1 class="mt-2 text-2xl font-bold font-helvetica  text-slate-800 ">RAICHU</h1>
          </RouterLink>
        </div>
        <div class="hidden md:flex space-x-4">
          
          <RouterLink to="/display"><h3 class=" text-slate-800 text-xl font-bold mt-2">Blogs</h3></RouterLink>
          <RouterLink to="/userblog"><h3 class=" text-slate-800 text-xl font-bold mt-2">My Blogs</h3></RouterLink>
          <RouterLink to="/post">
            <button
                class="bg-purple-color w-full h-[3rem] text-white text-xl font-bold rounded-md px-4 hover:bg-transparent hover:border hover:border-purple-color hover:text-purple-color"
                type="submit"
              >
                Create Blog
              </button>
          </RouterLink>
        </div>
        <div class="md:hidden">
          <button @click="toggleMenu" class="text-white focus:outline-none">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
            </svg>
          </button>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    data() {
    },

  };
  </script>
  
  <style scoped>
  /* Add any additional styles here */
  </style>