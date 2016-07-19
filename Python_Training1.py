import time
import sys

#print("\n") = One line spacing
#time.sleep(2) = wait for 2 seconds

def intro():
    print("You see four eggs,\n\n")
    print("1.This egg is almost going to crack.\n")
    print("2.This egg has beautiful emerald colour with decorations\n")
    print("3.This egg has a galaxy milky way drawn on it. \n")
    print("4.This egg has a golden poop drawn on it.\n")
    a = int(input("Choose your egg: "))
    
    if a ==1:
        QUESTIONOne1()
    elif a ==2:
        QUESTIONTwo1()
    elif a ==3:
        QUESTIONThird1()
    elif a == 4:
        QUESTIONFour1()
##------------------------------------------------------------------- Part.1 Question Begin 
def QUESTIONOne1():
        print("\n---")
        time.sleep(2) 
        print("What will you do?")
        print("1. Dance with it")
        print("2. Put it inside your bed\n")
        SelectionOne1()
def QUESTIONOne2():
        print("\n---")
        time.sleep(2)
        print("What will you do?")
        print("1.Decide to give the egg to your boyfriend")
        print("2.Reject him and keep it yourself\n")
        SelectionOne2()
def QUESTIONOne3():
        print("\n---")
        time.sleep(2)
        print("What will you do?")
        print("1.Go to the backyard to check if your egg is safe")
        print("2.Wait for 4 more weeks\n")
        SelectionOne3()
def QUESTIONOne4():
        print("\n---")
        time.sleep(2)
        print("What will you do?")
        print("1.Feed a chicken ")
        print("2.Feed a corn\n")
        SelectionOne4()
def QUESTIONOne5():
        print("----")
        time.sleep(2)
        print("What will you do?")
        print("1.Prepare an oil for its bath ")
        print("2.Prepare a spicy sauce for a bath")
        print("3.Prepare a honey butter sauce for a bath\n")
        SelectionOne5()
##-------------------------------------------------------------------  Part.1  End
        
##==============================================================================================        
        
##-------------------------------------------------------------------  Part.2 Question Begin 
def QUESTIONTwo1():
        print("\n---")
        time.sleep(2) 
        print("What will you do?")
        print("1. Mind your own business")
        print("2. You, also run towards the box\n")
        SelectionTwo1()
def QUESTIONTwo2():
        time.sleep(2)
        print("\n---")
        print("Arrived <Your Home>")
        print("What are you going to do?")
        print("1. Put an egg into the refrigerator")
        print("2. Place it in a blanket and keep it warm.\n")
        SelectionTwo2()
def QUESTIONTwo3():
        print("\n---")
        time.sleep(2) 
        print("What will you do?")
        print("1. Throw it in the air")
        print("2. Softy place it on the bed\n")
        SelectionTwo3()
def QUESTIONTwo4():
        print("\n---")
        time.sleep(2) 
        print("What will you do?")
        print("1. Trash it")
        print("2. Feed it")
        print("3. Turn on the classical music\n")
        SelectionTwo4()
def QUESTIONTwo5():
        print("\n---")
        time.sleep(2) 
        print("What would you give your baby chick?")
        print("1. Chicken")
        print("2. Rice")
        SelectionTwo5()
def QUESTIONTwo6():
        print("\n---")
        time.sleep(2) 
        print("What do you want to give?")
        print("1. Soy sauce - present")
        print("2. Spicy seasoning - present")
        print("3. Original - present")
        SelectionTwo6()
##-------------------------------------------------------------------  Part.2 Question  End
    
##==============================================================================================
        
##-------------------------------------------------------------------  Part.3 Question Begin 
def QUESTIONThird1():
        print("You are walking on the street and you found a egg that looks gorgeous with the ")
        print("mixture of silver, emerald and purple and it has completely charmed your eyes. You ")
        print("decide to take the egg home before someone else sees it. You start to think about ")
        print("hatching the egg. You put the egg on a soft blanket. Now you will try to raise the egg. ")
        print("Good Luck!")
        print("\n---")
        time.sleep(2)
        print("What will you do to the egg?")
        print("1. You put it into a freezer.")
        print("2. You turn on some comforting music.")
        SelectionThird1()
def QUESTIONThird2():
        print("\n---")
        time.sleep(2)
        print("Now what will you do?")
        print("1. You hold it in your hands and give it a cuddle.")
        print("2. You decide to do a massage on your face with the egg.")
        print("3. You keep it warm.")
        SelectionThird2()
def QUESTIONThird3():
        print("\n---")
        time.sleep(2)
        print("Now what will you do?")
        print("1. Smack the chick because it is too loud")
        print("2. Give it some wasabi.")
        print("3. Give it raw rice.")
        SelectionThird3()
def QUESTIONThird4():
        print("\n---")
        time.sleep(2)
        print(" Now what will you do?")
        print("1. Give it a tabasco bath.")
        print("2. Give it a oil bath.")
        print("3. Give it a special oil bath with surgery.")
        SelectionThird4()
##-------------------------------------------------------------------  Part.3 Question  End

##==============================================================================================     

##-------------------------------------------------------------------  Part.4 Question Begin 
def QUESTIONFour1():
        print("While walking down the street, you see a solemn chicken holding an egg. You get ")
        print("curious about the chicken and go near to him. A chicken sees you. You see the ")
        print("chicken. The chicken tries to say something to you, but you just hear it as a ‘ ")
        print("KoKoDaek!!!! Kokko!!! ‘ Even though you can not understand what the chicken is ")
        print("saying, you feel that you need to take care of the egg. You see the egg, and oh. ")
        print("What is this. There is a >golden poop< drawn on the egg. You feel like your heart ")
        print("pumping. You really feel like you like the egg, and you think that it will be fun to hatch ")
        print("it. You smile to the chicken and chicken waves his hand. You go back to home.")
        time.sleep(2)
        print("\n[Home.]")
        print("What are you going to do? ")
        print("1. Prepare a chicken feathered blanket.")
        print("2. Put it in the refrigerator.\n")
        Selectionfour1()       
def QUESTIONFour2():
        time.sleep(2)
        print("Buy it?")
        print("1. Yes")
        print("2. NO.")
        Selectionfour2()       
def QUESTIONFour3():
        print("\n---")
        time.sleep(2)
        print("What are you going to do?")
        print("1. Take care of it.")
        print("2. Give it to someone else.")
        Selectionfour3()       
def QUESTIONFour4():
        print("\n---")
        time.sleep(2)
        print("What will you do?")
        print("1. Prepare a soy sauce to shower the chick.")
        print("2. Prepare a spice-mixed water to shower the chick.")
        print("3. Prepare an oil to shower the chick.")
        Selectionfour4()    
def EndingQUESTION1():
        print("\n---")
        time.sleep(2)
        print("Are you going to see the ending?")
        print("1. Yes!")
        print("2. Yeees!!!")
        print("3. Why there is no ‘NO’, I will just see it!")
        Ending1()      
                 
def EndingQUESTION2():
        print("\n---")
        time.sleep(2)
        print("Are you going to see the ending?")
        print("1. Yeah")
        print("2. Ooh, yeah")
        print("3. Cool, huh?")
        Ending2()
        
def EndingQUESTION3():
        print("\n---")
        time.sleep(2)
        print("Are you going to see the ending?")
        print("1. Yes!")
        print("2. Yeees!!!")
        print("3. Why there is no ‘NO’, I will just see it!")
        Ending3() 
##-------------------------------------------------------------------  Part.4 Question  End

##==============================================================================================     

##------------------------------------------------------------------- Part.1 Selection Answer Begin   
def SelectionOne1():
        a = int(input("Choose Number: "))
        if a == 1:
            print("You go to your room and turn on very loud music. You can listen its beating. You ")
            print("think that the egg is having fun too. You got over excited and shake the egg up and ")
            print("down really fast. The egg cracks, which you really wished to. However, not a chick, ")
            print("but with a white thing and a yolk..Your mom enters your room and look at the mess. ")
            print("Clean it up or there won’t be a dinner” Oops….Maybe I’ll have to eat scrambled ")
            print("egg as my dinner…?")
            intro()
        elif a == 2:
            print("You enter your room and put the egg inside your bed. It seems very comfortable.")
            print("You take a picture and post it on a Facebook. Ring. Your boyfriend wrote a comment on your post.")
            print("Can I take care of that egg pleassssse?")    
            QUESTIONOne2()
            
def SelectionOne2():
        a = int(input("Choose Number: "))
        if a == 1:
            print("You write a reply to him. Sure!! Come to my house at 3:30. After few minutes,")
            print("you hear somebody knocking the door. You run towards the door ")
            print("with your egg and open the door. You see your boyfriend and quickly hand ")
            print("him an egg. However, the egg falls off from your hand and land on his")
            print("shoes cracked, with white thing and yolk all over the shoes. Well...You've lost  ")
            print("your only one boyfriend.")
            intro()
        elif a ==2:
            print(" You decide to take care of it yourself and search the internet about how to  ")
            print("hatch an egg. It says Keep it warm in nice and quiet place. You cover up the  ")
            print("egg with very cozy blanket and put it in your backyard. The sun is very warm  ")
            print("and you think this is the best place for hatching an egg. You waited for 2 ")
            print("weeks, giving the egg a nice time for hatching. ")
            QUESTIONOne3()
            
def SelectionOne3():    
        a = int(input("Choose Number: "))
        if a == 1:
            print("Empty. Area where you placed the egg is empty. There's only a blanket lying")
            print("under the tree. You see the birds on the tree above, with their beaks wet ")
            print("with yellow liquid. In their nest, there's an egg shell break into pieces.  ")
            print("OMG...Your poor little egg is now being digested.. ")
            intro()
        elif a ==2:
            print("After 4 weeks later, you go out to check if your egg is safe. You can see a  ")
            print("beautiful yellow chick wandering around the backyard. Congratulation! You  ")
            print("have hatched the egg!!! ")
            QUESTIONOne4()
def SelectionOne4():   
        a = int(input("Choose Number: "))
        if a == 1:
            print("You open the refrigerator to find something to feed. You can see the leftover ")
            print("chicken from yesterday. You wonder what will happen if you feed chicken to  ")
            print("a chick. With full of excitement, you give a piece of fried chicken to your")
            print("chick. As it pecks on the chicken, its face is turning red and a noisy groan ")
            print("comes out from its mouth. You can see it running all over the place with")
            print("steam coming out from its head. Suddenly, it stopped and pass out on the")
            print("ground. Rest In Peace, poor little chick...")
            intro()
        elif a ==2:
            print("You search on internet what to feed to a chick. You find out that chick likes")
            print("to eat a corn. You open the refrigerator and see if there's any corn. Luckily, ")
            print("there's a spoonful of corn. You pour it on a plate and bring it to your chick ")
            print("with full of excitement. As it peck on the corn, it gets bigger and bigger, and  ")
            print("finally become a huge chicken. You observe the chicken for few minutes and")
            print("find out there's something written on its neck with a nametag. It says 'BHC' ")
            print("with a blue marker. You realized that it was a chicken from famous chicken ")
            print("company, BHC. \n")
            QUESTIONOne5()
            
def SelectionOne5():
           a = int(input("Choose Number: "))
           if a == 1:
              print("You prepare a bucket of an oil and start washing the chicken carefully. ")
              print("Chicken goes birp birp, as if it's enjoying the bath. Chicken gradually change ")
              print("to a brown color. After 6 weeks later, it floats up with a delicious sound. ")
              print("Congratulation, you succeed in making a fried chicken in BHC!!")
              intro()
           elif a ==2:                    
              print("You prepare a spoonful of spicy sauce for a chicken. You carefully spread a  ")
              print("spicy sauce on a chicken. You can see it turning red. With a smell of its spicy  ")
              print("sauce, you leave it there for 4 more weeks. After 4 weeks, you put it in a hot  ")
              print("boiling oil. Chicken slowly turns into dark red color and floats up.  ")
              print("Congratulation, you succeed in making a spicy chicken in BHC!! ")
              intro()
           elif a ==3:
              print("You prepare a spoonful of honey butter sauce for a chicken. You dip the  ")
              print("chicken into a sauce, and you can see it turning bright yellow. Chicken  ")
              print("flutters its wings, enjoying its bath in a sweet honey sauce.")
              print(" ")
              print("Now, you put it on a boiling oil tub. With its sweet smell, it slowly floats up  ")
              print("and you can see its shining cover that makes you want to eat it right away.  ")
              print("Congratulation, you succeed in making a honey butter chicken, the best menu  ")
              print("in BHC!! ")
              intro()
##------------------------------------------------------------------- Part.1 Selection Answer End



##------------------------------------------------------------------- Part.2 Selection Answer Begin

def SelectionTwo1():
        a = int(input("Choose Number: "))
        if a == 1:
            print("The boy finds an egg in the box,  but he drops it. Sorry, game over. ")
            print("Try again~ Good luck~")
            intro()
        elif a ==2:
            print("You made it! The egg has beautiful emerald colour with decorations. You ")
            print("immediately find out that it’s  not a normal egg.  What would you do next? You ")
            print("decide to bring it  home.")
            QUESTIONTwo2()
def SelectionTwo2():
        a = int(input("Choose Number: "))
        if a == 1:
            print("Put the egg into the refrigerator")
            print("As soon as  you put the egg in the refrigerator,  the fancy decorations disappear ")
            print("and turn into a normal egg.")
            print("Sorry, you can have it for your brunch tomorrow! Try again~ Good luck~")
            intro()
        elif a ==2:
            print("Place the egg into a brooder.")
            print("Next, you try to make a bed for your little cute egg!")
            print("After you finish making a bed, you hold up your egg")
            QUESTIONTwo3()
def SelectionTwo3():
        a = int(input("Choose Number: "))
        if a == 1:
            print("Throw")
            print("\n")
            print("LOL!! You can see the yolk from the little crack of your egg!! HAHA. Game over. ")
            print("Try again~ Good luck~")
            intro()
        elif a ==2:
            print("Softy place it on the bed")
            print("On the back of your egg, you  see a series of little letters “meyong pumm”")
            print("---------after 3 weeks and 4 days later--------")
            print("Shake shake...shake shake…..")
            print("FINALLY!!!!  Congratulation!!! Your egg hatched!")
            QUESTIONTwo4()
def SelectionTwo4():
        a = int(input("Choose Number: "))
        if a == 1:
            print("Trash it")
            print("\n")
            print("You go outside, and release your chick….OMG!!")
            print("Police sees what you’re doing to the chick.")
            print("BYE BYE youre in a prison for 2 months!")
            intro()
        elif a == 2:
            print("Feed it")
            print("\n")
            print("Hmmm……. What should you…..Oh!! You walk to the kitchen")
            print("")
            print("")
            QUESTIONTwo5()
        elif a == 3:
            QUESTIONTwo5()
def SelectionTwo5():
        a = int(input("Choose Number: "))
        if a == 1:  
            print("Chicken")
            print("\n")
            print("Oh!!!! Your favorite food, CHICKEN!!")
            print("Hi my little baby, try this!” You give little bit of chicken to your little chick.")
            print("You realize that your chick is also a chicken to be, too.")
            print("“Baby, you know you are a chicken, too..! And this is chicken...LOL ")
            print("HHAHAHAAHHAHHA!!! You might……!”Your chick is dead, because it ")
            print("understands your words and gets a heart attack. BYEBYE… Game over. Try again~~")
            intro()
        elif a ==2:
            print("Rice")
            print("\n")
            print("+health +50!!")
            print("")
            print("Congratulation! You just reached 2nd stage of growth!!! :) ")
            print("------4 months later-----")
            print("You can’t imagine when your baby was chick! Because, now, they are chicken!")
            print("----- 1 month later -------")
            print("Fe,,,w……. Life is so hard….smell, food, ew…. You hate it!!")
            print("You decide to give your baby a present!")
            QUESTIONTwo6()

def SelectionTwo6():
        a = int(input("Choose Number: "))
        if a == 1:
            print("Your baby became a delicious soy sauce chicken! You can meet your  ")
            print("baby in chicken restaurant in front of your school, which is “meyong  ")
            print("pumm chicken”!!! Have a nice day~")
            intro()
        elif a == 2:
            print("Your baby became a delicious Spicy seasoning chicken! You can meet  ")
            print("your baby in chicken restaurant in front of your school, which is ")
            print(" meyong pumm chicken”!!! Have a nice day~ ")
            intro()
        elif a == 3:
            print("Your baby became a delicious original fried chicken! You can meet  ")
            print("your baby in chicken restaurant in front of your school, which is  ")
            print("meyong pumm chicken”!!! Have a nice day~ ")
            intro()
##------------------------------------------------------------------- Part.2 Selection Answer End

##------------------------------------------------------------------- Part.3 Selection Answer Begin

def SelectionThird1():
        a = int(input("Choose Number: "))
        if a == 1:
            print("\n")
            print("hours after, your egg is completely frozen. You can’t do anything about it so you ")
            print("just leave it there. 1 hours later, you check your freezer. The egg is gone. Your mom ")
            print("walks behind you. “I threw it away to the cat next door.”")
            print("Congratulations. You failed try again.")
            intro()
        elif a ==2:
            print("\n")
            print("After you turn on the music, the egg starts shaking a little bit. You are excited. You ")
            print("are determined now to make the egg hatch into a cute chick.")
            QUESTIONThird2()
def SelectionThird2():
        a = int(input("Choose Number: "))
        if a == 1:
            print("\n")
            print("The egg gets broken while you are cuddling it. Yolk and white comes out. Your mom ")
            print("sees it and yells at you. “CLEAN UP.” ")
            print("Congratulations, you failed. Try again.")
            intro()
        elif a ==2:
            print("\n")
            print("You are searching things up in the internet and there was a posting.")
            print(" If you massage your face with an egg, you will look 10 years younger! Try.”")
            print("You are amazed by that and you hold up you egg. You start massaging your face.")
            print("While you are massaging the egg cracks. Maybe you face was too hard.. OOpps. ")
            print("You can see the whites and yolk and now you decide to make a egg fry out of it. You ")
            print("turn on the stove and break the egg on it. ")
            print("Congratulations, you had a good brunch. Try again. ")
            intro()
        elif a == 3:
            print("\n")
            print("You have decided to keep in warm. You buy a special blanket for the egg.")
            print("35 days after        Congratulations, you have succeeded hatching the egg.")
            print("trying to raise the chick into a chicken. The chick is crying in hunger. ")
            QUESTIONThird3()
def SelectionThird3():
        a = int(input("Choose Number: "))
        if a == 1:
            print("\n")
            print("The chick was disturbing your ear drums. You has erupted you smack the chick ")
            print("Whack!")
            print("The chick starts squirming on the floor and it is dead. Congratulations! You just ")
            print("killed a living animal with the reason in is disturbing your ear drums. Try again.")
            intro()
        elif a == 2:
            print("\n")
            print("You open the refrigerator and see an interesting substance in a lock-lock. You decide ")
            print("to feed it to your chick. As the chick pecks on the wasabi, you can see steam coming ")
            print("out from it’s eyes. The chick turns green and poof! It is gone with a purple, green fog. ")
            print("Congratulations. The chick is gone, and your room smells like fart.")
            QUESTIONThird4()
        elif a == 3:
            print("\n")
            print("You see rice in a plastic bag near the sofa. You open it up and scatter it on the floor ")
            print("of your room. The chick comes and starts pecking. The chick starts growing, and ")
            print("when it became sort of a chicken, you see it has a name tag. It is named KFC. You ")
            print("realized the chick is from the famous brand KFC.")
            QUESTIONThird4()
def SelectionThird4():
        a = int(input("Choose Number: "))
        if a == 1:
            print("\n")
            print("You prepare a bottle of tabasco sauce and start washing the chick that looks like a ")
            print("chicken with the tabasco sauce. The chick flutters it’s wings. It seems that the chick ")
            print("is enjoying the bath. After 4 weeks of the tabasco bath, the chick becomes red. ")
            print("\n")
            print("Now, you prepare a tub of oil and heat it up. You like the chick, so you don’t want to ")
            print("let it go, but the chick waves it’s wings and commits suicide. After 1 hours of boiling a ")
            print("red spicy tabasco chicken floats up on the oil. You had succeeded in making a hot ")
            print("menu in KFC. ")
            print("\n")
            print("“ A Tabasco chicken Jumbo  Bucket.”  The price is,19800 won. ")
            
        elif a == 2:
            print("\n")
            print("You prepare a bucket of oil and plop your chick in. The chick is enjoying it’s bath ")
            print("swimming in the oil. The chicken is going Birp Birp. After 6 weeks of the bath, the ")
            print("chicken is brown.")
            print("\n")
            print("Now you prepare boiled oil on the fire. You are sad that you have to put the chick into ")
            print("the oil, tears are gathering under your eyes. However, destiny is destiny. You cannot ")
            print("deny it. Goodbye little chick. The chick flutters as it falls into the boiling oil. After 2 ")
            print("hours 30 minutes, a brown well fried chicken floats up. You had succeeded making a ")
            print("menu in KFC.")
            print("\n")
            print("“ 5 sets of original chicken “. The price is 5 x 2300, 11500 won. ") 
           
            
        elif a == 3:
            print("\n")
            print("You prepare a tub of oil. You mix spicy powder and sauce into it. Also add a special ")
            print("recipe; KFC’s special sauce. You give your chick a shower with the mixture you had ")
            print("made. The chick is enjoying the bath. Unfortunately, the menu you want to make is ")
            print("boneless. You have to have a special surgery with the chicken. You give an ")
            print("anesthetic to the chick. The chick goes into sleep. Tragically, you had killed the chick, ")
            print("and you made slices of boneless chicken.")
            print("\n")
            print("Now you prepare hot boiling oil. The chick is already dead. You had plenty of tears ")
            print("when you were cutting them. Now without hesitation, you throw in all of the slices ")
            print("and after 1 hours, you see several pieces of delicious looking chicken pieces. You ")
            print("had succeeded making a menu in KFC.")
            print("\n")
            print("“ A boneless hot crispy chicken jumbo bucket”. The price is 16000.")
           
##------------------------------------------------------------------- Part.3 Selection Answer End

##------------------------------------------------------------------- Part.4 Selection Answer Begin

def Selectionfour1():
        a = int(input("Choose Number: "))
        if a == 1:
            print("\n")
            print("You buy the blanket. You think that you might need a heater to make it warm. ")
            QUESTIONFour2()
        elif a ==2:
            print("\n")
            print("You put the egg in the refrigerator. After few hours, you see the egg is cold. You put ")
            print("it in the boiling water and enjoy your snack, a boiled egg.")
            print("\n")
            print("[ Game over. Your goal was to eat a chicken, not a boiled egg! ]\n")
            intro()
def Selectionfour2():
        a = int(input("Choose Number: "))
        if a == 1:
            print("\n")
            print("You turn on the heater. You fold the blanket and place the egg on it. You sleep.")
            print("\n")
            print("~After 30 days.")
            print("You see the egg shaking! It is cracking, and a golden chick comes out!")
            QUESTIONFour3()
        elif a ==2:
            print("The egg got frozen. The little life ready to come out to the world died because of you. ")
            print("\n")
            print("[ Game over. Your goal was to eat a chicken, not to kill it! ]")
            intro()
def Selectionfour3():
        a = int(input("Choose Number: "))
        if a == 1:
            print("\n")
            print("You choose to have a little chick as your baby. As you hug the chick, you realize that ")
            print("he has a name tag on its neck. It says ‘KyoChon.’")
            print("\n")
            print("You realize that this chicken is from KyoChon Chicken.")
            QUESTIONFour4()
        elif a ==2:
            print("\n")
            print("The chick died as you drived to your friend’s car. The car-sickness led the poor little, ")
            print("cute chick to death. It is all because of you.")
            print("\n")
            print("[ Game over. Your goal was to eat a chicken, not to kill it by carsickness! ]")
            intro()
def Selectionfour4():
        a = int(input("Choose Number: "))
        if a == 1:
            print("\n")
            print("You pour a soy sauce and a tin of oil in the small bath-tub for babies. The colour of ")
            print("the spice looks like a soy sauce chicken.")
            print("\n")
            print("You hold the chick and shower it with the oil. The chick goes Birp, birp. It looks like ")
            print("the chick likes the shower. ")
            print("You take him out from the tub and rinse it with water.")
            print("\n")
            print("-After 5 months of soy sauce showering.-")
            EndingQUESTION1()
            
        elif a == 2:
            print("\n")
            print("You pour a spice-mixed water into the small bath-tub for babies. The colour of the ")
            print("water indicates you the spicy chicken. ")
            print("\n")
            print("You hold the chick and shower it with spice-mixed water. The chick goes Biiiir!!! ")
            print("Birp!!!! It looks like the chick is enjoying the shower. ")
            print("You take him out from the tub and rinse it with water.")
            print("\n")
            print("-After 5 months of spice-mixed water showering.-")
            print("\n")
            EndingQUESTION2()
            
        elif a == 3:
            print("\n")
            print("You pour a tin of oil into the bathtub for babies. The colour of the oil indicates you a ")
            print("fried chicken. ")
            print("\n")
            print("You hold the chick and shower it with oil. The chick goes b..i..r..p..! Bir..p! It looks like ")
            print("he loves the shower.")
            print("You take him out and rinse it off with water.")
            print("\n")
            print("-After 5 months of oil showering.-")            
            EndingQUESTION3()
    
def Ending1():
    print("-Ending. (Soy sauce)")
    print("You see the chicken. You see Kyochon. Kyochon walks into the boiling oil. You are ")
    print("going to cry, but Kyochon just nods to you to say that he is okay. Your teardrop fall. ")
    print("Kyochon stares at you, then dive into the oil. After 20 minutes of crying, you see the ")
    print("brown soy sauce chicken floating. ")
    print("------------------------------------------END------------------------------------------")
    
def Ending2():
    print("-Ending. (Spice-mixed water)")
    print("You see the chicken. You see Kyochon. He waves his wings to fly into the tub of ")
    print("boiling water. You cry. You shout, don’t go. Kyochon slightly shakes his head like he ")
    print("is saying that it is his destiny to go into the oil. Like a tough guy, he runs at the back ")
    print("of the table to the tub, slightly flying. After 20 minutes of tears, red, spicy chicken ")
    print("floats up. ")
    print("------------------------------------------END------------------------------------------")
    
def Ending3():
    print("You see the chicken. You see Kyochon. You remember the happy times you have ")
    print("sent with him. Your sight get gloomy. Teardrops fall. Your teardrops wet the feather ")
    print("of Kyochon. He wipes your eyes with his wings, like he is saying it is all okay, don’t ")
    print("cry. After hugging you for few minutes, he slowly walks toward to the oil tank. He ")
    print("jumps in waving his wings, saying good bye. After 20 minutes of tears, light brown ")
    print("fried chicken floats up.")
    print("------------------------------------------END------------------------------------------")
    
##------------------------------------------------------------------- Part.4 Selection Answer End
              
intro()
