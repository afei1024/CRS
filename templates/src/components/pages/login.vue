<!-- src/views/Login.vue -->
<template>
  <div class="login-container">
    <form @submit.prevent="login">
      <div class="form-group">
        <label>用户名:</label>
        <input v-model="username" type="text" required />
      </div>
      <div class="form-group">
        <label>密码:</label>
        <input v-model="hashed_password" type="hashed_password" required />
      </div>
      <button type="submit" class="login-btn">登录</button>
      <p v-if="error" class="error-msg">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import { safeStorage } from '../../utils/storage'

export default {
  data() {
    return {
      username: '',
      hashed_password: '',
      error: ''
    }
  },
  methods: {
    async login() {
      try {
        // 显示加载状态
        // this.$store.commit('setLoading', true)

        const response = await this.$axios.post('/api/auth_router/login', {
          username: this.username,
          password: this.hashed_password,
          grant_type: 'password'
        })

        // 安全存储token
        safeStorage.setItem('access_token', response.data.access_token)

        // 跳转前清除加载状态
        // this.$store.commit('setLoading', false)

        // 跳转到仪表盘
        this.$router.push('/dashboard')
      } catch (error) {
        console.error('登录失败:', error)
        this.error = error.response?.data?.message || '登录失败，请稍后重试'
        // this.$store.commit('setLoading', false)
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 1rem;
}

.login-btn {
  background: #42b983;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.error-msg {
  color: #ff4757;
  margin-top: 1rem;
}
</style>