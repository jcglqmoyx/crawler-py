import time
from datetime import datetime

import requests

l, r = 470000, 7 * 10 ** 5
while l < r:
    mid = l + r + 1 >> 1
    url = 'https://www.acwing.com/user/myspace/index/' + str(mid)
    print('mid: %d,' % mid, end=' ')
    response = requests.get(url)
    if '找不到页面' in response.text:
        r = mid - 1
        print('大了')
    else:
        l = mid
        print('小了')
    time.sleep(0.3)
print('AcWing一共有%d名用户' % l)
file = open('./acw_user_count.log', 'a')
file.write('[' + str(datetime.now()) + ']: ' + 'AcWing一共有%d名用户\n' % l)
file.close()
