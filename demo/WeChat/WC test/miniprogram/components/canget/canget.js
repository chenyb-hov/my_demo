var app = getApp();
Component({
  data:{
    lika:[]
  },
  ready:function(){
    this.main();
  },
  methods:{
    main:function(){
      this.setData({
        lika:[]
      })
      var list=[]
      for(var i in app.globalData.lika){
        if(app.globalData.lika[i].hcid=="000001"){
          list.push(app.globalData.lika[i])
        }
      }
      this.setData({
        lika:list
      })
      console.log(this.data.lika)
    },
    golq:function(event){
      var id = event.currentTarget.dataset.lq;
      var likas = app.globalData.lika;
      for(var i in likas){
        if(likas[i].id==id){
          likas[i].ruid = likas[i].uid;
          likas[i].uid = "000001";
          likas[i].hcid = '';
          break;
        }
      }
      app.globalData.lika = likas;
      this.main();
      var myeventdata={num:1};
      var myeventoption={};
      this.triggerEvent('lqlkparentEvent',myeventdata,myeventoption)
    },
    goth:function(event){
      var id = event.currentTarget.dataset.th;
      for(let i in app.globalData.lika){
        if(app.globalData.lika[i].id==id){
          app.globalData.lika[i].hcid='';
          break;
        }
      }
      var myeventdata={num:1};
      var myeventoption={};
      this.triggerEvent('lqthparentEvent',myeventdata,myeventoption);
      this.main();
    }
  }
})