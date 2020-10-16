import tkinter as tk
from PIL import Image, ImageTk
from random import randint

MOV_INC = 20
MOV_PER_SEC = 15
GAME_SPEED = 1000 // MOV_PER_SEC

class Snake(tk.Canvas):

    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)

        self.snake_positions = [(100,100), (80,100) ,( 60, 100)]
        self.food_positions = self.set_new_foodposition()
        self.score = 0 
        self.direction = "Right"
        self.bind_all("<Key>", self.onkeyPress)

        self.after(GAME_SPEED, self.performActions)
        self.loadAssets()
        self.create_objects()
    
    def loadAssets(self):
        try:
            self.snake_body_image = Image.open("./assests/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.snake_food_image = Image.open("./assests/food.png")
            self.snake_food = ImageTk.PhotoImage(self.snake_food_image)

        except IOError as error:
            print(error)
            root.destroy()
    
    def create_objects(self):
        self.create_image(self.food_positions[0], self.food_positions[1], image=self.snake_food, tag="food")
        self.create_text(
            45,12, text=f"Score : {self.score}",
            tag= "score",
            fill="#fff",
            font=("TkDefaultFont", 14)
        )
        self.create_rectangle(7,27,593,613, outline ="#525d69")
        for x_positon, y_position in self.snake_positions:
            self.create_image(x_positon, y_position, image=self.snake_body, tag="snake")


    def movSnake(self):
        # print("a")
        head_x_position, head_y_position = self.snake_positions[0]

        if self.direction == "Left":
            new_head_position = (head_x_position - MOV_INC, head_y_position)
            # print("l")
        elif self.direction == "Right":
            new_head_position = (head_x_position+ MOV_INC, head_y_position)
            # print("r")

        elif self.direction == "Down":
            new_head_position = (head_x_position , head_y_position + MOV_INC)
            # print("d")
        elif self.direction == "Up":
            new_head_position = (head_x_position , head_y_position - MOV_INC)
            # print("u")


        # new_head_position = (head_x_position+ MOV_INC, head_y_position)

        self.snake_positions =[new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions ):
            self.coords(segment, position)

    def performActions(self):
        if self.checkCollision():
            self.end_game()
            return 
        self.checkFoodCollision()
        self.movSnake()
        self.after(GAME_SPEED, self.performActions)

    def checkCollision(self):
        head_x_position, head_y_position = self.snake_positions[0]

        return(
            head_x_position in (0, 600)
            or head_y_position in (20, 620)
            or (head_x_position, head_y_position) in  self.snake_positions[1:]
        )
    
    def onkeyPress(self, e):
        new_direction = e.keysym
        print(new_direction)

        all_direction = ( "Up", "Down", "Right", "Left")

        opposites = ({"up", "Down"},
        {"Left", "Down"})

        if (new_direction in all_direction and {new_direction , self.direction} not in opposites):
            self.direction= new_direction

        self.direction = new_direction
    
    def checkFoodCollision(self):
        if self.snake_positions[0] == self.food_positions:
            self.score +=1
            self.snake_positions.append(self.snake_positions[-1])

            if self.score %5==0:
                global MOV_PER_SEC
                MOV_PER_SEC +=1
            self.create_image( self.snake_positions[-1], image =self.snake_body, tag="snake" )

            self.food_positions = self.set_new_foodposition()
            self.coords(self.find_withtag("food"), self.food_positions)
             
            score = self.find_withtag("score")
            self.itemconfig(score, text=f"Score : {self.score}", tag="score")

    def set_new_foodposition(self):
        while True:
            x_positon = randint(1,29) * MOV_INC
            y_position = randint(3, 30) * MOV_INC
            food_positions = (x_positon, y_position)

            if food_positions not in self.snake_positions:
                return food_positions
    
    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width()/2,
            self.winfo_height()/2,
            text= f"GAME OVER!! You Scored {self.score}!",
            fill="#fff",
            font=("TkDefaultFont", 24)
        )
        self.create_text(
            self.winfo_width()/1.5,
            self.winfo_height()/1.5,
            text= f"Never Give Up - Suraj",
            fill="#fff",
            font=("TkDefaultFont", 24)
        )

root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

board = Snake()

board.pack()

root.mainloop()
