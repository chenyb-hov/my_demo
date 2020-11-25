var app = getApp();
Component({
  data:{
    'lika':[]
  },
  methods:{
    onShareAppMessage:function( options ){
      　　var that = this;
      　　// 设置菜单中的转发按钮触发转发事件时的转发内容
      　　var shareObj = {
      　　　　title: "赠送...",        // 默认是小程序的名称(可以写slogan等)
      　　　　path: '/pages/share/share',        // 默认是当前页面，必须是以‘/’开头的完整路径
      　　　　imgUrl: '',     //自定义图片路径，可以是本地文件路径、代码包文件路径或者网络图片路径，支持PNG及JPG，不传入 imageUrl 则使用默认截图。显示图片长宽比是 5:4
      　　　　success: function(res){
      　　　　　　// 转发成功之后的回调
      　　　　　　if(res.errMsg == 'shareAppMessage:ok'){
      　　　　　　}
      　　　　},
      　　　　fail: function(){
      　　　　　　// 转发失败之后的回调
      　　　　　　if(res.errMsg == 'shareAppMessage:fail cancel'){
      　　　　　　　　// 用户取消转发
      　　　　　　}else if(res.errMsg == 'shareAppMessage:fail'){
      　　　　　　　　// 转发失败，其中 detail message 为详细失败信息
      　　　　　　}
      　　　　},
      　　　　complete: function(){
      　　　　　　// 转发结束之后的回调（转发成不成功都会执行）
    　　　　}
      　　}
      　　// 来自页面内的按钮的转发
      　　if( options.from == 'button' ){
      　　　　var eData = options.target.dataset;
      　　　　console.log( eData.name );     // shareBtn
      　　　　// 此处可以修改 shareObj 中的内容
      　　　　shareObj.path = '/pages/btnname/btnname?btn_name='+eData.name;
      　　}
      　　// 返回shareObj
      　　return shareObj;
      },
      getdata:function(){
        console.log(app.globalData.shopcarts);
        var obj = {'id':1,'number':2};
        app.globalData.shopcarts.push(obj);
        console.log(app.globalData.shopcarts);
      }
  },
  ready:function(){
    var list=[]
    for(var i in app.globalData.lika){
      if(app.globalData.lika[i].uid=="000001"){
        list.push(app.globalData.lika[i])
      }
    }
    this.setData({
      lika:list
    })
    console.log(this.data.lika)
  }
})