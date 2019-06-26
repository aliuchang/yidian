<template>
  <div class="y_detail" id="y_detail">
    <!--面包屑-->
    <crumbs></crumbs>
    <!-- 商品购买信息 -->
    <div class="y_info">
      <div class="y_info_img">
        <img
          :src="ImgUrl"
          alt
          :class="{'active':isChoose}"
        >
        <!-- <pic-zoom :previewImg="ImgUrl" :zoomImg="bigImg" :src="ImgUrl"></pic-zoom> -->
        <div class="y_info_small_img" >
          <div class="y_info_small_img_item" v-for="img in imgUrl">
            <div @click="getIndex(img.url)">
                <img :src="img.url">
            </div>
          </div>
        </div>
      </div>

      <div class="y_info_desc">
        <el-form :model="detailForm">
          <h3>{{detailForm.title}}</h3>
          <p class="y_info_desc_p1">{{detailForm.title_en}}</p>
          <div class="y_info_border"></div>
          <p class="y_info_desc_p2">{{detailForm.desc}}</p>
          <p class="y_info_desc_p3 y_price">
            <span>{{detailForm.price}}</span>
            <span>RMB</span>
          </p>
          <div class="y_info_color_select">
            <span>颜色分类</span>
            <template v-for="(value,index) in span_object">
                <span class="y_color_item1"
                      :key="value.color"
                      :style="{'background':value.color}" 
                      @click="setChecked($event,index)"
                      >
                    <i :class="value.ls"></i>                  
                </span>
            </template>
          </div>
          <div class="y_info_num">
            <span class="y_num_span_01">数量</span>
            <el-input-number v-model="num" @change="handleChange" :min="1" :max="10" size="mini"></el-input-number>
            <span class="y_num_span_02">库存31件</span>
          </div>
          <el-form-item>
            <el-button class="y_info_button" @click="buy_btn">立即购买</el-button>
            <el-button @click="addCar_btn">加入购物车</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>

    <div class="y_desc">
      <div class="y_desc_img_title">
        <img src="@/assets/y_detail_img/y_detail_06.png" alt>
      </div>      
      <div class="y_desc_img" v-for="img in y_detail_content_img">
            <img :src="img.url">
      </div>
      <div class="y_desc_img_title" style="margin-bottom: 0;">
        <img src="@/assets/y_detail_img/y_detail_07.png" alt>
      </div>
    </div>
    <commond/>
  </div>
</template>

<script>
import commond from '@/components/z-chair.vue'
import crumbs from '@/components/crumbs.vue'
// import picZoom from '../../components/y-pic-zoom'
export default {
  data() {
    return {
      // 商品详情图片
      y_detail_content_img:[
        {index:1,url:require('@/assets/y_detail_img/y_detail_content_01.png')},
        {index:1,url:require('@/assets/y_detail_img/y_detail_content_02.png')},
        {index:1,url:require('@/assets/y_detail_img/y_detail_content_03.png')},
        {index:1,url:require('@/assets/y_detail_img/y_detail_content_04.png')},
        {index:1,url:require('@/assets/y_detail_img/y_detail_content_05.png')},
      ],
      // 缩略图
      imgUrl:[
        {index:1,url:require('@/assets/y_detail_img/y_detail_01.jpg')},
        {index:1,url:require('@/assets/y_detail_img/y_detail_02.jpg')},
        {index:1,url:require('@/assets/y_detail_img/y_detail_03.jpg')},
        {index:1,url:require('@/assets/y_detail_img/y_detail_04.jpg')},
        ],
      ImgUrl:require('@/assets/y_detail_img/y_detail_01.jpg'),
      // 颜色
      span_object:[
        {color:'#ffca57','ls': 'el-icon-check unshow'},
        {color:'#e9c7ab','ls': 'el-icon-check unshow'},
        {color:'#caca74','ls': 'el-icon-check unshow'},
        {color:'#cacf94','ls': 'el-icon-check unshow'}
      ],
      detailForm: {
        title: "·北欧旅程·现代简约椅",
        title_en: "Nordic journey modern Minimalist lounge chair",
        desc:
          "沙发木框线条柔美，全木质的结构，细节经手工打磨，扶手对接处使用烟袋衔接，过渡顺滑，手感细腻，扶手，靠背边缘的屋檐设计更显秀气禅意之美",
        price: "999.00"
      },
      isChoose: false,
      num: 1,
      isshow: true,
    };
  },
  components:{
    commond,
    crumbs,
    // picZoom
  },
  methods: {
    getIndex(imgUrl){
        this.ImgUrl = imgUrl;
    },
    setChecked(e, num) {
        console.log(e,num)
        let arr= this.span_object[num]['ls'].split(" ");
        if (arr[1] == "unshow") {

          arr[1] = "show";
        } else if(arr[1] == "show") {
          arr[1] = "unshow";
        }
      this.span_object[num]['ls'] = arr[0] + " " + arr[1];
    },

    buy_btn() {
      this.$router.push({name:'shop'})
    },
    addCar_btn() {
      this.$router.push({name:'shop'})
    },
    imgScc: function() {
      this.isChoose = !this.isChoose;
    },
    handleChange(value) {
      console.log(value);
    }
  },
};
</script>

<style>
body {
  overflow-x: hidden;
}
#y_detail{
  text-align: left;
}
#y_detail .unshow {
  display: none;
}
#y_detail .show {
  display: inline-block;
}
#y_detail {
  width: 1200px;
  margin: 0 auto;
}
#y_detail .y_info {
  width: 100%;
  height: 600px;
  position: relative;
}
#y_detail .y_info_img {
  width: 500px;
  height: 460px;
  position: absolute;
  left: 0;
  top: 0;
}
#y_detail .y_info_img img {
  display: block;
  width: 80%;
  height: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  transform: scale(1); /*图片原始大小1倍*/
  transition: all ease 0.5s; /*图片放大所用时间*/
}
#y_detail img.active {
  transform: scale(1.3); /*图片需要放大3倍*/
  position: absolute; /*是相对于前面的容器定位的，此处要放大的图片，不能使用position：relative；以及float，否则会导致z-index无效*/
  z-index: 100;
}
#y_detail img.active2 {
  transform: scale(1.3);
  position: absolute;
  z-index: 100;
}
#y_detail .y_info_desc {
  width: 600px;
  height: 100%;
  position: absolute;
  top: 0;
  right: 0;
  padding-top: 50px;
  box-sizing: border-box;
}
#y_detail .y_info_desc .el-form-item {
  margin: 0;
  padding: 0;
}
#y_detail .y_info_desc h3 {
  font-size: 24px;
  margin-bottom: 10px;
}
#y_detail .y_info_desc_p1 {
  margin-bottom: 10px;
}
#y_detail .y_info_border {
  width: 40px;
  height: 8px;
  margin: 20px 0;
  border-radius: 10px;
  background: #ffca57;
}
#y_detail .y_info_desc_p2 {
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  width: 80%;
  font-weight: 300;
  font-size: 14px;
  margin: 20px 0;
}
#y_detail .y_info_desc_p3 {
  font-size: 24px;
  font-weight: 600;
  margin: 20px 0;
}
#y_detail .y_info_desc_p3 span:nth-child(2) {
  margin-left: 10px;
  font-size: 12px;
  font-weight: 400;
}
#y_detail .y_info_color_select {
  height: 50px;
  line-height: 50px;
  margin: 10px 0;
  font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
#y_detail .y_color_item1 {
  display: inline-block;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #ffca57;
  vertical-align: middle;
  margin-left: 20px;
  line-height: 40px;
  text-align: center;
  color: #fff;
}
/*增加按钮*/
#y_detail .y_info_num {
  width: 100%;
  font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
#y_detail .y_info_num .y_num_span_01 {
  font-size: 16px;
  letter-spacing: 30px;
}
#y_detail .y_info_num .y_num_span_02 {
  font-size: 14px;
  color: #727272;
}

#y_detail .y_info_desc .el-button {
  color: black;
  font-size: 18px;
  letter-spacing: 3px;
  width: 200px;
  border-radius: 0px;
  margin: 20px 10px 20px 0;
  border: 1px solid #b2b2b2;
}

/**/
#y_detail .y_info_small_img {
  width: 400px;
  height: 100px;
  position: absolute;
  bottom: -100px;
  left: 0;right:0;
  margin: auto;

}
#y_detail .y_info_small_img_item {
  display: inline-block;
  width: 60px;
  height: 60px;
  margin-right: 10px;
  position: relative;
}
#y_detail .y_info_small_img_item img {
  width: 100%;
  left: 0;
}
#y_detail .y_desc_img {
  width: 94%;
  margin: 0 auto;
}
#y_detail .y_desc_img_title {
  width: 50%;
  margin: 50px auto;
}
#y_detail .y_desc_img img,.y_desc_img_title img {
  width: 100%;
  margin-bottom: 50px;
}

#y_detail .el-input-number--mini {
  margin-right: 20px;
  position: relative;
}
#y_detail .el-input-number__decrease,.el-input-number__increase {
  width: 20px !important;
  height: 20px !important;
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto 0;
  line-height: 20px;
  border-radius: 50%;
}
#y_detail .el-input__inner {
  display: inline-block;
  width: 50%;
  padding: 0 !important;
  margin-left: 32px;
  border-radius: 20px;
}
#y_detail .el-button:focus,.el-button:hover {
  background: #5ed5e0;
  color: #fff;
}
</style>
