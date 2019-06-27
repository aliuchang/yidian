// 支付方式
<template>
    <div class="n-pay">
        <paycrumbs/>
        <paystep statuss="3"/>
        <div class="ordertips">
            <img src="@/assets/img/ordertips.png" class="ordericon">
            <img src="@/assets/img/paytips.png" class="paytips">
            <p class="time">
                <span>{{payment.min}}</span>
                <span>{{payment.s}}</span>
                <span>{{payment.ms}}</span>
            </p>
            <div class="ordernum">{{payment.ordernum}}</div>
            <div class="payprice">{{payment.price}}</div>
        </div>
        <div class="paymenttips">
            <img src="@/assets/img/payment.png" class="paymenticon">
            <el-radio-group v-model="radio" @change="showselect">
            <div class="payment">
                <div class="fastpayment">
                    <el-radio label="1">快捷支付 (点击第三方设备进行付款)</el-radio>
                </div>
                <div class="sweepcode">
                    <el-radio label="2">扫码支付</el-radio>
                </div>
            </div>

            <el-radio-group v-model="select">
                <div class="select" :class="{ show : isshow }">

                        <div class="apily">
                            <el-radio label="1"><img src="@/assets/img/apily.png"></el-radio>
                        </div>
                        <div class="wechat">
                            <el-radio label="2"><img src="@/assets/img/wechat.png"></el-radio>
                        </div>

                </div>
            </el-radio-group>

            <div class="internetbank">
                <el-radio label="3">网银支付</el-radio>
            </div>
            </el-radio-group>
            <div class="total">
                <div class="title">
                    <div class="name">应付总额 ：</div>
                    <div class="ename"> Total payable ：</div>
                </div>
                <div class="paymoney">{{payment.price}}</div>
                <div class="rmb">RMB</div>
            </div>
            <div class="account" @click="buy">结算</div>
        </div>
    </div>
</template>

<script>
import paycrumbs from '@/components/crumbs.vue'
import paystep from '@/components/z-status.vue'

export default {
    data(){
        return {
            payment: {
                min: 0,
                s: 0,
                ms: 0,
                ordernum: 2019042814458299,
                price: '3146.00'
            },
            radio: '1',
            select: '1',
            isshow: false
        }
    },
    components:{
        paystep,
        paycrumbs
    },
    methods:{
        showselect(val){
            // console.log(val)
            if( val != 1 ){
                this.isshow = true
            }else if( val == 1 ){
                this.isshow = false
            }
        },
        buy(){
            this.$router.push({name:'success'})
            window.scroll(0,0)
        }
    }
}
</script>

<style>
.n-pay{
    width: 1200px;
    margin: 0 auto;
}

.n-pay .ordertips,.paymenttips{
    width: 1200px;
    height: 300px;
    margin: 60px auto;
    position: relative;
}
.n-pay .ordertips .ordericon,.paymenticon{
    position: absolute;
    top: 0;
    left: 0;
}
.n-pay .ordertips .paytips{
    position: absolute;
    top: 80px;
    left: 140px;
}
.n-pay .ordertips .time{
    width: 256px;
    position: absolute;
    top: 182px;
    left: 160px;
    display: flex;
    justify-content: space-around;
}
.n-pay .ordertips .time span{
    width: 56px;
    font-size: 30px;
    font-weight: 700;
    line-height: 42px;
    color: #e42828;
}
.n-pay .ordertips .ordernum,.payprice{
    font-size: 30px;
    font-weight: 700;
    position: absolute;
    top: 250px;
    left: 238px;
}
.n-pay .ordertips .payprice{
    left: 656px;
}
.n-pay .paymenttips{
    height: 620px;
    margin: 50px auto 100px;
}
.n-pay .paymenttips .payment{
    padding-top: 140px;
    padding-bottom: 20px;
    display: flex;
    justify-content: space-between;
}
.n-pay .el-radio-group{
    text-align: left;
}
.n-pay .el-radio__input{
    margin-left: 20px;
}
.n-pay  .el-radio__label{
    font-size: 18px;
    font-weight: 700;
    color: #333;
}
.n-pay .el-radio__inner{
    border: 1px solid #ccc;
    background: #ccc;
}
.n-pay .el-radio__inner::after{
    background-color: transparent;
}
.n-pay .el-radio__input.is-checked+.el-radio__label{
    color: #333;
}
.n-pay .el-radio__input.is-checked .el-radio__inner{
    border-color: #4cc0cb;
    background: #4cc0cb;
}
.n-pay .paymenttips .payment .fastpayment,.sweepcode{
    width: 561px;
    height: 67px;
    border: 1px solid #a8a8a8;
    display: flex;
    align-items: center;
}
.n-pay .select{
    height: 60px;
    padding-bottom: 20px;
    display: flex;
    align-items: center;
}
.n-pay .show{
    display: none;
}
.n-pay .select .apily,.wechat{
    margin-right: 70px;
    display: flex;
    align-items: center;
}
.n-pay .internetbank{
    width: 1198px;
    height: 67px;
    border: 1px solid #a8a8a8;
    display: flex;
    align-items: center;
    font-size: 18px;
    font-weight: 700;
    color: #333;
}
.n-pay .total{
    height: 160px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
}
.n-pay .total .name{
    font-size: 20px;
    color: #393939;
}
.n-pay .total .ename{
    font-size: 10px;
    color: #8c8c8c;
}
.n-pay .total .paymoney{
    font-size: 48px;
    font-weight: 700;
    letter-spacing: -5px;
    color: #e42828;
    margin: 0 10px;
}
.n-pay .account{
    width: 247px;
    height: 77px;
    background: #7d7d7d;
    font-size: 24px;
    color: #fff;
    font-weight: 700;
    text-align: center;
    line-height: 77px;
    box-shadow: 0 0 10px 1px #d0d0d0;
    float: right;
    cursor: pointer;
}
</style>
