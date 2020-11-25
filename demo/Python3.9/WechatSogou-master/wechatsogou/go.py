import wechatsogou

ws_api = wechatsogou.WechatSogouAPI()
ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)
ws_api = wechatsogou.WechatSogouAPI(proxies={
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888",
})