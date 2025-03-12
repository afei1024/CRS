// Element
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// flex 布局库
import 'flex.css'
// 组件
import '@/components'
// svg 图标
import '@/assets/svg-icons'

// 功能插件
import pluginError from '@/plugin/error'
import pluginLog from '@/plugin/log'
import pluginOpen from '@/plugin/open'
import pluginPermission from '@/plugin/permission'

export default {
  async install (Vue, options) {
    // 设置为 false 以阻止 vue 在启动时生成生产提示
    // https://cn.vuejs.org/v2/api/#productionTip
    Vue.config.productionTip = false
    // 当前环境
    Vue.prototype.$env = process.env.NODE_ENV
    // 当前的 baseUrl
    Vue.prototype.$baseUrl = process.env.BASE_URL
    // 当前版本
    Vue.prototype.$version = process.env.VUE_APP_VERSION
    // 构建时间
    Vue.prototype.$buildTime = process.env.VUE_APP_BUILD_TIME

    var uploadFile, imgServerHost, printUrl

    if (process.env.NODE_ENV === 'development') {
      uploadFile = process.env.VUE_APP_UPLOADFILE
      imgServerHost = process.env.VUE_APP_IMGSERVERHOS
      printUrl = process.env.VUE_APP_PRINTURL
      $GlobalConfig.VUE_APP_API02 = process.env.VUE_APP_API02
    } else {
      uploadFile = $GlobalConfig.VUE_APP_UPLOADFILE
      imgServerHost = $GlobalConfig.VUE_APP_IMGSERVERHOS
      printUrl = $GlobalConfig.VUE_APP_PRINTURL
    }

    // 文件上传
    Vue.prototype.$uploadFile = uploadFile
    //测试版      服务地址,图片上传文件
    Vue.prototype.$imgServerHost = imgServerHost
    Vue.prototype.$imghost = imgServerHost
    //测试版      标签打印后台的url   -----这个url 不需要http://   切记
    Vue.prototype.$printUrl = printUrl

    //本地开发      服务地址,图片上传文件
    // Vue.prototype.$imgServerHost = 'http://localhost:9635'
    // Vue.prototype.$imghost = 'http://localhost:9635'
    // //本地开发      标签打印后台的url   -----这个url 不需要http://   切记
    // Vue.prototype.$printUrl = 'localhost:9635/api/print'



   
    // Element
    Vue.use(ElementUI)
    // 插件
    Vue.use(pluginError)
    Vue.use(pluginLog)
    Vue.use(pluginOpen)
    Vue.use(pluginPermission, options)
  }
}
