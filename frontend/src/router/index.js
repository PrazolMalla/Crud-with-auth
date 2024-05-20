import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: () => import('../views/FormComponent.vue')
    },
    {
      path: '/display',
      name: 'display',
      component: () => import('../views/AllBlogs.vue')
    },
    {
      path: '/create',
      name: 'create',
      component: () => import('../views/FormComponent.vue')
    },
    {
      path: '/post',
      name: 'post',
      component: () => import('../views/PostBlog.vue')
    },
    {
      path: '/edit/:id',
      name: 'edit',
      component: () => import('../views/EditPage.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/SignUp.vue')
    },
    {
      path: '/userblog',
      name: 'userblog',
      component: () => import('../views/UserBLogs.vue')
    }
  ]
})

export default router
