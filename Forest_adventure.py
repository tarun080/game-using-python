import sys
import time

a = 2
b = 0.2
c = 0.08

def intro1():
    time.sleep(a) 
    n = input('Will you continue the game(y/n): ')
    if n == 'y' or n == 'Y':
        time.sleep(a) 
        intro()
    else: 
        time.sleep(a)
        print('better next time')

def path_end1(): 
    time.sleep(a)
    print()
    print('You started running toward the forest')
    time.sleep(a)
    print()
    path_end2()

def path_end2():
    time.sleep(a)
    print()
    print('Scared and tired you run deep End of the forest the forest!!')
    time.sleep(a)
    print('After running this far you heard noise of water')
    time.sleep(a)
    s1 = ['Splash...', 'Splash...', 'Splash...']
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(1)
    print(end='')
    print()
    time.sleep(a)
    print('Following the sound you reach at the bottom end of waterfall')
    time.sleep(a)
    path_end3()

def path_end3():
    print()
    time.sleep(a)
    print('After refreshing yourself you saw something behind the waterfall')
    time.sleep(a)
    print('You noticed a Huge cave!!!')
    print()
    time.sleep(a)
    print('...There was a rumbling sound...')
    time.sleep(a)
    s1 = "Who are you?? and Why are you here"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print()
    time.sleep(a)
    s1 = '...I\'m Mario, I was looking for a way out of this forest...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print()
    time.sleep(a)
    s1 = 'This is the only way out of this Forest'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    s1 = 'For that you have to answer any one of my Riddles'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print()
    time.sleep(a)
    print('From out of nowhere there appear a screen with 5 buttons!!')
    print()
    time.sleep(a)
    s1 = '"Choose any one of them to answer"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    s1 = '"If you answer it wrong you will never leave this place"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    n = input('Which one will you choose(1/2/3/4/5): ')
    time.sleep(a)
    if n == '1': 
        print('You chose the first riddle')
        time.sleep(a)
        s5 = '"What is always in front of you but can’t be seen?"'
        for character in s5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        time.sleep(a)
        n = input('>>> ')
        if n.lower() == 'future':
            time.sleep(a) 
            path_end4()
        else:
            time.sleep(a)
            lost()
    elif n == '2': 
        print('You chose the second riddle')
        time.sleep(a)
        s5 = '" What walks on four legs in the morning, two legs at noon, and three legs in the evening?"'
        for character in s5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        time.sleep(a)
        n = input('>>> ')
        if n.lower() == 'man':
            time.sleep(a) 
            path_end4()
        else:
            time.sleep(a)
            lost()
    elif n == '3': 
        print('You chose the third riddle')
        time.sleep(a)
        s5 = '"What is easy to get into but hard to get out of?"'
        for character in s5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        time.sleep(a)
        n = input('>>> ')
        if n.lower() == 'trouble':
            time.sleep(a) 
            path_end4()
        else:
            time.sleep(a)
            lost()
    elif n == '4': 
        print('You chose the fourth riddle')
        time.sleep(a)
        s5 = '"What breaks and never falls"'
        for character in s5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        time.sleep(a)
        n = input('>>> ')
        if n.lower() == 'day':
            time.sleep(a) 
            path_end4()
        else:
            time.sleep(a)
            lost()
    elif n == '5': 
        print('You chose the fifth riddle')
        time.sleep(a)
        s5 = '"I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?"'
        for character in s5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        time.sleep(a)
        n = input('>>> ')
        if n.lower() == 'map':
            time.sleep(a) 
            path_end4()
        else:
            time.sleep(a)
            lost()

def lost():
    time.sleep(a) 
    print()
    s1 = '"Your answer is incorrect!!"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    s1 = '"Now you will stay here for etenity!!!"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print('Game over!!!')
    intro1()

def path_end4(): 
    time.sleep(a)
    print('...There was a rumbling noise...')
    time.sleep(a)
    print('...The cave began to open...')
    time.sleep(a)
    s1 = '"You gave the correct answer!!"'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    s1 = '"Now you are Free to leave...."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print()
    print()
    print('*************************************')
    s1 = "'Congragulations! You Won'"
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print('*************************************')
    print()
    print()

def intro():
    print()
    print("(EVERYTHING IS DARK)")
    time.sleep(a)
    print("You feel around, using your hands to see.")
    time.sleep(a)
    print("The ground is cold, damp, and covered in thick vines.")
    time.sleep(a)
    print("You feel a round rock that sinks into the floor when you press it.")
    time.sleep(a)
    print("The ground starts rumbling.")
    time.sleep(a)
    print("Light begins flooding in.")
    time.sleep(a) 
    question = '"I\'m in a cave...?"'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1.0)
    print()
    print()
    print("The rock released a boulder that was blocking the cave entrance.")
    time.sleep(a)
    print("Two paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Exit forward through the caves entrance, into the light.")
    time.sleep(a)
    print("Path #2: Climb down the vines into a bottomless hole in the ground.")
    time.sleep(a)
    print()
    firstPath = input("Which path will you choose? (1/2): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()


def path1():
    print("You exit forward through the cave's entrance, into the light.")
    time.sleep(a)
    print("It's incredibly bright but your vision adjusts as you continue.")
    time.sleep(a)
    print("The cave exit closes, there's no going back now.")
    time.sleep(a)
    print("You are on a incredible mountain.")
    time.sleep(a)
    print()
    s1 = 'Continuing your journey to the bottom of the mountain...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print("You see two paths ahead:")
    time.sleep(a)
    print("Path #1: Take the set path down the mountain to the plains.")
    time.sleep(a)
    print("Path #2: Scale down the side of the mountain to the deep forest.")
    time.sleep(a)
    print()
    secondPath = input("Which path will you choose? (1/2): ")
    if secondPath == '1':
        path1_1()
    elif secondPath == '2':
        path1_2()


def path1_1():
    print()
    print("You begin walking down the mountain toward the plains.")
    time.sleep(a)
    print("The path is long, winding and difficult.")
    time.sleep(a)
    print("The sky is bright and blue and a warm breeze hits your face.")
    time.sleep(a)
    s8 = '  "I could get used to this..."'
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself.')
    time.sleep(a)
    print("A man calls out to you.(He had a Gun in his holster)")
    time.sleep(a)
    print()
    s1 = '"You There"...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s1 = '  "Who is this Guy???..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print()
    s5 = "...Ca.. can you tell how to leave th... this area..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    time.sleep(a)
    print("He smirks and point out the gun at your head")
    time.sleep(a)
    s3 = "...Hand over all your belongings here and then I will show you the way out..."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    print('You have 3 options: ')
    time.sleep(a)
    print('#1 : Give all your belongings')
    time.sleep(a)
    print('#2 : Run')
    time.sleep(a)
    print('#3 : Fight and Run')
    time.sleep(a)
    n = input('Which option will you choose(1/2/3): ')
    if n == '1': 
        print('You had nothing to give')
        time.sleep(2)
        print('Gunshot')
        time.sleep(b)
        print('You are Dead!!')
        time.sleep(a)  
        print('Game Over!!')
        intro1()
    elif n =='2':
        s1 = 'This was a wrong choice...Boy!!'
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(b)
        print()
        print('Gunshot')
        print('You are Dead!!')
        print('Game Over!!')
        intro1()
    else: 
        print('You picked up the stone and threw at him')
        time.sleep(2)
        print('And then you ran.....')
        path_end1()
        print()
    

def path1_2():
    print()
    print("You begin scaling down the side of the mountain toward the bottom.")
    time.sleep(a)
    print("It's a long way down but you soon grow strong enough to appreciate the view.")
    time.sleep(a)
    print("Although you're still about halfway up the mountain, clouds surround you and the world seems small.")
    time.sleep(a)
    s1 = '  "I don\'t believe my eyes..."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('  --You think to yourself')
    time.sleep(a)
    print()
    print("You continue down the mountain for days until you reach the bottom.")
    time.sleep(a)
    s2 = '  "Let\'s find a place out of here!!"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(.25)
    print('--You yell')
    time.sleep(a)
    print("The Forest has Beautiful trees and there was chirping of Birds")
    time.sleep(a)
    print("You start walking towards the path")
    time.sleep(a)
    print("While walking ahead you hear a noise in the bush!!")
    time.sleep(a)
    print("After a second or two you see a pair of eyes watching you....")
    time.sleep(a)
    print('And a wild boar apppears out of it...')
    print()
    print('What will you do....')
    print()
    print('#1: Grab a nearby rock and throw at him')
    time.sleep(a)
    print("#2: Lie down and act like dead")
    time.sleep(a)
    print('#3: Run and hide behind the boulder')
    n = input('What will you choose(1/2/3): ')
    if n == '1':
        print('You grabbed a nearby rock and threw at him....')
        time.sleep(a)
        print('But he regains it control and start running toward you...')
        time.sleep(a)
        print('#1: To throw another stone')
        time.sleep(a)
        print("#2: To run and hide behind the boulder")
        time.sleep(a)
        print("#3: Run")
        time.sleep(a)
        n = input('What will you choose: ')
        if n == '1': 
            print('This time the stone hit at it legs and it stumbles....')
            time.sleep(a)
            print("Without looking back you start to run deep inside the Forest")
            time.sleep(a)
            path_end2() 
        elif n == '2':
            print('You run and Hide behind the boulder...')
            time.sleep(a)
            print('After a second you hear footsteps right behind the boulder...')
            time.sleep(a)
            print('You are mauled by the boar')
            time.sleep(a)
            print('Game Over!!')
            intro1()
        else: 
            print('You start running ahead...')
            time.sleep(a)
            print('...But the boar catches you in no time...')
            time.sleep(a)
            print('You are mauled by the boar')
            time.sleep(a)
            print('Game Over!!')
            intro1()
    elif n == '2': 
        print('It was the easy way to get mauled')
        time.sleep(a)
        print('You\'re Dead')
        time.sleep(a)
        print('Game Over!!!')
        intro1()
    else: 
        print()
        print('You run and Hide behind the boulder...')
        time.sleep(a)
        print('After a second you hear footsteps right behind the boulder...')
        time.sleep(a)
        print('You are mauled by the boar')
        time.sleep(a)
        print('Game Over!!')
        intro1()
   

def path2():
    print("You climb down the vines into a bottomless hole in the ground")
    time.sleep(a)
    print("It's dark, damp, and hard to climb down the vines, but your vision and muscles eventually adjust.")
    time.sleep(a)
    print("A huge boulder slides into place above you, blocking your escape.")
    time.sleep(a)
    print("You continue climbing down the vines until you hear something whirring below you.")
    time.sleep(a)
    print("...You reach a underground river...")
    time.sleep(a)
    print()
    print('There was a old and rusty boat nearby ')
    print()
    print()
    print('#1: You will use the boat')
    time.sleep(a)
    print('#2: You will swim')
    time.sleep(a)
    n = input('What will you do(1/2): ')  
    time.sleep(a)  
    print()
    if n == '1':
        time.sleep(a) 
        print('You use the old boat to move ahead....')
        time.sleep(a)
        print('It was long day boating...')
        time.sleep(a)
        print('...There were different species of fishes and vines inside the river...')
        time.sleep(a)
        print('After some time you saw a ray of light ahead')
        time.sleep(a)
        print('You saw the end for the underground tunnel')
        time.sleep(a)
        print('...You crossed the underground river and were in a vast river in the middle of forest...')
        time.sleep(a)
        print('...After some time the weather changed and It started raining heavy...')
        time.sleep(a)
        print('...There was a storm ahead...')
        time.sleep(a)
        print('...You tried to change the direction of the boat...')
        time.sleep(a)
        print('...While changing the direction the boat started breaking apart...')
        time.sleep(a)
        print('...And it broke and you drowned in the river...')
        time.sleep(a)
        print('...Using the support of the log of the boat you started swimming...')
        time.sleep(a)
        print('...Swimming with the flow of the water you find two ways ahead')
        time.sleep(a)
        print('path#1: You go Left')
        time.sleep(a)
        print('path #2: You go straight ahead')
        n = input('Which way will you choose(1/2): ')
        time.sleep(a)
        if n == '1': 
            print('You start swimming in the left direction.... ')
            time.sleep(a)
            print('After swimming a while there was sudden rush in the water...')
            time.sleep(a)
            print('And you noticed a waterfall up ahead...')
            time.sleep(a)
            print('You try to swim in the other direction...')
            time.sleep(a)
            print('But you fell from the waterfall....')
            s5 = "........."
            for character in s5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
            s5 = "........."
            for character in s5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
            s5 = "........."
            for character in s5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(b)
            print()
            print('After some time....')
            time.sleep(a)
            print('Light falls upon you...')
            time.sleep(a)
            print('And you try to block it with you hands....')
            time.sleep(a)
            print('But you suddenly realize what happened and sitting straight you look around your surroundings...')
            time.sleep(a)
            print('You find yourself near the watefall shore...')
            time.sleep(a)
            path_end3()

        else: 
            print('You start swimming in the straight direction...')
            time.sleep(a)
            print('...There was something nagging on your legs...')
            time.sleep(a)
            print('...There was utter fear on your face when you saw piranha eating you alive..,')
            time.sleep(a)
            print('...And more are coming...')
            time.sleep(a)
            print('You\'re Dead!!')
            time.sleep(a)
            print('Game over!!')
            time.sleep(a)
            intro1()

    else:
        time.sleep(a)
        print('You started swimming...')
        time.sleep(a)
        print('Suddenly your leg got stuck in the vines underriver...')
        time.sleep(a)
        print('You tried to untangle the vines but....')
        time.sleep(a)
        print('...were not able to in time...')
        time.sleep(a)
        print('You Drown')
        time.sleep(a)
        print('Game Over!!')
        time.sleep(a)
        intro1()


# Main Function ###

print()
print()
print("     #########################")
print("     #                       #")
print("     #    Forest Wilderness  #")
print("     #                       #")
print("     #########################")
print()
print()
time.sleep(a)
print("Wha... What happened? Where am I?")
time.sleep(a)
print("It's too dark to see anything...")
time.sleep(a)
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
    intro()
