print("Welcom to the treasure land !")

direction = input('Left or right\n')
if direction.lower() ==  "left" :
    print('Survive')
    swim_wait = input('Swim or wait\n')
    if swim_wait.lower() == 'wait' :
        print('Survive')
        which_door = input('Choose 1 door , "Red" "Yellow" "Blue"\n ')
        if which_door.lower() == 'yellow' :
            print('You win')
        else : 
            print('Game over')
    else : 
        print('Game over')
        
        
else :
    print('Game over')
    
        
        

    



