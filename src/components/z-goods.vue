<template>
    <div class="z-goods">
        <el-checkbox-group v-model="checkList1" class="z-goods2" @change="changes">
            <template v-for="(i, v) in goods">
                <!-- -->
                <div class="w-good">
                    <div class="item-input">
                        <el-checkbox class="item" size="medium" :label="v"></el-checkbox>
                    </div>
                    <div class="image1" @click="check">
                        <img :src="i.img" alt>
                    </div>
                    <ul class="info">
                        <li class="items">
                            <p class="ps">{{i.name}}</p>
                            <p>{{i.infos}}</p>
                        </li>
                        <li class="items">
                            <p>"{{i.ku}}"</p>
                        </li>
                        <li class="items">
                            <p>
                                W:
                                <span>{{i.num1}}</span>
                            </p>
                            <p>
                                H:
                                <span>{{i.num2}}</span>
                            </p>
                            <p>
                                L:
                                <span>{{i.num3}}</span>
                            </p>
                        </li>
                        <li class="items">
<!--                            <p>{{i.number}}</p>-->
                            <el-input-number v-model="i.number" :min="1" @change="changenum" :max="10" size="mini"></el-input-number>
                        </li>
                        <li class="items">
                            <p>
                                <span class="money">{{i.nums1}}</span>RMB
                            </p>
                        </li>
                        <li class="items">
                            <p>
                                <span class="money">{{i.nums2}}</span>RMB
                            </p>
                            <div class="bot">
                                <i class="el-icon-delete"></i>
                                删除
                            </div>
                        </li>
                    </ul>
                </div>
            </template>
        </el-checkbox-group>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                list: [],
                checkList1: [],
                freight: 0,
                allprice: 0
            };
        },
        methods: {
            check() {
                console.log(this.checkList);
            },
            changes() {
                // console.log(this.goods)
                this.freight = 0;
                this.allprice = 0;
                this.checkList1.forEach((i, v) => {
                    this.allprice =
                        this.allprice + this.goods[i].number * this.goods[i].nums1;
                    this.freight = 100 * (v + 1);
                });
                // console.log(this.allprice)
                // console.log(this.checklist)
                // console.log(this.checkList1)
                this.$emit("allchange", this.checkList1);
            },
            changenum(){
                this.$emit("numchange", this.goods)
            }
        },
        props: ["goods", "checklist"],
        watch: {
            'checklist'() {
                this.checkList1 = this.checklist
            },

        }
    };
</script>

<style>
    .z-goods .item-input {
        width: 46px;
        height: 100%;
        float: left;
    }

    .z-goods2 {
        width: 100%;
        height: 100%;
    }

    .z-goods .item-input .item {
        margin-left: 16px;
        padding-top: 100px;
    }

    .z-goods .w-good {
        width: 1200px;
        height: 214px;
        border-bottom: 2px solid #e5e5e5;
    }

    .z-goods .image1 {
        float: left;
        width: 162px;
        height: 214px;
    }

    .z-goods .image1 img {
        margin-top: 35px;
    }

    .z-goods .info {
        list-style: none;
        padding: 0;
        margin: 0;
        float: left;
        width: 992px;
        height: 100%;
        overflow: hidden;
    }

    .z-goods .items {
        float: left;
        width: 165px;
        height: 100%;
        padding-top: 50px;
        position: relative;
    }

    .z-goods .items p {
        font-family: "站酷文艺体", "Avenir", Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        font-size: 16px;
    }

    .z-goods .el-checkbox__label {
        display: none;
    }

    .z-goods .bot {
        position: absolute;
        bottom: 90px;
        left: 0;
        right: 0;
        height: 20px;
        width: 100%;
    }

    .z-goods .ps {
        font-weight: 700;
    }

    .z-goods .money {
        font-size: 22px;
        font-weight: 700;
    }

    .z-goods .y_desc_img img, .y_desc_img_title img {
        width: 100%;
        margin-bottom: 50px;
    }

    .z-goods.el-input-number--mini {
        margin-right: 20px;
        position: relative;
    }

    .z-goods .el-input-number__decrease, .el-input-number__increase {
        width: 20px !important;
        height: 20px !important;
        position: absolute;
        top: 0;
        bottom: 0;
        margin: auto 0;
        line-height: 25px;
        border-radius: 50%;
    }

    .z-goods .el-input__inner {
        display: inline-block;
        width: 50%;
        padding: 0 !important;
        /*margin-left: 10px;*/
        border-radius: 20px;
    }

    .z-goods .el-button:focus, .el-button:hover {
        background: #5ed5e0;
        color: #fff;
    }

    .z-goods  .y_info_desc .el-button {
        color: black;
        font-size: 18px;
        letter-spacing: 3px;
        width: 200px;
        border-radius: 0px;
        margin: 20px 10px 20px 0;
        border: 1px solid #b2b2b2;
    }
</style>
