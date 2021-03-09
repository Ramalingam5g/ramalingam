user_person = int(input("enter where you want to go :"))
ground_floor=0
ending_floor=5
while(ground_floor < ending_floor):
    if (ground_floor == user_person):
        print("you are in ",user_person,"floor")
        person2 = int(input("enter where you want to go :"))
        if (person2 != user_person ):
            user_person=person2

        else:
            print("please enter valid floor number")    
            continue
        ground_floor =0
    ground_floor =ground_floor+1

if(user_person>=5):
    print("please enter valid floor number")

   