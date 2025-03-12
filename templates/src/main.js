
import { createApp } from 'vue';
import './assets/main.css'
import App from './App.vue'
// 菜单和路由设置
import router from './router'; // Import the router
import axiosInstance from './plugins/axios.js'; // 导入 Axios 插件


// createApp(App).mount('#app'); // 完全兼容Vite+Vue3项目‌:ml-citation{ref="4" data="citationList"}
const app = createApp(App)

// 全局挂载axios
app.config.globalProperties.$axios = axiosInstance
// app.use(store); // 关键：注入 $store

app.mount('#app')