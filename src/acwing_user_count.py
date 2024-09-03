import time

import requests

l, r = 0, 10 ** 7
while l < r:
    mid = l + r + 1 >> 1
    url = 'https://www.acwing.com/user/myspace/index/' + str(mid)
    print('mid: %d' % mid)
    response = requests.get(url)
    if '找不到页面' in response.text:
        r = mid - 1
        print('大了')
    else:
        l = mid
        print('小了')
    time.sleep(1)
print('AcWing一共有%d名用户' % l)
