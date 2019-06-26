import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
    routes: [
        // 登录
        {
            path: '/login',
            name: 'login',
            hidden: false,
            component: () => import('@/views/Login.vue'),
        },
        // 注册
        {
            path: '/register',
            name: 'register',
            hidden: false,
            component: () => import('@/views/Register.vue'),
        },
        // 首页
        {
            path: '/',
            name: 'homepage',
            hidden: false,
            component: () => import('@/views/homepage/homepage.vue'),
            redirect: { name: 'firstpage' },
            children: [
                // 首页
                {
                    path: 'firstpage',
                    name: 'firstpage',
                    hidden: false,
                    component: () => import('@/views/homepage/firstpage.vue'),
                },
                // 商品列表
                {
                    path: 'list',
                    name: 'list',
                    hidden: false,
                    component: () => import('@/views/homepage/list.vue'),
                    meta: { title: '商品列表' }
                },
                // 商品详情
                {
                    path: 'detail',
                    name: 'detail',
                    hidden: false,
                    component: () => import('@/views/homepage/detail.vue'),
                    meta: { title: '商品详情' },
                },
                // 购物车
                {
                    path: 'shop',
                    name: 'shop',
                    hidden: false,
                    component: () => import('@/views/homepage/shop.vue'),
                    meta: { title: '购物车' }
                },
                // 填写订单信息
                {
                    path: 'address',
                    name: 'adderss',
                    hidden: false,
                    component: () => import('@/views/homepage/address.vue'),
                    meta: { title: '填写订单信息' }
                },
                // 选择支付方式
                {
                    path: 'pay',
                    name: 'pay',
                    hidden: false,
                    component: () => import('@/views/homepage/pay.vue'),
                    meta: { title: '选择支付方式' }
                },
                // 成功提交订单
                {
                    path: 'success',
                    name: 'success',
                    hidden: false,
                    component: () => import('@/views/homepage/Successview.vue'),
                    meta: { title: '成功提交订单' },
                },
                // 个人中心
                {
                    path: 'personal',
                    name: 'personal',
                    hidden: false,
                    component: () => import('@/views/homepage/personal.vue'),
                    meta: { title: '个人中心' },
                    redirect: { name: 'wait' },
                    children: [
                        {
                            path: 'wait',
                            name: 'wait',
                            hidden: false,
                            component: () => import('@/components/personal/shop.vue'),
                        },
                        {
                            path: 'transport',
                            name: 'transport',
                            hidden: false,
                            component: () => import('@/components/personal/shop.vue'),
                        },
                        {
                            path: 'end',
                            name: 'end',
                            hidden: false,
                            component: () => import('@/components/personal/shop.vue'),
                        },
                    ]
                },
            ]
        },
    ]
})
