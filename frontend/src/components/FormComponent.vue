<template>
  <div class="form-container">
    <form id="form" @submit.prevent="submitData">
      <h2>{{ title }}</h2>
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" v-model="user.email" required />
      </div>
      <div>
        <label for="phone">Phone</label>
        <input type="text" id="phone" v-model="user.phone" />
      </div>
      <div>
        <label for="address">Address</label>
        <input type="text" id="address" v-model="user.address" />
      </div>
      <div>
        <label for="gender">Gender</label>
        <input type="radio" id="male" value="Male" v-model="user.gender" />
        <label for="male">Male</label>
        <input type="radio" id="female" value="Female" v-model="user.gender" />
        <label for="female">Female</label>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
  <p v-if="errorMsg !== ''">{{ errorMsg }}</p>
</template>

<script>
const APIUrl = 'http://127.0.0.1:8000/api/v1/user/'
export default {
  props: {
    title: String
  },
  data() {
    return {
      user: {
        email: '',
        phone: null,
        address: '',
        gender: ''
      },
      errorMsg: ''
    }
  },
  methods: {
    async submitData() {
      try {
        const config = {
          method: 'POST',
          header: {
            Accept: 'application/json',
            'Content-type': 'application/json'
          },
          body: JSON.stringify(this.user)
        }
        const response = await fetch(APIUrl, config)
        if (response.ok) {
          alert('User Created ')
          return response
        } else {
          console.log('response error')
        }
      } catch (error) {
        console.log('hello world')
      }
    }
  }
}
</script>

<style scoped>
#form {
  display: flex;
  flex-direction: column;
  padding: 1.25rem;
  gap: 20px;
  width: 400px;
  height: 400px;
  background-color: transparent;
  border-radius: 10px;
  box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
}

.form-container {
  width: 80vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
