<template>
  <div>
    <table>
      <tr>
        <th>Id</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Address</th>
        <th>Gender</th>
      </tr>
      <tr v-for="(data, index) in datas" :key="index">
        <td>{{ data.id }}</td>
        <td>{{ data.email }}</td>
        <td>{{ data.phone }}</td>
        <td>{{ data.address }}</td>
        <td>{{ data.gender }}</td>
        <RouterLink :to="{ path: '/edit/' + data.id }">
          <button @click="editButton">edit</button>
        </RouterLink>
        <button @click="deleteUser(data.id)">delete</button>
      </tr>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      datas: [],
      APIUrl: 'http://127.0.0.1:8000/api/v1/user/',
      editButtonClicked: false
    }
  },
  methods: {
    async fetchUser() {
      try {
        const response = await fetch(this.APIUrl)
        this.datas = await response.json()
      } catch (error) {
        console.log(error)
      }
    },
    async deleteUser(id) {
      try {
        const config = {
          method: 'DELETE'
        }
        const response = await fetch(this.APIUrl + id, config)
        if (response.ok) {
          alert('user is deleted')
          return response
        } else {
          console.log('error')
        }
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted() {
    this.fetchUser()
  },

  watch: {
    datas: {
      handler() {
        this.fetchUser()
      }
    }
  }
}
</script>
<style lang=""></style>
