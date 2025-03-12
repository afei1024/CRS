// plugins/axios.js
import { createApp } from 'vue';

import axios from 'axios';

// Create an Axios instance
const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:9000', // Replace with your API base URL
  timeout: 5000, // Request timeout
   headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
});


export default axiosInstance;