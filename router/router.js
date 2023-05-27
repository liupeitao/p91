// 导入组件

// import VueRouter from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router'
import MainFrame from "../src/components/MainFrame.vue";


const routes = [
    {
        path: '/index',
        name: 'mainFrame',
        component: MainFrame
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
