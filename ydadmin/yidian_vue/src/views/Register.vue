<template>
  <el-container>
    <el-main>
      <div class="login-box">
        <img class="back" src="../assets/index/login.png" alt>
        <div class="login">
          <div class="login-header">
            <img class="login-he" src="../assets/index/register.png" alt>
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
                :rules="[{ required: true, message: '账号不能为空'},]"
              >
                <el-input
                  type="text"
                  v-model.number="numberValidateForm.name"
                  placeholder="手机号/账号/邮箱"
                  class="text1"
                ></el-input>
              </el-form-item>
              <el-form-item prop="验证码" class="code">
                <el-input class="send-left" v-model="numberValidateForm.sendcode" placeholder="请输入验证码"></el-input>
                <el-button class="send-right" type="button" @click="sendcode" :disabled="disabled" v-if="disabled==false">发送验证码
                </el-button>
                <el-button type="button" @click="sendcode" :disabled="disabled" v-if="disabled==true">{{btntxt}}
                </el-button>
            </el-form-item>
              <el-form-item
                prop="password"
                :rules="[{ required: true, message: '密码不能为空'},]"
              >
                <el-input
                  type="password"
                  v-model.number="numberValidateForm.password"
                  autocomplete="off"
                  placeholder="密码"
                  class="text1"
                ></el-input>
              </el-form-item>
              <el-form-item class="addel">
                <span @click="login">请登录</span>
              </el-form-item>
              <el-form-item>
                <el-button
                  type="primary"
                  @click="submitForm('numberValidateForm')"
                  class="loginn"
                >立即注册</el-button>
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
        password: "",
        sendcode: "",
      },
    disabled: false,
    time: 0,
    btntxt: "重新发送",
    };
  },
  methods: {
    sendcode() {
      const reg = 11 && /^((13|14|15|17|18)[0-9]{1}\d{8})$/
      if (!reg.test(this.numberValidateForm.name)) {
        this.$message({
          message: "请输入正确的手机号",
          center: true
        });
        return 111;
      } else {
        this.$message({
          message: "发送成功",
          type: "success",
          center: true
        });
        this.time = 60;
        this.disabled = true;
        this.timer();
      }
    },
    // 60S倒计时
    timer() {
      if (this.time > 0) {
        this.time--;
        this.btntxt = this.time + "s后重新获取";
        setTimeout(this.timer, 1000);
      } else {
        this.time = 0;
        this.btntxt = "获取验证码";
        this.disabled = false;
      }
    },
    // 注册提交
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {                                                                                                                                  //  this.$axios.get('api/login/')
          // web后台接收formData，这里是json,后来不用json了，直接就是data
          let data = new FormData();
          // console.log(document.cookie)  // 用正则切出来
          // let reg = /csrftoken=([\w]+[;]?)/g;
          //直接匹配字符串
          // console.log(reg.exec(document.cookie))   main.js认证
          // 在http里加一个内容让后台可以接收到，cookie，这样才能做到跨域的验证 用做好的在博客上

          //data添加一些数据,username从当前的numberValidateForm中来
          data.append('username',this.numberValidateForm.name);
          data.append('password',this.numberValidateForm.password);
          // console.log(data)
          this.$axios.post('api/register/',data).then((res)=>{
            console.log(res)
            // console.log(typeof res)
            if(res.data.code == "ok"){
              this.$router.push({ name: "login" });
               this.$message({
                 message: res.data.message,
                 type: 'success'
               });
            }else {
              this.$message.error(res.data.message);
            }
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },


    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    login() {
      this.$router.push({ name: "login" });
    },
    loginn() {
      this.$router.push({ name: "login" });
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
.form-box .send-left{
    width: 50%;
    float: left;
}
.form-box .send-right{
    width: 40%;
    float: right;
}
.el-form-item__label {
  width: 50px;
}
.form-box .addel {
  margin-top: -15px;
}
.form-box .addel span {
  color: #000000;
  opacity: 0.6;
  cursor: pointer;
  float: left;
}

.form-box .loginn {
  width: 100%;
  background-color: #7d7d7d;
  box-shadow: 0px 3px 5px 0px rgba(195, 195, 195, 0.74);
  color: #ffffff;
  opacity: 0.8;
  letter-spacing: 2px;
}
</style>
