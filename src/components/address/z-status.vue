<template>
  <div class="z-status">
    <div class="dingwei">
      <div class="li one">
        <div class="li_body">
          <span>查看购物车</span>
          <div :class="add1()"></div>
          <img src="@/assets/w-img/status.png" :class="dispay1()" alt>
          <div :class="solid1()"></div>
        </div>
      </div>
      <div class="li two absolute">
        <span>填写订单信息</span>
        <div :class="add2()"></div>
        <img src="@/assets/w-img/status.png" :class="dispay2()" alt>
        <div :class="solid2()"></div>
      </div>
      <div class="li three absolute">
        <span>选择支付方式</span>
        <div :class="add3()"></div>
        <img src="@/assets/w-img/status.png" :class="dispay3()" alt>
        <!-- <div class="solid"></div> -->
        
      </div>
      <div class="li four absolute">
        <span>选择支付方式</span>
        <div :class="add4()"></div>
        <img src="@/assets/w-img/status.png" :class="dispay4()"  alt>
        <div :class="solid3()"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

  props:{
      statuss:String,
      required: true
  },
  created(){
      console.log(this.statuss)
  },
  methods: {
    dispay1() {
      if (this.statuss == "1") {
        return "show";
      } else {
        return "unshow";
      }
    },
    add1() {
      if (this.statuss == "1") {
        return "yuan color";
      } else {
        return "yuan";
      }
    },
    solid1() {
      if (this.statuss == "1") {
        return "solid color";
      } else {
        return "solid";
      }
    },
    dispay2() {
      if (this.statuss == "2") {
        return "show";
      } else {
        return "unshow";
      }
    },
    add2() {
      if (this.statuss == "2") {
        return "yuan color";
      } else {
        return "yuan";
      }
    },
    solid2() {
      if (this.statuss == "2") {
        return "solid color";
      } else {
        return "solid";
      }
    },
    dispay3() {
      if (this.statuss == "3") {
        return "show";
      } else {
        return "unshow";
      }
    },
    add3() {
      if (this.statuss == "3") {
        return "yuan color";
      } else {
        return "yuan";
      }
    },
    solid3() {
      if (this.statuss == "3" | this.statuss == "4" ) {
        return "solid color";
      } else {
        return "solid";
      }
    },
    dispay4() {
      if (this.statuss == "4") {
        return "show";
      } else {
        return "unshow";
      }
    },
    add4() {
      if (this.statuss == "4") {
        return "yuan color";
      } else {
        return "yuan";
      }
    },
  }
};
</script>

<style>
.z-status {
  margin: 0 auto;
  width: 1200px;
  height: 83px;
  background: #f3f3f3;
}
.z-status .dingwei {
  width: 100%;
  height: 100%;
  position: relative;
}
.z-status .li {
  width: 25%;
  height: 100%;
  position: absolute;
}
.z-status .li_body {
  width: 100%;
  height: 100%;
  position: relative;
}
.z-status .two {
  left: 300px;
}
.z-status .three {
  left: 600px;
}
.z-status .four {
  left: 900px;
}
.z-status .li span {
  font-family: zcoolwenyiti;
  font-size: 20px;
  color: #000000;
  opacity: 0.9;
  position: absolute;
  left: 100px;
  top: 23px;
  z-index: 3;
}
.z-status .yuan {
  width: 10px;
  height: 10px;
  background-color: #000000;
  opacity: 0.1;
  border-radius: 50%;
  position: absolute;
  left: 145px;
  top: 54px;
}
.z-status .color {
  opacity: 1 !important;
  background: #4cc0cb !important;
}
.z-status img {
  position: absolute;
  left: 180px;
  top: 15px;
  display: none;
}
.z-status .unshow {
  display: none !important;
}
.z-status .show {
  display: block !important;
}
.z-status .absolute img{
  position: absolute;
  left: 200px;
  top: 15px;
}
.z-status .solid {
  width: 290px;
  height: 1px;
  background-color: #000000;
  opacity: 0.1;
  position: absolute;
  left: 155px;
  top: 59px;
}
.z-status .four .solid {
  left: -145px;
}
</style>
