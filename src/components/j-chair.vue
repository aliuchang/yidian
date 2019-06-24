<template>
    <div class="J-chair">
        <template v-for="i in jchairs">
            <div class="j-chairbox" :key="i.titles">
                <div class="j-img1">
                    <img :src="i.img">
                </div>
                <div class="j-img2"><img src="../assets/j-a3.png" alt=""></div>
                <div class="j-english">{{i.english}}</div>
                <div class="j-title">^&nbsp <span>{{i.title}}</span> &nbsp^</div>
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
                    img: require('@/assets/j-img/j-a2.png'),
                    english: 'ZEST ONE',
                    title: '装饰椅',
                    info: '现代小椅，随处安放的舒适',
                    price: '599.00',
                },
                {
                    img: require('@/assets/j-img/j-a4.png'),
                    english: 'MORNING TWILIGHT',
                    title: '晨暮青',
                    info: '脱开引力，自右旋转',
                    price: '499.00',
                },
                {
                    img: require('@/assets/j-img/j-a5.png'),
                    english: 'WINDSOR CHAIR',
                    title: '温莎椅',
                    info: '设计简单而不是尊贵',
                    price: '460.00',
                },
                {
                    img: require('@/assets/j-img/j-a6.png'),
                    english: 'LUXURY DINING CHAIR',
                    title: '轻奢餐椅',
                    info: '不止黑白灰的高雅',
                    price: '599.00',
                },
                {
                    img: require('@/assets/j-img/j-a7.png'),
                    english: 'CASTLE PEAK CHAIR',
                    title: '青山椅',
                    info: '抽离繁琐的设计，体现美的线条',
                    price: '599.00',
                },
                {
                    img: require('@/assets/j-img/j-a8.png'),
                    english: 'CONCH CHAIR',
                    title: '海螺椅',
                    info: '现代小椅，随处安放的舒适',
                    price: '588.00',
                },
                {
                    img: require('@/assets/j-img/j-a9.png'),
                    english: 'WINDSOR CHAIR',
                    title: '温莎椅',
                    info: '设计简单而不是尊贵',
                    price: '460.00',
                },
                {
                    img: require('@/assets/j-img/j-a10.png'),
                    english: 'CHUN MU HOME',
                    title: '春沐椅',
                    info: '写意太师，蕴照东方',
                    price: '1290.00',
                },
                {
                    img: require('@/assets/j-img/j-a11.png'),
                    english: 'HAMMARN',
                    title: '哈马恩',
                    info: '设计简单而不是尊贵',
                    price: '268.00',
                },
                {
                    img: require('@/assets/j-img/j-a12.png'),
                    english: 'LAZY CHAIR',
                    title: '懒人椅子',
                    info: '拉丝不锈钢金属架，值得你选择',
                    price: '888.00',
                },
                {
                    img: require('@/assets/j-img/j-a13.png'),
                    english: 'OBEDIENCE FUJIJO',
                    title: '藤条椅',
                    info: '设计简单而不是尊贵',
                    price: '460.00',
                },
                {
                    img: require('@/assets/j-img/j-a14.png'),
                    english: 'NET RED CHAIR',
                    title: '网红椅',
                    info: '无任何人造板和贴皮',
                    price: '540.00',
                },
                {
                    img: require('@/assets/j-img/j-a15.png'),
                    english: 'CASTLE PEAK CHAIR',
                    title: '青山椅',
                    info: '抽离繁琐的设计，体现美的线条',
                    price: '599.00',
                },
                {
                    img: require('@/assets/j-img/j-a16.png'),
                    english: 'CONCH CHAIR',
                    title: '海螺椅',
                    info: '现代小椅，随处安放的舒适',
                    price: '588.00',
                },
            ]  
        }
    },
    methods: {
    godetail(){
        this.$router.push('detail'),
        window.scroll(0, 0);
    }
  }
}
</script>

<style>
.J-chair .j-chairbox{
    width: 160px;
    height: 320px;
    float: left;
    margin: 20px 66px;
    transition: all .3s linear;
    position: relative;
    overflow: hidden;
}
.J-chair .j-back{
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
.J-chair .j-chairbox:hover .j-back{
    transform: translate(0,-110px);
    /* box-shadow: 0.5px 0.5px 20px 5px rgba(0,0,0,0.1); */
}
.J-chair .j-chairbox:hover .j-img1{
    transform: scale(1.4);
    background: #F3F3F3;
    border-radius: 25px;
}
.J-chair img{
    width: 100%;
    height: 100%;
}
.J-chair .j-img1{
    width: 120px;
    height: 155px;
    margin: 20px auto;
    transition: all 0.6s;
}
.J-chair .j-top{
    width: 160px;
    height: 50px;
    background-color: #FFDC92;
    margin-top: -26px;
    z-index: 5;
}
.J-chair .j-english2{
    text-align: center;
    padding-top: 6px;
    font-weight: 800;
}
.J-chair .j-bottom{
    width: 160px;
    height: 50px;
    /* background-color: #FFDC92; */
    position: relative;
}
.J-chair .j-bottom .j-price-left{
    position: absolute;
    left: 0;
    bottom: 0;
}
.J-chair .j-buy{
    position: absolute;
    right: 5px;
    bottom: 0;
    border: 1px solid #999;
    padding: 4px 8px;
}
.J-chair .j-buy:hover{
    background:pink;
}
.J-chair .j-img2{
    width: 16px;
    height: 4px;
    margin: 0 auto;
}
.J-chair .j-english{
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
.J-chair .j-title{
    text-align: center;
    margin-top: 10px;
    color: #999;
}
.J-chair .j-title span{
    color: #000000;
}
.J-chair .j-info{
    font-size: 10px;
    color: #999;
    text-align: center;
    font-family: 'Courier New', Courier, monospace;
    margin-top: 10px;
}
.J-chair .j-price{
    font-size: 20px;
    margin-top: 10px;
    text-align: center;
}
.J-chair .j-price span{
    font-size: 10px;
    color: #999;
    margin-left: 5px;
}
</style>

