<template>
    <div class="n-nav">
        <template v-for="i in personal">
            <div class="title" :key="i.title">
                <img :src="i.icon" class="titleicon">
                <div class="line"></div>
                <div class="titlecont">
                    <p class="zh">{{i.title}}</p>
                    <p class="en">{{i.etitle}}</p>
                </div>
            </div>
            <div class="items" :key="i.etitle">
                <template  v-for="item in i.items">
                    <div class="item" :key="item.info">
                        <img :src="item.icon" class="itemicon">
                        <div class="iteminfo">{{item.info}}</div>
                    </div>
                </template>
            </div>
        </template>
    </div>
</template>

<script>
export default {
    data(){
        return {
            personal:[
                {
                    icon: require('../../assets/img/icon1.png'),
                    title: '个·人·中·心',
                    etitle: 'PERSONAL INFORMATION',
                    items: [
                        {
                            icon: require('@/assets/img/item1.png'),
                            info: '我的资料 / My profile'
                        },
                        {
                            icon: require('@/assets/img/item2.png'),
                            info: '收货地址管理 / Receiving address'
                        },
                        {
                            icon: require('@/assets/img/item3.png'),
                            info: '账户安全 / Account security'
                        }
                    ]
                },
                {
                    icon: require('@/assets/img/icon2.png'),
                    title: '我·的·订·单',
                    etitle: 'MY ORDER',
                    items: [
                        {
                            icon: require('@/assets/img/item4.png'),
                            info: '我的订单 / My order'
                        },
                        {
                            icon: require('@/assets/img/item5.png'),
                            info: '退换货管理 / Return and Exchange'
                        },
                        {
                            icon: require('@/assets/img/item6.png'),
                            info: '我的优惠券 / My coupon'
                        }
                    ]
                },
                {
                    icon: require('../../assets/img/icon3.png'),
                    title: '服·务·中·心',
                    etitle: 'SERVICE CENTER',
                    items: [
                        {
                            icon: require('@/assets/img/item7.png'),
                            info: '物流管理 / Logistics Management'
                        },
                        {
                            icon: require('@/assets/img/item8.png'),
                            info: '售后管理 / After-sales'
                        },
                        {
                            icon: require('@/assets/img/item9.png'),
                            info: '联系客服 / Contact Customer'
                        },
                        {
                            icon: require('@/assets/img/item10.png'),
                            info: '我的维权 / My rights'
                        }
                    ]
                }
            ]
        }
    }
}
</script>

<style>
.n-nav .title{
    height: 64px;
    background: #f3f3f3;
    display: flex;
    justify-content: center;
    align-items: center;
}
.n-nav .title .line{
    width: 2px;
    height: 22px;
    background: #c2c2c2;
    margin: 0 10px;
}
.n-nav .title .titlecont{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    color: #454545;
    font-size: 20px;
}
.n-nav .title .titlecont .en{
    font-size: 10px;
    color: #797979;
}
.n-nav .items{
    padding: 43px 0 43px 24px;
    background: #fff;
}
.n-nav .items .item{
    height: 42px;
    font-size: 14px;
    color: #9d9d9d;
    display: flex;
    align-items: center;
}
.n-nav .items .item .iteminfo{
    margin-left: 12px;
}
</style>
