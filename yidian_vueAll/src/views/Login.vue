<template>
  <el-container>
    <el-main>
      <div class="login-box">
        <img class="back" src="../assets/index/login.png" alt>
        <div class="login">
          <div class="login-header">
            <img class="login-he" src="../assets/index/login01.png" alt>
          </div>
          <div class="form-box">
            <el-form
              :model="numberValidateForm"
              status-icon
              ref="numberValidateForm"
              class="demo-ruleForm"
            >
              <el-form-item
                prop="name"
                :rules="[
            { required: true, message: '账号不能为空'},

          ]"
              >
                <el-input
                  type="text"
                  v-model.number="numberValidateForm.name"
                  
                  placeholder="手机号/账号/邮箱"
                  class="text1"
                ></el-input>
              </el-form-item>
              <el-form-item
                prop="pass"
                :rules="[
            { required: true, message: '密码不能为空'},
          ]"
              >
                <el-input
                  type="password"
                  v-model.number="numberValidateForm.pass"
                  autocomplete="off"
                  placeholder="密码"
                  class="text1"
                ></el-input>
              </el-form-item>
              <el-form-item class="addel">
                <span @click="register">立即注册</span>
                <span @click="forgetpass">忘记密码?</span>

              </el-form-item>
              <el-form-item>
                <el-button
                  type="primary"
                  @click="submitForm('numberValidateForm')"
                  class="loginn"
                >立即登录</el-button>
              </el-form-item>
              <el-form-item class="BAT-box">
                <div class="qq-box"><img src="../assets/index/qq.png" alt=""></div>
                <div class="qq-box"><img src="../assets/index/weixin.png" alt=""></div>
                <div class="qq-box"><img src="../assets/index/weibo.png" alt=""></div>
              </el-form-item>

            </el-form>
          </div>
        </div>
      </div>
    </el-main>
  </el-container>
</template>
<script>
export default {
  data() {
    return {
      numberValidateForm: {
        name: "",
        pass: ""
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          let data = new FormData()
          data.append('username',this.numberValidateForm.name)
          data.append('password',this.numberValidateForm.pass)
          this.$axios.post('api/login/',data).then((res)=>{
            console.log(res)
            if(res.data.code == "ok"){
              this.$router.push({ name: "firstpage" });
            }
            else{
              console.log("error！")
            }

          })

        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    register(){
      this.$router.push({ name: "register" });
    },
    forgetpass(){
      this.$router.push({ name: "register" });
    }
  }
};
</script>



<style>
* {
  margin: 0;
  padding: 0;
}
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-main {
  width: 100%;
  padding: 0;
  overflow: hidden;
  box-sizing: border-box;
}
.el-main .login-box {
  width: 100%;
  height: 645px;
  overflow: hidden;
  box-sizing: border-box;
  position: relative;
}
.el-main .login-box .back {
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  margin: auto;
}
.login {
  width: 377px;
  height: 464px;
  background: #ffffff;
  box-shadow: 4px 3px 16px 0px#cacaca;
  position: absolute;
  top: 90px;
  right: 15%;
}
.login .login-header {
  width: 214px;
  height: 40px;
  margin: auto;
  margin-top: 50px;
}
.login .login-header .login-he {
  height: 100%;
  margin: auto;
}
.form-box {
  width: 282px;
  height: 324px;
  margin: auto;
  margin-top: 53px;
  box-sizing: border-box;
  overflow: hidden;
}
.el-form-item__label {
  width: 50px;
}
.form-box .addel{
  margin-top:-15px; 
}
.form-box .addel span{
   color: #000000;
    opacity: 0.6;
    cursor: pointer;
}
.form-box .addel span:nth-child(1){
  float: left;
 
}
.form-box .addel span:nth-child(2){
  float: right;
}
.form-box .loginn{
  width: 100%;
  background-color: #7d7d7d;
	box-shadow: 0px 3px 5px 0px 
		rgba(195, 195, 195, 0.74);
    color: #ffffff;
	opacity: 0.8;
  letter-spacing: 2px;
}
.form-box .BAT-box{

  width: 182px;
  height: 20px;
  margin: auto;

}
.form-box .BAT-box .qq-box{
  width: 24px;
  height: 100%;
}
.form-box .BAT-box .qq-box:nth-child(1){
  float: left;
}
.form-box .BAT-box .qq-box:nth-child(2){
  float: left;
  margin-left:55px ;
}
.form-box .BAT-box .qq-box:nth-child(3){
  float: right;
}
.form-box .BAT-box .qq-box img{
  height: 100%;
}
</style>
