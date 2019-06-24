import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    // mode: 'history',
    // base: process.env.BASE_URL,
    routes:[
        //登录

        //列表页
        {
            path: '/list',
            name:'list',
            component: () => import('@/views/list'),
            meta: {title:'座椅'},
            children:[
                {
                    path:'detail',
                    name:'detail',
                    component: () => import('@/views/detail'),
                    // meta包含一些需要的属性
                    meta:{title:'座椅zi'},
                    children:[
                        {
                            path:'details',
                            name:'details',
                            component: () => import('@/views/detail'),
                            // meta包含一些需要的属性
                            meta:{title:'座椅zi'}
                        }
                    ]
                }
            ]
        },
        

       
        
    ]
})