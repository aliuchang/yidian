<template>
  <div class="n-tab">
    <template v-for="i in tabs">
      <div class="tab" :key="i.title">
        <img :src="i.image">
        <div class="tabname">
          <span></span>
          <p>{{i.title}}</p>
          <span></span>
        </div>
        <div class="tabename">{{i.etitle}}</div>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tabs: [
        {
          image: require("../../assets/img/wait.png"),
          title: "待发货",
          etitle: "WAITING FOR SHIPMENT",
        },
        {
          image: require("../../assets/img/car.png"),
          title: "运输中",
          etitle: "IS BEING TRANSPORTED"
        },
        {
          image: require("../../assets/img/end.png"),
          title: "已完成",
          etitle: "IS BEING END"
        }
      ]
    };
  }
};
</script>

<style>
.n-tab{
    display: flex;
}
.n-tab .tab{
  width: 170px;
  height: 76px;
  padding: 20px 0;
  margin: 18px 50px 18px 0;
  border: 2px solid #e5e5e5;
  background: #fff;
}
.n-tab .tab .tabname{
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  color: #7b7b7b;
  line-height: 40px;
}
.n-tab .tab .tabname span{
  display: inline-block;
  width: 2px;
  height: 10px;
  background: #7f7f7f;
  margin: 0 10px;
}
.n-tab .tab .tabename{
  font-size: 10px;
  color: #9f9f9f;
}
</style>
