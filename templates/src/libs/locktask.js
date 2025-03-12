// Vue
// import Vue from 'vue'
import store from '@/store/index'
// TODO 待改造
const locktask = {
}

const _LOCK_TIMEOUT = 60 * 30 // PRO
const _HEART_INT = 60000 // PRO 10秒钟检测一次

// const _LOCK_TIMEOUT = 6 // DEV
// const _HEART_INT = 1000 // DEV 1秒钟检测一次

let waits = 0
let timer = null

locktask.getWaits = function () {
  return waits
}

locktask.setWaits = function (s) {
  waits = s
}

locktask.start = function (isLock) {
  clearInterval(timer)
  timer = null
  this.setTimer(isLock)
}

locktask.setTimer = function (isLock) {
  if (timer == null && !isLock) {
    timer = setInterval(() => {
      // console.log('开始定时...每过一秒执行一次', ++waits)
      waits++
      // waits += 10
      if (waits > _LOCK_TIMEOUT) {
        store.dispatch('d2admin/lock/set', { isLock: true })
        clearInterval(timer)
      }
    }, _HEART_INT)
  }
}

locktask.clearInterval = function () {
  clearInterval(timer)
}

export default locktask
