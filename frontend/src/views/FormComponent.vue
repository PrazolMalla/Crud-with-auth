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
          <h1 class="text-4xl mb-5 font-helvetica text-purple-color">Welcome Back</h1>
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

          <div class="flex justify-between">
            <label class="block text-gray-500 font-bold my-4"
              ><input type="checkbox" />
              <span class="py-2 text-sm text-gray-600"> Remember Me </span></label
            >
            <label class="block text-gray-500 font-bold my-4">
              <a class="cursor-pointer border-b-2 border-purple-300 hover:border-purple-color">
                <span class="text-purple-color">Forgot Password?</span>
              </a>
            </label>
          </div>
          <div class="mt-6">
            <button
              class="bg-purple-color w-full h-[3rem] text-white text-xl font-bold rounded-sm hover:bg-transparent hover:border hover:border-purple-color hover:text-purple-color"
              type="submit"
            >
              Login
            </button>
            <RouterLink to="/signup"><span class="mt-4 text-purple-color text-xl cursor-pointer">Sign Up</span>
            </RouterLink>
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
        email: '',
        password: ''
      }
    }
  },
  methods: {
    ...mapActions(['setToken','setLoggedIn']),
    login() {
      axios
        .post('http://127.0.0.1:8000/api/v1/login', {
          email: this.user.email,
          password: this.user.password
        })
        .then((response) => {
          console.log(response);
          if(response.status ==200){
            this.setToken(response.data.token)
            this.setLoggedIn(true)
            toast.success('User login Successful')
            this.$router.push({ name: 'display' });
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
