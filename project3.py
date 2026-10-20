print("Welocme \nto the PERSONALITY QUIZ!!!")
matcha_points = 0
chai_points = 0
coffee_points = 0

print("Let's get started!\n")
answer1 = input ("Do you like iced or hot drinks?\n")
if answer1 == "iced":
    matcha_points +=1
    chai_points +=1
    coffee_points +=1
elif answer1 == "hot":
    matcha_points +=1
    chai_points +=1
    coffee_points +=1
if answer1 == "iced" or "Iced":
        print("nice answers let's keep going!\n")
if answer1 == "Hot" or "hot":
    print ("NICE answers!!!")
answer2 = input ("Do you like herbs, spices or beans?\n") 
if answer2 == "spices":
    chai_points +=2
elif answer2 == "herbs":
    matcha_points +=2
elif answer2 == "beans":
    coffee_points +=2
if answer2 == "Herbs" or "Spices":
    print ("            ")
print("Nice!")
print(" \t  ")
print ("ok next question")
print ("                                ")
answer3 = input ("Do you like the smell of vanilla, pumkin, or dryer sheets?\n")
if answer3 == "vanilla":
    matcha_points +=1 
elif answer3 == "pumkin":
    chai_points +=1
elif answer3 == "dryer sheets":
    coffee_points +=1
if answer3 == "Vanilla" or "vanilla":
    print ("\nGood job let's keep going!\n")
if answer3 == "Pumkin" or "pumkin":
    print ("\n Great job let's keep going!\n")
if answer3 == "Dryer Sheets" or "dryer sheets":
    print ("\n Great job let's keep going!")
answer4 = input ("do you like slick back, loose curls, or half up half down with claw clip?\n")
if answer4 == "slick back":
if matcha_points > chai_points and matcha_points > coffee_points:
    print ("You are like matcha!")
elif chai_points > coffee_points and chai_points > matcha_points:
    print("You are a chai person!") 
elif coffee_points > matcha_points and chai_points > matcha_points:
    print ("You are a coffee person!")