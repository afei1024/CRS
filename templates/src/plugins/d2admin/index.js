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
    // BioBank---测试版      服务地址,图片上传文件
    Vue.prototype.$imgServerHost = imgServerHost
    Vue.prototype.$imghost = imgServerHost
    // BioBank---测试版      标签打印后台的url   -----这个url 不需要http://   切记
    Vue.prototype.$printUrl = printUrl

    // BioBank---本地开发      服务地址,图片上传文件
    // Vue.prototype.$imgServerHost = 'http://localhost:9635'
    // Vue.prototype.$imghost = 'http://localhost:9635'
    // // BioBank---本地开发      标签打印后台的url   -----这个url 不需要http://   切记
    // Vue.prototype.$printUrl = 'localhost:9635/api/print'

    // // BioBank---基础版   服务地址,图片上传文件
    // Vue.prototype.$imgServerHost = 'http://39.98.34.197:9672'
    // Vue.prototype.$imghost = 'http://39.98.34.197:9672'
    // // BioBank---基础版   标签打印后台的url   -----这个url 不需要http://   切记
    // Vue.prototype.$printUrl = '39.98.34.197:9672/api/print'

    // BioBank---标准版   服务地址,图片上传文件
    // Vue.prototype.$imgServerHost = 'http://47.108.24.36:8006'
    // Vue.prototype.$imghost = 'http://47.108.24.36:8006'
    // // BioBank---标准版   标签打印后台的url   -----这个url 不需要http://   切记
    // Vue.prototype.$printUrl = '47.108.24.36:8006/api/print'

    // // 四川濒危物种      服务地址,图片上传文件
    // // 文件上传
    // Vue.prototype.$uploadFile = 'http://192.168.27.3:9333/dir/assign'
    // Vue.prototype.$uploadFileurl = 'http://192.168.27.3:9333'
    // Vue.prototype.$imgServerHost = 'http://192.168.27.3:9655'
    // Vue.prototype.$imghost = 'http://192.168.27.3:9655'
    // // 四川濒危物种      标签打印后台的url   -----这个url 不需要http://   切记
    // Vue.prototype.$printUrl = '192.168.27.3:9655/api/print'

    // 北京协议医院---生物样本库系统
    // Vue.prototype.$imgServerHost = 'http://192.168.3.67:9655'
    // Vue.prototype.$imghost = 'http://192.168.3.67:9655'
    // Vue.prototype.$printUrl = '192.168.3.67:9655/api/print'

    // 世纪坛医院---生物样本库地址
    // Vue.prototype.$imgServerHost = 'http://192.168.177.128:9655'
    // Vue.prototype.$imghost = 'http://192.168.177.128:9655'
    // Vue.prototype.$printUrl = '192.168.177.128:9655/api/print'

    // 临沂人民医院---遗传检验科地址
    // Vue.prototype.$imghost = 'http://188.188.30.89:9655'
    // Vue.prototype.$printUrl = '188.188.30.89:9655/api/print'

    // // 广东佛山妇幼---标准版   服务地址,图片上传文件
    // Vue.prototype.$imgServerHost = 'http://39.98.34.197:9682'
    // Vue.prototype.$imghost = 'http://39.98.34.197:9682'
    // // 广东佛山妇幼---标准版   标签打印后台的url   -----这个url 不需要http://   切记
    // Vue.prototype.$printUrl = '39.98.34.197:9682/api/print'

    // // 省立医院---标准版   服务地址,图片上传文件
    // Vue.prototype.$imgServerHost = 'http://39.98.34.197:9694'
    // Vue.prototype.$imghost = 'http://39.98.34.197:9694'
    // // 省立医院---标准版   标签打印后台的url   -----这个url 不需要http://   切记
    // Vue.prototype.$printUrl = '39.98.34.197:9694/api/print'

    // // 长三角      服务地址,图片上传文件
    // // 文件上传
    // Vue.prototype.$uploadFile = 'http://weed1.labsop.cn:9333/dir/assign'
    // Vue.prototype.$uploadFileurl = 'http://weed1.labsop.cn:9333'
    // Vue.prototype.$imgServerHost = 'http://39.98.34.197:9692'
    // Vue.prototype.$imghost = 'http://39.98.34.197:9692'
    // // 长三角      标签打印后台的url   -----这个url 不需要http://   切记
    // Vue.prototype.$printUrl = '39.98.34.197:9692/api/print'

    // 工作流图片地址
    // Vue.prototype.$actiimghost_dqm = '//39.98.34.197:9635/api/'
    // Vue.prototype.$actiimghost_drugd = '//39.98.34.197:9650/api/'
    // Vue.prototype.$actiimghost_nuwa = '//39.98.34.197:9652/api/'
    // Element
    Vue.use(ElementUI)
    // 插件
    Vue.use(pluginError)
    Vue.use(pluginLog)
    Vue.use(pluginOpen)
    Vue.use(pluginPermission, options)
  }
}
