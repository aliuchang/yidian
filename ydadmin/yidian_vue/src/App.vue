<template>
  <div id="app">
    <heads/>
    <routes/>
    <router-view></router-view>
    <footers/>
  </div>
</template>

<script>
import heads from '@/components/Z-header.vue';
import routes from '@/components/z-router.vue';
import footers from '@/components/z-bottom.vue'

export default {
  name: 'app',
  components: {
    heads,
    routes,
    footers
  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
  text-decoration: none;
}
#app {
  font-family: '站酷文艺体','Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
