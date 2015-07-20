import math
class MovementHelper:
    @staticmethod
    def get_possible_movement_spaces(movement_range, x, y):
        possible_movement = []
        
        # maths incoming
        for distance in range(movement_range + 2):
            # go through all the possible angles in a circle
            for angle in range(0,360):
                # find the x and y coords on given the above distance and angle
                # using maths :(
                x_increment = int(math.ceil(distance * math.cos(angle)))
                y_increment = int(math.ceil(distance * math.sin(angle)))
                
                # if the x + y coords are too big or zero ignore it
                absolute_value = math.fabs(x_increment) + math.fabs(y_increment)
                if  absolute_value > movement_range or absolute_value == 0 :
                    continue
                
                MovementHelper.__insert_item(possible_movement,  x_increment + x,  y_increment + y)          
                
        return possible_movement
    
    @staticmethod
    def __insert_item(a_list, x, y):
        if [x,y] not in a_list:
            a_list.append([x,y])