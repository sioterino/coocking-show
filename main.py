import pyautogui
import time

# rpa error safe
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

# emails !!!
emails = [
    "logan.shadowknight12@gmail.com", "mia.cyberwolf34@gmail.com", "jack.pixelrider56@gmail.com",
    "chloe.dragonborn78@gmail.com", "liam.mysticfox90@gmail.com", "ava.gamerx01@gmail.com",
    "ben.shadowhunter23@gmail.com", "olivia.pixelwizard45@gmail.com", "lucas.cyberknight67@gmail.com",
    "ethan.starlight89@gmail.com", "emma.ninja12@gmail.com", "zoe.dragonheart34@gmail.com",
    "james.arcadeking56@gmail.com", "sophia.cybersamurai78@gmail.com", "noah.moonlight90@gmail.com",
    "lily.gamerfox01@gmail.com", "jack.shadowknight23@gmail.com", "amelia.pixelrider45@gmail.com",
    "logan.cyberwolf67@gmail.com", "grace.dragonborn89@gmail.com", "liam.mysticfox12@gmail.com",
    "mia.gamerx34@gmail.com", "nathan.shadowhunter56@gmail.com", "olivia.pixelwizard78@gmail.com",
    "ethan.cyberknight90@gmail.com", "zoe.starlight01@gmail.com", "lucas.ninja23@gmail.com",
    "emma.dragonheart45@gmail.com", "logan.arcadeking67@gmail.com", "chloe.cybersamurai89@gmail.com",
    "ben.moonlight12@gmail.com", "amelia.gamerfox34@gmail.com", "james.shadowknight56@gmail.com",
    "sophia.pixelrider78@gmail.com", "jack.cyberwolf90@gmail.com", "lily.dragonborn01@gmail.com",
    "noah.mysticfox23@gmail.com", "logan.gamerx45@gmail.com", "mia.shadowhunter67@gmail.com",
    "liam.pixelwizard89@gmail.com", "grace.cyberknight12@gmail.com", "ethan.starlight34@gmail.com",
    "zoe.ninja56@gmail.com", "lucas.dragonheart78@gmail.com", "ben.arcadeking90@gmail.com",
    "chloe.cybersamurai01@gmail.com", "amelia.moonlight23@gmail.com", "dylan.shadowrider234@gmail.com"
    "lily.gamerx123@gmail.com", "logan.shadowhunter567@gmail.com", "ava.pixelmage890@gmail.com",
    "noah.dragonheart456@gmail.com", "mia.cyberwolf321@gmail.com", "james.nightslayer789@gmail.com",
    "zoe.firestorm234@gmail.com", "liam.arcadeking098@gmail.com", "sophia.pixelrider567@gmail.com",
    "emma.shadowknight432@gmail.com", "lucas.darkshadow654@gmail.com", "chloe.mysticflame987@gmail.com",
    "ben.pixelwizard213@gmail.com", "olivia.blaze123@gmail.com", "ethan.cyberwolf789@gmail.com",
    "grace.moonlightfox432@gmail.com", "jack.pixelwarrior098@gmail.com", "amelia.starlight567@gmail.com",
    "nathan.ninja890@gmail.com", "lily.shadowhunter234@gmail.com", "joshua.arcadequeen456@gmail.com",
    "hannah.cybersamurai789@gmail.com", "mason.warlock567@gmail.com", "ella.zeldafan123@gmail.com",
    "william.phantom456@gmail.com", "ava.dragonborn890@gmail.com", "logan.ninja567@gmail.com",
    "mia.stormchaser234@gmail.com", "daniel.darkphoenix789@gmail.com", "sophia.pixelwizard098@gmail.com",
    "nathan.gamerx123@gmail.com", "lily.cyberknight567@gmail.com", "oliver.mysticwolf890@gmail.com",
    "grace.shadowhunter234@gmail.com", "ethan.arcadeking456@gmail.com", "harper.pixelwarrior789@gmail.com",
    "zoe.dragonmaster123@gmail.com", "james.nightslayer456@gmail.com", "emma.firestorm789@gmail.com",
    "lucas.cyberwolf567@gmail.com", "ava.shadowknight098@gmail.com", "noah.pixelrider234@gmail.com",
    "amelia.dragonheart789@gmail.com", "jack.moonlight567@gmail.com", "chloe.cybersamurai890@gmail.com",
    "ben.arcadehero123@gmail.com", "olivia.stormborn456@gmail.com", "logan.gamerfox789@gmail.com",
    "sarah.mysticflame123@gmail.com", "lucas.dragonheart789@gmail.com", "ben.arcadeking234@gmail.com",
    "chloe.cybersamurai567@gmail.com", "amelia.moonlight123@gmail.com"
]

number: int = 0

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


# static public void main
if __name__ == '__main__':

    set_conditions()
    # sets up browser
    open_chrome()
    sleep(1)
    open_ema()
    sleep(23)

    # votes for every email
    while number < len(emails):
        print(f"vote cycle: {number}")
        log_out()
        sleep(2)
        vote_best_new()
        vote_push()
        sleep(1)
        vote_kpop()
        number = number + 1

    close_chrome()
