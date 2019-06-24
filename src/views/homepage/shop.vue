<template>
  <div class="z-shop">
    <z-status :statuss="status"></z-status>
    <div class="shop-title">
      <div class="shop-reight">
        <el-checkbox v-model="list" size="medium" class="input">全选</el-checkbox>
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
    <z-goods></z-goods>
    <div class="bott-1">
      <div class="bott-1-1">
        <span>3</span>个结果
      </div>
      <div class="bott-1-2">
        运费：
        <span>300.00</span> RMB
      </div>
      <div class="bott-1-3">
        应付总额：
        <span>Total payable:</span>
      </div>
      <div class="bott-1-4">
        <span>3146.00</span>RMB
      </div>
      <div class="jie">结 算</div>
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
export default {
  data() {
    return {
      status: "1",
      radio: "1",
      list: [],
      checkList: []
    };
  },
  components: {
    zStatus,
    zChair,
    zGoods
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
.z-shop .bott-1-3 span{
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
