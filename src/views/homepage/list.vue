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
                        <span class="j-caizhi-right" :class="[type == item.id? 'hover':'hover1']" @click="textureClick(item.id)">{{item.title}}</span>
                    </template>
                </span>
            </div>
            <div class="j-sort j-sort2">
                <span class="j-sort-left">风&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;格</span>
                <span class="j-sort-right">
                    <template v-for="item in style">
                        <span class="j-caizhi-right" :class="[type2 == item.id? 'hover':'hover1']" @click="styleClick(item.id)">{{item.title}}</span>
                    </template>
                </span>
            </div>
            <div class="j-sort">
                <span class="j-sort-left">适用人数</span>
                <span class="j-sort-right">
                    <template v-for="item in fit_people">
                        <span class="j-caizhi-right" :class="[type3 == item.id? 'hover':'hover1']" @click="fit_peopleClick(item.id)">{{item.title}}</span>
                    </template>
                </span>
            </div>
            <div class="j-sort j-sort2">
                <span class="j-sort-left">五星脚材质</span>
                <span class="j-sort-right ">
                    <template v-for="item in materials">
                        <span class="j-caizhi-right" :class="[type4 == item.id? 'hover':'hover1']" @click="materialsClick(item.id)">{{item.title}}</span>
                    </template>
                </span>
            </div>
        </div>
        <!-- 按钮结束 -->
        <!-- 座椅开始 -->
        <div class="j-body">
            <div class="j-body1">
                <img src="@/assets/j-img/j-a1.png" alt="">
                <p class="j-body-price">{{jval1}}<span>RMB</span></p>
                <p class="j-body-go" @click="godetail">GO</p>
            </div>
            <div class="J-chair">
                <template v-for="i in jchairs">
                    <div class="j-chairbox" :key="i.titles">
                        <div class="j-img1">
                            <img :src="i.img">
                        </div>
                        <div class="j-img2"><img src="@/assets/j-a3.png" alt=""></div>
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
                                <span class="j-buy" @click="godetail(i.id)">Buy</span>
                            </div>
                        </div>
                    </div>
                </template>
            </div>
            <!-- 座椅结束 -->
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

    </div>
</template>

<script>
import Crumbs from '@/components/crumbs.vue'
export default {
    data(){
        return{
            jval1: "1029.00",
            value: '',
            input: '',
            input1: '',
            jchairs:[

            ],
            type: '',
            type2:'',
            type3: '',
            type4:'',
            texture:[],
            style:[],
            fit_people:[],
            materials:[],
        };
    },
    components: {
        Crumbs
    },
    mounted(){
        if(localStorage.yiS_id !==undefined){
            this.type2 = localStorage.yiS_id
        }
        if(localStorage.yiT_id !==undefined){
            this.type = localStorage.yiT_id
        }
        if(localStorage.yiF_id !==undefined){
            this.type3 = localStorage.yiF_id
        }
        if(localStorage.yiM_id !==undefined){
            this.type4 = localStorage.yiM_id
        }



        this.$axios.get("/api/goods/attr/").then((res)=>{
            console.log(res.data)
            this.style = res.data.style
            this.fit_people = res.data.fitPeople
            this.texture = res.data.textrue
            this.materials = res.data.materials
        })
        this.filter_goods(this.type2,this.type,this.type3,this.type4)

    },
    methods: {
        setData(datas){
            console.log(datas)
            /*
            * [{
                    img: require('@/assets/j-img/j-a2.png'),
                    english: 'ZEST ONE',
                    title: '装饰椅',
                    info: '现代小椅，随处安放的舒适',
                    price: '599.00',
                }]
            * */
            let arr = []
            for(let item of datas){
                let obj = {}
                obj.img = item.img[0].img
                obj.english = item.en_name
                obj.title = item.name
                obj.info = item.desc
                obj.price = item.price
                obj.id = item.id
                arr.push(obj)
            }
            console.log(arr)
            this.jchairs = arr

        },

        godetail(id){
            this.$router.push({'name':'detail',params:{'id':id}})
            window.scroll(0, 0);
        },
        styleClick(v){
            this.type2 = v
            localStorage.yiS_id = v
            this.filter_goods(this.type2,this.type,this.type3,this.type4)
        },
        textureClick(v){
            this.type = v
            localStorage.yiT_id = v
            this.filter_goods(this.type2,this.type,this.type3,this.type4)
        },
        fit_peopleClick(v){
            this.type3 = v
            localStorage.yiF_id = v
            this.filter_goods(this.type2,this.type,this.type3,this.type4)
        },
        materialsClick(v){
            this.type4 = v
            localStorage.yiM_id = v
            this.filter_goods(this.type2,this.type,this.type3,this.type4)
        },
        filter_goods(s_id,t_id,f_id,m_id){
            let data = new FormData()
            data.append('t_id',t_id)
            data.append('s_id',s_id)
            data.append('f_id',f_id)
            data.append('m_id',m_id)
            this.$axios.post("/api/goods/",data).then((res)=>{
                this.setData(res.data)
            })
        }
    },
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

    .hover{
        background-color: #5ED5E0;
        color: #fff;
    }
.j-box .j-body{
    width: 1200px;
    height: 1540px;
    margin: 50px auto;
    position: relative;
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
    position: absolute;
    bottom: 0;
    left:400px;
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
.j-page .is-background .el-pager .more{
    width: 20px;
}
/*座椅开始*/
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
/*  座椅结束  */
</style>

