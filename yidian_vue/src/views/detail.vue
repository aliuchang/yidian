<template>
  <div class="box">111111111111111111111111
    <!-- 轮播图开始 -->
    <div class="banner">
      <el-carousel :interval="4000" arrow="always">
        <el-carousel-item>
          <img src="../assets/j-lunbo1.png" alt>
        </el-carousel-item>
        <el-carousel-item>
          <img src="../assets/j-lunbo2.png" alt>
        </el-carousel-item>
        <el-carousel-item>
          <img src="../assets/j-lunbo3.png" alt>
        </el-carousel-item>
        <el-carousel-item>
          <img src="../assets/j-lunbo4.png" alt>
        </el-carousel-item>
      </el-carousel>
    </div>
    <!-- 轮播图结束 -->
    <!-- 面包屑开始 -->
    <Crumbs></Crumbs>
    <!-- <router-view></router-view> -->
    <!-- 面包屑结束 -->
  </div>
</template>

<script>
import Crumbs from "@/components/crumbs.vue";
export default {
  data() {
    return {};
  },
  components: {
    Crumbs
  }
};
</script>

<style>
.box {
  width: 100%;
}
</style>

