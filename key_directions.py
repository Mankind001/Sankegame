
from the_logic import Hello

class Positioning:
    @staticmethod
    def up():
        if Hello.current_direction != 270 and Hello.current_direction != 90:
            Hello.current_direction = 90



    @staticmethod
    def down():
        if Hello.current_direction != 90 and Hello.current_direction != 270:

            Hello.current_direction = 270


    @staticmethod
    def right():
        if Hello.current_direction != 180 and Hello.current_direction != 0:
            Hello.current_direction = 0


    @staticmethod
    def left():
        if Hello.current_direction != 0 and Hello.current_direction != 180:
            Hello.current_direction = 180

