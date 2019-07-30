import turtle
import random

turtle.tracer(1,0)

#turtle placement
size_x=800
size_y=500
turtle.setup(size_x,size_y)

turtle.penup()

#turtle design
square_size=20
start_legnth=6
TIME_STEP=100

#lists
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

#set up positions
snake=turtle.clone()
snake.shape('square')
turtle.hideturtle()

#Function to draw a part of the snake on the screen
def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos) 
    my_stamp= snake.stamp()
    stamp_list.append(my_stamp)


for i in range(start_legnth) :
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=square_size

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

snake.direction = "Up"
up_edge = 250
down_edge = -250
right_edge = 400
left_edge = -400


def up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")

def down():
    snake.direction="Down"
    print('You pressed the down key!!')

def left():
    snake.direction="Left"
    print('you pressed the left key!')

def right():
    snake.direction="Right"
    print('you pressed the right key!')

turtle.onkeypress(up, "Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.listen()
turtle.register_shape("trash.gif")

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_stamps.append(food.stamp())
    

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= right_edge:
         print("You hit the right edge! Game over!")
         quit()
    if new_x_pos<= left_edge:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos>= up_edge:
        print("You hit the top edge! Game over!")
        quit()
    if new_y_pos<= down_edge:
        print("You hit the lower edge! Game over!")
        quit()
    new_stamp()
    remove_tail()

    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + square_size)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - square_size)
    elif snake.direction=="Right":
        snake.goto(x_pos+ square_size, y_pos)
    elif snake.direction=="Left":
        snake.goto(x_pos- square_size, y_pos)

    ######## SPECIAL PLACE - Remember it for Part 5

    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
    
    #HINT: This if statement may be useful for Part 8

    ...
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
    turtle.ontimer(move_snake,TIME_STEP) #<--Last line of function


move_snake()



turtle.mainloop()
