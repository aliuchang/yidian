<template>
  <div class="zrouter">
    <div class="router-left">
      <router-link to="/firstpage">
        <img src="@/assets/z-img/logo.png">
      </router-link>
    </div>
    <div class="router-middle-link">
      <router-link to="/list" class="push">
        <div class="title">全部</div>
        <div class="english">
          <span>ALL</span>
          <div class="border"></div>
        </div>
      </router-link>
      <router-link to="/list" class="push">
        <div class="title">座椅</div>
        <div class="english">
          <span>Seat</span>
          <div class="border"></div>
        </div>
      </router-link>
      <router-link to="/list" class="push">
        <div class="title">床</div>
        <div class="english">
          <span>Seat bed</span>
          <div class="border"></div>
        </div>
      </router-link>
      <router-link to="/list" class="push">
        <div class="title">柜子</div>
        <div class="english">
          <span>Seat cabinets</span>
          <div class="border"></div>
        </div>
      </router-link>
      <router-link to="/list" class="push">
        <div class="title">边几</div>
        <div class="english">
          <span>Seat Edge Several</span>
          <div class="border"></div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goindex() {
      this.$router.push({ name: "homepage" });
    }
  }
};
</script>

<style>
.zrouter {
  width: 1200px;
  height: 98px;
  margin: 0 auto 20px;
}
.zrouter .router-left {
  width: 185px;
  height: 49px;
  float: left;
  margin-left: 24px;
  padding-top: 25px;
  margin-right: 130px;
}
.zrouter .router-left img {
  width: 100%;
}
.zrouter .router-middle-link {
  float: left;
  display: flex;
  align-items: center;
  height: 100%;
}
.zrouter .router-middle-link .push {
  width: 110px;
}
.zrouter .router-middle-link .push .title {
  font-size: 18px;
  color: rgba(0, 0, 0, 0.7);
  font-family: zcoolwenyiti;
}
.zrouter .router-middle-link .push .english {
  font-size: 12px;
  font-family: Cabin-Regular;
  color: #000000;
  opacity: 0.5;
}
.zrouter .router-middle-link .push .english .border {
  width: 20px;
  height: 2px;
  background: #fff;
  margin: 0 auto;
  margin-top: 6px;
}
.zrouter .router-middle-link .router-link-exact-active .english .border {
  background: #000;
}
.zrouter .router-middle-link .router-link-exact-active .title {
  font-weight: 600;
  color: rgba(0, 0, 0, 0.9);
}
</style>
