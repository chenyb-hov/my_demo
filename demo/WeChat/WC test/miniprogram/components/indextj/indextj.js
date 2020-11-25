var app = getApp();
Component({
  data:{
    items:[],
    items1:[],
    animation:'',
    searchvalue:''
  },
  methods:{
    addshopcart:function(event){
      var idnum = parseInt(event.currentTarget.dataset.id);
      console.log(idnum)
      for (var i in app.globalData.shopcarts){
        if(app.globalData.shopcarts[i].id == idnum){
          app.globalData.shopcarts[i].number += 1;
          break;
        }
      }
      app.globalData.numbers += 1;
      app.globalData.shopcarts[i].cirle = true;
      this.setData({
        items:app.globalData.shopcarts
      })
      // this.animation.translate(-10,300).step()
      // this.setData({
      //   animation: this.animation.export()
      // })
      app.globalData.shopcarts[i].cirle = false;
      var that=this;
      setTimeout(function(){
        that.setData({
          items:app.globalData.shopcarts
        })
      },600)
      var myeventdata={num:1};
      var myeventoption={};
      this.triggerEvent('parentEvent',myeventdata,myeventoption)
    },
    gogood:function(event){
      wx.navigateTo({
        url: "/pages/good/good?id="+event.currentTarget.dataset.goodid
      });
    },
    getinputvalue:function(event){
      this.setData({
        searchvalue:event.detail.value
      })
    },
    onsearch:function(){
      if(this.data.searchvalue == null || this.data.searchvalue == ''){
        this.setData({
          items:items1
        })
      }
      else{
        var values = [];
        for(let i in this.data.items1){
          if(this.data.items1[i].name.indexOf(this.data.searchvalue)==-1){
            continue;
          }
          else{
            values.push(this.data.items1[i])
          }
        }
        this.setData({
          items:values
        })
      }
    }
  },
  ready:function(){
    // this.animation = wx.createAnimation({
    //   delay: 2500,
    //   timingFunction:"linear",
    //   delay:100,
    //   transformOrigin:'left top 0',
    //   success:function(res){}
    // })
    this.setData({
      items:app.globalData.shopcarts,
      items1:app.globalData.shopcarts,
    })
    console.log(this.data.items)
  }
})