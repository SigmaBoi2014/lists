Name=["spoodey","spooder","cookie"]
while True:
 choice=int(input("enter your choice_1.make a name,2.display all names,3.delete a name,4.exit"))
 if(choice==1):
     name=input("Write a name ")
     Name.append(name)
     print(Name)
 if(choice==2):
     print(Name)
 if(choice==3):
    delete=input("what name do you want to delete? ")
    Name.remove(delete)
 if(choice==4):
    print("Okay!")
    exit()






