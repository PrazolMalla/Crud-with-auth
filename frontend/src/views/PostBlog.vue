<template>
    <div class="w-full flex items-center justify-center">
      <div class="max-w-md w-full bg-white shadow-md rounded-lg px-8 pt-6 pb-8 mb-4 opacity-75 border-2 border-purple-color">
        <h1 class="text-3xl font-bold mb-4 text-center text-black">Create New Blog Post</h1>
        <form @submit.prevent="createBlog">
          <div class="mb-6">
            <label for="title" class="block text-gray-700  text-lg font-bold mb-2">Title:</label>
            <input type="text" v-model="title" required class=" border-2 rounded w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none ">
          </div>
          <div class="mb-6">
            <label for="description" class="block text-gray-700 text-lg font-bold mb-2">Description:</label>
            <textarea v-model="description" required class=" border-2 rounded w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none"></textarea>
          </div>
          <div class="flex items-center justify-center">
            <button
              class="bg-purple-color w-full h-[3rem] text-white text-xl font-bold rounded-sm hover:bg-transparent hover:border hover:border-purple-color hover:text-purple-color"
              type="submit"
            >Create Post
            </button>
          </div>

        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { mapGetters } from 'vuex';
  import { toast } from 'vue3-toastify'
  export default {
    data() {
      return {
        title: '',
        description: '',
      };
      
    },
    computed: {
    ...mapGetters(['getToken']),
    token() {
      return this.getToken;
    }
    },
    methods: {
      async createBlog() {
        try {
          await axios.post('http://localhost:8000/api/v1/blogs/', {
            title: this.title,
            desc: this.description,
          },{
          headers: {
            Authorization: `Bearer ${this.token}`
          }})
          .then((response) => {
          console.log(response);

          toast.success('post added sucessfully')

        })
          this.$router.push('/display');
        } catch (error) {
          console.error('Error creating blog:', error);
        }
      }
    },
  };
  </script>
  
  <style scoped>
  /* Add custom styling here */
  form {
    border-radius: 20px; /* Adjust the curve as needed */
  }
  </style>