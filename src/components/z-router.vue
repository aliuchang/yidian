<template>
    <div class="zrouter">
        <router-link to="/firstpage">
            <div class="router-left">
                <img src="@/assets/z-img/logo.png" alt>
            </div>
        </router-link>
        <div class="router-middle-link">
            <template v-for="item in routes">
                <router-link :to="item.path" class="push">
                    <div class="title">{{item.title}}</div>
                    <div class="english">
                        <span>{{item.en_name}}</span>
                        <div class="border"></div>
                    </div>
                </router-link>
            </template>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            routes: Array,
            required: true,
        },
        data() {
            return {}
        },
        mounted() {
            console.log(this.routes)
        }
    };
</script>

<style>
    .zrouter {
        width: 1200px;
        height: 98px;
        margin: 0 auto 20px;
    }

    .zrouter .router-left {
        width: 185px;
        height: 49px;
        float: left;
        margin-left: 24px;
        padding-top: 25px;
        margin-right: 130px;
    }

    .zrouter .router-left img {
        width: 100%;
    }

    .zrouter .router-middle-link {
        float: left;
        display: flex;
        align-items: center;
        height: 100%;
    }

    .zrouter .router-middle-link .push {
        width: 110px;
    }

    .zrouter .router-middle-link .push .title {
        font-size: 18px;
        color: rgba(0, 0, 0, 0.7);
        font-family: zcoolwenyiti;
    }

    .zrouter .router-middle-link .push .english {
        font-size: 12px;
        font-family: Cabin-Regular;
        color: #000000;
        opacity: 0.5;
    }

    .zrouter .router-middle-link .push .english .border {
        width: 20px;
        height: 2px;
        background: #fff;
        margin: 0 auto;
        margin-top: 6px;
    }

    .zrouter .router-middle-link .router-link-exact-active .english .border {
        background: #000;
    }

    .zrouter .router-middle-link .router-link-exact-active .title {
        font-weight: 600;
        color: rgba(0, 0, 0, 0.9);
    }
</style>
