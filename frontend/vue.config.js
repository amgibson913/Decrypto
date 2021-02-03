module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    proxy: 'http://localhost:5000'
  },
  proxy: {
    '/socket.io/': {
      target: 'http://${process.env.VUE_APP_FLASK_HOST}:5000',
      ws: true,
      changeOrigin: true
    }
  }
}