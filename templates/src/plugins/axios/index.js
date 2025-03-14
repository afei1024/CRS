import store from '@/store'
import axios from 'axios'
import { Message } from 'element-ui'
import util from '@/libs/util.js'
// import router from '@/router/index'
import loading from '@/libs/util.loading.js'
// import message from '@/libs/util.message'
import permission from '@/libs/util.permission.js'

// 创建一个错误
function errorCreate (msg) {
  const error = new Error(msg)
  errorLog(error)
  throw error
}

// 反馈消息弹框提示
function noticeMsg (dataAxios, type) {
  if (!dataAxios.msg) {
    return
  }
  Message({
    message: dataAxios.msg,
    type: type,
    duration: 3 * 1000
  })
}

// 记录和显示错误
function errorLog (error) {
  // 添加到日志
  store.dispatch('d2admin/log/push', {
    message: '数据请求异常',
    type: 'danger',
    meta: {
      error
    }
  })
  // 打印到控制台
  if (process.env.NODE_ENV === 'development') {
    util.log.danger('>>>>>> Error >>>>>>')
    console.log(error)
  }
  // 显示提示
  Message({
    message: error.message,
    type: 'error',
    duration: 5 * 1000
  })
}

var apiBaseURL, tenant
if (process.env.NODE_ENV === 'development') {
  apiBaseURL = process.env.VUE_APP_API
  tenant = process.env.VUE_APP_TENANT
} else {
  apiBaseURL = $GlobalConfig.VUE_APP_API
  tenant = $GlobalConfig.VUE_APP_TENANT
}

// 创建一个 axios 实例
const service = axios.create({
  baseURL: apiBaseURL,
  timeout: 40000 // 请求超时时间
})

// 请求拦截器
service.interceptors.request.use(
  config => {
    if (!permission.access(config, store)) {
      // eslint-disable-next-line no-throw-literal
      throw {
        type: '403',
        config: config
      }
    }
    loading.show(config)
    // 在请求发送之前做一些处理
    config.headers['Tenant'] = tenant
    // console.log(tenant, 'tenant', apiBaseURL, 'apiBaseURL')
    const token = util.cookies.get('token')
    // 让每个请求携带token-- ['Authorization']为自定义key 请根据实际情况自行修改
    config.headers['Authorization'] = 'Bearer ' + token
    // 数据权限Ids
    const ids = util.cookies.get('ids')
    config.headers['Ids'] = ids
    return config
  },
  error => {
    // 发送失败
    console.log(error)
    Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  response => {
    // dataAxios 是 axios 返回数据中的 data
    const dataAxios = response.data
    // 这个状态码是和后端约定的
    const { code } = dataAxios
    // 根据 code 进行判断
    if (code === undefined) {
      // 如果没有 code 代表这不是项目后端开发的接口 比如可能是 D2Admin 请求最新版本
      return dataAxios
    } else {
      // 有 code 代表这是一个后端接口 可以进行进一步的判断
      switch (code) {
        case 0:
          noticeMsg(dataAxios, 'success')
          // [ 示例 ] code === 0 代表没有错误
          if (dataAxios.data) { // && dataAxios.data.info
            return dataAxios.data
          } else {
            return response
          }
        case 1:
          noticeMsg(dataAxios, 'error')
          return response
        case -1:
          // code === -1 "保存失败"
          errorCreate(`[ code: -1 ] ${dataAxios.msg}`)
          break
        case -2:
          // code === -2 "已存在，请勿重复添加"
          errorCreate(`[ code: -2 ] ${dataAxios.msg}`)
          break
        case -3:
          // code === -3 "操作失败，请求信息不完整"
          errorCreate(`[ code: -3 ] ${dataAxios.msg}`)
          break
        case 'xxx':
          // [ 示例 ] 其它和后台约定的 code
          errorCreate(`[ code: xxx ] ${dataAxios.msg}`)
          break
        case 600:
          // errorCreate(`[code: 600] ${dataAxios.msg}`)
          return response
        case 601:
          // errorCreate(`[code: 601] ${dataAxios.msg}`)
          return response
        case 10001:
          // errorCreate(`[code: 10001] ${dataAxios.msg}`)
          return response
        default:
          // 不是正确的 code
          errorCreate(`${dataAxios.msg}`)
          break
      }
    }
  },
  error => {
    if (error && error.response) {
      switch (error.response.status) {
        case 400:
          error.message = '请求错误'
          break
        case 401:
          error.message = '未授权，请登录'
          break
        case 403:
          error.message = '拒绝访问'
          break
        case 404:
          error.message = `请求地址出错: ${error.response.config.url}`
          break
        case 408:
          error.message = '请求超时'
          break
        case 500:
          error.message = '服务器内部错误'
          break
        case 501:
          error.message = '服务未实现'
          break
        case 502:
          error.message = '网关错误'
          break
        case 503:
          error.message = '服务不可用'
          break
        case 504:
          error.message = '网关超时'
          break
        case 505:
          error.message = 'HTTP版本不受支持'
          break
        default:
          break
      }
    }
    errorLog(error)
    return Promise.reject(error)
  }
)

export default service
