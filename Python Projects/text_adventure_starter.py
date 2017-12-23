start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''


print(start)

endStatement = "The End"
print("Type 'left' to go left or 'right' to go right.")

done = False

while not done: 
    
    
    print("enter a valid option.")
    user_input = input()

    if user_input == "left":
        done = True
        print("You decide to go left and you run into a troll! Do you fight or run?") # finished the story by writing what happens

        while done:

            user_input= input()
            if user_input == "fight":
                print("The troll hits you on the head and you die.")
                print("The End")
                
            elif user_input == "run":
                print("The troll laughs as you run away like a baby")
                print(endStatement)
                
            else:
                print("Enter a valid option.")

    elif user_input == "right":
        print("You choose to go right and you walk up to a river.") # finished the story writing what happens
        done = True
        print("Swim across? Yes/No")

        while done:
            user_input = input()
            if user_input == "yes":
                
                print("The current is too strong and you die.")
                print(endStatement)
                
            elif user_input == "no":
                print("You sit down nex to the river and take a nap.")
                print(endStatement)
                
            else:
                  print("Enter a valid option.") 
      
    

    
