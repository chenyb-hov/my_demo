var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    comments:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var cmms = [];
    for(let i in app.globalData.orders){
      for(let j in app.globalData.orders[i].data){
        if(app.globalData.orders[i].data[j].comment == null || app.globalData.orders[i].data[j].comment == ''){
          continue;
        }
        else{
          cmms.push(app.globalData.orders[i].data[j])
        }
      }
    }
    this.setData({
      comments:cmms
    })
    console.log(cmms)
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

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