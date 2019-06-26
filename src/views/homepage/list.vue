<template>
    <div class="j-box">
        <!-- 轮播图开始 -->
        <div class="banner">
            <el-carousel :interval="4000" arrow="always">
            <el-carousel-item >
                <img src="@/assets/j-img/j-lunbo1.png" alt="">
            </el-carousel-item>
            <el-carousel-item >
                <img src="@/assets/j-img/j-lunbo2.png" alt="">
            </el-carousel-item>
            <el-carousel-item >
                <img src="@/assets/j-img/j-lunbo3.png" alt="">
            </el-carousel-item>
            <el-carousel-item >
                <img src="@/assets/j-img/j-lunbo4.png" alt="">
            </el-carousel-item>
        </el-carousel>
        </div>
        <!-- 轮播图结束 -->
        <!-- 面包屑开始 -->
        <Crumbs></Crumbs>
        <!-- 面包屑结束 -->
        <!-- 按钮开始 -->
        <div class="j-option">
            <div class="j-sort">
                <span class="j-sort-left">排&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;序</span>
                <span class="j-sort-right">
                    <el-select v-model="value" placeholder="按销量排序">
                        <el-option lable="按销量排序" value="按销量排序"></el-option>
                        <el-option lable="按综合排序" value="按综合排序"></el-option>
                        <el-option lable="按价格排序" value="按价格排序"></el-option>
                    </el-select>
                </span>
            </div>
            <div class="j-sort j-sort2">
                <span class="j-sort-left">价&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;格</span>
                <span class="j-price-right1 j-price-right2"><el-input v-model="input" placeholder="￥300"></el-input></span> —
                <span class="j-price-right1"><el-input v-model="input1" placeholder="￥600"></el-input></span>
            </div>
            <div class="j-sort">
                <span class="j-sort-left">面料材质</span>
                <span class="j-sort-right">
                    <template v-for="item in texture">
                        <span class="j-caizhi-right" :class="[type==item.id?'hover':'hover1']" @click="getData(item.id)">{{ item.title }}</span>
                    </template>
                </span>
            </div>
            <div class="j-sort j-sort2">
                <span class="j-sort-left">风&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;格</span>
                <span class="j-sort-right">
                    <span class="j-caizhi-right">日式</span>
                    <span class="j-caizhi-right">北欧</span>
                    <span class="j-caizhi-right">新中式</span>
                </span>
            </div>
            <div class="j-sort">
                <span class="j-sort-left">适用人数</span>
                <span class="j-sort-right">
                    <span class="j-caizhi-right">单人</span>
                    <span class="j-caizhi-right">双人</span>
                    <span class="j-caizhi-right">三人</span>
                </span>
            </div>
            <div class="j-sort j-sort2">
                <span class="j-sort-left">五星脚材质</span>
                <span class="j-sort-right j-sort-last">
                    <span class="j-caizhi-right">铁艺脚</span>
                    <span class="j-caizhi-right">实木脚</span>
                </span>
            </div>
        </div>
        <!-- 按钮结束 -->
        <div class="j-body">
            <div class="j-body1">
                <img src="@/assets/j-img/j-a1.png" alt="">
                <p class="j-body-price">{{jval1}}<span>RMB</span></p>
                <p class="j-body-go" @click="godetail">GO</p>
            </div>
            <Jchair></Jchair>
        </div>
        <!-- 分页开始 -->
        <div class="j-page">
            <el-pagination
                background
                layout="prev, pager, next"
                :total="1000">
            </el-pagination>
        </div>
        <!-- 分页结束 -->
    </div>
</template>

<script>
import Jchair from '@/components/j-chair.vue'
import Crumbs from '@/components/crumbs.vue'
export default {
    data(){
        return{
                jval1: "1029.00",
                value: '',
                input: '',
                input1: '',
                type:'wangbu',
                texture:[{id:1,title:'网布'},{id:2,title:'牛皮'}]

        };
    },
    components: {
        Jchair,
        Crumbs
    },
    mounted(){ // 加载时执行
        this.$axios.post("/api/goods/")
            .then((res)=>{
                console.log(res)
            })


    },
    methods: {
    godetail(){
        this.$router.push('detail'),
        window.scroll(0, 0);``
    },
    getData(v){
        alert(v)
      this.type = v;
    }
  }
}
</script>
<style >
.j-box{
    width: 100%;
}
.j-box span{
    cursor: pointer;
}
.j-box .banner{
    width: 1200px;
    height: 400px;
    margin: 0 auto;
}
.j-box img{
    width: 100%;
    height: 100%;
}
.j-box .el-carousel--horizontal .el-carousel__container {
    position: relative;
    height: 400px;
}
.j-box .j-option{
    width: 1200px;
    height: 240px;
    margin: 50px auto;
}
.j-box .j-sort{
    width: 45%;
    height: 60px;
    float: left;
    display: flex;
    justify-content: flex-start;
    align-items: center;
}
.j-box .j-sort2{
    margin-left: 100px;
}
.j-box .j-sort-left{
    width: 90px;
    height: 100%;
    line-height: 60px;
    padding-right: 10px;
}
.j-box .j-sort-right{
    height: 100%;
    line-height: 60px;
}
.j-box .el-input__inner{
    border-radius: 20px;
    text-align: center;
}
.j-box .j-price-right1 .el-input{
    width: 100px;
}
.j-box .j-caizhi-right{
    height: 60px;
    line-height: 60px;
    border-radius: 20px;
    border: 1px solid #e6e6e6;
    padding: 8px 40px;
    margin-right: 20px;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
.j-box .j-caizhi-right:hover{
    background-color: #5ED5E0;
    color: #fff;
}
.j-box .j-body{
    width: 1200px;
    height: 1420px;
    margin: 70px auto;
}
.j-box .j-body1{
    width: 50%;
    height: 320px;
    background: #f3f3f3;
    position: relative;
    float: left;
    margin: 20px 0;
}
.j-box .j-body1 img{
    height: 350px;
    margin-top: -40px;
    margin-left: -40px;
}
.j-box .j-body-price{
    font-size: 24px;
    position: absolute;
    top: 190px;
    right: 48px;
}
.j-box .j-body-price span{
    font-size: 10px;
    color: #999;
    margin-left: 10px;
}
.j-box .j-body-go{
    width: 66px;
    height: 30px;
    background-color: #5ED5E0;
    position: absolute;
    right: 100px;
    top: 240px;
    text-align: center;
    line-height: 30px;
    color: #fff;
    cursor: pointer;
}
.j-box .j-page{
    width: 400px;
    height: 30px;
    margin: 60px auto;
}
.j-box .j-page .el-pagination .el-pager .number{
    border-radius: 50%;
}
.j-box .j-page .el-pagination .btn-prev{
    border-radius: 50%;
}
.j-box .j-page .el-pagination .btn-next{
    border-radius: 50%;
}
.j-box .j-page .el-pagination .el-pager .btn-quicknext{
    border-radius: 50%;
}
    .hover{
        background-color:red;
    }
</style>

