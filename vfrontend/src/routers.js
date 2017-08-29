import Vue from 'vue';
import VueRouter from 'vue-router';
import store from './store'
import * as CookiesApi from 'utils/auth'
// in development env not use Lazy Loading,because Lazy Loading large page will cause webpack hot update too slow.so only in production use Lazy Loading

/* layout */
import Layout from '@/views/layout/Layout';

Vue.use(VueRouter);

/**
 * icon : the icon show in the sidebar
 * hidden : if hidden:true will not show in the sidebar
 * redirect : if redirect:noredirect will not redirct in the levelbar
 * noDropdown : if noDropdown:true will not has submenu
 * meta : { role: ['admin'] }  will control the page role
 **/

export const routes = [
    {path: '/login', component: require('@/views/login/login'), hidden: true},
    {path: '/404', component: require('@/views/error/404'), hidden: true},
    {path: '/401', component: require('@/views/error/401'), hidden: true},
    {
        path: '/',
        component: Layout,
        redirect: '/dashboard',
        name: 'dashboard',
        hidden: true,
        meta: {requiresAuth: true},
        children: [{path: 'dashboard', component: require('@/views/dashboard/index')}]
    },
    {
        path: '/users',
        component: Layout,
        redirect: '/user/index',
        name: '用户管理',
        icon: 'user',
        meta: {requiresAuth: true},
        children: [
            {path: 'user', component: require('@/views/users/user'), name: '用户列表'},
            {path: 'groups', component: require('@/views/users/usergroups'), name: '用户组列表'},
            {path: 'roles', component: require('@/views/users/roles'), name: '角色列表'},
        ]
    },
    {
        path: '/assets',
        component: Layout,
        redirect: '/assets/index',
        name: '主机管理',
        icon: 'server',
        meta: {requiresAuth: true},
        children: [
            {path: 'hosts', component: require('@/views/assets/hosts'), name: '主机列表'},
            {path: 'hostgroups', component: require('@/views/assets/hostgroups'), name: '主机组列表'},
        ]
    },
    {
        path: '/ansible',
        component: Layout,
        redirect: '/ansible/index',
        name: 'ansible管理',
        icon: 'leaf',
        meta: {requiresAuth: true},
        children: [
            {path: 'runcmd', component: require('@/views/ansible/runcmd'), name: '执行命令'},
        ]
    },
    // {
    //     path: '/chat',
    //     component: Layout,
    //     redirect: '/chat/index',
    //     name: '聊天管理',
    //     icon: 'wechat',
    //     meta: {requiresAuth: true},
    //     children: [
    //         {path: 'chat', component: require('@/views/chat/index'), name: '聊天'},
    //     ]
    // },
    {
        path: '/tools',
        component: Layout,
        redirect: '/tools/index',
        name: '工具管理',
        icon: 'cogs',
        meta: {requiresAuth: true},
        children: [
            {path: 'duty', component: require('@/views/tools/duty'), name: '值班交接'},
            {path: 'upload', component: require('@/views/tools/upload'), name: '上传管理'},
            {path: 'dragging', component: require('@/views/tools/dragging'), name: '拖拽编排'},
        ]
    },
    {
        path: '/jobs',
        component: Layout,
        redirect: '/jobs/index',
        name: '发布管理',
        icon: 'hourglass',
        meta: {requiresAuth: true},
        children: [
            {path: 'jobs', component: require('@/views/jobs/jobs'), name: '项目列表'},
            {path: 'jobgroups', component: require('@/views/jobs/jobgroups'), name: '项目组列表'},
        ]
    },
    {path: '*', redirect: '/404', hidden: true}
];

const router = new VueRouter({
    // mode: 'history', //后端支持可开
    scrollBehavior: () => ({y: 0}),
    routes
});

// 设置路由拦截
// 在vue-router的全局钩子中设置拦截
// 每个路由皆会的钩子函数
// to 进入 from 离开 next 传递
router.beforeEach((to, from, next) => {
    // console.log('to=', to.fullPath, '| from=', from.fullPath);
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!store.state.isLogin) {
            _checkToken().then(res => {
                store.dispatch("getUserInfo");
                next();
            }, function () {
                next({
                    path: '/login'
                })
            });
        } else {
            _checkToken().then(function () {
                store.dispatch("getUserInfo");
                next();
            }, function () {
                next({
                    path: '/login'
                })
            });
        }
    } else {
        next(); // 确保一定要调用 next()
    }
})

/**
 * Token验证，Token验证是否有效，时间验证过期
 * */
function _checkToken() {
    return new Promise(function (resolve, reject) {
        const token = CookiesApi.getToken();
        const token_time = CookiesApi.getTokenTime();
        const now_time = new Date().getTime();  // 毫秒数，token过期时间为 2小时
        if (token && (now_time - token_time) < 1000 * 60 * 60 * 2) {
            // 设置全局请求的token， 参考 https://segmentfault.com/q/1010000008595567/a-1020000008596744
            CookiesApi.setToken(token);
            CookiesApi.setTokenTime(token_time);
            resolve();
        } else {
            CookiesApi.removeToken();
            CookiesApi.removeTokenTime();
            reject();
        }
    })
}

export default router