import datetime
import pyautogui
import time

# rpa error safe
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

# emails !!!
# 00:24 >> 5:32
emails_300 = [
    "Alexei.Aurora53728@gmail.com", "Alexei.Beetlejuice16320@gmail.com", "Alexei.Cupid78759@yahoo.com", "Alexei.Daemon22184@hotmail.com", "Alexei.Kraken1380@naver.com", "Alexei.Nebula70761@gmail.com",
    "Amina.Artemis35936@gmail.com", "Amina.Aries16019@naver.com", "Amina.Berserk14185@yahoo.com", "Amina.Cupid26311@naver.com", "Amina.Hera5498@gmail.com", "Amina.Kraken81829@hotmail.com",
    "Anya.Beetlejuice4861@yahoo.com", "Anya.Draco69579@hotmail.com", "Anya.Eclipse8654@gmail.com", "Anya.Kraken44114@gmail.com", "Anya.Merlin32027@naver.com", "Anya.Sphinx59057@yahoo.com",
    "Arjun.Aries71176@naver.com", "Arjun.Beetlejuice69643@naver.com", "Arjun.Daemon12476@hotmail.com", "Arjun.Merlin5075@gmail.com", "Arjun.Ragnarok33967@yahoo.com", "Arjun.Titan45443@yahoo.com",
    "Carlos.Beetlejuice3183@gmail.com", "Carlos.Draco56172@gmail.com", "Carlos.Hera38057@hotmail.com", "Carlos.Kraken2499@yahoo.com", "Carlos.Neo92976@yahoo.com", "Carlos.Voyager76308@gmail.com",
    "Chen.Aries3946@naver.com", "Chen.Astro74219@gmail.com", "Chen.Daemon13652@naver.com", "Chen.Eclipse68199@yahoo.com", "Chen.Valkyrie11422@naver.com", "Chen.Voyager30948@yahoo.com",
    "Diego.Artemis17984@naver.com", "Diego.Cupid8532@yahoo.com", "Diego.Hera84157@naver.com", "Diego.Pegasus37854@gmail.com", "Diego.Phoenix25753@yahoo.com", "Diego.Titan21490@gmail.com",
    "Dmitri.Aries59783@gmail.com", "Dmitri.Astro27269@naver.com", "Dmitri.Cupid3765@yahoo.com", "Dmitri.Kraken38710@gmail.com", "Dmitri.Polaris47428@naver.com", "Dmitri.Stardust34725@yahoo.com",
    "Elena.Berserk36108@yahoo.com", "Elena.Neo6296@gmail.com", "Elena.Thanos24897@naver.com", "Elena.Titan47621@gmail.com", "Elena.Voyager14489@gmail.com", "Elena.Zeus36549@hotmail.com",
    "Francesca.Cupid35407@hotmail.com", "Francesca.Eclipse2326@gmail.com", "Francesca.Polaris48126@naver.com", "Francesca.Throne29508@gmail.com", "Francesca.Valkyrie96721@yahoo.com", "Francesca.Zeus5986@gmail.com",
    "Giulia.Aries84769@yahoo.com", "Giulia.Astro39738@hotmail.com", "Giulia.Merlin5832@gmail.com", "Giulia.Phoenix79432@yahoo.com", "Giulia.Stardust22347@hotmail.com", "Giulia.Zeus3299@gmail.com",
    "Hana.Artemis9528@gmail.com", "Hana.Cupid44122@gmail.com", "Hana.Nebula21744@yahoo.com", "Hana.Polaris53649@gmail.com", "Hana.Ragnarok13872@hotmail.com", "Hana.Sphinx76413@yahoo.com",
    "Ivan.Aries11083@gmail.com", "Ivan.Cupid38261@gmail.com", "Ivan.Draco9849@yahoo.com", "Ivan.Polaris18905@naver.com", "Ivan.Ragnarok56483@gmail.com", "Ivan.Titan38226@hotmail.com",
    "John.Astro67390@naver.com", "John.Daemon15870@gmail.com", "John.Hera49153@yahoo.com", "John.Polaris23192@gmail.com", "John.Stardust54107@hotmail.com", "John.Valkyrie70491@yahoo.com",
    "Lea.Cupid49267@gmail.com", "Lea.Hera94380@hotmail.com", "Lea.Kraken71283@gmail.com", "Lea.Polaris85762@naver.com", "Lea.Titan35649@yahoo.com", "Lea.Zeus2371@hotmail.com",
    "Liam.Aries64153@gmail.com", "Liam.Beetlejuice53206@naver.com", "Liam.Cupid51704@yahoo.com", "Liam.Daemon26741@gmail.com", "Liam.Ragnarok45630@hotmail.com", "Liam.Titan10392@naver.com",
    "Lucas.Astro4281@gmail.com", "Lucas.Cupid84926@yahoo.com", "Lucas.Hera94051@gmail.com", "Lucas.Phoenix56239@hotmail.com", "Lucas.Titan25184@gmail.com", "Lucas.Voyager14560@naver.com",
    "Mikhail.Berserk98364@yahoo.com", "Mikhail.Nebula74302@gmail.com", "Mikhail.Phoenix58932@yahoo.com", "Mikhail.Ragnarok2907@naver.com", "Mikhail.Titan13759@gmail.com", "Mikhail.Zeus6849@hotmail.com",
    "Nina.Artemis49812@gmail.com", "Nina.Eclipse5360@hotmail.com", "Nina.Polaris17453@naver.com", "Nina.Ragnarok69325@gmail.com", "Nina.Valkyrie82091@gmail.com", "Nina.Zeus46537@yahoo.com",
    "Sasha.Aries5014@gmail.com", "Sasha.Astro98510@hotmail.com", "Sasha.Eclipse19562@yahoo.com", "Sasha.Ragnarok45728@gmail.com", "Sasha.Titan19283@naver.com", "Sasha.Zeus56731@yahoo.com",
    "Viktor.Beetlejuice8904@gmail.com", "Viktor.Cupid70518@yahoo.com", "Viktor.Kraken34907@gmail.com", "Viktor.Nebula46520@gmail.com", "Viktor.Thanos38640@yahoo.com", "Viktor.Titan58790@hotmail.com",
    "Yuri.Aries13657@hotmail.com", "Yuri.Cupid78965@gmail.com", "Yuri.Kraken52407@yahoo.com", "Yuri.Merlin15083@gmail.com", "Yuri.Polaris28792@naver.com", "Yuri.Voyager47635@gmail.com",
    "Ivy.Beetlejuice5839@yahoo.com", "Ivy.Kraken21073@gmail.com", "Ivy.Merlin80754@naver.com", "Ivy.Throne36897@gmail.com", "Ivy.Titan71250@yahoo.com", "Ivy.Zeus9641@hotmail.com",
    "Leo.Aries58246@yahoo.com", "Leo.Berserk24179@gmail.com", "Leo.Phoenix43126@yahoo.com", "Leo.Sphinx9437@naver.com", "Leo.Voyager61802@gmail.com", "Leo.Zeus5703@hotmail.com",
    "Lorenzo.Astro9285@gmail.com", "Lorenzo.Eclipse51438@hotmail.com", "Lorenzo.Nebula16234@yahoo.com", "Lorenzo.Ragnarok30786@gmail.com", "Lorenzo.Valkyrie19284@gmail.com", "Lorenzo.Voyager15479@naver.com",
    "Amara.Cupid8571@gmail.com", "Amara.Hydra31247@yahoo.com", "Amara.Kraken96328@naver.com", "Amara.Mystic28495@hotmail.com", "Amara.Titan14208@gmail.com", "Amara.Valkyrie31785@yahoo.com",
    "Beatriz.Artemis98153@yahoo.com", "Beatriz.Cupid5172@gmail.com", "Beatriz.Nebula67430@gmail.com", "Beatriz.Pegasus32698@naver.com", "Beatriz.Phoenix14397@hotmail.com", "Beatriz.Voyager98026@gmail.com",
    "Boris.Beetlejuice17409@gmail.com", "Boris.Daemon24658@yahoo.com", "Boris.Merlin93756@hotmail.com", "Boris.Polaris14697@gmail.com", "Boris.Titan53814@naver.com", "Boris.Zeus78942@yahoo.com",
    "Clara.Artemis21846@gmail.com", "Clara.Cupid4362@yahoo.com", "Clara.Hydra32597@naver.com", "Clara.Mystic18745@gmail.com", "Clara.Sphinx65974@gmail.com", "Clara.Voyager58316@hotmail.com",
    "Dante.Aries73502@gmail.com", "Dante.Cupid84679@naver.com", "Dante.Merlin12507@yahoo.com", "Dante.Stardust1748@hotmail.com", "Dante.Thanos38716@gmail.com", "Dante.Zeus64298@naver.com",
    "Diana.Aries9472@yahoo.com", "Diana.Cupid32698@hotmail.com", "Diana.Mystic81475@gmail.com", "Diana.Ragnarok15307@yahoo.com", "Diana.Titan47263@gmail.com", "Diana.Voyager69582@naver.com",
    "Elijah.Beetlejuice37906@gmail.com", "Elijah.Cupid16432@hotmail.com", "Elijah.Kraken78591@yahoo.com", "Elijah.Polaris2937@gmail.com", "Elijah.Valkyrie50728@naver.com", "Elijah.Zeus12794@yahoo.com",
    "Evan.Aries6203@gmail.com", "Evan.Draco47561@naver.com", "Evan.Merlin75824@yahoo.com", "Evan.Phoenix29730@gmail.com", "Evan.Titan5869@hotmail.com", "Evan.Voyager34812@gmail.com",
    "Gabriel.Artemis31098@gmail.com", "Gabriel.Cupid58264@yahoo.com", "Gabriel.Hydra20347@gmail.com", "Gabriel.Kraken47186@hotmail.com", "Gabriel.Ragnarok5198@naver.com", "Gabriel.Sphinx28076@gmail.com",
    "Hugo.Aries37402@naver.com", "Hugo.Cupid27891@gmail.com", "Hugo.Merlin96038@gmail.com", "Hugo.Ragnarok15734@hotmail.com", "Hugo.Valkyrie32809@yahoo.com", "Hugo.Voyager64751@gmail.com",
    "Ines.Cupid19237@hotmail.com", "Ines.Hydra58293@gmail.com", "Ines.Phoenix9741@yahoo.com", "Ines.Ragnarok34028@naver.com", "Ines.Sphinx67125@gmail.com", "Ines.Titan42986@gmail.com",
    "Irene.Artemis49506@yahoo.com", "Irene.Cupid32409@gmail.com", "Irene.Mystic10758@gmail.com", "Irene.Ragnarok8763@naver.com", "Irene.Stardust43297@hotmail.com", "Irene.Titan13829@yahoo.com",
    "Joan.Aries57468@gmail.com", "Joan.Daemon8391@naver.com", "Joan.Hydra29784@hotmail.com", "Joan.Phoenix96142@gmail.com", "Joan.Sphinx18035@yahoo.com", "Joan.Zeus36421@gmail.com",
    "Jonas.Beetlejuice84217@yahoo.com", "Jonas.Cupid16230@hotmail.com", "Jonas.Mystic4908@gmail.com", "Jonas.Ragnarok23619@naver.com", "Jonas.Titan98764@gmail.com", "Jonas.Voyager61572@yahoo.com",
    "Kaleb.Artemis3802@gmail.com", "Kaleb.Draco15896@naver.com", "Kaleb.Kraken4739@hotmail.com", "Kaleb.Mystic28794@gmail.com", "Kaleb.Phoenix76853@gmail.com", "Kaleb.Valkyrie91427@yahoo.com",
    "Larissa.Beetlejuice9305@naver.com", "Larissa.Daemon1758@gmail.com", "Larissa.Hydra78294@yahoo.com", "Larissa.Ragnarok41983@gmail.com", "Larissa.Sphinx52768@hotmail.com", "Larissa.Titan62479@gmail.com",
    "Livia.Artemis1843@gmail.com", "Livia.Cupid67854@yahoo.com", "Livia.Nebula52138@hotmail.com", "Livia.Polaris6837@gmail.com", "Livia.Stardust90276@naver.com", "Livia.Zeus41739@gmail.com",
    "Lucas.Aries63709@naver.com", "Lucas.Cupid58341@gmail.com", "Lucas.Kraken27019@gmail.com", "Lucas.Polaris83765@yahoo.com", "Lucas.Sphinx10234@gmail.com", "Lucas.Valkyrie74358@gmail.com",
    "Maeve.Artemis57438@yahoo.com", "Maeve.Draco24986@gmail.com", "Maeve.Mystic96437@hotmail.com", "Maeve.Pegasus6321@gmail.com", "Maeve.Ragnarok8742@naver.com", "Maeve.Voyager52098@yahoo.com",
    "Marco.Aries40851@gmail.com", "Marco.Cupid29345@naver.com", "Marco.Merlin75028@gmail.com", "Marco.Phoenix48263@hotmail.com", "Marco.Sphinx63047@gmail.com", "Marco.Zeus98236@yahoo.com",
    "Miguel.Beetlejuice40217@naver.com", "Miguel.Hera8496@yahoo.com", "Miguel.Nebula36574@gmail.com", "Miguel.Polaris7108@hotmail.com", "Miguel.Titan48639@gmail.com", "Miguel.Voyager93057@gmail.com",
    "Olga.Artemis62730@yahoo.com", "Olga.Cupid34850@gmail.com", "Olga.Mystic96047@gmail.com", "Olga.Pegasus57834@hotmail.com", "Olga.Sphinx24085@gmail.com", "Olga.Valkyrie57302@naver.com",
    "Rafael.Beetlejuice31049@gmail.com", "Rafael.Draco48760@naver.com", "Rafael.Hydra26987@yahoo.com", "Rafael.Polaris6134@gmail.com", "Rafael.Titan89764@hotmail.com", "Rafael.Zeus5301@gmail.com",
    "Sofia.Aries46729@gmail.com", "Sofia.Cupid10576@naver.com", "Sofia.Hydra86093@gmail.com", "Sofia.Ragnarok4927@yahoo.com", "Sofia.Sphinx30786@gmail.com", "Sofia.Valkyrie58904@hotmail.com",
    "Thiago.Beetlejuice7038@gmail.com", "Thiago.Draco2189@hotmail.com", "Thiago.Hydra43702@yahoo.com", "Thiago.Phoenix97135@gmail.com", "Thiago.Stardust6948@naver.com", "Thiago.Zeus32810@gmail.com"
]


# 07:07 >> 08:08
emails_60 = [
    "Adrian.Apollo3874@gmail.com", "Adrian.Hydra29763@naver.com", "Adrian.Mystic47058@yahoo.com", "Adrian.Titan12347@gmail.com", "Adrian.Valkyrie82409@hotmail.com", "Adrian.Zeus58312@yahoo.com",
    "Alice.Cupid10984@gmail.com", "Alice.Kraken57263@yahoo.com", "Alice.Merlin23890@naver.com", "Alice.Phoenix91634@hotmail.com", "Alice.Sphinx43902@gmail.com", "Alice.Voyager57820@yahoo.com",
    "Bernard.Apollo31097@naver.com", "Bernard.Hydra89317@gmail.com", "Bernard.Mystic14620@hotmail.com", "Bernard.Titan9243@gmail.com", "Bernard.Valkyrie50784@yahoo.com", "Bernard.Zeus63028@gmail.com",
    "Camila.Aries45803@gmail.com", "Camila.Cupid7316@yahoo.com", "Camila.Hydra26048@hotmail.com", "Camila.Mystic94570@naver.com", "Camila.Polaris3629@gmail.com", "Camila.Sphinx80327@gmail.com",
    "Darius.Beetlejuice3287@hotmail.com", "Darius.Cupid50198@gmail.com", "Darius.Mystic74903@naver.com", "Darius.Polaris15942@yahoo.com", "Darius.Stardust93047@gmail.com", "Darius.Zeus82076@gmail.com",
    "Elsa.Apollo7352@gmail.com", "Elsa.Cupid12839@naver.com", "Elsa.Mystic59084@yahoo.com", "Elsa.Phoenix40231@gmail.com", "Elsa.Sphinx28714@hotmail.com", "Elsa.Valkyrie90326@gmail.com",
    "Finn.Aries1489@hotmail.com", "Finn.Cupid68437@gmail.com", "Finn.Daemon27963@yahoo.com", "Finn.Phoenix10384@gmail.com", "Finn.Stardust32847@naver.com", "Finn.Voyager57106@gmail.com",
    "Hana.Apollo59123@yahoo.com", "Hana.Cupid67458@gmail.com", "Hana.Mystic73809@naver.com", "Hana.Phoenix43691@hotmail.com", "Hana.Sphinx20573@gmail.com", "Hana.Titan31864@gmail.com",
    "Isaac.Artemis20457@gmail.com", "Isaac.Hydra59372@yahoo.com", "Isaac.Kraken10846@gmail.com", "Isaac.Polaris76034@hotmail.com", "Isaac.Sphinx18347@naver.com", "Isaac.Zeus49358@gmail.com",
    "Mira.Aries18436@gmail.com", "Mira.Daemon24791@naver.com", "Mira.Hydra69853@yahoo.com", "Mira.Mystic10387@gmail.com", "Mira.Polaris48509@hotmail.com", "Mira.Zeus76534@gmail.com"
]


# xx:xx >> xx:xx
emails = [
    "aaron.pixelwizard342@gmail.com", "emma.shadowknight564@gmail.com", "noah.arcadehero129@gmail.com",
    "mia.cybermage784@gmail.com", "james.starlight562@gmail.com", "sophia.dragonflame230@gmail.com",
    "zoe.nightslayer892@gmail.com", "jack.pixelmaster456@gmail.com", "lily.mysticfox621@gmail.com",
    "logan.dragonheart135@gmail.com", "chloe.cyberwolf249@gmail.com", "liam.shadowhunter478@gmail.com",
    "ethan.gamerwizard953@gmail.com", "emma.ninjafox315@gmail.com", "ben.stormbringer168@gmail.com",
    "ava.pixelrider542@gmail.com", "lucas.moonlight378@gmail.com", "grace.arcadeking490@gmail.com",
    "harper.cybersorcerer741@gmail.com", "sophia.dragonlord236@gmail.com", "will.shadowmage253@gmail.com",
    "amelia.gamerfox198@gmail.com", "nathan.nightblade314@gmail.com", "zoe.cyberninja267@gmail.com",
    "logan.firestorm521@gmail.com", "mia.mysticrider672@gmail.com", "ethan.pixelknight730@gmail.com",
    "grace.dragonfire143@gmail.com", "liam.nightprowler684@gmail.com", "chloe.cyberfox981@gmail.com",
    "emma.pixelwizard429@gmail.com", "joshua.gamerlord675@gmail.com", "amelia.shadowblade298@gmail.com",
    "noah.arcademaster453@gmail.com", "mia.moonlight269@gmail.com", "olivia.nightsorcerer781@gmail.com"
]

number: int = 9
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
    time: str = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
    print(f"user voting: {choice} TIME: {time}")
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

    # voting starts at:
    start: int = 1521
    # voting ends at:
    end: int = 1526

    while True: # WHILE 1
        # variable now changes every 1 second
        time.sleep(1)
        now: int = int(datetime.datetime.now().strftime('%H%M'))

        # if now is the voting start period you vote
        if now >= start:
            start_broser(security_time=23)
            # while numbers of voters is lesser then the number of usable emails
            while number < cycle_range: # WHILE 2
                # if it is not 1/4, you vote
                if number % 25 != 0:
                    user_votes(number=number)
                # end of IF
                else: # if it is a quarter you open chrome
                    if number != 0:
                        close_chrome()
                        print(f"close chrome: {number}")
                    # end of IF
                    start_broser(security_time=23)
                    user_votes(number=number)
                # end of ELSE

                # increment by one
                number = number + 1
                # end test to see if the time's up
                now: int = int(datetime.datetime.now().strftime('%H%M'))
                if now >= end:
                    # if time's up, you break out of the loop
                    break
                # end og IF
            # end of WHILE 2
        # end of IF

        if now >= end:
            # if time's up, you break out of the loop
            # ends voting
            close_chrome()
            alert(seconds=0)
            break
        # end og IF
    # end of WHILE 1

