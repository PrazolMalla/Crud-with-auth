<template>

    <div class="container mx-auto px-4 py-8">
      <div>
        <h1 class="text-4xl font-bold mb-4 text-center font-helvetica">Posts</h1>
        <div v-if="blogs.length === 0" class="text-gray-500">No blogs found.</div>
        <div v-else>
          <div class="  flex flex-row gap-10 flex-wrap">
            <div v-for="blog in blogs" :key="blog.id" class=" relative bg-white rounded-lg shadow-md p-6 mb-4 w-[30%] h-[25rem] max-h-[25rem] overflow-hidden border-2 border-purple-color">
              <h2 class="text-xl font-bold mb-2 font-helvetica">{{ blog.title}}</h2>
              <p class="text-gray-700 font-helvetica">{{ blog.desc }}</p>
              <br>
              <p class="font-helvetica"><span class="text-purple-color font-bold">Author: </span>{{ blog.author__first_name}}</p>
              <div class="flex flex-row justify-center items-center">
                <button
                  class=" absolute bottom-4 bg-purple-color w-[8rem] h-[3rem] text-white text-xl font-bold rounded-sm hover:bg-transparent hover:border hover:border-purple-color hover:text-purple-color"
                >
                  Read More 
                </button>
              </div>
          </div>
          </div>
        </div>
      </div>
  </div>    
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        blogs: [],
      };
    },
    mounted() {
      this.fetchBlogs();
    },
    methods: {
      async fetchBlogs() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/v1/blogs');
          this.blogs = response.data;
          console.log(response.data);
        } catch (error) {
          console.log(error);
          
        }
      }
    }
  }
  </script>
