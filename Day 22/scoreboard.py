from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24 , 'normal')

class Scoreboard(Turtle):
    def __init__(self): 
        super().__init__()
        self.hideturtle()
        
        self.right = 0
        self.left = 0
        self.update_scoreboard()

    def update_scoreboard(self) :
        self.goto(0,250)
        self.color('white')
        self.write(f'{self.left} : {self.right}',align=ALIGNMENT, font=FONT)

    # def score(self,point) :
    #     if point == 'RIGHT' :
    #         self.right += 1 
    #         self.update_score()
    #     if point == 'LEFT' :
    #         self.left += 1 
    #         self.update_score()