// src/utils/storage.js
import CryptoJS from 'crypto-js'

const SECRET_KEY = import.meta.env.VITE_STORAGE_SECRET

export const safeStorage = {
  setItem(key, value) {
    const ciphertext = CryptoJS.AES.encrypt(value, SECRET_KEY).toString()
    localStorage.setItem(key, ciphertext)
  },
  getItem(key) {
    const ciphertext = localStorage.getItem(key)
    if (!ciphertext) return null
    const bytes = CryptoJS.AES.decrypt(ciphertext, SECRET_KEY)
    return bytes.toString(CryptoJS.enc.Utf8)
  }
}