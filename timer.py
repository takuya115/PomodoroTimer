#タイマー機能

import time

#25分のタイマー
def work():
    time.sleep(60*25)
    print("work end")
    return relax()
#5分休憩のタイマー
def relax():
    time.sleep(60*5)
    print("relax end")
    return work()

if __name__ == "__main__":
    print("starttimer")
    work()
    

