var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    orders:[]
  },
  main:function(){
    this.setData({
      orders:app.globalData.orders
    })
    console.log(this.data.orders)
    var os = this.data.orders;
    for(let i in os){
      var moneys = 0;
      var count = 0;
      for(let j in os[i].data){
        moneys += os[i].data[j].num * os[i].data[j].price;
        if(os[i].data[j].comment==null||os[i].data[j].comment==''){
          count += 1;
        }
      }
      if(count>0){
        os[i].comment = true
      }
      else{
        os[i].comment = false
      }
      os[i].moneys = moneys;
    }
    this.setData({
      orders:os
    })
  },
  gopl:function(event){
    wx.navigateTo({
      url: '/pages/bjpl/bjpl?oid='+event.currentTarget.dataset.oid,
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    this.main();
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})