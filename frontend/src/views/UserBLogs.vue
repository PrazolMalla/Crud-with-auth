<template>
    <div class="relative flex justify-center w-full h-screen  " > 
    <div v-if="isEdit" class="absolute w-full h-screen bg-black opacity-5 z-0 "></div>
    <div class="absolute z-10 pt-9 ">
        <h1 class="text-3xl font-bold mb-4 font-helvetica">My Posts</h1>
        <div v-if="blogs.length === 0" class="text-gray-500 ">No blogs found.</div>
        <div v-else>
            <div v-for="blog in blogs" :key="blog.id" class="bg-white rounded-lg shadow-md p-6 mb-4 border-2 border-purple-color container" v-bind:class="{bgColor:isEdit}">
            <h2 class="text-xl font-semibold mb-2 font-helvetic">{{ blog.title }}</h2>
            <p class="text-gray-700 font-helvetic">{{ blog.desc }}</p>
            <p class="font-helvetica"><span class="text-purple-color font-bold">Author:</span> {{ blog.author__first_name}}</p>
            <div class="actions mt-4 flex flex-row gap-4 flex-wrap">
                <img
                class=" w-8 h-8 cursor-pointer"
                src="../assets/img/editing.png"
                @click="editButton(blog.id)"
                alt=""
                srcset=""
                />
                <img class="w-8 h-8 cursor-pointer" src="../assets/img/delete.png" @click="deleteBlog(blog.id)" />
                </div>
            </div>
        </div>
    </div>
    <div v-if="isEdit" class="absolute top-5 right-16 cursor-pointer "  @click="close"><span class=" text-purple-color font-bold text-4xl">&#10005;</span></div>
    <div v-if="isEdit" class=" mt-36 absolute z-20 bg-white w-[25%] h-[20rem] p-4 drop-shadow-lg border-2 border-purple-color backdrop-blur-lg">
        
        <div class="form-img"></div>
          <form id="form" @submit.prevent="updateBlog">
          <h1 class="text-4xl text-center text-purple-color font-helvetica font-bold">Edit Blog</h1>
          <div>
            <label for="email" class=" text-2xl text-slate-500 font-helvetica ">Title</label>
            <br />
            <input type="text" class="w-full h-8 border-2 " v-model="updatedBlog[0].title" required />
          </div>
          <br />
          <div>
            <label for="phone" class=" text-2xl text-slate-500 font-helvetica ">Description</label>
            <br />
            <textarea  required class=" border-2 rounded w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none" v-model="updatedBlog[0].desc"></textarea>
          </div>

            <button class="btn1" type="submit">Update</button>
      </form>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { toast } from 'vue3-toastify'
  import { mapGetters } from 'vuex';
  export default {
    data() {
      return {
        blogs: [],
        isEdit :false,
        updatedBlog:[],
        updateId : null
      };
    },
    computed: {
    ...mapGetters(['getToken']),
    token() {
      return this.getToken;
    }
    },
    mounted() {
      this.fetchBlogs();
    },
    methods: {
      async fetchBlogs() {
        try {
            const response = await axios.get('http://localhost:8000/api/v1/user-blog', {
          headers: {
            'Authorization': `Bearer ${this.token}`
          }
        });
          this.blogs = response.data;
          console.log(response.data);
        } catch (error) {
          console.log(error);
        } 
      },
      async deleteBlog(id){
        try{
            const response = await axios.delete(`http://localhost:8000/api/v1/blog/${id}`)
            this.blogs = this.blogs.filter(blogs => blogs.id !== id)
        }
        catch(error){
            console.log(error);
        }
        
      },
      editButton(id){
        console.log(id)
        this.isEdit = true
        this.updateId = id
        this.updatedBlog = this.blogs.filter(blogs => blogs.id === id)
        console.log(this.updateBlog)
      },
      async updateBlog(){
        try{        
            console.log(this.updateId);
            const response = await axios.put(`http://localhost:8000/api/v1/blog/${this.updateId}`, {
            title: this.updatedBlog[0].title,
            desc: this.updatedBlog[0].desc
          });
          toast.success("update Successful")
          this.$router.push('/display');
           
        }
        catch(error){
            console.log(error);
        }
      },
      close(){
        this.isEdit = false
      }
    }
  }
  </script>
  
  <style scoped>
.bgColor{
    filter: blur(5px);
}
  </style>
  