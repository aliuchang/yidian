<template>
  <div class="z-goods">
    <template v-for="i in goods">
      <!-- -->
      <div class="w-good" :key="i.name">
        <div class="item-input">
          <el-checkbox class="item" size="medium"></el-checkbox>
        </div>
        <div class="image1">
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
            <p>1</p>
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      goods: [
        {
          img: require("@/assets/z-img/03.png"),
          name: "ADE-阿德",
          infos: "餐椅 简约风",
          ku: "白色 米黄色",
          num1: "45cm",
          num2: "50cm",
          num3: "60cm",
          nums1: 456.0,
          nums2: 456.0
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
          nums2: 467.0
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
          nums2: 105.0
        }
      ],
      list: [],
      checkList: []
    };
  }
}
</script>

<style>
.z-goods .item-input{
    width: 46px;
    height: 100%;
    float: left;
    
}
.z-goods .item-input .item{
    margin-left: 16px;
    padding-top:100px;
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
</style>
