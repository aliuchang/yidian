<template>
  <div class="n-shop">
    <template v-for="item in shopitem">
        <div class="shopitem" :key="item.title">
            <img :src="item.image">
            <div class="name">
              <p class="title">{{item.title}}</p>
              <p class="desc">{{item.desc}}</p>
            </div>
            <p class="num">{{item.num}}</p>
            <p class="price">{{item.price}}<span>RMB</span></p>
            <div class="status">
              <img src="../../assets/img/waitshop.png">
              <p>待发货</p>
            </div>
            <div class="btn">查看物流</div>
            <div class="detail">订单号: <span>{{item.detail}}</span></div>
        </div>
    </template>
  </div>
</template>

<script>
export default {
  props:['title'],
  created(){
    console.log(this.title)
  },
  data() {
    return {
      shopitem: [
        {
          image: require("../../assets/img/shop-poang.png"),
          title: "POÄNG-波昂",
          desc: "摇椅 北欧风",
          num: 1,
          price: '699.00',
          detail: 174683827949
        },
        {
          image: require("../../assets/img/shop-odgre.png"),
          title: " ODGER-奥德格",
          desc: "餐椅 北欧风",
          num: 1,
          price: '399.00',
          detail: 279274301847
        },
        {
          image: require("../../assets/img/shop-ade.png"),
          title: " ADE-阿德",
          desc: "餐椅 北欧风",
          num: 1,
          price: '456.00',
          detail: 174685227949
        },
        {
          image: require("../../assets/img/shop-antilop.png"),
          title: "ANTILOP-安迪咯",
          desc: "高脚椅 北欧风",
          num: 1,
          price: '467.00',
          detail: 174683894949
        }
      ]
    };
  }
};
</script>

<style>
.n-shop .shopitem{
  width: 864px;
  height: 210px;
  background: #fff;
  border-bottom: 2px solid #e5e5e5;
  font-family: '苹方';
  display: flex;
  align-items: center;
  position: relative;
}
.n-shop .shopitem>img{
  position: absolute;
  /* top: 46px; */
  left: 16px;
}
.n-shop .shopitem .name{
  font-weight: 700;
  position: absolute;
  top: 46px;
  left: 190px;
  font-size: 12px;
}
.n-shop .shopitem .name .desc{
  color: #838383;
  font-size: 10px;
  margin-top: 6px;
}
.n-shop .shopitem .num{
  font-weight: 700;
  position: absolute;
  top: 46px;
  left: 400px;
}
.n-shop .shopitem .price span{
  font-size: 8px;
  color: #7d7d7d;
  margin-left: 4px;
}
.n-shop .shopitem .price{
  font-weight: 700;
  position: absolute;
  top: 46px;
  left: 480px;
}
.n-shop .shopitem .status{
  font-weight: 700;
  font-family: '站酷文艺体';
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  position: absolute;
  top: 45px;
  left: 650px;
}
.n-shop .shopitem .status p{
  margin-top: 8px;
}
.n-shop .shopitem .btn{
  width: 78px;
  height: 30px;
  background: #7d7d7d;
  font-size: 12px;
  color: #fff;
  text-align: center;
  line-height: 30px;
  position: absolute;
  top: 40px;
  right: 30px;
}
.n-shop .shopitem .detail{
  position: absolute;
  bottom: 25px;
  right: 25px;
  font-size: 14px;
  color: #8c8c8c;
}
.n-shop .shopitem .detail span{
  font-size: 18px;
  color: #191919;
  font-weight: 700;
}
</style>
