# def add_turtle():
#     new_turtle = Turtle()
#     new_turtle.penup()
#     new_turtle.color("darkred")
#     new_turtle.shape("square")
#     new_turtle.goto(saved_tail_position_x - 20, saved_tail_position_y)

# saved_tail_position_x = 0
# saved_tail_position_y = 0

# screen.onkey(add_turtle, "space")

#     for seg in range(len(segments) - 1, 0, -1):
#         new_x = segments[seg - 1].xcor()  # Retrieving the x coordinate of the second to last segment, on upward
#         new_y = segments[seg - 1].ycor()  # Retrieving the y coordinate of the second to last segment, on upward
#         # This would place each segment in the position of the segment in front of it.
#         segments[seg].goto(new_x, new_y)
#     # After looping through to move
#     segments[0].forward(20)

# game_is_on = True
# screen.tracer(0)
# screen.update()
#
# while game_is_on:
#     screen.update()
#     time.sleep(0.06)
#     for seg in range(len(segments) - 1, 0, -1):
#         new_x = segments[seg - 1].xcor()  # Retrieving the x coordinate of the second to last segment, on upward
#         new_y = segments[seg - 1].ycor()  # Retrieving the y coordinate of the second to last segment, on upward
#         # This would place each segment in the position of the segment in front of it.
#         segments[seg].goto(new_x, new_y)
#     # After looping through to move
#     segments[0].forward(20)
#     segments[0].left(90)
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale")


class Reptile(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        # This means the super class breathe will be performed,
        # as well as something else if added
        super().breathe()
        print("Breathing as a reptile.")
    
    def shed_scales(self):
        print("I'm shedding scales.")


cobra = Reptile()
cobra.breathe()