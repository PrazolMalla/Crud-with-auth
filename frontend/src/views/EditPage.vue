<template>
  <div class="container">
    <div class="form-container">
      <div class="form-img"></div>
      <form id="form" @submit.prevent="updateUser">
        <h1>Edit Details</h1>
        <div>
          <label for="email">Email:</label>
          <br />
          <input type="email" id="email" v-model="user.email" required />
        </div>
        <div>
          <label for="phone">Phone:</label>
          <br />
          <input type="text" id="phone" v-model="user.phone" />
        </div>
        <div>
          <label for="address">Address:</label>
          <br />
          <input type="text" id="address" v-model="user.address" />
        </div>
        <div>
          <label for="gender">Gender:</label>
          <br />
          <div class="gender-radio">
            <input type="radio" id="male" value="Male" v-model="user.gender" />
            <label class="radio-label" for="male">Male</label>
            <input type="radio" id="female" value="Female" v-model="user.gender" />
            <label class="radio-label" for="female">Female</label>
          </div>
        </div>
        <div class="buttons">
          <!-- <RouterLink to="/"><button class="btn1" type="submit">Go Back</button></RouterLink> -->
          <button class="btn1" type="submit">Submit</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
// import { toHandlerKey } from 'vue'
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'
export default {
  props: {
    id: Number
  },
  data() {
    return {
      user: {
        email: '',
        phone: null,
        address: '',
        gender: ''
      },
      APIUrl: 'http://127.0.0.1:8000/api/v1/user/'
    }
  },
  mounted() {
    this.getUser()
  },
  methods: {
    async getUser() {
      try {
        const response = await fetch(this.APIUrl + this.id)
        this.user = await response.json()
      } catch (error) {
        console.log(error)
      }
    },
    async updateUser() {
      try {
        const config = {
          method: 'PUT',
          header: {
            Accept: 'application/json',
            'Content-type': 'application/json'
          },
          body: JSON.stringify(this.user)
        }
        const response = await fetch(this.APIUrl + this.id, config)
        if (response.ok) {
          toast.success('User Updated Successfully!', {
            autoClose: 4000
          })
        } else {
          toast.error(response.status)
        }
        this.$router.push('/')
      } catch (error) {
        toast.error(error)
      }
    }
  }
}
</script>
<style scoped>
/* h1 {
  color: white;
  text-align: center;
} */
/* #form {
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 1rem;
  gap: 20px;
  width: 400px;
  height: 500px;
  background-color: white;
  border-left: 10px solid var(--vt-c-blue);
}

.form-img {
  width: 400px;
  height: 500px;
  background-color: white;
  background-image: url('../assets/img/Forgot password-rafiki.png');
  background-position: center;
  background-size: 300px;
  background-repeat: no-repeat;
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
