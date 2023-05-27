
// import { createApp } from 'vue'
// import './style.css'
// import App from './App.vue'


// Vue.use(ElementUI);
// createApp(App).mount('#app')

import { createApp } from 'vue'
import './style.css'
// 引入element依赖文件
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from "../router/router.js";
const app = createApp(App)

app.config.productionTip = false
app.use(ElementPlus)
app.use(router)
app.mount('#app')
