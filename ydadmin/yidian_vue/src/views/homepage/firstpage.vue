<template>
  <el-main class="firstpage">
    <!-- 轮播图 -->
    <div class="box">
      <el-carousel :height="'600'+'px'">
        <el-carousel-item v-for="item in imagesbox" :key="item.id">
          <h3>{{ item.number }}</h3>
          <img :src="item.idView" class="image" @click="bannerbuy">
        </el-carousel-item>
      </el-carousel>
    </div>
    <!-- 新品首发 -->
    <div class="first-img">
      <img src="@/assets/index/first-img.png" alt>
    </div>
    <!-- 亨利克 -->
    <div class="h-box">
      <div class="h-left">
        <img src="@/assets/index/h1.png" alt>
      </div>
      <div class="h-right" :v-model="chairdata">
        <h1>NEW PRODL</h1>
        <h3>{{chairdata.brand}}</h3>
        <div class="heng"></div>
        <h4>{{chairdata.name}}</h4>
        <p>{{chairdata.info}}</p>
        <div class="h-money">
          RMB
          <strong>{{chairdata.money}}</strong>
        </div>
        <div class="h-buy" @click="hbuy">Buy</div>
      </div>
    </div>
    <!-- 波昂 -->
    <div class="h-box">
      <div class="h-right2">
        <h1>PRODUCTS</h1>
        <h4>沙发套可拆洗</h4>
        <h4>沙发套可选</h4>
        <p>这是一款非常棒的椅子。采用曲木设计，结</p>
        <p>实耐用，十分灵活，都贴合人体曲线，打造理想舒适感</p>
        <div class="h-money2">
          RMB
          <strong>999.00</strong>
        </div>
        <div class="h-buy2" @click="bbuy">Buy</div>
      </div>
      <div class="h-left2">
        <img src="@/assets/index/h2.png" alt>
      </div>
    </div>
    <!-- 人气推荐 -->
    <div class="first-img">
      <img src="@/assets/index/two-img.png" alt>
    </div>
    <div class="per-box1">
      <img src="@/assets/index/renqi1.png" alt>
      <div class="per-name1">脚蹬，芬斯塔 天蓝色</div>
      <div class="per-name2">落地灯/阅读灯，镀镍</div>
      <div class="per-price1">349.00</div>
      <div class="per-price2">299.00</div>
      <div class="per-buy1" @click="perbuy1">Buy</div>
      <div class="per-buy2" @click="perbuy2">Buy</div>
    </div>
    <div class="per-box2">
      <img src="@/assets/index/renqi2.png" alt>
      <div class="per-name01">靠背椅, 尤帕 深绿色</div>
      <div class="per-name02">
        这款高靠背座椅为颈部提供额外支撑，给你带来真正
        放松的舒适体验，表面柔软，紧致厚实，具有反光效果。
      </div>
      <div class="per-price01">499.00</div>
      <div class="per-buy01" @click="perbuy1">Buy</div>
    </div>
    <!-- 今日特价 -->
    <div class="first-img">
      <img src="@/assets/index/five-img.png" alt>
    </div>
    <div class="day-box">
      <el-carousel :height="'373'+'px'" indicator-position="outside">
        <el-carousel-item v-for="item in dayimg">
          <div class="today-box" v-for="v in item" :key="v.id">
            <img :src="v.idView" class="image" @click="bannerbuy">
            <h3>{{ v.number }}</h3>
            <h4>{{ v.name }}</h4>
            <h5>{{ v.eng }}</h5>
            <div class="day-buy-box">
              <div class="daybuy-left">
                RMB
                <strong>{{ v.money }}</strong>
              </div>
              <div class="daybuy-right" @click="perbuy2">Buy</div>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="shopping-box">
      <img src="@/assets/index/抢购1.png" alt>
      <div class="time-box">
        <span
          v-if="Date.parse(new Date(deadline)) <= Date.parse(new Date()) && Date.parse(new Date()) < Date.parse(new Date(start))"
        >待开始</span>
        <span v-else-if="Date.parse(new Date())===Date.parse(new Date(start))">已开始</span>
        <span v-else>
          {{day}}
          <span>天</span>
          {{hr}}
          <span>时</span>
          {{min}}
          <span>分</span>
          {{sec}}
          <span>秒</span>
        </span>
      </div>
      <div class="shopping" @click="perbuy1">立即抢购</div>
    </div>
    <!-- 关于我们 -->
    <div class="first-img">
      <img src="@/assets/index/three-img.png" alt>
    </div>
    <div class="about-box">
      <p>
        家具是指人类维持正常生活是，必不可少的器具设施大类。家具也跟随
        <br>时代的脚步不断发展创新，到如今门类繁多，用料各异，品种齐全，用途不一。是建立工作生活空间的重要基础。
      </p>
      <p>
        Furniture refers to human beings to maintain normal life, engage in production practice and
        <br>carry outsocial activities Essential appliance facilities inarge categories.Furniture also follows the footsteps of the Times to continue to develop and innovate,
        <br>to today a wide range of materials Different, variety complete, different uses. .
      </p>
    </div>
    <div class="more">MORE</div>
  </el-main>
</template>

<script>
export default {
  props: ["deadline", "start"],
  name: "dateComponent",
  data() {
    return {
      day: 0,
      hr: 0,
      min: 0,
      sec: 0,
      chairdata: {
        brand: "HENRIKSDAL 亨利克",
        name: "椅子、桦木、格雷伯 白色",
        info:
          "愉快地享用完漫长的餐点后，如果桌布椅套可以清洗，那可真是美事一桩。HENRIKSDAL 亨利克 可能是我们最舒适的椅子了！",
        money: "459.00"
      },
      imagesbox: [
        { id: 0, idView: require("@/assets/index/banner1.png"), number: "01" },
        { id: 1, idView: require("@/assets/index/banner1.png"), number: "02" },
        { id: 2, idView: require("@/assets/index/banner1.png"), number: "03" },
        { id: 3, idView: require("@/assets/index/banner1.png"), number: "04" }
      ],
      dayimg: [
        [
          {
            id: 0,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "维哈默",
            eng: "Vikhammer",
            money: "99.00"
          },
          {
            id: 1,
            idView: require("@/assets/index/day02.png"),
            number: "PS MASKROS",
            name: "奥思迪",
            eng: "HYQuHeiW",
            money: "99.00"
          },
          {
            id: 2,
            idView: require("@/assets/index/day03.png"),
            number: "HAMMARN",
            name: "马克鲁斯",
            eng: "Ps maskros",
            money: "99.00"
          },
          {
            id: 3,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "哈马恩",
            eng: "Hammarn",
            money: "99.00"
          }
        ],
        [
          {
            id: 0,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "维哈默",
            eng: "Vikhammer",
            money: "99.00"
          },
          {
            id: 1,
            idView: require("@/assets/index/day02.png"),
            number: "PS MASKROS",
            name: "奥思迪",
            eng: "HYQuHeiW",
            money: "99.00"
          },
          {
            id: 2,
            idView: require("@/assets/index/day03.png"),
            number: "HAMMARN",
            name: "马克鲁斯",
            eng: "Ps maskros",
            money: "99.00"
          },
          {
            id: 3,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "哈马恩",
            eng: "Hammarn",
            money: "99.00"
          }
        ],
        [
          {
            id: 0,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "维哈默",
            eng: "Vikhammer",
            money: "99.00"
          },
          {
            id: 1,
            idView: require("@/assets/index/day02.png"),
            number: "PS MASKROS",
            name: "奥思迪",
            eng: "HYQuHeiW",
            money: "99.00"
          },
          {
            id: 2,
            idView: require("@/assets/index/day03.png"),
            number: "HAMMARN",
            name: "马克鲁斯",
            eng: "Ps maskros",
            money: "99.00"
          },
          {
            id: 3,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "哈马恩",
            eng: "Hammarn",
            money: "99.00"
          }
        ],
        [
          {
            id: 0,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "维哈默",
            eng: "Vikhammer",
            money: "99.00"
          },
          {
            id: 1,
            idView: require("@/assets/index/day02.png"),
            number: "PS MASKROS",
            name: "奥思迪",
            eng: "HYQuHeiW",
            money: "99.00"
          },
          {
            id: 2,
            idView: require("@/assets/index/day03.png"),
            number: "HAMMARN",
            name: "马克鲁斯",
            eng: "Ps maskros",
            money: "99.00"
          },
          {
            id: 3,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "哈马恩",
            eng: "Hammarn",
            money: "99.00"
          }
        ],
        [
          {
            id: 0,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "维哈默",
            eng: "Vikhammer",
            money: "99.00"
          },
          {
            id: 1,
            idView: require("@/assets/index/day02.png"),
            number: "PS MASKROS",
            name: "奥思迪",
            eng: "HYQuHeiW",
            money: "99.00"
          },
          {
            id: 2,
            idView: require("@/assets/index/day03.png"),
            number: "HAMMARN",
            name: "马克鲁斯",
            eng: "Ps maskros",
            money: "99.00"
          },
          {
            id: 3,
            idView: require("@/assets/index/day01.png"),
            number: "ÅRSTID",
            name: "哈马恩",
            eng: "Hammarn",
            money: "99.00"
          }
        ]
      ]
    };
  },
  mounted: function() {
    this._interval = setInterval(() => {
      this.countdown();
    }, 1000);
  },
  destroyed() {
    clearInterval(this._interval);
  },
  methods: {
    bannerbuy() {
      this.$router.push({ name: "detail" });
    },
    hbuy() {
      this.$router.push({ name: "detail" });
    },
    bbuy() {
      this.$router.push({ name: "detail" });
    },
    perbuy1() {
      this.$router.push({ name: "detail" });
    },
    perbuy2() {
      this.$router.push({ name: "detail" });
    },
    countdown: function() {
      const end = Date.parse(new Date("2019-8-01"));
      const now = Date.parse(new Date());
      const msec = end - now;
      let day = parseInt(msec / 1000 / 60 / 60 / 24);
      let hr = parseInt((msec / 1000 / 60 / 60) % 24);
      let min = parseInt((msec / 1000 / 60) % 60);
      let sec = parseInt((msec / 1000) % 60);
      this.day = day;
      this.hr = hr > 9 ? hr : "0" + hr;
      this.min = min > 9 ? min : "0" + min;
      this.sec = sec > 9 ? sec : "0" + sec;
    }
  }
};
</script>

<style>
/* 轮播图 */
.firstpage .box {
  width: 1200px;
  height: 600px;
  margin: auto;
  position: relative;
  cursor: pointer;
}
.firstpage .el-carousel__item h3 {
  color: #475669;
  font-size: 48px;
  opacity: 0.75;
  position: absolute;
  right: 80px;
  bottom: 100px;
}
.firstpage .el-carousel__item img {
  position: absolute;
  left: 0;
  top: 0;
}
/* 轮播图二 */
.firstpage .day-box {
  width: 1200px;
  height: 400px;
  margin: auto;
}
.firstpage .day-box .el-carousel .el-carousel__container {
  background: #fff;
}
.firstpage .today-box {
  width: 215px;
  height: 100%;
  margin: 0 42px;
  float: left;
  position: relative;
}
.firstpage .today-box img {
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
}
.firstpage .today-box h3 {
  display: block;
  width: 100%;
  height: 50px;
  position: absolute;
  top: 170px;
  left: 18px;
  right: 0;
  bottom: 0;
  margin: auto;
  font-size: 18px;
  line-height: 51px;
  color: #000000;
  opacity: 0.9;
  text-align: center;
}
.firstpage .today-box h4 {
  display: block;
  width: 100%;
  height: 50px;
  position: absolute;
  top: 210px;
  left: 18px;
  right: 0;
  bottom: 0;
  margin: auto;
  font-size: 18px;
  line-height: 51px;
  color: #000000;
  opacity: 0.7;
  text-align: center;
}
.firstpage .today-box h5 {
  display: block;
  width: 100%;
  height: 50px;
  position: absolute;
  top: 250px;
  left: 18px;
  right: 0;
  bottom: 0;
  margin: auto;
  font-size: 12px;
  line-height: 51px;
  color: #000000;
  opacity: 0.5;
  text-align: center;
}
.firstpage day-buy-box {
  width: 187px;
  height: 33px;
  position: absolute;
  right: 0;
  bottom: -5px;
}
.firstpage .daybuy-left {
  float: left;
  font-size: 10px;
  color: #000000;
  opacity: 0.8;
}
.firstpage .daybuy-left strong {
  font-size: 18px;
  color: #000000;
  opacity: 0.9;
}
.firstpage .daybuy-right {
  width: 50px;
  height: 22px;
  border: 1px solid black;
  color: rgb(0, 0, 0);
  font-size: 12px;
  line-height: 22px;
  text-align: center;
  cursor: pointer;
  float: right;
}
.firstpage .el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}
/* 中间图 */
.firstpage .first-img {
  width: 340px;
  height: 117px;
  margin: 149px auto 58px;
  position: relative;
}
.firstpage .first-img img {
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
}
/* 亨利克第一个 */
.firstpage .h-box {
  width: 1200px;
  height: 547px;
  margin: auto;
  margin-bottom: 110px;
  overflow: hidden;
}
.firstpage .h-left {
  width: 680px;
  height: 100%;
  float: left;
}
.firstpage .h-right {
  width: 510px;
  height: 100%;
  background: #fff;
  margin-left: 10px;
  float: left;
  text-align: left;
}
.firstpage .h-right h1 {
  line-height: 50px;
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
  font-size: 80px;
  text-align: left;
  color: rgb(0, 0, 0);
  opacity: 0.06;
  margin-left: 47px;
  margin-bottom: 22px;
}
.firstpage .h-right h3 {
  font-size: 30px;
  line-height: 50px;
  color: rgb(0, 0, 0);
  margin-bottom: 13px;
  opacity: 0.9;
}
.firstpage .h-right .heng {
  width: 36px;
  height: 4px;
  background: rgb(255, 202, 87);
  border-radius: 2px;
  margin-bottom: 29px;
}
.firstpage .h-right h4 {
  font-size: 20px;
  line-height: 18px;
  color: rgb(0, 0, 0);
  opacity: 0.7;
  margin-bottom: 30px;
}
.firstpage .h-right p {
  font-size: 12px;
  line-height: 18px;
  color: rgb(0, 0, 0);
  opacity: 0.6;
}
.firstpage .h-money {
  margin-top: 50px;
  font-size: 12px;
  color: rgb(0, 0, 0);
  opacity: 0.8;
}
.firstpage .h-money strong {
  font-size: 24px;
  color: rgb(0, 0, 0);
  opacity: 0.9;
}
.firstpage .h-buy {
  margin-top: 15px;
  width: 50px;
  height: 22px;
  border: 1px solid black;
  color: rgb(0, 0, 0);
  font-size: 12px;
  line-height: 22px;
  text-align: center;
  cursor: pointer;
}
/* 第二个 */
.firstpage .h-left2 {
  width: 680px;
  height: 100%;
  float: left;
  margin-left: 50px;
}
.firstpage .h-right2 {
  width: 367px;
  height: 100%;
  background: #fff;
  margin-left: 10px;
  float: left;
}
.firstpage .h-right2 h1 {
  line-height: 50px;
  font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
  font-size: 80px;
  text-align: right;
  color: rgb(0, 0, 0);
  opacity: 0.06;
  margin-left: 47px;
  margin-bottom: 90px;
}
.firstpage .h-right2 h4 {
  font-weight: 400;
  font-size: 20px;
  line-height: 18px;
  color: rgb(0, 0, 0);
  opacity: 0.7;
  margin: 20px 0;
  text-align: right;
}
.firstpage .h-right2 p {
  font-size: 12px;
  line-height: 18px;
  color: rgb(0, 0, 0);
  opacity: 0.6;
  text-align: right;
}
.firstpage .h-money2 {
  margin-top: 50px;
  font-size: 12px;
  color: rgb(0, 0, 0);
  opacity: 0.8;
  text-align: right;
}
.firstpage .h-money2 strong {
  font-size: 24px;
  color: rgb(0, 0, 0);
  opacity: 0.9;
}
.firstpage .h-buy2 {
  margin-top: 15px;
  width: 50px;
  height: 22px;
  border: 1px solid black;
  color: rgb(0, 0, 0);
  font-size: 12px;
  line-height: 22px;
  text-align: center;
  cursor: pointer;
  float: right;
}
/* 人气推荐 第一个 */
.firstpage .per-box1 {
  width: 1200px;
  height: 432px;
  margin: auto;
  position: relative;
  margin-bottom: 92px;
}
.firstpage .per-box1 img {
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
}
.firstpage .per-name1 {
  font-size: 12px;
  line-height: 18px;
  color: #000000;
  opacity: 0.6;
  position: absolute;
  top: 210px;
  left: 140px;
}
.firstpage .per-name2 {
  font-size: 12px;
  line-height: 18px;
  color: #000000;
  opacity: 0.6;
  position: absolute;
  top: 280px;
  right: 280px;
}
.firstpage .per-price1 {
  font-size: 24px;
  color: rgb(0, 0, 0);
  opacity: 0.9;
  position: absolute;
  left: 170px;
  top: 240px;
}
.firstpage .per-price2 {
  font-size: 24px;
  color: rgb(0, 0, 0);
  opacity: 0.9;
  position: absolute;
  right: 280px;
  top: 315px;
}
.firstpage .per-buy1 {
  width: 50px;
  height: 22px;
  border: 1px solid black;
  color: rgb(0, 0, 0);
  font-size: 12px;
  line-height: 22px;
  text-align: center;
  position: absolute;
  left: 200px;
  top: 285px;
  cursor: pointer;
}
.firstpage .per-buy2 {
  width: 50px;
  height: 22px;
  border: 1px solid black;
  color: rgb(0, 0, 0);
  font-size: 12px;
  line-height: 22px;
  text-align: center;
  position: absolute;
  right: 340px;
  top: 360px;
  cursor: pointer;
}
/* 第二个 */
.firstpage .per-box2 {
  width: 1200px;
  height: 432px;
  margin: auto;
  position: relative;
}
.firstpage .per-box2 img {
  width: 100%;
  position: absolute;
  top: 0;
  left: 100px;
}
.firstpage .per-price01 {
  font-size: 24px;
  color: rgb(0, 0, 0);
  opacity: 0.9;
  position: absolute;
  left: 560px;
  top: 255px;
}
.firstpage .per-buy01 {
  width: 50px;
  height: 22px;
  border: 1px solid black;
  color: rgb(0, 0, 0);
  font-size: 12px;
  line-height: 22px;
  text-align: center;
  cursor: pointer;
  position: absolute;
  left: 527px;
  top: 300px;
}
.firstpage .per-name01 {
  font-size: 14px;
  font-weight: 600;
  color: #000000;
  opacity: 0.8;
  line-height: 18px;
  position: absolute;
  top: 180px;
  left: 525px;
}
.firstpage .per-name02 {
  width: 292px;
  height: 30px;
  position: absolute;
  left: 525px;
  top: 215px;
  font-size: 12px;
  color: #000000;
  opacity: 0.6;
  line-height: 18px;
}
.firstpage .shopping-box {
  width: 1200px;
  height: 500px;
  position: relative;
  margin: auto;
}
.firstpage .shopping-box img {
  position: absolute;
  left: 0;
  top: 0;
}
.firstpage .time-box {
  width: 350px;
  height: 50px;
  position: absolute;
  left: 150px;
  top: 250px;
}
.firstpage .time-box span {
  font-size: 30px;
  color: aqua;
}
.firstpage .time-box span span {
  font-size: 20px;
  color: #000000;
}
/* 今日特价 */
.firstpage .shopping {
  width: 181px;
  height: 43px;
  line-height: 43px;
  text-align: center;
  color: #ffffff;
  font-size: 20px;
  background: #53b0be;
  position: absolute;
  left: 159px;
  top: 390px;
  cursor: pointer;
}
/* 关于我们 */
.firstpage .about-box {
  width: 1200px;
  height: 150px;
  text-align: center;
  color: #000000;
  opacity: 0.7;
  font-size: 14px;
  margin: auto;
  overflow: hidden;
}
.firstpage .about-box p {
  margin-bottom: 29px;
}
.firstpage .more {
  width: 181px;
  height: 43px;
  line-height: 43px;
  text-align: center;
  font-size: 20px;
  color: #000000;
  opacity: 0.7;
  margin: auto;
  border: 1px solid #000000;
  margin-top: 30px;
}
</style>