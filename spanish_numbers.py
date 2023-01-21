####################
# Work in progress
####################

import random

class SpanishNumbers:
    def __init__(self):
        self.ones = {'0':'','1':'uno', '2':'dos', '3':'tres', '4':'cuatro', '5':'cinco', '6':'seis', '7':'siete', '8':'ocho', '9':'nueve'}
        self.tens = {'0':'','1':'dieci', '2':'veinte', '3':'treinta', '4':'cuarenta', '5':'cincuenta', '6':'sesenta', '7':'setenta', '8':'ochenta', '9':'noventa'}
        self.exceptions = {'10': 'diez', '11':'once', '12':'doce', '13':'trece', '14':'catorce', '15':'quince'}  

        self.max_number = 9999
        self.rounds = 0
        self.incorrect = 0

    def number_to_text(self, number):
        """We convert int to string to allow indexing.  Reversing the int keeps consistency in indexing.  
        For example, ones place is 2nd if two digit number and third in a three digit number.  If reversed it's always first."""
        number = number[::-1]
        print("Number is...", number)
        text = ''
        if len(number) >= 4:
            text += self._thousands_place_to_text(number[3])
        if len(number) >= 3:
            text += self._hundreds_place_to_text(number[2])
        if len(number) >= 2:
            print("MORE THAN 2")
            print(number[0:1])
            text += self._tens_and_ones_place_to_text(number[0:2])
        if len(number) == 1:
            text = self._tens_and_ones_place_to_text(number[0])
        return text


    def _thousands_place_to_text(self, number:str):
        """Converts single thousands place digit to the appropriate Spanish word"""
        if number != '1':
            return self.ones.get(number) + ' mil'
        else:
            return 'mil'

    def _hundreds_place_to_text(self, number:str):
        """Converts single hundreds place digit to the appropriate Spanish word"""
        match number:
            case '5':
                return 'quinientos'
            case '1':
                return 'cientos'
            case '0':
                return ''
            case other:
                return self.ones.get(number) + 'cientos'

    def _tens_and_ones_place_to_text(self, number:str):
        """Converts both the ones and tens place digits to the appropriate Spanish word."""
        # Return number to actual order
        number = number[::-1]
        integer = int(number)
        print("ADDING TENS PLACE")
        if integer < 10:
            print("UNDER 10")
            return self.ones.get(number)
        elif integer < 16:
            print("UNDER 16")
            return self.exceptions.get(number)      
        else:
            print("NORMAL")
            return self.tens.get(number[0]) + self.ones.get(number[1])


    def _ask_parameters(self):
        print("What is the max number you want?")
        self.max_number = int(input())

        print("How many rounds do you want?")
        self.rounds = int(input())

    def _ask_number(self):
        integer = random.randint(1, self.max_number)
        print("int", integer)
        number = str(integer)
        text = self.number_to_text(number)
        print('Que es' , text , '?')
        answer = input()

        # Verify
        if answer == number:
            print('Si.  Correct.')
        else:
            print('No. ' + str(integer) + ' Try again.')
            self.incorrect += 1


    def run(self):
        print("Hola.  Welcome to Spanish Numbers")
        self._ask_parameters()

        while self.rounds > 0:
            self._ask_number()
            self.rounds -= 1

        correct = self.rounds - self.incorrect
        print('You scored', correct, 'out of', self.rounds)
        input()
        print('Adios')




def main():
    game = SpanishNumbers()
    game.run()



if __name__ == '__main__':
    main()


####### 
# MVP Goals
#######
# Data validation
# Try again option
# Refactor - less conversaions, less order flipping
# Split the 1s and 10s function to follow pattern
# If the 10s place is a 1, just branch off seperately to a teens exception page

########
# Long Term
#######
# Add a GUI
# Create a GIT website page for it instead (if possible)
