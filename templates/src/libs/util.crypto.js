import CryptoJS from 'crypto-js'

const crypto = {}

crypto.encrypt = function (word, keyStr, ivStr) {
  keyStr = keyStr || 'dashoo20dashoo20'
  ivStr = ivStr || 'dashoo20dashoo20'
  let key = CryptoJS.enc.Utf8.parse(keyStr)
  let iv = CryptoJS.enc.Utf8.parse(ivStr)
  let srcs = CryptoJS.enc.Utf8.parse(word)

  let encrypted = CryptoJS.AES.encrypt(srcs, key, {
    iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
  })
  return encrypted.ciphertext.toString() // hex
  // return encrypted.toString() // base64
}
export default crypto
