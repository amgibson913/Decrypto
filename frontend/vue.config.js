module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    proxy: 'http://localhost:5000'
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/decrypto/'
    : '/'
}