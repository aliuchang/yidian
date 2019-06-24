module.exports = {
    publicPath: '',   // 根路径
    outputDir:'dist',  // 打包时生成的一个文件名

    // 开发服务器
    devServer:{
      open: true,   // 启动项目后自动开启浏览器
      host: '127.0.0.1',
      port: 5000,
      proxy: null,   // 设置代理
    }
  }
  
  // 可以百度vue.config查看配置
  // npm run dist