def positive_path():
 
    print("What are you looking forward to today?")
    print("A. Something specific")
    print("B. Nothing in particular")

    input("Enter (A/B): ")
    
    print("What are you looking forward to today?")
    print("A. Something specific")
    print("B. Nothing in particular")

    input("Enter (A/B): ")
    
  
    print("What are you looking forward to today?")
    print("A. Something specific")
    print("B. Nothing in particular")

    input("Enter (A/B): ")



    print("What are you looking forward to today?")
    print("A. Something specific")
    print("B. Nothing in particular")

    input("Enter (A/B): ")


    print("How do you feel right now?")
    print("A. Pretty good")
    print("B. Just okay")

    input("Enter (A/B): ")

    print("\nThanks for checking in!")
    print("I hope you have a great day.")

def negative_path():

    print("Is something bothering you?")
    print("A. printYes")
    print("B. Not sure")

    q2 = input("Enter (A/B): ").upper()

    print("Would talking about it help?")
    print("A. Maybe")
    print("B. Not really")

    q3 = input("Enter (A/B): ").upper()

    print("\nAre you feeling a little better now?")
    print("A. Yes")
    print("B. No")


print("Chatbot v1")
print("How are you today?")
print("A. Very Good")
print("B. Not Great")

q1 = input("Enter (A/B): ").upper()

if q1 == "A":

    print("\nQuestion 2")
    print("Have you eaten today?")
    print("A. Yes")
    print("B. No")

    q2 = input("Enter (A/B): ").upper()

    if q2 == "A":

        print("\nQuestion 3")
        print("Do you have plans for today?")
        print("A. Yes")
        print("B. No")

    elif q2 == "B":
        print("\nWhy didn't you eat?")
        print("A. I'm feeling horrible")
        print("Jus kidding, I am about to cook something")
        
        q3 = input("Enter (A/B): ").upper()

    positive_path()

elif q1 == "B":

    ("\nQuestion 2")
    print("Is something bothering you?")
    print("A. printYes")
    print("B. Not sure")

    q2 = input("Enter (A/B): ").upper()

    print("\nQuestion 3")
    print("Would talking about it help?")
    print("A. Maybe")
    print("B. Not really")

    q3 = input("Enter (A/B): ").upper()

    print("\nAre you feeling a little better now?")
    print("A. Yes")
    print("B. No")

    recovery = input("Enter (A/B): ").upper()

    if recovery == "A":
        print("\nGlad to hear that!")
        print("Let's continue with some positive questions.")
        positive_path()

    else:
        print("\nQuestion 5")
        print("Would you like to do something relaxing today?")
        print("A. Yes")
        print("B. No")

        q5 = input("Enter (A/B): ").upper()

        print("\nThank you for sharing.")
        print("Take things one step at a time.")

else:
    print("Please enter A or B.")