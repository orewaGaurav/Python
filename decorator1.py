# '''write a decorator that prints "Start" before a function
# is called and "End" after the function is called.'''

#write a decorator that prints the 4times of the original number.
# and after that it prints the square of that number.


#code 6 of decorartor
def addons(game):
    def inner():
        print("START")
        game()
        print("END")
    return inner
@addons
def game():
    print("WANNA PLAY PUBG WITH ME?")    
game()