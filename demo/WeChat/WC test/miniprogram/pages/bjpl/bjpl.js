var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    order:[],
    Oid:0,
    fbz:false
  },
  fabu:function(){
    app.globalData.orders[this.data.Oid].data = this.data.order;
    this.setData({
      fbz:true
    })
    wx.showToast({
      title: '评论成功',
      icon: '',     //默认值是success,就算没有icon这个值，就算有其他值最终也显示success
      duration: 500,      //停留时间
    })
    setTimeout(function(){
      wx.navigateTo({
      url: '/pages/index/index?status='+3,
      })
    },500)
  },
  writepl:function(event){
    var od = this.data.order;
    od[event.currentTarget.dataset.gid].comment = event.detail.value;
    console.log(event.detail.value)
    this.setData({
      order:od
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var oid = options.oid;
    this.setData({
      Oid:oid
    })
    //console.log(oid)
    var os =[]
    for(let i in app.globalData.orders[oid].data){
      if(app.globalData.orders[oid].data[i].comment==null||app.globalData.orders[oid].data[i].comment==''){
        var x = app.globalData.orders[oid].data[i];
        x.status = true;
        os.push(x)
      }
      else{
        var x = app.globalData.orders[oid].data[i];
        x.status = false;
        os.push(x)
      }
    }
    this.setData({
      order:os
    })
    
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