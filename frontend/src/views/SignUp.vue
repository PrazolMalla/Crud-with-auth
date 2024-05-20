<template>
    <div class="flex flex-row items-center h-screen w-full">
      <div class="form-container w-full h-full bg-white flex flex-row">
        <div class="form-img flex justify-center items-center">
          <div class="relative w-[30rem] h-[30rem]">
            <div class="absolute w-[30rem] h-[30rem] z-10 flex justify-center items-center">
              <h1 class="font-helvetica text-4xl text-slate-700 p-10">
                Unveiling the Unseen
                <br />
                <br />
                <span class="text-slate-500 text-4xl font-helvetica font-bold"
                  >Explore, Discover, and Share the Stories That Matter.</span
                >
              </h1>
            </div>
  
            <div class="absolute w-[30rem] h-[30rem] bg-white opacity-35 rounded-xl z-0"></div>
          </div>
        </div>
        <div class="w-[55vw] h-full bg-white flex items-center justify-center">
          <form
            id="form"
            class="w-[400px] h-[500px] flex flex-col justify-center"
            @submit.prevent="login"
          >
            <h1 class="text-4xl mb-5 font-helvetica text-purple-color">Start Your Journey</h1>
            <div class="mt-4 flex flex-row gap-1">
                <div>
                    <label for="firstname" class="mt-4 text-xl font-bold font-helvetica text-slate-400"
                    >First Name</label>
                    <br />
                    <input
                        type="text"
                        class="mt-2 p-2 focus:outline-none  h-10 mb rounded-sm border"
                        id="firstname"
                        v-model="user.first_name"
                        required
                    />
                </div>
                <div>
                    <label for="firstname" class="mt-4 text-xl font-bold font-helvetica text-slate-400"
                    >Last Name</label>
                    <br />
                    <input
                        type="text"
                        class="mt-2 p-2 focus:outline-none  h-10 mb rounded-sm border"
                        id="lastname"
                        v-model="user.last_name"
                        required
                    />
                </div>
              
            </div>
            <div class="mt-4">
              <label for="email" class="mt-4 text-xl font-bold font-helvetica text-slate-400"
                >Email</label
              >
              <br />
              <input
                type="email"
                class="mt-2 p-2 focus:outline-none w-full h-10 mb rounded-sm border"
                id="email"
                v-model="user.email"
                required
              />
            </div>
            <div class="mt-4">
              <label for="password" class="text-xl font-bold font-helvetica text-slate-400"
                >Password</label
              >
              <br />
              <input
                type="password"
                class="p-2 mt-2 focus:outline-none w-full h-10 mb rounded-sm border"
                v-model="user.password"
              />
            </div>
            <div class="mt-4">
              <label for="phone" class="text-xl font-bold font-helvetica text-slate-400"
                >Phone</label
              >
              <br />
              <input
                type="text"
                class="p-2 mt-2 focus:outline-none w-full h-10 mb rounded-sm border"
                v-model="user.phone"
              />
            </div>
            <div class="mt-4">
              <label for="phone" class="text-xl font-bold font-helvetica text-slate-400"
                >Address</label
              >
              <br />
              <input
                type="text"
                class="p-2 mt-2 focus:outline-none w-full h-10 mb rounded-sm border"
                v-model="user.address"
              />
            </div>
            <div class="mt-6">
              <button
                class="bg-purple-color w-full h-[3rem] text-white text-xl font-bold rounded-sm hover:bg-transparent hover:border hover:border-purple-color hover:text-purple-color"
                type="submit"
              >
                Sign Up
              </button>
              <RouterLink to="/"><span class="mt-4 text-purple-color text-xl cursor-pointer">Login</span></RouterLink>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { toast } from 'vue3-toastify'
  import 'vue3-toastify/dist/index.css'
  import axios from 'axios'
  import { mapActions } from 'vuex';
  export default {
    
    data() {
      return {
        user: {
          first_name:'',
          last_name:'',
          phone:null,
          address:'',
          email: '',
          password: '',

        }
      }
    },
    methods: {
      ...mapActions(['setToken','setLoggedIn']),
      login() {
        axios
          .post('http://127.0.0.1:8000/api/v1/user/', {
            email: this.user.email,
            password: this.user.password,
            first_name:this.user.first_name,
            last_name:this.user.last_name,
            address:this.user.address,
            phone:this.user.phone
          })
          .then((response) => {
            console.log(response);
            if(response.status ==200){
              toast.success('User created Successfully')
              this.$router.push({ name: 'login' });
            }
            else{
                toast.error(response.msg)
              }
            
          })
          .catch((error) => {
            toast.error(error)
          })
      }
    }
  }
  </script>
  
  <style scoped>
  .body {
    background-image: url();
  }
  
  .form-img {
    width: 45vw;
  
    background-image: url('../assets/img/background.jpg');
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
  }
  </style>
  