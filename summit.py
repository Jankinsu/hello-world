import requests
import time
urls = ["http://api.turinglabs.net/api/v1/jd/ddfactory/create/P04z54XCjVWnYaS5m9cZ2f-3nxKlrAmYQV3xz4/",
        "https://github.com/Jankinsu/J_D_auto/runs/1688536579?check_suite_focus=true",
        "https://code.chiang.fun/api/v1/jd/jdcash/create/eU9YCabBDqNjuySfgTFv/",
        "http://api.turinglabs.net/api/v1/jd/ddfactory/create/P04z54XCjVWnYaS5m9cZwWyrhQV0GEflA8j8g/",
        "http://api.turinglabs.net/api/v1/jd/ddfactory/create/P04z54XCjVWnYaS5m9cZ2epjH0YlHbJaWzu2ZY/",
        "http://api.turinglabs.net/api/v1/jd/bean/create/4npkonnsy7xi3smpxocizkqtluyfcjgmiywfw5a/",
        "http://api.turinglabs.net/api/v1/jd/bean/create/nkiu2rskjyetbs6rn3p3t5itliqvt5szqmg7qua/",
        "http://api.turinglabs.net/api/v1/jd/bean/create/4npkonnsy7xi2eaa3jnazggk4xl2kveisfbfhay/",
        "http://api.turinglabs.net/api/v1/jd/farm/create/854cebbe338d4ef9aef50945bd3d8e56/",
        "http://api.turinglabs.net/api/v1/jd/farm/create/de8e60b6c68c4ab9936bc8c3f6b2500b/",
        "http://api.turinglabs.net/api/v1/jd/farm/create/6961410a2ced47a49a77907217ac487e/",
        "http://api.turinglabs.net/api/v1/jd/pet/create/MTAxODc2NTEzNDAwMDAwMDAxOTk2NTM3NQ==/",
        "http://api.turinglabs.net/api/v1/jd/pet/create/MTAxODc2NTEzOTAwMDAwMDAyMjM5Mjk2NQ==/",
        "http://api.turinglabs.net/api/v1/jd/pet/create/MTE1NDUyMjEwMDAwMDAwNDI1NDc3ODM=/",
        "http://api.turinglabs.net/api/v1/jd/jxfactory/create/1wAHpnyz0wiCFnaqBFoDCQ==/",
        "http://api.turinglabs.net/api/v1/jd/jxfactory/create/5rE5veg8Sxmw06JXaHEujQ==/",
        "https://code.chiang.fun/api/v1/jd/jdzz/create/AUWE5mKuTzTULWWeqj3wekQ",
        "https://code.chiang.fun/api/v1/jd/jdzz/create/AUWE5-ufjpWpNQiqylz42",
        "http://api.turinglabs.net/api/v1/jd/jxfactory/create/u8PgQuKCPoPXQiXXuEOv5Q==/"]
#headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Mobile Safari/537.36 Edg/87.0.664.47"}
#existed = "existed"
#success = "200"
n=1
for url in urls:
        res = requests.get(url,timeout=30)
        print(n)
        print(res.text)
        n=n+1
        time.sleep(1)
