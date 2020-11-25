//index.js
const app = getApp()
Page({
  data: {
    nownum:0,
    numbers:0
  },
  goindex:function(){
    this.setData({
      nownum:0
    })
  },
  setnum:function(){
    this.setData({
      numbers:app.globalData.numbers
    })
  },
  main:function(){
    this.setData({
      numbers:app.globalData.numbers
    })
  },
  onReady:function(){
    var that=this;
    setInterval(function(){
      that.main();
    },1000)
    this.main();
    var urls = 'http://10.3.1.85:8080/api/tenfupda'
    wx.request({
      url: 'http://10.3.1.85:8080/api/tenfupda',
      header:{
        'Content-Type':'application/json'
      },
      data:{
        Method:'pda.get.org'
      },
      success:function(res){
        console.log(res.data)
      }
    })
  },
  gotj:function(){
    this.setData({
      nownum:1
    })
  },
  gomyxx:function(){
    this.setData({
      nownum:2
    })
  },
  gomywc:function(){
    // wx.navigateTo({
    //   url: '/components/canget/canget',
    // })
    this.setData({
      nownum:3
    })
  },
  onShareAppMessage: function() {
    let users = wx.getStorageSync('user');
    if (res.from === 'button') {}
    return {
      title: '转发',
      path: '/pages/index/index',
      success: function(res) {}
    }
  },
  onLoad:function(option){
    this.setData({
      nownum:option.status
    })
  }
})
