var app = getApp();
Page({
  data:{
    items:''
  },
  onReady:function(){
    var itemlist = [];
    for(let i in app.globalData.collection){
      for(let j in app.globalData.shopcarts){
        if(app.globalData.shopcarts[j].id==app.globalData.collection[i].gid){
          itemlist.push(app.globalData.shopcarts[j]);
          break;
        }
      } 
    }
    this.setData({
      items:itemlist
    })
  },
  gogood:function(event){
    wx.navigateTo({
      url: '/pages/good/good?id='+event.currentTarget.dataset.goodid
    })
  }
})