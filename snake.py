import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=10

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

snake=turtle.clone()
snake.shape("square")

turtle.hideturtle()

for loop1 in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)
    stamp1=snake.stamp()
    stamp_list.append(stamp1)

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3

direction=UP
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400

def up():
    global direction
    direction=UP
    print('you pressed the UP key!')

def left():
    global direction
    direction=LEFT
    print('you pressed the LEFT key!')

def down():
    global direction
    direction=DOWN
    print('you pressed the DOWN key!')

def right():
    global direction
    direction=RIGHT
    print('you pressed the RIGHT key!')

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()

turtle.register_shape("trash.gif")
food=turtle.clone()
food.shape("trash.gif")

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())
    
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right')
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left')
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down')
    else:
        print('?')

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    #special place for part 5
    
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you have eaten the food!')
        
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    if new_x_pos >=RIGHT_EDGE:
        print('you hit the right edge! game over!')
        quit()
    elif new_x_pos <=LEFT_EDGE:
        print('you hit the left edge! game over!')
        quit()
    elif new_y_pos <=DOWN_EDGE:
        print('you hit the down edge! game over!')
        quit()
    elif new_y_pos >=UP_EDGE:
        print('you hit the up edge! game over!')
        quit()
   
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
make_food()
turtle.register_shape("trash.gif")
food=turtle.clone()
food.shape("trash.gif")

food_pos=[(100,100),(-100,100),(-100,-100),(100,-100)]
food_stamps=[]
food.hideturtle()

turtle.pendown()
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)
    
    
    
    
    


















