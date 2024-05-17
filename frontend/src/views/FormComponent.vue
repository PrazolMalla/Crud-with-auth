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
            <span class="mt-4 text-purple-color text-xl cursor-pointer">Sign Up</span>
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
    login() {
      axios
        .post('http://127.0.0.1:8000/api/v1/login', {
          email: this.user.email,
          password: this.user.password
        })
        .then((response) => {
          toast.success('User login Successful')
          setTimeout(() => {
            this.$router.push({ name: 'display' })
          }, 1000)
        })
        .catch((error) => {
          toast.error('Login Failed')
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
/* h1 {
  text-align: center;
}
#form {
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  gap: 20px;
  width: 400px;
  height: 500px;
  background-color: transparent;
  border-left: 10px solid var(--vt-c-blue);
}


.container {
  width: 80vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.form-container {
  width: 800px;
  height: 500px;
  background-color: white;
  display: flex;
  background-color: transparent;
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
}

input[type='text'] {
  width: 80%;
  height: 40px;
  border: none;
  border-bottom: 2px solid var(--vt-c-blue);
}
input[type='email'] {
  width: 80%;
  height: 40px;
  border: none;
  border-bottom: 2px solid var(--vt-c-blue);
}

input[type='radio'] {
  margin-left: 1rem;
  width: 20px;
  height: 20px;
}

input:focus {
  outline: none;
}

label {
  font-size: 1rem;
}

.radio-label {
  margin-left: 0.5rem;
  margin-top: -0.5rem;
}

.buttons {
  display: flex;
  gap: 1rem;
} */
</style>
