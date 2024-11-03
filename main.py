import pyautogui
import time

# rpa error safe
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

# emails !!!


number: int = 0
cycle_range: int = len(emails)

# alert for debugging purposes
def alert(seconds: int):
    for i in range(seconds):
        print(i + 1)
        sleep(1)
    pyautogui.alert("alerting you!")


# i get lazy, dont wanna write time.sleep(x)
def sleep(seconds: int):
    time.sleep(seconds)


# minimizes pycharm
def set_conditions():
    sleep(1)
    pyautogui.click(x=1803, y=15)
    pyautogui.moveTo(x=997, y=569)

# opening google chrome
def open_chrome():
    pyautogui.press('win')
    pyautogui.write("chrome", interval=.05)
    pyautogui.press('enter')


# closes google chrome
def close_chrome():
    pyautogui.click(x=1894, y=8)


# opening emas voting site
def open_ema():
    pyautogui.write("https://www.mtvema.com/pt-br/vota/best-new", interval=.05)
    pyautogui.press('enter')


# logs out before each section
def log_out():
    pyautogui.scroll(-20000)
    pyautogui.scroll(-500)
    pyautogui.click(x=943, y=839)
    pyautogui.click(x=962, y=159)
    pyautogui.scroll(10000)


# logs in with a new user
def log_in():
    user = email(number, emails)
    pyautogui.click(x=876, y=269)
    pyautogui.write(user, interval=.05)
    pyautogui.click(x=955, y=319)


# decides user email
def email(cycle: int, mails):
    choice = mails[cycle]
    print(f"user voting: {choice}")
    return choice


# voting function
def vote(x_axis: int, y_axis: int):
    pyautogui.click(x=x_axis, y=y_axis, clicks=10, interval=0.1)
    pyautogui.click(x=870, y=245)


# vote lesserafim for best new artist
def vote_best_new():
    pyautogui.click(x=949, y=894)
    pyautogui.click(x=736, y=946)
    log_in()
    vote(737, 947)


# vote lesserafim for best push performance
def vote_push():
    pyautogui.scroll(-500)
    pyautogui.click(x=947, y=984)
    pyautogui.scroll(-500)
    vote(736, 857)


# vote lesserafim for best k-pop
def vote_kpop():
    pyautogui.scroll(-10000)
    pyautogui.click(x=959, y=341)
    vote(1265, 621)


# starts browser
def start_broser(security_time: int):
    set_conditions()
    # sets up browser
    open_chrome()
    sleep(1)
    open_ema()
    sleep(security_time)


# user votes
def user_votes(number: int):
    print(f"vote cycle: {number}")
    log_out()
    sleep(2)
    vote_best_new()
    vote_push()
    sleep(1)
    vote_kpop()


# static public void main
if __name__ == '__main__':

    # is it okay to start?
    alert(seconds=0)

    # iterates through all the emails
    while number < cycle_range:
        if number % 25 != 0:
        # if it is not 1/4, you vote
            user_votes(number=number)
        else:
        # if it is a quarter you open
            if number != 0:
                close_chrome()
                print(f"close chrome: {number}")
            start_broser(security_time=23)
            user_votes(number=number)
        # last, increment by one
        number = number + 1

    # ends voting
    close_chrome()
    alert(seconds=0)
