def rock_paper():
    def win():
        print("you win")
    def lose():
        print("you lose")
    p=input("enter the p :")
    c=input("enter the c :")
    if p=="rock" and c=="scissors":
        win()
    elif p=="rock" and c=="paper":
        lose()
    elif p=="paper" and c=="scissors":
        lose()
    elif p=="scissors" and c=="paper":
        win()
    elif p=="paper" and c=="rock":
        lose()
rock_paper()