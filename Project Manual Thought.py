# -*- coding: utf-8 -*-
"""
Project Thought
"""
import webbrowser
import os
from random import randint
from threading import Timer

def thoughtChoice():
    '''
    Prompts user to choose between Manual and Automatic thought
    Sends the user to the correct thought program
    '''
    thought_cond = 1
    while thought_cond == 1:
        thought_choice = input("Choose Manual or Automatic Thought: ")
        if thought_choice.lower() == "manual":
            t_c = "M"
            thought_cond += 1
        elif thought_choice.lower() == "automatic":
            t_c = "A"
            thought_cond += 1
        elif thought_choice.lower() == "void":
            t_c = "V"
            thought_cond += 1
        else:
            print("Invalid Choice. Please choose Manual or Automatic")
    return t_c

def Automatic_Thought():
    print("Thank you for choosing Automatic Thought")
    rand_num = randint(1, 10)
    if rand_num == 1:
        webbrowser.open("https://www.youtube.com/watch?v=q2LughbIfyE")
        Timer(28, Force_Restart, ()).start()
    elif rand_num == 2:
        webbrowser.open("https://www.youtube.com/watch?v=erh2ngRZxs0")
        Timer(66, Force_Restart, ()).start()
    elif rand_num == 3:
        webbrowser.open("https://www.youtube.com/watch?v=axSnW-ygU5g")
        Timer(63, Force_Restart, ()).start()
    elif rand_num == 4:
        webbrowser.open("https://www.youtube.com/watch?v=O6rHeD5x2tI")
        Timer(61, Force_Restart, ()).start()
    elif rand_num == 5:
        webbrowser.open("https://www.youtube.com/watch?v=cUvUcHpQbZc")
        Timer(30, Force_Restart, ()).start()
    elif rand_num == 6:
        webbrowser.open("https://www.youtube.com/watch?v=OLHBAzAiFNk")
        Timer(8, Force_Restart, ()).start()
    elif rand_num == 7:
        webbrowser.open("https://www.youtube.com/watch?v=aKTROAPWvok")
        Timer(29, Force_Restart, ()).start()
    elif rand_num == 8:
        webbrowser.open("https://www.youtube.com/watch?v=_SGj9KdmzR4")
        Timer(31, Force_Restart, ()).start()
    elif rand_num == 9:
        webbrowser.open("https://www.youtube.com/watch?v=owGykVbfgUE")
        Timer(32, Force_Restart, ()).start()
    elif rand_num == 10:
        webbrowser.open("https://www.youtube.com/watch?v=2PU8ZxQj7eE")
        Timer(60, Force_Restart, ()).start()
        
def Void():
    print("Thank you for choosing VOID")
    Timer(5, print_void, ("1")).start()
    Timer(10, print_void, ("2")).start()
    Timer(12, Force_End, ()).start()    

def print_void(V_cond):
    if V_cond == "1":
        print("You have made the correct choice")
    elif V_cond == "2":
        print("GOODBYE")
        
def Manual_Thought(name):
    print("Thank you for choosing Manual Thought", name.upper())
    name_file = open('name_file','a+')
    name_file.write(" ")
    name_file.write(name)
    name_file.close()
    section_number = 0
    while section_number <= 4:
            manual_thought_guide(section_number)
            section_number += Continue_Check()
    Manual_Thought_Completion()

def manual_thought_guide(sec):
    if sec == 0:
        print("\n Manual Thought has begun \n")
        input("Press any key to continue: ")
        print("\n You are now breathing manually \n")
        input("Press any key to continue: ")
        print("\n You are now blinking manually \n")
        input("Press any key to continue: ")
        print('''                                                                                                     
                                                  `.-:::::.                                         
                                               `oyhhyyhyyyhs/`                                      
                                              /hdhsyhddhhyyyyyo`                                    
                                             odho:.......---.hho                                    
                                             hho-```        `oyy                                    
                                             ddo-`-::.` ...` +yy                                    
                                             shh--+osy.:oo+-`/hs`                                   
                                             /oh:..-:+-.:::. /y/-                                   
                                             .os/-`.:/.``   `/:-                                    
                                              -++:`.:/+:-    /:                                     
                                               -o:-:++o+-:`  /                                      
                                                /o:::++:.  .o.                                      
                                                `dso+:.``-:.+                                       
                                               -oh++sso/-.` o-                                      
                                             -+s:o+//+-`    /o`                                     
                                         .-::-.//:o:.:.``  -..+-.                                   
                                     `-:/-..`` `+-./.``-``-. -` `--.`                               
                                   -/:-..``     `/-`-::-.-` ..     `.--.                            
                                `:/-...`          -:``::-` -.         `.:-.                         
                               .o/..+-`            `:-:. `-`             `.+`                       
                               o.:-`+/`             `o:.`-                .:s                       
                              -+` -::/`             `+..-             :`.-../:                      
                              o.   //+`             `/  -             +.--.  o                      
                              s`   :o+.              :  -            `o...`  o                      
                             .+`   :ss.              :``.`           -/```   o                      
                             +-`   -ss.              :-.:           `+.``    +                      
                            `s``   `s+.              :  -          `/+`.:    +                      
                            :/```   +/.              :  -          `o/.:.    /`                     
                            s````   //`             `:..:        ` `s::-.    `+                     
                           `+``.`   .o``            `--.:.       ```s/.`-     o                     
                           +:`...`   o.`            `:  -`       ``-y-./o     +`                    
                          `y``.---`` /-`            `-  -        ``+o-/+---.` o`                    
                          :o``.::/:/:::``           `-``:        `.o+:/:-..`  y                     
                          .s.```````.++.`            :-.:        `-y:::-..`  :+                     
                           //``.....-s+-``          `-  :        `/s-:.   .  s`                     
                           `o```````.:y/..          .`  /       `.s/:.--. `..o`                     
                            s.`.`     /o/-``        ..:`:       `-s:-:.-:-`  /.                     
                            /+`..``   `ooo+:.`      --../     `--s+.`./:..  .+                      
                            `s-.-.`    -ysyo//:` ```+:../`  `-:/sy:-.``--  .+                       
                             `o:::.    ./hyssooo/+//+o//s/:/ossyh+--:.    -+                        
                               :o+/-.-+o+++:://+++/:/:::///+//oy+-. `:  `::                         
                             ``.+ho//os-```````//-//y+/-::--:+s+-.`  ` .:/-.`                       
                        ``-//+o+//yssy:....````-:--.``..-o-.```:/- `  ./   .-:-`                    
                     `-:/o+///-.....:o++//:::/:-///o++///-....--:y/:++/:::.   .-::.                 
                  `.//::o++++//:-........`...-:ys+////+so+++//+oooo:-----:o/`    `:/-`              
                `-/:-----.--/oyyo/:--...```.-::oysoossyyhsssssso++o++///+o+//       -/:`            
              `:/:..:://///+//+osyyso+/::-...`..:+s:/-``/o:---/o:...--:/+o+/s-.``   .`-+:           
             -+-`.:/:::++/:--.......-:/++oo+/:::---+-.:` `--`  `::`        `-::/-......-oo.         
            /:  ````.-.`                ``.:oyyso+//s-.:-   `...  .--``        `-:-.`...`.o-        
           /-     `-`                    `-:/+oyddhhhh+---.`         .`           `-:-  `  /:       
         `:s                        `.---...-:::/++ooydy+-.:/-.`                            s       
        :o/o.                   `.-----::/+++ooosyhhhyyyyyso+oso+/::--.````               `/-       
      `+ysoos:`   ``.-::://////++++++//+////////++++ooo+++///////+/+++ossoo+++/:-..``` ``-os.       
     -o/:/+oosys+////::::::--.............--:::////::::---------------:::/oo+//+oooooosoooooo.      
    :/-/+osoo/:----.----.....--------------::/::::---------:---------------:+o+///++///ossso+s-     
   `o-//::--------------------------::::/:/+////////+++++o+ooyosssssooooooooosyyssoooo+/+//+o++o`   
  -h++++++ooooooooooossooooooosssssyyyyyysyyyyysyyssoosoosssssssssssooooossyysssssssssyyyyysosshs   
  `:oddhyysssssssssooooooooooooooooosssssssyssssssssssssssssssssssssssssssssssssyysysssssssyyys+-   
      `:+oo++++ooooo+++o+++++++++++++++++++++++++/++++/++++++///////////////////+++/+/://::-`       
                                                                                                    
''')
        print("Please sit in the stance pictured above \n")
        input("Press any key to continue: ")
        print("\n Feel all three points of contact with the Earth \n")
        input("Press any key to continue: ")
        print("\n Let your muscles relax and let go of all tension you're carrying with you")
        input("Press any key to continue: ")
        print("\n As thoughts arise let them slowly fade away \n")        
        input("Press any key to continue: ")
        print("\n Let your thoughts return to your breathing \n")
        input("Press any key to continue: ")
        print("\n Breath slowly in... and slowly out \n")
        input("Press any key to continue: ")
        print("\n Focus your attention to a spot on the wall \n")
        input("Press any key to continue: ")
        print("\n Know that spot.. learn it.. love it.. hate it... \n")
        input("Press any key to continue: ")
        print("\n Manual Thought Stage 1 Complete \n")
    elif sec == 1:
        print("\n As you touch the keys, become aware of that feeling \n")
        input("Press any key to continue: ")
        print("\n Touch is just one of your senses \n")
        input("Press any key to continue: ")
        print("\n Focus now on your hearing \n")
        input("Press any key to continue: ")
        print("\n The silence of the room is a lie \n")
        input("Press any key to continue: ")
        print("\n Hear the small things.. the air conditioning.. shuffling of feet.. your blood roaring through your body \n")
        input("Press any key to continue: ")
        print("\n That blood roaring is proof you're alive \n")
        input("Press any key to continue: ")
        print("\n You can smell too \n")
        input("Press any key to continue: ")
        print("\n As you breath in through your nose try to pick out each scent \n")
        input("Press any key to continue: ")
        print("\n Is it the smell of paint, your own deodorant, wood, tile, etc. \n")
        input("Press any key to continue: ")
        print("\n You are experiencing life constantly \n")
        input("Press any key to continue: ")
        print("\n Don't get caught up in any one thing \n")
        input("Press any key to continue: ")
        print("\n Life can be overwhelming, take it one step at a time \n")
        input("Press any key to continue: ")
        print("\n Focus back on your breathing \n")
        input("Press any key to continue: ")
        print("\n Manual Thought Stage 2 Complete \n")
    elif sec == 2:
        print("\n Become aware of other people \n")
        input("Press any key to continue: ")
        print("\n You are not alone \n")
        input("Press any key to continue: ")
        print("\n I'm right there behind the screen \n")
        input("Press any key to continue: ")
        print("\n My life is just as complex as yours \n")
        input("Press any key to continue: ")
        print("\n A screen can muddle this fact \n")
        input("Press any key to continue: ")
        print("\n The screen is a lie \n")
        input("Press any key to continue: ")
        print("\n Other people are there and your actions are real \n")
        input("Press any key to continue: ")
        print("\n If you wanted to you could reach out and touch them \n")
        input("Press any key to continue: ")
        print("\n Knowing someone else is scary \n")
        input("Press any key to continue: ")
        print("\n Fear is a lie too \n")
        input("Press any key to continue: ")
        print("\n Forget fear for a moment \n")
        input("Press any key to continue: ")
        print("\n Think about how that makes you feel \n")
        input("Press any key to continue: ")
        print("\n Do you feel more free or less? \n")
        input("Press any key to continue: ")
        print("\n Manual Thought Stage 3 Complete \n")
    elif sec == 3:
        print("\n Become aware of yourself \n")
        input("Press any key to continue: ")
        print("\n You are not who you think you are \n")
        input("Press any key to continue: ")
        print("\n You are something altogether different \n")
        input("Press any key to continue: ")
        print("\n You are always changing \n")
        input("Press any key to continue: ")
        print("\n Nothing stays the same \n")
        input("Press any key to continue: ")
        print("\n Entropy increases inenvitably \n")
        input("Press any key to continue: ")
        print("\n Learn to accept this... embrace it... \n")
        input("Press any key to continue: ")
        print("\n To label me is to negate me \n")
        input("Press any key to continue: ")
        print("\n Thinking yourself to be one way is a trap \n")
        input("Press any key to continue: ")
        print("\n Thinking others to be one way is a trap \n")
        input("Press any key to continue: ")
        print("\n There is a great multiplicity inside us all \n")
        input("Press any key to continue: ")
        print("\n Life is so real it becomes fake, and so fake it becomes real \n")
        input("Press any key to continue: ")
        print("\n Focus now on your breath \n")
        input("Press any key to continue: ")
        print("\n Manual Thought Stage 4 Complete \n")
    elif sec == 4:
        print("\n Think now about death")
        Continue_Check()
        print("\n Think now about pain")
        Continue_Check()
        print("\n When did you last feel real pain?")
        Continue_Check()
        print("\n Do you wish to bury this pain?")
        Continue_Check()
        print("\n Do you wish to forget it?")
        Continue_Check()
        print("\n There is no good without the bad")
        Continue_Check()
        print("\n To live life without pain is to destroy any chance at its opposite")
        Continue_Check()
        print("\n Life is full of contradictions such as this")
        Continue_Check()
        print("\n Open yourself up to pain, to heartbreak, to love, to anything")
        Continue_Check()
        print("\n Do not fear though")
        Continue_Check()
        print("\n I will not fear")
        Continue_Check()
        print("\n Fear is the mind-killer")
        Continue_Check()
        print("\n Fear is the little death the brings total obliteration")
        Continue_Check()
        print("\n I will face my fear")
        Continue_Check()
        print("\n I will permit it to pass over me and through me.")
        Continue_Check()
        print("\n And when it has gone past I will turn the inner eye to see its path")
        Continue_Check()
        print("\n Where the fear has gone there will be nothing.")
        Continue_Check()
        print("\n Only I will remain. \n")
        input("Press any key to continue: ")
        print("\n Final Stage Complete \n")
 
def Manual_Thought_Completion():
    print("Thank you for participating in Manual Thought. Good Luck")
    webbrowser.open("https://www.youtube.com/watch?v=1Bix44C1EzY")
    Timer(23, Force_Restart, ()).start()

def Continue_Check():
    exit_cond = 1
    while exit_cond == 1:    
        cont_cond_1 = input("Would you like to proceed? y/n:  ")
        if cont_cond_1.lower() == "y":
            exit_cond += 1
            return 1
        elif cont_cond_1.lower() == "n":
            print("You cannot exit manual thought once it has begun")
            cont_cond_2 = input("Force Terminate? y/n: ")
            if cont_cond_2.lower() == "y":
                Force_Restart()
            elif cont_cond_2.lower() == "n":
                continue
            else:
                print("Invalid Choice.")
        else:
            print("Invalid Choice.")

def Force_Restart():
    os.system("shutdown /r /t 1")

def Force_End():
    os.system("shutdown /s /t 1")

def main():
    t_c_return = thoughtChoice()
    if t_c_return == "A":
        Automatic_Thought()
    elif t_c_return == "V":
        Void()
    elif t_c_return == "M":
        name = str(input("Please enter your name: "))
        Manual_Thought(name)
        
if __name__ == "__main__":
    main()