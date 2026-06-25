print("Hello World!!")

print("How are you today?")
print("A. Very Good")
print("B. Not Great")

mood = input("Enter (A, B): ").upper()

if mood == "A":
    print("Have you eaten?")
    print("A. Nope, I don't plan to.")
    print("B. Yes, I did!")

    answer = input("Enter (A, B): ").upper()

    if answer == "B":
        print("Nice! What do you plan to do today?")
    else:
        print("Try to eat something when you can!")

elif mood == "B":
    print("Is everything going well today?")
    print("A. I was just kidding, it is.")
    print("B. Something happened.")

    answer = input("Enter (A, B): ").upper()

    if answer == "B":
        print("I'm sorry to hear that. Want to talk about it?")
    else:
        print("Glad things are okay!")

else:
    print("Please enter A or B.")