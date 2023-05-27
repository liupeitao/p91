// 导入组件

// import VueRouter from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router'
import MainFrame from "../src/components/MainFrame.vue";
import mainFrame from "../src/components/MainFrame.vue";

const routes = [
    {
        path: '/index',
        name: 'Ma',
        component: mainFrame
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
