<template>
  <div class="successview">
    <Crumbs/>
    <z-status :statuss="status"></z-status>
    <div class="successimg">
      <img src="@/assets/z-img/successimg.png" alt>
      <span class="number">2019042814458299</span>
    </div>
    <div class="successview-buttom">
      <div class="btn check" @click="push1()">查看订单</div>
      <div class="btn more1" @click="push2()">还想看看</div>
    </div>
    <div class="recommend">
      <div class="recommendimg">
        <img src="@/assets/z-img/recommend.png" alt>
      </div>
    </div>
    <div class="recommend_body">
      <z-chair></z-chair>
    </div>
  </div>
</template>

<script>
import zStatus from "@/components/z-status.vue";
import zChair from "@/components/z-chair.vue";
import Crumbs from "@/components/crumbs.vue";
export default {
  data() {
    return {
      status: "4"
    };
  },
  components: {
    zStatus,
    zChair,
    Crumbs
  },
  methods: {
    push1() {
      //  this.$router.push()
    },
    push2() {
      //  this.$router.push()
    }
  }
};
</script>

<style>
.successview {
  width: 1200px;
  margin: 0 auto;
}
.successview .successimg {
  width: 901px;
  margin: auto;
  position: relative;
  padding-top: 96px;
}
.successview .successimg img {
  width: 100%;
}
.successview .successimg .number {
  font-family: Cabin-Bold;
  font-size: 30px;
  color: #000000;
  position: absolute;
  left: 346px;
  bottom: 50px;
}
.successview .successview-buttom {
  width: 901px;
  margin: 0 auto;
  height: 44px;
  margin-top: 71px;
}
.successview .successview-buttom .btn {
  height: 100%;
  width: 125px;
  background-color: #b2b2b2;
  opacity: 0.7;
  color: #fff;
  line-height: 50px;
  text-align: center;
  float: left;
  margin-left: 276px;
}
.successview .successview-buttom .more1 {
  background-color: #000000;
  opacity: 0.6;
  margin-left: 134px;
}
.successview .recommend {
  margin-top: 60px;
}
.successview .recommendimg {
  width: 210px;
}
.successview .recommendimg img {
  width: 100%;
}
.successview .recommend_body {
  width: 100%;
  height: 400px;
  margin-top: 20px;
}
</style>
