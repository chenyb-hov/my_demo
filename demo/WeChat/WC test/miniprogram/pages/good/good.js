var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    id: '',
    item: {},
    nickName:'',
    avatarUrl:'',
    comments:[]
  },
  oncollection:function(event){
    var obj={};
    obj.gid=event.currentTarget.dataset.gid;
    console.log(obj);
    var x = 0;
    for(let i in app.globalData.collection){
      if(app.globalData.collection[i].gid==obj.gid){
        x += 1;
        break;
      }
    }
    if(x==0){
      app.globalData.collection.push(obj);
      wx.showToast({
        title: '收藏成功',
        icon: '',     //默认值是success,就算没有icon这个值，就算有其他值最终也显示success
        duration: 1500,      //停留时间
      })
    }
  },
  addsc:function(event){
    for(let i in app.globalData.shopcarts){
      if(app.globalData.shopcarts[i].id==event.currentTarget.dataset.gid){
        app.globalData.shopcarts[i].number += 1;
        app.globalData.numbers += 1;
        wx.showToast({
          title: '成功加入购物车',
          icon: '',     //默认值是success,就算没有icon这个值，就算有其他值最终也显示success
          duration: 1500,      //停留时间
        })
        break;
      }
    }
    
  },
  main: function () {
    for (let i in app.globalData.shopcarts) {
      if (app.globalData.shopcarts[i].id == this.data.id) {
        this.setData({
          item: app.globalData.shopcarts[i]
        })
      }
    }
  },
  gomay:function(event){
    for(let i in app.globalData.shopcarts){
      if(app.globalData.shopcarts[i].id==event.currentTarget.dataset.gid){
        app.globalData.shopcarts[i].number += 1;
        app.globalData.numbers += 1;
        wx.navigateTo({
          url: "/pages/index/index?status="+2
        });
        break;
      }
    }
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      id: options.id
    })
    console.log(this.data.id)
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */


  onReady: function () {
    this.main();
    var that = this;
    wx.getUserInfo({
      success: function (res) {
       that.setData({
          nickName: res.userInfo.nickName,
          avatarUrl: res.userInfo.avatarUrl,
        })
        var orders = [];
        for(let i in app.globalData.orders){
          for(let j in app.globalData.orders[i].data){
            if(app.globalData.orders[i].data[j].comment != null && app.globalData.orders[i].data[j].comment != ''){
              //console.log(app.globalData.orders[i].data[j])
              var obj = {};
              obj.id = app.globalData.orders[i].data[j].id;
              obj.nickName = that.data.nickName;
              obj.avatarUrl = that.data.avatarUrl;
              obj.comment = app.globalData.orders[i].data[j].comment
              orders.push(obj);
            }
          }
        }
        console.log(orders)
        that.setData({
          comments:orders
        })
        console.log(res.userInfo.nickName)
      },
    })
    
    
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