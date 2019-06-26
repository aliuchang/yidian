<template>
    <div class="j-chair">
        <template v-for="i in jchairs">
            <div class="j-chairbox" :key="i.titles">
                <div class="j-img1">
                    <img :src="i.img">
                </div>
                <div class="j-img2"><img src="@/assets/img/j-a3.png"></div>
                <div class="j-english">{{i.english}}</div>
                <div class="j-title">^&nbsp; <span>{{i.title}}</span> &nbsp;^</div>
                <div class="j-info">{{i.info}}</div>
                <div class="j-price">{{i.price}}<span>RMB</span></div>
                <div class="j-back">
                    <div class="j-top">
                        <div class="j-english2">{{i.english}}</div>
                        <div class="j-title"><span>{{i.title}}</span></div>
                    </div>
                    <div class="j-bottom">
                        <div class="j-price j-price-left">{{i.price}}<span>RMB</span></div>
                        <span class="j-buy" @click="godetail">Buy</span>
                    </div>
                </div>
            </div>
        </template>
    </div>
</template>

<script>
export default {
    data(){
        return{
            jchairs:[
                {
                    img: require('@/assets/img/j-a2.png'),
                    english: 'ZEST ONE',
                    title: '装饰椅',
                    info: '现代小椅，随处安放的舒适',
                    price: '599.00',
                },
                {
                    img: require('@/assets/img/j-a4.png'),
                    english: 'MORNING TWILIGHT',
                    title: '晨暮青',
                    info: '脱开引力，自右旋转',
                    price: '499.00',
                },
                {
                    img: require('@/assets/img/j-a5.png'),
                    english: 'WINDSOR CHAIR',
                    title: '温莎椅',
                    info: '设计简单而不是尊贵',
                    price: '460.00',
                },
                {
                    img: require('@/assets/img/j-a6.png'),
                    english: 'LUXURY DINING CHAIR',
                    title: '轻奢餐椅',
                    info: '不止黑白灰的高雅',
                    price: '599.00',
                }
            ]  
        }
    },
    methods:{
        godetail(){
            console.log(1)
            this.$router.push({name:'detail'})
            window.scroll(0,0)
        }
    }
}
</script>

<style>
.j-chair{
    width: 1200px;
    height: 400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-around;
}
.j-chair .j-chairbox{
    width: 160px;
    height: 320px;
    float: left;
    margin: 20px 36px;
    transition: all .3s linear;
    position: relative;
    overflow: hidden;
}
.j-chair .j-back{
    width: 160px;
    height: 100px;
    background: #FFF;
    position: absolute;
    top: 332px;
    left: 0;
    right: 0;
    margin: 0 auto;
    font-size: 12px;
    transition: all .3s linear;
    padding: 15px 5px;
    box-sizing: border-box;
}
.j-chair .j-chairbox:hover .j-back{
    transform: translate(0,-102px);
}
.j-chair .j-chairbox:hover .j-img1{
    transform: scale(1.2);
    background: #F3F3F3;
    border-radius: 25px;
}
.j-chair img{
    width: 100%;
    height: 100%;
}
.j-chair .j-img1{
    width: 120px;
    height: 160px;
    margin: 20px auto;
    transition: all 0.6s;
}
.j-chair .j-top{
    width: 160px;
    height: 50px;
    background-color: #FFDC92;
    margin-top: -26px;
    z-index: 5;
}
.j-chair .j-english2{
    text-align: center;
    padding-top: 6px;
    font-weight: 800;
}
.j-chair .j-bottom{
    width: 160px;
    height: 50px;
    position: relative;
}
.j-chair .j-bottom .j-price-left{
    position: absolute;
    left: 0;
    bottom: 0;
}
.j-chair .j-buy{
    position: absolute;
    right: 5px;
    bottom: 0;
    border: 1px solid #999;
    padding: 2px 6px;
    cursor: pointer;
}
.j-chair .j-buy:hover{
    background:#FFDC92;
}
.j-chair .j-img2{
    width: 16px;
    height: 4px;
    margin: 0 auto;
}
.j-chair .j-english{
    padding-left: 4px;
    text-align: center;
    font-weight: 800;
    font-size: 14px;
    color: #7F7F7F;
    margin-top: 14px;
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;/*文本不换行*/
}
.j-chair .j-title{
    text-align: center;
    margin-top: 10px;
    color: #999;
}
.j-chair .j-title span{
    color: #000000;
}
.j-chair .j-info{
    font-size: 10px;
    color: #999;
    text-align: center;
    font-family: 'Courier New', Courier, monospace;
    margin-top: 10px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap; 
}
.j-chair .j-price{
    font-size: 20px;
    margin-top: 10px;
    text-align: center;
}
.j-chair .j-price span{
    font-size: 10px;
    color: #999;
    margin-left: 5px;
}
</style>

