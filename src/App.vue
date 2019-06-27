<template>
    <div id="app">
        <heads></heads>
        <routes :routes="routess"></routes>
        <router-view></router-view>
        <footers/>
        <!-- 回到顶部 -->
        <img v-if="btnFlag" class="go-top" src="./assets/index/topback.png" @click="backTop">
    </div>
</template>

<script>
    import heads from "@/components/Z-header.vue";
    import routes from "@/components/z-router.vue";
    import footers from "@/components/z-bottom.vue";

    export default {
        data() {
            return {
                btnFlag: false,
                routess: [
                    {
                        path: '/list',
                        title: '全部',
                        en_name: 'ALL'
                    },
                    {
                        path: '/list',
                        title: '座椅',
                        en_name: 'Seat'
                    },
                    {
                        path: '/list',
                        title: '床',
                        en_name: 'Seat bed'
                    },
                    {
                        path: '/list',
                        title: '柜子',
                        en_name: 'Seat cabinets'
                    },
                    {
                        path: '/list',
                        title: '边几',
                        en_name: 'Seat Edge Several'
                    }
                ]
            };
        },
        name: "app",
        components: {
            heads,
            routes,
            footers
        },
        mounted: function () {
            window.addEventListener("scroll", this.scrollToTop);
        },
        destroyed() {
            window.removeEventListener("scroll", this.scrollToTop);
        },
        methods: {
            // 点击图片回到顶部方法，加计时器是为了过渡顺滑
            backTop() {
                let that = this;
                let timer = setInterval(() => {
                    let ispeed = Math.floor(-that.scrollTop / 5);
                    document.documentElement.scrollTop = document.body.scrollTop =
                        that.scrollTop + ispeed;
                    if (that.scrollTop === 0) {
                        clearInterval(timer);
                    }
                }, 16);
            },

            // 为了计算距离顶部的高度，当高度大于60显示回顶部图标，小于60则隐藏
            scrollToTop() {
                let that = this;
                let scrollTop =
                    window.pageYOffset ||
                    document.documentElement.scrollTop ||
                    document.body.scrollTop;
                that.scrollTop = scrollTop;
                if (that.scrollTop > 60) {
                    this.btnFlag = true;
                } else {
                    this.btnFlag = false;
                }
            }
        }
    };
</script>

<style>
    * {
        margin: 0;
        padding: 0;
    }

    a {
        text-decoration: none;
        outline: none;
    }

    #app {
        font-family: "站酷文艺体", "Avenir", Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    /* 回到顶部 */
    .go-top {
        width: 50px;
        height: 50px;
        position: fixed;
        right: 30px;
        bottom: 50px;
        box-sizing: border-box;
        opacity: 0.5;
    }

    .go-top img {
        width: 100%;
    }
</style>
