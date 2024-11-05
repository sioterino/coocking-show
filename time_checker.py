import datetime
import time

if __name__ == "__main__":

    start = datetime.timedelta(hours=20, minutes=00)
    end = datetime.timedelta(days=1, hours=8, minutes=00)
    now = datetime.timedelta(hours=19, minutes=55)

    print(now - datetime.timedelta(hours=12))

    print(f"start : {start}")
    print(f"end   : {end}")
    print(f"now   : {now}")
    print("\n\n\n")
    print(datetime.datetime.now())

    current = datetime.timedelta(days=1, hours=datetime.datetime.now().hour, minutes=datetime.datetime.now().minute)
    print(current)

    # Check type and comparison
    print(current > datetime.timedelta(days=1,hours=16))
    print("\n\n\n")

    num = 0
    cycle_range = 11

    while True:
        # time.sleep(0.05)
        now += datetime.timedelta(minutes=1)

        if now >= start:
            while num < cycle_range and now >= start:  # WHILE 2
                # time.sleep(0.05)
                # if it is not 1/4, you vote
                if num % 25 != 0:
                    print(f"vote {now} >> {num}")
                # end of IF
                else:  # if it is a quarter you open chrome
                    if num != 0:
                        print("CLOSE chrome")
                    # end of IF
                    print("OPEN chrome")
                    print(f"vote {now} >> {num}")

                # increment by one
                num += 1
                # end test to see if the time's up
                now += datetime.timedelta(minutes=1)
                if now >= end:
                    break

        if  now >= end:
            print("close")
            break