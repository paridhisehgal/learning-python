Time = int(input("\nWhat's the time now? "))

if Time < 12:
    print("It's" , Time ,"a.m.," ,"Good morning mate!")
elif Time < 18:
    print("It's" , Time ,"p.m.," ,"Good afternoon mate!")
else:
    print("Good evening mate!")