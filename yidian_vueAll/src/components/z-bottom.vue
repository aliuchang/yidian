<template>
  <div class="z-bottom">
    <div class="fotter">
      <div class="b-left">
        <div class="img-body">
          <div class="img">
            <img src="@/assets/z-img/weixin.png" alt>
          </div>
        </div>
        <div class="img-body">
          <div class="img">
            <img src="@/assets/z-img/chengxu.png" alt>
          </div>
        </div>
        <div class="img-body">
          <div class="img last">
            <img src="@/assets/z-img/dianhua.png" alt>
          </div>
        </div>
      </div>
      <div class="b-right">
        <ul class="ri-body">
          <li>
            <div class="bo-title">售后保障</div>
            <div>物流配送</div>
            <div>收货指南</div>
          </li>
          <li>
            <div class="bo-title">购物无忧</div>
            <div>品质保证</div>
            <div>保养说明</div>
          </li>
          <li>
            <div class="bo-title">售后保障</div>
            <div>自由定制</div>
          </li>
        </ul>
      </div>
      <div class="bottom-last">
        <div class="bottom-name">官方微信</div>
        <div class="bottom-name name2">小程序</div>
        <div class="bottom-name name3">400-373-8333</div>
        <div class="number">© Inter A LTTLE LIFE Systems B.V. 1999 - 2019</div>
        <div class="bottom-search">
          <input type="text" placeholder="Search for what you want ">
          <div class="submit">
            <i class="iconfont icon-you"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    
}
</script>

<style>
.z-bottom {
  height: 276px;
  border-top: 2px solid #000;
  padding-top: 40px;
  box-sizing: border-box;
}
.z-bottom .fotter {
  width: 1200px;
  margin: 0 auto;
}
.z-bottom .b-left {
  width: 514px;
  float: left;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding-top: 29px;
}
.z-bottom .b-right {
  width: 686px;
  float: left;
  padding-top: 31px;
}
.z-bottom .img-body .last {
  padding-top: 30px;
}
.z-bottom .img-body span {
  font-size: 14px;
  font-family: zcoolwenyiti;
  color: #000000;
  opacity: 0.9;
}
.z-bottom .ri-body {
  width: 100%;
  display: flex;
  justify-content: space-around;
}
.z-bottom .ri-body li {
  padding-top: 20px;
  height: 100%;
  width: 33.3%;
  font-family: NotoSansHans-Regular;
  font-size: 12px;
}
.z-bottom .ri-body li div {
  padding-top: 21px;
}
.z-bottom .ri-body li .bo-title {
  padding: 0;
  font-family: zcoolwenyiti;
  font-size: 18px;
  color: #000000;
  opacity: 0.8;
  font-weight: 600;
}
.z-bottom .bottom-last {
  display: flex;
  justify-content: flex-start;
  width: 100%;
  height: 100px;
  align-items: center;
}
.z-bottom .bottom-name {
  font-family: zcoolwenyiti;
  font-size: 13.94px;
  color: #000000;
  opacity: 0.9;
  margin-left: 58px;
  font-weight: 600;
}
.z-bottom .bottom-last .name2 {
  margin-left: 120px;
}
.z-bottom .bottom-last .name3 {
  margin-left: 100px;
}
.z-bottom .bottom-last .number {
  margin-left: 70px;
  font-family: Cabin-Bold;
  font-size: 12px;
  color: #000000;
  opacity: 0.6;
  font-weight: 500;
}
.z-bottom .bottom-search {
  width: 328px;
  height: 36px;
  display: flex;
}
.z-bottom .bottom-search input {
  height: 36px;
  background-color: #dbdbdb;
  width: 284px;
  outline: none;
  border: 0;
  padding-left: 10px;
  box-sizing: border-box;
  margin-left: 32px;
}
.z-bottom .bottom-search input::-webkit-input-placeholder {
  color: #fff;
  font-family: Cabin-Bold;
  font-size: 12px;
}
.z-bottom .bottom-search .submit {
  width: 45px;
  height: 36px;
  background-color: #8f8f8f;
  color: #fff;
  text-align: center;
  line-height: 36px;
}
.z-bottom .bottom-search .submit i {
  font-size: 12px;
}
</style>
