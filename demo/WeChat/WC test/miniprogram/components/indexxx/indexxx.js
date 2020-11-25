var app = getApp();
Component({
  data: {
    items: [],
    numbers: 0,
    summoney: 0,
    jsz:false
  },
  methods: {
    main: function () {
      this.setData({
        items: app.globalData.shopcarts,
        numbers: app.globalData.numbers,
      })
      var sum=0;
      for(let i in this.data.items){
        sum += this.data.items[i].price * this.data.items[i].number;
      }
      this.setData({
        summoney:sum
      })
    },
    upnum: function (event) {
      var a = parseInt(event.currentTarget.dataset.up);
      var id = parseInt(event.currentTarget.dataset.id);
      app.globalData.numbers += a;
      console.log(a, id)
      for (var i in app.globalData.shopcarts) {
        if (app.globalData.shopcarts[i].id == id) {
          app.globalData.shopcarts[i].number += a
        }
      }
      console.log(app.globalData.shopcarts)
      this.setData({
        items: app.globalData.shopcarts,
        numbers: app.globalData.numbers
      })
      var myeventdata = {
        num: 1
      };
      var myeventoption = {};
      this.triggerEvent('cartparentEvent', myeventdata, myeventoption);
      this.main();
    },
    clearshopcart:function(){
      var that = this;
      wx.showModal({
        title: '提示',
        content:'确定要清空购物车',
        success:function(sm){
          if(sm.confirm){
            for(let i in app.globalData.shopcarts){
              app.globalData.shopcarts[i].number = 0;
            }
            app.globalData.numbers=0;
            var myeventdata = {
              num: 1
            };
            var myeventoption = {};
            that.triggerEvent('clecartparentEvent', myeventdata, myeventoption);
            that.main();
          }
        }
      })
    },
    onjiesuan:function(event){
      var summn = event.currentTarget.dataset.summn;
      if(summn == 0){
        return;
      }
      var that = this
      wx.showModal({
        title: '结算',
        content:'一共'+summn+"元,确认下单并支付?",
        success:function(sm){
          if(sm.confirm){
            var order = {};
            var lists = [];
            for(let i in app.globalData.shopcarts){
              var obj = {};
              if(app.globalData.shopcarts[i].number!=0){
                obj.id = app.globalData.shopcarts[i].id;
                obj.num = app.globalData.shopcarts[i].number;
                obj.name = app.globalData.shopcarts[i].name;
                obj.ms = app.globalData.shopcarts[i].ms;
                obj.price = app.globalData.shopcarts[i].price;
                lists.push(obj);
              }
              app.globalData.shopcarts[i].number = 0;
            }
            order.data = lists;
            app.globalData.orders.push(order);
            app.globalData.numbers=0;
            var myeventdata = {
              num: 1
            };
            var myeventoption = {};
            that.triggerEvent('clecartparentEvent', myeventdata, myeventoption);
            that.setData({
              jsz:true
            })
            wx.showToast({
              title: '下单成功',
              icon: 'success',
              duration: 1000//持续的时间
            })
            setTimeout(function(){
              that.main();
              that.setData({
                jsz:false
              })
            },800)
            console.log(app.globalData.orders)
          }
        }
      })
    }
  },
  ready: function () {
    this.main();
  }
})