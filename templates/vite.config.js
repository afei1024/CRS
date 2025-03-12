import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server:{
      open: '/login',           // 是否自动打开项目
      host: '127.0.0.1',      // 制定域名
      port: 9001,           // 端口号
      https: false,         // 把访问变成https
      hotOnly: false,       // 热更新
  }
})
