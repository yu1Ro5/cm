import psutil
import schedule
import time
def job():
    # メモリ使用率を取得
    mem = psutil.virtual_memory() 
    print(mem.percent)
    #[結果] 55.9
schedule.every(1).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)