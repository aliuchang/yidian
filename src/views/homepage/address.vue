<template>
  <div class="w-add">
    <!-- 步骤条 -->
    <status statuss='2'></status>
    <!-- 配送地址 -->
    <div class="w-pei">
      <div class="w-head">
        <div class="w-little">
          <div class="image">
            <img src="@/assets/w-img/w1.png" alt>
          </div>
          <div class="w-box"></div>
          <div class="w-info">
            <p>配送地址</p>
            <p class="lp">Shipping Address</p>
          </div>
          <div class="w-photo">
            <img src="@/assets/w-img/01.png" alt>
          </div>
        </div>
      </div>
    </div>
    <div class="w-address">
      <div class="w-left">
        <div class="w-left-box">
          <div class="w-floor1">
            <div class="w-image1">
              <img src="@/assets/w-img/bian.jpg" alt>
            </div>
            <div class="w-image2">
              <img src="@/assets/w-img/shan.jpg" alt>
            </div>
          </div>
          <div class="w-floor2">
            <p>李思思</p>
          </div>
          <div class="w-floor3">
            <div class="w-floor3-1">
              <div class="w-floor3-1-img">
                <img src="@/assets/w-img/lian.jpg" alt>
              </div>
              <p>{{phone}}</p>
            </div>
            <div class="w-floor3-1">
              <div class="w-floor3-1-img">
                <img src="@/assets/w-img/di.jpg" alt>
              </div>
              <p>{{address}}</p>
            </div>
          </div>
          <div class="w-floor4">
            <div class="moren">默认</div>
          </div>
        </div>
      </div>
      <div class="w-right">
        <div class="w-right-box" @click="dialogFormVisible = true">
          <div class="w-right-box-image">
            <img src="@/assets/w-img/w2.png" alt>
          </div>
          <p>添加收货地址</p>
        </div>
      </div>
    </div>
    <!-- 商品信息 -->
    <div class="w-pei">
      <div class="w-head">
        <div class="w-little">
          <div class="image">
            <img src="@/assets/w-img/w1.png" alt>
          </div>
          <div class="w-box"></div>
          <div class="w-info">
            <p>商品信息</p>
            <p class="lp">Product Info</p>
          </div>
          <div class="w-photo">
            <img src="@/assets/w-img/02.png" alt>
          </div>
        </div>
      </div>
      <div class="bigbox">
        <div class="bigbox-1">
          <p>返回购物车修改 ></p>
        </div>
        <ul class="bigbox-2">
          <li class="bigbox-item">商品描述</li>
          <li class="bigbox-item">颜色</li>
          <li class="bigbox-item">尺码</li>
          <li class="bigbox-item">数量</li>
          <li class="bigbox-item">单价</li>
          <li class="bigbox-item">总价</li>
        </ul>
        <goods></goods>
        <div class="bott-1">
          <div class="bott-1-1">
            <span>3</span>个结果
          </div>
          <div class="bott-1-2">
            运费：
            <span>300.00</span> RMB
          </div>
          <div class="bott-1-3">
            应付总额：
            Total payable:
          </div>
          <div class="bott-1-4">
            <span>3146.00</span>RMB
          </div>
          <div class="jie">结 算</div>
        </div>
      </div>
    </div>
    <!-- 弹出的对话框 -->
    <el-dialog :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-input type="text" class="w-name" v-model="form.name"></el-input>
        <el-input type="text" class="w-tel" v-model="form.tel"></el-input>
        <el-select v-model="form.privince" placeholder="请选择" class="w-province">
          <el-option label="北京市" value="1"></el-option>
          <el-option label="上海市" value="2"></el-option>
          <el-option label="天津市" value="3"></el-option>
          <el-option label="河北省" value="4"></el-option>
          <el-option label="山西省" value="5"></el-option>
          <el-option label="湖南省" value="6"></el-option>
          <el-option label="河北省" value="7"></el-option>
          <el-option label="四川省" value="8"></el-option>
        </el-select>
        <el-input type="text" class="w-city" v-model="form.city"></el-input>
        <el-input type="text" class="w-area" v-model="form.area"></el-input>
        <el-input type="text" class="w-street" v-model="form.street"></el-input>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button class="button1" @click="dialogFormVisible = false">保 存</el-button>
        <el-button class="button2" @click="dialogFormVisible = false">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import goods from "@/components/address/goods.vue"
import status from "@/components/address/z-status.vue"

export default {
  data() {
    return {
      phone: "18435995678",
      address: "北京市  西城区  长安西街街道",
      dialogFormVisible: false,
      form: {
        name: "",
        tel: "",
        province: "",
        city: "",
        area: "",
        street: ""
      }
    }
  },
  methods: {},
  components: {
    goods,
    status
  }
}
</script>

<style>
#app .w-add .el-steps {
  background-color: #f3f3f3;
  border-radius: 5px;
  margin-top: 35px;
  width: 1200px;
  height: 84px;
  margin: 0 auto;
  position: relative;
}
.w-add .el-step__main {
  position: absolute;
  top: 10px;
  left: 35%;
}
.w-add .el-step__head {
  position: absolute;
  bottom: 10px;
  left: 0;
}
.w-add .el-step__title.is-finish {
  color: #333;
  font-size: 16px;
  font-weight: 700;
}
.w-add.el-step__title.is-wait {
  color: #333;
  font-size: 16px;
  font-weight: 700;
}
.w-add .w-pei {
  width: 1200px;
  margin: 0 auto;
}
.w-add .w-head {
  height: 126px;
  margin-top: 30px;
}
.w-add .w-little {
  width: 222px;
  height: 126px;
  position: relative;
}
.w-add .image {
  margin-top: 40px;
  margin-left: 5px;
  float: left;
}
.w-add .w-box {
  width: 2px;
  height: 20px;
  background-color: #cccccc;
  position: absolute;
  top: 45px;
  left: 36px;
}
.w-add .w-info {
  float: left;
  position: absolute;
  top: 17px;
  left: 53px;
  z-index: 2;
}
.w-add .w-info .lp {
  font-size: 10px;
  margin-top: 0;
  font-weight: 400;
}
.w-add .w-info p {
  margin-bottom: 8px;
  font-weight: 700;
}
.w-add .w-photo {
  float: left;
  position: relative;
  z-index: 1;
}
.w-add .w-photo img {
  position: absolute;
  left: 80px;
}
.w-add .w-address {
  width: 1200px;
  height: 190px;
  margin: 0 auto;
}
.w-add .w-left {
  float: left;
  width: 442px;
  height: 100%;
  border: 3px solid #b2b2b2;
}
.w-add .w-left-box {
  width: 423px;
  height: 173px;
  border: 4px dotted #cccccc;
  margin: 5px 5px;
}
.w-add .w-floor1 {
  height: 28px;
  position: relative;
}
.w-add .w-floor1 .w-image1 {
  position: absolute;
  top: 5px;
  right: 76px;
}
.w-add .w-floor1 .w-image2 {
  position: absolute;
  top: 5px;
  right: 14px;
}
.w-add .w-floor2 {
  height: 20px;
}
.w-add .w-floor2 p {
  padding-left: 20px;
  width: 60px;
  height: 20px;
  margin: 0;
  font-size: 18px;
  font-weight: 700;
}
.w-add .w-floor3 {
  height: 78px;
}
.w-add .w-floor3 .w-floor3-1 {
  height: 50%;
}
.w-add .w-floor3 .w-floor3-1 .w-floor3-1-img {
  float: left;
  padding-top: 10px;
  padding-left: 22px;
}
.w-add .w-floor3 .w-floor3-1 p {
  float: left;
  padding-top: 12px;
  padding-left: 10px;
  margin: 0;
}
.w-add .w-floor4 {
  height: 45px;
}
.w-add .w-floor4 .moren {
  float: right;
  margin-right: 15px;
  width: 60px;
  height: 32px;
  background-color: #838383;
  border-radius: 2px;
  text-align: center;
  line-height: 32px;
  color: #fff;
}
.w-add .w-right {
  margin-left: 76px;
  float: left;
  width: 203px;
  height: 190px;
  border: 3px solid #e5e5e5;
  position: relative;
}
.w-add .w-right-box {
  width: 120px;
  height: 120px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  text-align: center;
}
.w-add .w-right-box-image {
  width: 50px;
  height: 50px;
}
.w-add .w-right-box-image img {
  height: 100%;
  width: 100%;
  margin-left: 35px;
  margin-top: 20px;
}
.w-add .w-right-box p {
  color: #b3b3b3;
  padding-top: 20px;
}
.w-add .bigbox {
  width: 1200px;
  height: 1100px;
}
.w-add .bigbox-1 {
  width: 100%;
  height: 48px;
}
.w-add .bigbox-1 p {
  width: 162px;
  float: right;
}
.w-add .bigbox-2 {
  padding-left: 158px;
  list-style: none;
  height: 62px;
  text-align: center;
  border: 2px solid #e5e5e5;
}
.w-add .bigbox-item {
  padding-top: 23px;
  width: 173px;
  float: left;
}
.w-add .bott-1 {
  margin-top: 64px;
  position: relative;
}
.w-add .bott-1-1 {
  float: left;
  margin-left: 40px;
}
.w-add .bott-1-2 span {
  font-size: 32px;
  font-weight: 700;
}
.w-add .bott-1-3 {
  position: absolute;
  right: 190px;
  top: 0;
  width: 106px;
  height: 42px;
  font-size: 18px;
}
.w-add .bott-1-4 {
  position: absolute;
  right: 5px;
  top: 0;
  font-size: 18px;
}
.w-add .bott-1-4 span {
  font-size: 36px;
  color: #e72727;
  font-weight: 700;
}
.w-add .jie {
  width: 250px;
  height: 80px;
  background-color: #7d7d7d;
  text-align: center;
  color: #fff;
  font-size: 30px;
  line-height: 80px;
  float: right;
  margin-top: 30px;
  font-weight: 600;
  box-shadow: 0 0 10px 1px #d0d0d0;
}
/* 增加地址弹框 */
.w-add .el-dialog {
  width: 722px;
  height: 732px;
  background: url("../../assets/w-img/tan.png") no-repeat center/100%;
  box-shadow: none;
  position: relative;
}
.w-add .el-dialog .el-input .el-input__inner {
  height: 50px;
}
.w-add .w-name {
  width: 468px;
  position: absolute;
  top: 232px;
  left: 180px;
}
.w-add .w-tel {
  width: 468px;
  position: absolute;
  top: 324px;
  left: 180px;
}
.w-add .w-province {
  width: 104px;
  position: absolute;
  top: 420px;
  left: 150px;
  border: none;
}
.w-add .w-city {
  width: 90px;
  position: absolute;
  top: 420px;
  left: 355px;
}
.w-add .w-area {
  width: 90px;
  position: absolute;
  top: 420px;
  left: 560px;
}
.w-add .w-street {
  width: 450px;
  position: absolute;
  top: 520px;
  left: 210px;
}
.w-add .dialog-footer .button1 {
  width: 152px;
  height: 50px;
  border: #7d7d7d;
  background-color: #7d7d7d;
  position: absolute;
  right: 370px;
  bottom: 50px;
  color: #fff;
}
.w-add .dialog-footer .button2 {
  width: 152px;
  height: 50px;
  background-color: #c4c4c4;
  border: #c4c4c4;
  position: absolute;
  right: 130px;
  bottom: 50px;
  color: #fff;
}
.w-add .el-dialog__headerbtn {
  display: none;
}
</style>