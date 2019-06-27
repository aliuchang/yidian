<template>
  <div class="zheader">
    <div class="header_body">
      <div class="body_right">
        <el-row>
          <!-- -->
          <el-col :span="8">
            <router-link to="/list"  class="header-a">
              <!-- <img src="@/assets/z-img/z-find.png" @click="list"> -->
              <i class="iconfont icon-sousuo"></i>
            </router-link>
          </el-col>

          <el-col :span="8">
            <router-link to="/shop" class="header-a">
              <!-- <img src="@/assets/z-img/z-shop.png" @click="goshop"> -->
              <i class="iconfont icon-gouwudai"></i>
            </router-link>
          </el-col>
          <el-col :span="8">
            <!-- <img src="@/assets/z-img/z-my.png" @click="my"> -->
            <router-link to="/personal"  class="header-a">
              <i class="iconfont icon-gerenzhongxin"></i>
            </router-link>
          </el-col>
          <el-col :span="8">
            <router-link to="/login"  class="header-a">
              <!-- <img src="@/assets/z-img/z-shouchang.png" @click="shoucang"> -->
              <i class="iconfont icon-wujiaoxing"></i>
            </router-link>
          </el-col>
        </el-row>
      </div>
      <div class="button_body">
        <div class="body_world">
          <span  v-show="shows">请您</span>
          <span v-show="!shows">欢迎</span>
        </div>
        <div class="body_si" v-show="shows">
          <router-link to="/login" class="left">登录</router-link>
          <router-link to="/register" class="right">注册</router-link>
        </div>
        <div v-show="!shows">
          {{name}}
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data(){
    return{
      shows:true,
      name:''
    }
  },
  methods: {
    list() {
      this.$router.push({ name: "list" });
    },
    goshop() {
      this.$router.push("shop");
    },
    my() {
      this.$router.push({ name: "personal" });
    },
    shoucang() {
      console.log(this.$route);
    }
  },
  mounted() {
    let item = sessionStorage.getItem('name')
    console.log(item)
    this.name = item
    if(item){
        this.shows=false
    }else {
      this.shows=true
    }
  }
};
</script>
<style>

.zheader {
  width: 100%;
  height: 62px;
  background-color: #f3f3f3;
}
.zheader .header_body {
  width: 1200px;
  height: 100%;
  margin: 0 auto;
}
.zheader .body_right {
  float: right;
  height: 100%;
}
.zheader .el-row {
  display: flex;
  justify-content: space-around;
  height: 100%;
  width: 244px;
  float: right;
  align-items: center;
}
.zheader .el-row .el-col-8 img {
  width: 24px;
  height: 24px;
}
.zheader .header-a i{
 text-decoration:none; 
  outline: none;
  font-size: 24px;
  color: #000;
}
.zheader .body_si {
  width: 124px;
  height: 30px;
  border-radius: 15px;
  border: solid 1px rgba(0, 0, 0, 0.3);
  line-height: 30px;
  float: right;
  font-size: 16px;
  font-weight: 800;
}
.zheader .body_si .left {
  padding-right: 10px;
  border-right: 1px solid #000;
}
.zheader .body_si .right {
  padding-left: 10px;
}
.zheader .body_si a {
  color: #000;
  opacity: 0.9;
}
.zheader .body_world {
  float: right;
  font-size: 16px;
  color: #000000;
  opacity: 0.6;
}
.zheader .button_body {
  width: 205px;
  display: flex;
  justify-content: space-around;
  height: 100%;
  float: right;
  align-items: center;
}
</style>
