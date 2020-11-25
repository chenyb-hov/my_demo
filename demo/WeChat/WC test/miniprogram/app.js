//app.js
App({
  onShareAppMessage: function() {
    let users = wx.getStorageSync('user');
    if (res.from === 'button') {}
    return {
      title: '转发',
      path: '/pages/index/index',
      success: function(res) {}
    }
  },
  onLaunch: function () {
    if (!wx.cloud) {
      console.error('请使用 2.2.3 或以上的基础库以使用云能力')
    } else {
      wx.cloud.init({
        // env 参数说明：
        //   env 参数决定接下来小程序发起的云开发调用（wx.cloud.xxx）会默认请求到哪个云环境的资源
        //   此处请填入环境 ID, 环境 ID 可打开云控制台查看
        //   如不填则使用默认环境（第一个创建的环境）
        // env: 'my-env-id',
        traceUser: true,
      })
    }

    this.globalData = {
      shopcarts :[
        {'id':0,
        'number':0,
        'name':'good1',
        'ms':'this is good1',
        "rprice":198,
        'price':168,
        'cirle':false
        },
        {'id':1,
        'number':0,
        'name':'good2',
        'ms':'this is good2',
        "rprice":288,
        'price':258,
        'cirle':false
        },
        {'id':2,
        'number':0,
        'name':'good3',
        'ms':'this is good3',
        "rprice":678,
        'price':666,
        'cirle':false
        },
        {'id':3,
        'number':0,
        'name':'good4',
        'ms':'this is good4',
        "rprice":1234,
        'price':998,
        'cirle':false
        },
        {'id':4,
        'number':0,
        'name':'good5',
        'ms':'this is good5',
        "rprice":888,
        'price':666,
        'cirle':false
        },
        {'id':5,
        'number':0,
        'name':'good6',
        'ms':'this is good6',
        "rprice":1998,
        'price':1666,
        'cirle':false
        }
        ],
      'numbers':0,
      'lika':[
        {'id':'000001',
          'money':100,
          'img':'',
          'uid':'000001',
          'ruid':'000002',
          'hcid':''
        },
        {'id':'000002',
          'money':200,
          'img':'',
          'uid':'000001',
          'ruid':'000003',
          'hcid':''
        },
        {'id':'000003',
          'money':300,
          'img':'',
          'uid':'000001',
          'ruid':'000004',
          'hcid':''
        },
        {'id':'000004',
          'money':500,
          'img':'',
          'uid':'000001',
          'ruid':'000005',
          'hcid':''
        },
        {'id':'000005',
          'money':1200,
          'img':'',
          'uid':'000001',
          'ruid':'000006',
          'hcid':''
        },
        {'id':'000006',
          'money':20,
          'img':'',
          'uid':'000001',
          'ruid':'000008',
          'hcid':''
        },
        {'id':'000007',
          'money':90,
          'img':'',
          'uid':'000002',
          'ruid':'000003',
          'hcid':'000001'
        },
        {'id':'000008',
          'money':60,
          'img':'',
          'uid':'000003',
          'ruid':'000005',
          'hcid':'000001'
        },
      ],
      collection:[],
      orders:[],
      address:['新景中心','软件园二期','软件园三期']
    }
  }
})
