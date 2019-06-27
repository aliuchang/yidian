<template>
    <div class="z-shop">
        <Crumbs/>
        <z-status :statuss="status"></z-status>
        <div class="shop-title">
            <div class="shop-reight">
                <el-checkbox v-model="list" size="medium" class="input" @change="changes">全选</el-checkbox>
            </div>
            <div class="shop-left">
                <div class="title">商品描述</div>
                <div class="title">颜色</div>
                <div class="title">尺码</div>
                <div class="title">数量</div>
                <div class="title">单价</div>
                <div class="title">总价</div>
            </div>
        </div>
        <!--   -->
        <z-goods :goods="good" :checklist="checkLists" @allchange="allchange2($event)"
                 @numchange='numchange2($event)'></z-goods>
        <div class="bott-1">
            <div class="bott-1-1">
                <span>3</span>个结果
            </div>
            <div class="bott-1-2">
                运费：
                <span>{{freight}}</span> RMB
            </div>
            <div class="bott-1-3">
                应付总额：
                <span>Total payable:</span>
            </div>
            <div class="bott-1-4">
                <span>{{allprice}}</span>RMB
            </div>
            <div class="jie" @click="push">结 算</div>
        </div>
        <div class="shop-item-tuijian">
            <img src="@/assets/z-img/z-tuiijan.png" alt>
        </div>
        <div class="shop-tuijian-li">
            <z-chair></z-chair>
        </div>
    </div>
</template>

<script>
    import zStatus from "@/components/z-status.vue";
    import zChair from "@/components/z-chair.vue";
    import zGoods from "@/components/z-goods.vue";
    import Crumbs from "@/components/crumbs.vue";

    export default {
        data() {
            return {
                status: "1",
                radio: "1",
                list: false,
                checkLists: [],
                good: [
                    {
                        img: require("@/assets/z-img/03.png"),
                        name: "ADE-阿德",
                        infos: "餐椅 简约风",
                        ku: "白色 米黄色",
                        num1: "45cm",
                        num2: "50cm",
                        num3: "60cm",
                        nums1: 456.0,
                        nums2: 456.0,
                        number: 1
                    },
                    {
                        img: require("@/assets/z-img/04.png"),
                        name: "ANTILOP-安迪咯",
                        infos: "高脚椅 简约风",
                        ku: "塑料 天蓝色",
                        num1: "45cm",
                        num2: "50cm",
                        num3: "60cm",
                        nums1: 467.0,
                        nums2: 467.0,
                        number: 1
                    },
                    {
                        img: require("@/assets/z-img/05.png"),
                        name: "KVART-卡特",
                        infos: "工作灯 北欧风",
                        ku: "黑色 可调节",
                        num1: "45cm",
                        num2: "50cm",
                        num3: "60cm",
                        nums1: 105.0,
                        nums2: 105.0,
                        number: 1
                    }
                ],
                freight: 0, //运费
                allprice: 0,  //总价
            };
        },
        components: {
            zStatus,
            zChair,
            zGoods,
            Crumbs
        },
        methods: {
            changes() {
                if (this.list) {
                    this.checkLists = []
                    this.good.forEach((i, v) => {
                        this.checkLists.push(v);
                    });
                } else {
                    this.checkLists = [];
                }
                // console.log(this.checkLists)
            },
            allchange2(res) {
                console.log(res)
                this.checkLists = res
                if (res.length == this.good.length) {
                    this.list = true;

                } else {
                    this.list = false;
                }

            },
            numchange2(res) {
                this.good = res
                this.allprice = 0
                this.freight = 0
                this.checkLists.forEach((i, v) => {
                    this.allprice =
                        this.allprice + this.good[i].number * this.good[i].nums1 + 100
                    this.freight = 100 * (v + 1);
                });
            },
            push(){
                if(this.allprice>0){
                    this.$router.push('/address')
                }else {
                    alert("请选择商品")
                }

            }
        },
        watch: {
            'checkLists'() {
                this.allprice = 0
                this.freight = 0
                this.checkLists.forEach((i, v) => {
                    this.allprice =
                        this.allprice + this.good[i].number * this.good[i].nums1 + 100
                    this.freight = 100 * (v + 1);
                });
            },
            'good'() {
                this.allprice = 0
                this.freight = 0
                this.checkLists.forEach((i, v) => {
                    this.allprice =
                        this.allprice + this.good[i].number * this.good[i].nums1 + 100
                    this.freight = 100 * (v + 1);
                });
            }
        }
    };
</script>

<style>
    .z-shop {
        width: 1200px;
        margin: 0 auto;
    }

    .z-shop .shop-title {
        width: 1196px;
        height: 65px;
        border: solid 2px rgba(0, 0, 0, 0.1);
    }

    .z-shop .shop-reight {
        float: left;
        width: 176px;
        margin-left: 20px;
        height: 100%;
        box-sizing: border-box;
    }

    .z-shop .shop-reight .input {
        float: left;
        margin-top: 23px;
    }

    .z-shop .shop-left {
        float: left;
        width: 1000px;
        height: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }

    .z-shop .el-checkbox__input.is-checked + .el-checkbox__label {
        color: #000000;
    }

    .z-shop .el-checkbox__label {
        font-family: zcoolwenyiti;
        font-size: 18px;
        color: rgba(0, 0, 0, 0.7);
    }

    .z-shop .title {
        font-family: zcoolwenyiti;
        font-size: 18px;
        color: rgba(0, 0, 0, 0.7);
    }

    .z-shop .shop-item {
        height: 207px;
        width: 100%;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        display: flex;
    }

    .z-shop .item-input {
        width: 46px;
        height: 100%;
    }

    .z-shop .item-input .item {
        margin-left: 16px;
        padding-top: 100px;
    }

    .z-shop .img-box {
        width: 127px;
    }

    .z-shop .img-box img {
        width: 100%;
        margin-top: 38px;
        margin-left: 36px;
    }

    .z-shop .textlisst {
        width: 1100px;
        color: #000;
    }

    .z-shop .shop-item-tuijian {
        width: 533px;
        margin: 120px auto 90px;
    }

    .z-shop .shop-item-tuijian img {
        width: 100%;
    }

    .z-shop .shop-tuijian-li {
        width: 1200px;
        height: 400px;
    }

    .z-shop .bott-1 {
        margin-top: 64px;
        position: relative;
        margin-bottom: 200px;
    }

    .z-shop .bott-1-1 {
        float: left;
        margin-left: 40px;
    }

    .z-shop .bott-1-2 span {
        font-size: 32px;
        font-weight: 700;
    }

    .z-shop .bott-1-3 {
        position: absolute;
        right: 190px;
        top: 0;
        width: 106px;
        height: 42px;
        font-size: 18px;
    }

    .z-shop .bott-1-3 span {
        font-family: Cabin-Bold;
        font-size: 10px;
        color: #000000;
        opacity: 0.6;
    }

    .z-shop .bott-1-4 {
        position: absolute;
        right: 5px;
        top: 0;
        font-size: 18px;
    }

    .z-shop .bott-1-4 span {
        font-size: 36px;
        color: #e72727;
        font-weight: 700;
    }

    .z-shop .jie {
        width: 250px;
        height: 80px;
        background-color: #7d7d7d;
        text-align: center;
        color: #fff;
        font-size: 30px;
        line-height: 80px;
        float: right;
        margin-top: 30px;
        font-weight: 600;
        box-shadow: 0 0 10px 1px #d0d0d0;
    }
</style>
