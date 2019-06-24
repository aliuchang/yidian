<template>
  <div class="zheader">
    <div class="header_body">
      <div class="body_right">
          <el-row>
            <el-col :span="8" >
              <img src="@/assets/z-img/z-find.png" @click="list">
            </el-col>
            <el-col :span="8">
              <img src="@/assets/z-img/z-shop.png" @click="goshop">
            </el-col>
            <el-col :span="8">
              <img src="@/assets/z-img/z-my.png" @click="my">
            </el-col>
            <el-col :span="8">
              <img src="@/assets/z-img/z-shouchang.png" @click="shoucang">
            </el-col>
          </el-row>
        </div>
        <div class="button_body">
          <div class="body_world">
            <span>请您</span>
          </div>
          <div class="body_si">
            <router-link to="/login" class="left">登录</router-link>
            <router-link to="/register" class="right">注册</router-link>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
export default {
  methods:{
    list(){
      this.$router.push({name:'list'})
    },
    goshop(){
      this.$router.push('shop')
    },
    my(){
      this.$router.push({name:'personal'})
    },
    shoucang(){
      console.log(this.$route)
    }
  }
}
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
.zheader .el-row .el-col-8 img{
  width: 24px;
  height: 24px;
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
