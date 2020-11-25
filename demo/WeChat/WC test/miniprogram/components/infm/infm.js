var app = getApp();
Page({
  data:{
    name:'',
    gender:'',
    img:'',
    country:'',
    city:'',
    province:'',
    address:[],
    addressindex:0
  },
  seladdress:function(event){
    this.setData({
      addressindex:event.detail.value
    })
    
  },
  onReady:function(){
    this.setData({
      address:app.globalData.address
    })
    function tqsex(sex){
      var arr = ['','男','女']
      return arr[sex]
    }
    function tqcountry(c){
      var obj={'China':'中国',"England":'英格兰','Amarican':'美国'};
      return obj[c];
    }
    function tqprovince(p){
      var obj={'Fujian':'福建',"GuangDong":'广东','ZheJiang':'浙江'};
      return obj[p];
    }
    function tqcity(city){
      var obj={'Zhangzhou':'漳州',"Xiamen":'厦门','Fuzhou':'福州','Quanzhou':'泉州'};
      return obj[city];
    }
    var that=this;
    /**
     * 获取用户信息
     */
    wx.getUserInfo({
      success: function (res) {
        console.log(res)
        that.setData({
          name: res.userInfo.nickName,
          img: res.userInfo.avatarUrl,
          gender:tqsex(res.userInfo.gender),
          country:tqcountry(res.userInfo.country),
          province:tqprovince(res.userInfo.province),
          city:tqcity(res.userInfo.city),
        })
      }
    })
  }
})