// router/index.js
// import Vue from 'vue';
// import VueRouter from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router';



import Login from '../components/pages/login.vue'; // Import your Login component

// Vue.use(VueRouter); // Use Vue Router

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login }
  ]
})

// const router = new VueRouter({
//   mode: 'history', // Use history mode for clean URLs
//   routes, // Pass the routes
// });

export default router;
