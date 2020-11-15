def eligible_for_vote():
    user=int(input("enter age"))
    if user<18:
        print("not eligible")
    elif user>=18:
        print("you are eligible")
eligible_for_vote()