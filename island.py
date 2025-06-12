print("welcom to my island")#طباعه رساله ترحيب
print("there are tow dors in found of you\nared door\\ablue door")
which=input("which door do you want to open?\n(red)or(blue)").lower()
if which=="blue":
    print("Oops!!!! you chose the CROCODILE door\n Game over!!!!!")
elif which=="red":
    print("creat!!!Now you intered a ROOm")
    which1=input("you found three POX\n \\_white\\_black\\_green \n which box do you want to open?").lower()
    if which1=="white":
        print("Oops!!!!you opened a box filed a SNAKES\n Game over!!!!!")
    elif which1=="black":
        print("Oops!!!!you opened a box filed a SPIDER\n Game over!!!!!")
    elif which1=="green":
        print("CONGRATULATIONS!!!!you found the ****Gold****")
    else:
        print("!!!!!!!!!!!!!!!!???????")
else:
    print("!!!!!!!!!!!!!!!!!!????????")