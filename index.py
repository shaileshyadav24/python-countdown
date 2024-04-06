import time

def countdownClock(inputTime):
    totalTime = inputTime * 60

    while totalTime > 0:
        minuteLeft = int(totalTime / 60)
        secondsLeft = totalTime % 60
        print('{:02d}'.format(minuteLeft),":", '{:02d}'.format(secondsLeft))
        time.sleep(1)
        totalTime -= 1
    print("Thank you for using countdown clock. Have a nice day!!")

t = input("Enter time in minutes to start countdown:")
countdownClock(int(t))