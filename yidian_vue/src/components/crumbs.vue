// 面包屑
<template>
    <div class="crumb-box">
        <div class="j-point"></div>
        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/index' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>{{cmenus.meta.title}}</el-breadcrumb-item>
        </el-breadcrumb>
    </div>
</template>

<script>
export default {
    data(){
        return {
            cmenus: "",
        }
    },
    props:["crumbsname"],
    created() {
        this.cmenus = this.$route.matched[0];
    },mounted(){
        // console.log(this.$router.options.routes[0].children[0])
        // console.log(this.$route.matched)
        let arr = this.$route.matched
        arr.forEach((i,v)=>{
            i.path
        })
    }
}
</script>

<style>
.crumb-box{
    width: 1200px;
    height: 50px;
    margin: 30px auto;
}
.j-point{
    width: 8px;
    height: 8px;
    background: #4CC0CB;
    border-radius: 50%;
    margin: 20px 20px 20px 0;
    float: left;
}
.el-breadcrumb{
    display: block;
    height: 50px;
    line-height: 50px;
    float: left;
}

</style>
