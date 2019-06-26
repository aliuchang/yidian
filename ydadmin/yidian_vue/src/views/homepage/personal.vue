// 个人中心
<template>
  <div class="n-personal">
    <percrumbs/>
    <div class="n-information">
      <div class="n-information-left">
        <p class="name">
          <img src="@/assets/img/headportrait.png" class="headportrait">
          青花瓷的秘密
          <img src="@/assets/img/viplogo.png" class="viplogo">
        </p>
        <pernav/>
      </div>
      <div class="n-information-right">
        <div class="infocard">
          <img src="@/assets/img/headphone.png">
          <div class="infocont">
            <p class="title">{{information.title}}</p>
            <p class="autograph">
              {{information.autograph}}
              <img src="@/assets/img/edit.png">
            </p>
            <div class="news">
              <p class="nickname">
                昵称:
                <span>{{information.nickname}}</span>
              </p>
              <p class="gender">
                性别:
                <span>{{information.gender}}</span>
              </p>
              <p class="address">
                现居:
                <span>{{information.address}}</span>
              </p>
              <p class="phone">
                手机:
                <span>{{information.phone}}</span>
              </p>
            </div>
          </div>
          <div class="information">
            <img src="@/assets/img/message.png">
            <img
              src="@/assets/img/shopppingbag.png"
              style="height: 24px;width:auto;margin:0 20px 0 50px;"
            >
          </div>
        </div>
        <pertab title="this.title"/>
        <div class="tabitem">
          <div class="shop">商品</div>
          <div class="shopdesc">商品描述</div>
          <div class="num">数量</div>
          <div class="price">单价</div>
          <div class="status">状态</div>
          <div class="btn">查看</div>
        </div>
        <router-view/>
      </div>
    </div>
    <img src="@/assets/img/featured-prodects.png">
    <perchair/>
  </div>
</template>

<script>
import percrumbs from "@/components/crumbs.vue";
import pernav from "@/components/personal/nav.vue";
import pertab from "@/components/personal/tab.vue";
import perchair from "@/components/personal/j-chair.vue";

export default {
  data() {
    return {
      information: {
        title: "青花瓷的秘密",
        autograph: "我们不相信会有完美无缺的家，要相信自己可以~~",
        nickname: "青花瓷的秘密",
        gender: "女",
        address: "山西-太原",
        phone: "18535053757"
      }
    };
  },
  components: {
    percrumbs,
    pernav,
    pertab,
    perchair
  }
};
</script>

<style>
.n-personal .n-information {
  width: 1200px;
  margin: 0 auto;
  padding-top: 50px;
  display: flex;
  justify-content: space-between;
}
.n-personal .n-information-left {
  width: 278px;
  height: 1002px;
  border: 2px solid #e5e5e5;
}
.n-personal .n-information-left .name {
  height: 132px;
  background: #fff;
  color: #3e3e3e;
  line-height: 132px;
  position: relative;
}
.n-personal .n-information-left .name .headportrait {
  position: absolute;
  top: -40%;
  left: 0;
  right: 0;
  margin: 0 auto;
}
.n-personal .n-information-left .name .viplogo {
  position: absolute;
  top: 86px;
  left: 0;
  right: 0;
  margin: 0 auto;
}
.n-personal .n-information-right .infocard {
  width: 864px;
  height: 200px;
  padding: 30px;
  box-sizing: border-box;
  background: #fff;
  border: 2px solid #e5e5e5;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}
.n-personal .n-information-right .infocard .infocont {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-left: 20px;
  font-size: 18px;
  color: #343434;
}
.n-personal .n-information-right .infocard .infocont .autograph {
  font-size: 10px;
  color: #7e7e7e;
  margin: 12px 0 16px;
}
.n-personal .n-information-right .infocard .infocont .news {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  font-size: 14px;
  color: #444;
}
.n-personal .n-information-right .infocard .infocont .news p {
  width: 260px;
  margin-top: 25px;
  display: flex;
  justify-content: flex-start;
}
.n-personal .n-information-right .infocard .infocont .news p span {
  font-size: 12px;
  color: #838383;
}
.n-personal .n-information-right .information {
  display: flex;
}
.n-personal .tabitem {
  width: 840px;
  height: 61px;
  padding-left: 20px;
  border: 2px solid #e5e5e5;
  background: #fff;
  font-size: 18px;
  color: #737373;
  display: flex;
  align-items: center;
}
.n-personal .tabitem .shop {
  width: 170px;
  text-align: left;
}
.n-personal .tabitem .shopdesc {
  width: 158px;
  text-align: left;
}
.n-personal .n-information-right .tabitem .num,
.price,
.status,
.btn {
  width: 128px;
}
</style>
