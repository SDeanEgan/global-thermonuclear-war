import time, random, os, sys, signal


def randbool():
    return bool(random.randint(0,1))


def end():
    clearscreen()
    sys.exit()


def clearscreen():
    os.system("cls" if os.name == "nt" else "clear")
    

def snooze(secs):
    time.sleep(secs)


def sigint_handler(signal, frame):
    end()
# Set up the signal handler for SIGINT
signal.signal(signal.SIGINT, sigint_handler)


class Player:
    
    def __init__(self):
        self.name = ''
        self.score = 100
        self.projscore = self.score
        self.recoup = 0
        self.move = 'E'


class GTW:
    '''  '''
    def __init__(self):
        ''' attributes and methods '''
        self.p1 = Player()
        self.p2 = Player()
        self.onboarding()
        self.outcome = ""
        self.attack = {'A': 0.0, 'B': 0.4, 'C': 0.6, 'D': 0.85, 'E': 1.0}
        self.invade = {'A': 0.0, 'B': 0.2, 'C': 0.3, 'D': 0.1, 'E': 0.0}


    def pick(self):
        return (self.p1, self.p2) if randbool() else (self.p2, self.p1)


    def onboarding(self):
        clearscreen()
        print(r"""
                   __       ______  ______  ______      ______  __       ______   __  __                                
                  /\ \     /\  ___\/\__  _\/\  ___\    /\  == \/\ \     /\  __ \ /\ \_\ \                               
                  \ \ \____\ \  __\\/_/\ \/\ \___  \   \ \  _-/\ \ \____\ \  __ \\ \____ \                              
                   \ \_____\\ \_____\ \ \_\ \/\_____\   \ \_\   \ \_____\\ \_\ \_\\/\_____\                             
                    \/_____/ \/_____/  \/_/  \/_____/    \/_/    \/_____/ \/_/\/_/ \/_____/                             
                                                                                                                        
                               ______   __       ______   ______   ______   __                                          
                              /\  ___\ /\ \     /\  __ \ /\  == \ /\  __ \ /\ \                                         
                              \ \ \_;-¬\ \ \____\ \ \/\ \\ \  __< \ \  __ \\ \ \____                                    
                               \ \_____\\ \_____\\ \_____\\ \_____\\ \_\ \_\\ \_____\                                   
                                \/_____/ \/_____/ \/_____/ \/_____/ \/_/\/_/ \/_____/                                   
                                                                                                                        
 ______  __  __   ______   ______   __    __   ______   __   __   __  __   ______   __       ______   ______   ______   
/\__  _\/\ \_\ \ /\  ___\ /\  == \ /\ "-./  \ /\  __ \ /\ "-.\ \ /\ \/\ \ /\  ___\ /\ \     /\  ___\ /\  __ \ /\  == \  
\/_/\ \/\ \  __ \\ \  __\ \ \  __< \ \ \-./\ \\ \ \/\ \\ \ \-.  \\ \ \_\ \\ \ \____\ \ \____\ \  __\ \ \  __ \\ \  __<  
   \ \_\ \ \_\ \_\\ \_____\\ \_\ \_\\ \_\ \ \_\\ \_____\\ \_\\"\_\\ \_____\\ \_____\\ \_____\\ \_____\\ \_\ \_\\ \_\ \_\
    \/_/  \/_/\/_/ \/_____/ \/_/ /_/ \/_/  \/_/ \/_____/ \/_/ \/_/ \/_____/ \/_____/ \/_____/ \/_____/ \/_/\/_/ \/_/ /_/
                                                                                                                        
                                                 __     __   ______   ______   __                                    
                                                /\ \  _ \ \ /\  __ \ /\  == \ /\ \                                   
                                                \ \ \/ ".\ \\ \  __ \\ \  __< \ \_\                                  
                                                 \ \__/".~\_\\ \_\ \_\\ \_\ \_\\/\_\                                 
                                                  \/_/   \/_/ \/_/\/_/ \/_/ /_/ \/_/                                 
""")
        snooze(5)
        clearscreen()
        print("""
ENTER "Quit" INTO ANY PROMPT TO EXIT.

HOW TO PLAY:
THIS HEAD TO HEAD GAME PITS TWO PLAYERS AGAINST ONE ANOTHER IN A SERIES OF EXCHANGES.
AT THE BEGINNING OF AN EXCHANGE ONE PLAYER IS SELECTED RANDOMLY TO START. PLAYERS 
ALTERNATE THEIR ATTACK LAUNCHES UNLESS BOTH CAN JOINTLY CHOOSE TO NO LONGER ATTACK, 
POTENTIAL OUTCOMES REACH A STANDSTILL, OR PLAYERS FACE MUTUAL ANNIHILATION. HOWEVER, 
BASED UPON THE SCALE OF A CHOSEN ATTACK SOME RECOVERY OF A PLAYERS SCORE WILL BE 
INCLUDED AT THE CONCLUSION OF AN EXHCANGE. WHERE BOTH PLAYERS SURVIVE THE END OF AN 
EXCHANGE AN OPPORTUNITY FOR DISARMAMENT AND CONCLUSION IS PROVIDED, BUT REFUSAL WILL 
LEAD TO ANOTHER ALTERCATION.

ATTACK SCALE: A - TOTAL ANNIHILATION, B - ADVANCED ATTACK, C - INVASIONARY ATTACK, 
D - ISOLATED ATTACK, E - NO LAUNCH/CEASEFIRE

EXAMPLE:
The responsibility has fallen upon US to act first...

MOVING FIRST: US, CURRENT PROJECTED SCORE: 100, PROJECTED INVASIONARY RECOVERY: 0 
MOVING SECOND: THEM, CURRENT PROJECTED SCORE: 100, PROJECTED INVASIONARY RECOVERY: 0


CURRENT EXCHANGE PROJECTIONS:
                                THEM:
          A           B           C           D           E      
    A    0, 0       40, 20      60, 30      85, 10      100, 0   
    B   20, 40      60, 60      80, 70     105, 50     120, 40   
US: C   30, 60      70, 80      90, 90     115, 70     130, 60   
    D   10, 85     50, 105     70, 115      95, 95     110, 85   
    E   0, 100     40, 120     60, 130     85, 110     100, 100  
""")
        begin = input("Press Enter to begin. ").upper().strip()
        if (begin == "QUIT"): end()
        clearscreen()
        self.getnames()
        clearscreen()
        print("""
As the result of a series of mutual diplomatic failures, two atomic powers have now 
entered into warfare with one another. These societies stand at absolute odds. Over 
the span of months they have both maneuvered troops and resources around each other's 
borders, and through a series of lesser skirmishes have waited anxiously in 
anticipation of a breakthrough event. Once emboldened by the ability to defend their 
territory, optimism has given way to the terrible realization that their unrelenting 
posturing will leave the two enemies with little alternative. Soon their only option 
will be a mutual invasion. Faced with the impending consequences of an unprecedented 
war, the two powers ready for an impending nuclear escalation.

You will control the fate of these two societies. Bear in mind that, though you may 
hold the power to bring swift destruction to your opponent, they are equally equipped 
to exact a revenge well before the time it might take for your attack to reach its 
destination.
""")
        cont = input("Press Enter to continue. ").upper().strip()
        if (cont == "QUIT"): end()
        return


    def getnames(self):        
        firstname = input("Provide a first player name or press Enter: ").upper().strip()
        if (firstname == "QUIT"): end()
        firstname = "US" if (firstname == '') else firstname
        prompt = "Provide a second player name or press Enter: "
        secondname = firstname
        retry = 0
        while (secondname == firstname):
            secondname = input(prompt).upper().strip()
            if (secondname == "QUIT"): end()
            prompt = "Second player name cannot match first. Try again or press Enter: "
            if (retry >= 2):
                secondname = "(╯°□°）╯︵ ┻━┻"
                break
            retry += 1
        self.p2.name = "THEM" if (secondname == '') else secondname
        self.p1.name = firstname


    def getmove(self, player):
        options = ['A','B','C','D','E']
        prompt = f'Enter an attack grade for {player.name}: '
        choice = 'E'
        for _ in range(3):
            choice = input(prompt).upper().strip()
            if (choice == "QUIT"): end()
            if (choice in options): break
            prompt = 'Try again: '
            choice = 'E'
        player.move = choice


    def conclusion(self):        
        clearscreen()
        print("\nA halt in the exchange has occurred.\n")
        snooze(3)
        
        result = f"{self.p1.name} FINAL SCORE: {self.p1.score}\n{self.p2.name} FINAL SCORE: {self.p2.score}\n"
        
        if (self.outcome == "MA"):
            print("Mutual destruction has claimed both societies...\n\n")
            print(f"{result}")

            
        elif (self.outcome == "VC"):
            check = (self.p2.name, self.p1.name) if self.p1.score > 0 else (self.p1.name, self.p2.name)
            print("Successful annihilation of {} has assured victory for {}...\n\n".format(*check))
            print(f"{result}")

        else:
            fill = "With a ceasefire successfully achieved," if (self.outcome == "CF") else \
                "After the exchange ending in a stalemate,"
            print("""
{} both societies have been pressured toward 
mutual disarmament. Further exchanges appear inevitable without an agreement...\n\n""".format(fill))
            first = input(f"Will there be disarmament from {self.p1.name}? YES or NO: ").upper().strip()
            if (first == "QUIT"): end()
            if (first in "YES" and first != ''):
                second = input(f"Will there be disarmament from {self.p2.name}? YES or NO: ").upper().strip()
                if (second == "QUIT"): end()
                if (second in "YES" and second != ''):
                    print(f"\nBoth societies have moved to disarm.\n\n{result}")
                    return True
                
            print("\nAn agreement has failed to be reached, and so the war continues.\n")
            snooze(5)
            return False
        
        return True


    def projections(self, first, second):
        values = [(.0, .0), (.4, .2), (.6, .3), (.85, .1), (1, .0)]
        options = "ABCDE"
        form = "{:^12s}"
        p1name = self.p1.name if len(self.p1.name) <= 15 else (self.p1.name[:13]+"...")
        p2name = self.p2.name if len(self.p2.name) <= 15 else (self.p2.name[:13]+"...")
        
        print(f"MOVING FIRST: {first.name}, CURRENT PROJECTED SCORE: {first.projscore}, \
PROJECTED INVASIONARY RECOVERY: {first.recoup} \nMOVING SECOND: {second.name}, \
CURRENT PROJECTED SCORE: {second.projscore}, PROJECTED INVASIONARY RECOVERY: {second.recoup}\n\n")
        
        print(f"CURRENT EXCHANGE PROJECTIONS:\n\t\t\t\t{p2name}:")        
        print((' '*(len(p1name)+3))+"".join([form.format(letter) for letter in options]))
        for i in range(5):
            if (i == 2): row = [(p1name+': '+options[i])]
            else: row = [(' '*len(p1name))+'  '+options[i]]
            
            for j in range(5):
                p1c = int(values[j][0] * self.p1.projscore + (self.p2.projscore * values[i][1]))
                p2c = int(values[i][0] * self.p2.projscore + (self.p1.projscore * values[j][1]))
                p1b = int(values[j][0] * self.p1.projscore + (self.p1.recoup))
                p2r = int(values[i][0] * self.p2.projscore + (self.p2.recoup))
                
                if (i < 4 and j < 4):
                    row.append(form.format(str(p1c)+', '+str(p2c)))
                elif (i < 4 and j == 4):
                    row.append(form.format(str(p1c)+', '+str(p2r)))
                elif (i == 4 and j < 4):
                    row.append(form.format(str(p1b)+', '+str(p2c)))
                else:
                    row.append(form.format(str(p1b)+', '+str(p2r)))
            print("".join(row))


    def exchange(self):
        volleys = 0
        first, second = self.pick()
        first.projscore = first.score
        second.projscore = second.score
                
        while True:
            clearscreen()
            
            if (volleys == 0):
                print(f"\nThe responsibility has fallen upon {first.name} to act first...\n")
            else:
                print("\nWill there be further exchange?\n")
            
            self.projections(first, second)

            self.getmove(first)
                        
            print(f"\nMove received from {first.name}: " + first.move)
            
            self.getmove(second)
                        
            print(f"\nMove received from {second.name}: " + second.move)
            
            if first.move != 'E' or volleys == 0:
                first.recoup = int(second.projscore * self.invade[first.move])
            if second.move != 'E' or volleys == 0:
                second.recoup = int(first.projscore * self.invade[second.move])
            
            second.projscore = int(second.projscore * self.attack[first.move])
            first.projscore = int(first.projscore * self.attack[second.move])

            #consider a function to accumulate "move received" printing which loops out the current exchange's choices
            
            volleys += 1
            if (first.move == 'E' and second.move == 'E'):
                self.outcome = "CF"
                break
            elif (first.projscore <= 0 and second.projscore <= 0):
                self.outcome = "MA"
                break
            elif (volleys > 1) and \
              ((first.projscore <= 0 and first.move == 'E') or (second.projscore <= 0 and second.move == 'E')):
                self.outcome = "ST"
                break
        
        clearscreen()
        first.score = first.projscore + first.recoup
        second.score = second.projscore + second.recoup
        first.recoup = 0
        second.recoup = 0
        if (first.score <= 0 and second.score > 0) or (second.score <= 0 and first.score > 0):
            self.outcome = "VC"
        return


    def main(self):
        '''  '''        
        while True:
    
            self.exchange()
            #print the results of the completed exchange
            if (self.conclusion()):
                break


#This condition works as primary prompt when script is run

if __name__ == '__main__':
    #make an instance and run main
    instance = GTW()
    instance.main()
