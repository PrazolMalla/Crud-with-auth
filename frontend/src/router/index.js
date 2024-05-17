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
      component: () => import('../views/DisplayAllData.vue')
    },
    {
      path: '/create',
      name: 'create',
      component: () => import('../views/FormComponent.vue')
    },

    {
      path: '/edit/:id',
      name: 'edit',
      component: () => import('../views/EditPage.vue')
    }
  ]
})

export default router
