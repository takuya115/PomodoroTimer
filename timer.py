#タイマー機能

import time

#25分のタイマー
def work():
    time.sleep(60*25)
    return relax()
#5分休憩のタイマー
def relax():
    time.sleep(60*5)
    return work()

