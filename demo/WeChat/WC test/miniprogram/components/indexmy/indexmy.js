
Component({
  data:{
    avatarUrl:"",//用户头像
    nickName:"",//用户昵称
  },
  methods:{
    gomyinfm:function(){
       wx.navigateTo({
        url: "/components/infm/infm"
      })
    },
    gokabao:function(){
      wx.navigateTo({
        url: "/components/indexsy/indexsy"
      })
    },
    goCollection:function(){
      wx.navigateTo({
        url: "/pages/collection/collection"
      });
    },
    goorder:function(){
      wx.navigateTo({
        url: "/pages/order/order"
      });
    },
    gocomment:function(){
      wx.navigateTo({
        url: "/pages/comment/comment"
      });
    }
  },
  ready: function () {
    var that=this;
    /**
     * 获取用户信息
     */
    wx.getUserInfo({
      success: function (res) {
       that.setData({
          nickName: res.userInfo.nickName,
          avatarUrl: res.userInfo.avatarUrl,
        })
      },
    })
  },

})