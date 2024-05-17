<template>
  <div class="edit-page" v-bind:class="{ blurClass: editButtonClicked }">
    <div class="table">
      <h1>Dashboard</h1>
      <table>
        <tr>
          <th>Id</th>
          <th>Email</th>
          <th>Phone</th>
          <th>Address</th>
          <th>Gender</th>
          <th>Actions</th>
        </tr>
        <tr v-for="(data, index) in datas" :key="index">
          <td>{{ data.id }}</td>
          <td>{{ data.email }}</td>
          <td>{{ data.phone }}</td>
          <td>{{ data.address }}</td>
          <td>{{ data.gender }}</td>

          <td>
            <!-- <RouterLink :to="{ path: '/edit/' + data.id }">
              <img
                class="icon"
                src="../assets/img/editing.png"
                @click="editUser"
                alt=""
                srcset=""
              />
            </RouterLink> -->
            <img
              class="icon"
              src="../assets/img/editing.png"
              @click="editUser(data.id)"
              alt=""
              srcset=""
            />
            <img class="icon" src="../assets/img/delete.png" @click="deleteUser(data.id)" />
          </td>
        </tr>
      </table>
      <RouterLink to="/create">
        <button class="btn1">Create User</button>
      </RouterLink>
    </div>
    <div v-if="editButtonClicked === true" class="Editform">
      <div class="model">
        <span class="close" @click="cancelEdit">&times;</span>
        <EditPage :id="id" />
      </div>
    </div>
  </div>
</template>
<script>
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'
import EditPage from './EditPage.vue'
export default {
  components: {
    EditPage
  },
  data() {
    return {
      datas: [],
      APIUrl: 'http://127.0.0.1:8000/api/v1/user/',
      editButtonClicked: false,
      id: null
    }
  },
  methods: {
    async fetchUser() {
      try {
        const response = await fetch(this.APIUrl)
        this.datas = await response.json()
        this.datas = this.datas.filter((data) => data.isDeleted === false)
      } catch (error) {
        console.log(error)
      }
    },
    async deleteUser(id) {
      try {
        const config = {
          method: 'DELETE',
          body: JSON.stringify({})
        }
        const response = await fetch(this.APIUrl + id, config)

        if (response.ok) {
          this.datas = this.datas.filter((data) => data.id !== id)
          toast.success('User Deleted Successfully!', {
            autoClose: 4000
          })
        } else {
          toast.error(response.statusText)
        }
      } catch (error) {
        toast.error(error)
      }
    },
    editUser(id) {
      this.id = id
      this.editButtonClicked = true
      console.log(this.id)
    },
    cancelEdit() {
      this.editButtonClicked = false
    }
  },

  mounted() {
    this.fetchUser()
  }
}
</script>
<style>
@import '/src/assets/base.css';
.table {
  margin-top: 3.25rem;
  width: 100%;
}
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  border-bottom: 1px solid #ddd;
}

th {
  color: var(--vt-c-white-soft);
  padding: 1.25rem;
  text-align: left;
  background-color: var(--primary-color);
  font-size: var(--h3-font-size);
}
td {
  padding: 1.25rem;
  text-align: left;
}

.icon {
  margin: 0.5rem;
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.model-container {
  position: relative;
  /* width: 100vw;*/
  height: 100vh;

  overflow: hidden;
}

.Editform {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(1px);
}

.close {
  position: absolute;
  top: 5px;
  right: 10px;
  font-size: 36px;
  cursor: pointer;
  color: white;
}
</style>
