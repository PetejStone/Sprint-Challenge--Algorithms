# It can move left or right.
# It can pick up an item
# If it tries to pick up an item while already holding one, it will swap the items instead.
# It can compare the item it's holding to the item in front of it.
# It can switch a light on its head on or off.


# You may use any pre-defined robot methods.
# You may NOT modify any pre-defined robot methods.
# You may use logical operators. (if, and, or, not, etc.)
# You may use comparison operators. (>, >=, <, <=, ==, is, etc.)
# You may use iterators. (while, for, break, continue)
# You may NOT store any variables. (=)
# You may NOT access any instance variables directly. (self._anything)
# You may NOT use any Python libraries or class methods. (sorted(), etc.)
# You may define robot helper methods, as long as they follow all the rules.




class SortingRobot:
    def __init__(self, arr):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = arr          # The list the robot is tasked with sorting
        self._item = None     # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

        

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    #################### Plan for Sorting ############
       # SWAP 
        ### Iterative swap example - loops through values, if one is greater, swap values
        ##### if current index was 2      .
        ##                          [ 1,2,4,3,5 ]
        ## inside loop found that 4 is > 3, so new cur_index is 3 (3) -- > cur_index = arr[3]
        ### temp = arr[2] (4) - so temp value is 4
        #### arr[2] == arr[3] -- so 4 is now = 3 -> [1,2,3,3,5]
        #### arr[cur_index] = temp   --> aka  -->  (arr[3]) == arr[2] -> [1,2,3,4,5]

      ##################################################

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # Bubble Sort
        self.set_light_on() ## turn light on
        while self.light_is_on(): ## while the light is on
            ## will run when it is at the beginning of the list
            # print('start of function again')
            self.move_to_right() # call the sort right fn
            # WHILE light is on and WHILE move left is true then loop this FN... this will move back to the beginning
            while(self.can_move_left()): #reset to the far left
                # print("you moved left")
                self.move_left()
            
        

    def move_to_right(self):
        self.set_light_off() # Turn light off -- this keeps the above function from calling the move left loop
        while(self.can_move_right()): # While it can move right  -- stay in this function  until the end of the list
            self.swap_item() ## swap the item 
            # print(f'you are now holding {self._item}') 
            self.move_right() ## move right
            # print('you moved right')
            if self.compare_item() == 1: # if the item held is greater then swap, if not, move left again (per line 159)
                self.swap_item() # swap if greater
                self.set_light_on() ## turn light on -- this is for when you reach the end of the list, this will not exit the loop until then because of line 149 being true
                # print('you turned light on')
                # print(f'you are holding {self._item}')
            self.move_left() ## Per line 154, if the item is not greater, go back left (to original spot) 
            # print('you moved left')
            self.swap_item() ## and swap
            # print(f'you are now holding {self._item}')
            self.move_right()  ## move right -- this will restart the loop and go back to line 150.
            # print(f'you moved right')

    ### commented out prints, or else the robot would take too long

        

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    arr = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(arr)

    robot.sort()
    print(robot._list)