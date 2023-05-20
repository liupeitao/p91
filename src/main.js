
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
const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')
