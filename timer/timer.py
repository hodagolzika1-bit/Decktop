import time
print("welcome to thr pomodoro timer !!")
#نطلب من المستخدم يدخل الوقت 
mint=int(input("enter time in minutes :"))

total_soucand=mint*60
while total_soucand>0:
    try:
        hours=total_soucand//3600
        mint=(total_soucand%3600)//60
        secs=total_soucand%60
        clock=f"{hours:02d}:{mint:02d}:{secs:02d}"
        print(f"\r {clock} ",end="timer")
        time.sleep(1)
        total_soucand -=1
    except (ValueError,IndexError):
        print("Please enter a valid number only!")