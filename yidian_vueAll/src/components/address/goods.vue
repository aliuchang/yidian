<template>
    <div class="W-good">
        <template  v-for="i in goods">
            <div class="w-good"  :key='i.title'>
                <div class="image1" >
                    <img :src="i.img" @click="godetail">
                </div>
                <ul class="info">
                    <li class="items">
                        <p class="ps">{{i.name}}</p>
                        <p>{{i.infos}}</p>
                    </li>
                    <li class="items">
                        <p>"{{i.ku}}"</p>
                    </li>
                    <li class="items">
                        <p>W: <span>{{i.num1}}</span></p>
                        <p>H: <span>{{i.num2}}</span></p>
                        <p>L: <span>{{i.num3}}</span></p>
                    </li>
                    <li class="items">
                        <p>1</p>
                    </li>
                    <li class="items">
                        <p><span class="money">{{i.nums1}}</span>RMB</p>
                    </li>
                    <li class="items">
                        <p><span class="money">{{i.nums2}}</span>RMB</p>
                        <el-button class="bot" type="text" @click="open">
                            <i class="el-icon-delete"></i>
                            删除
                        </el-button>
                    </li>
                </ul>
            </div>
        </template>
    </div>
</template>
<script>
export default {
    data(){
        return{
            goods:[
                {
                    img: require('@/assets/w-img/03.png'),
                    name: "ADE-阿德",
                    infos:"餐椅 简约风",
                    ku:"白色 米黄色",
                    num1:'45cm',
                    num2:'50cm',
                    num3:'60cm',
                    nums1: 456.00,
                    nums2:456.00,
                },
                {
                    img: require('@/assets/w-img/04.png'),
                    name: "ANTILOP-安迪咯",
                    infos:"高脚椅 简约风",
                    ku:"塑料 天蓝色",
                    num1:'45cm',
                    num2:'50cm',
                    num3:'60cm',
                    nums1: 467.00,
                    nums2:467.00,
                },
                {
                    img: require('@/assets/w-img/05.jpg'),
                    name: "KVART-卡特",
                    infos:"工作灯 北欧风",
                    ku:"黑色 可调节",
                    num1:'45cm',
                    num2:'50cm',
                    num3:'60cm',
                    nums1:105.00,
                    nums2:105.00,
                }
            ]
        }
    },
    methods:{
        open() {
        this.$confirm('删除该商品?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
        }).then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      godetail(){
          this.$router.push({name:'detail'})
          window.scroll(0,0)
      }
    }
}
</script>
<style>
.W-good .w-good{
    width: 1200px;
    height: 214px;
    border-bottom: 2px solid #e5e5e5;
}
.W-good .image1{
    float: left;
    width: 162px;
    height: 214px;
}
.W-good .image1 img{
    margin-top: 35px;
    width: 100%;
}
.W-good .info{
    list-style: none;
    padding: 0;
    margin: 0;
    float: left;
    width: 1038px;
    height: 100%;
    overflow: hidden;
}
.W-good .items{
    float: left;
    width: 173px;
    height: 100%;
    padding-top: 50px;
    position: relative;
}
.W-good .bot{
    position: absolute;
    bottom: 90px;
    right: 50px;
    height: 20px;
    cursor: pointer;
}
.W-good .ps{
    font-weight: 700;
}
.W-good .money{
    font-size: 22px;
    font-weight: 700;
}
</style>
