import datetime
import time


# gets time in timedelta type
def get_time(over_midnight: bool):
    temp: datetime.timedelta
    if over_midnight:
        temp = datetime.timedelta(days=1, hours=datetime.datetime.now().hour, minutes=datetime.datetime.now().minute)
    else:
        temp = datetime.timedelta(days=0, hours=datetime.datetime.now().hour, minutes=datetime.datetime.now().minute)
    
    return temp


# defines if process has been up over midnight
def is_midnight(current: datetime.timedelta, end: datetime.timedelta):
    end = datetime.timedelta(days=1, hours=8, minutes=00)
    spooky_hour = datetime.timedelta(hours=0,minutes=0, seconds=0)
    limit_daytime = end - datetime.timedelta(days=end.days)

    # current = datetime.timedelta(hours=4, minutes=43,seconds=12)

    if spooky_hour < current < limit_daytime:
        return True
    else:
        return False


if __name__ == "__main__":

    start = datetime.timedelta(hours=21, minutes=59)
    # end = datetime.timedelta(days=1, hours=8, minutes=00)
    end = datetime.timedelta(hours=22, minutes=00)

    print("\n\n\n")
    print(f"start : {start}")
    print(f"end   : {end}")
    print(f"now   : {get_time(False)}")

    print("\n")

    # MIDNIGHT
    midnight: bool = is_midnight(get_time(False), end)
    print(f"midnight: {midnight}")

    current_time = get_time(midnight)
    print(current_time)
    print("\n\n\n")

    num = 0
    cycle_range = 1100

    while True:
        time.sleep(0.5)
        now = get_time(midnight)
        midnight = is_midnight(now, end)

        if  now >= end:
            print(f"end   : {end}")
            print(f"now   : {now}")
            print("close")
            break

        if now >= start:
            while num < cycle_range and now >= start:  # WHILE 2
                if now >= end:
                    break

                time.sleep(0.5)
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
                now = get_time(midnight)
                midnight = is_midnight(now, end)
