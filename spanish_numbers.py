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

    ####################
    # Conversions
    ####################
    def number_to_text(self, number:str):
        """Converts a number into Spanish text."""
        # Reversing number keeps index consist.  (Ones place is always [0])
        reversed_num = number[::-1]
        text = ''

        # Special Cases
        if 10 <= int(number) <= 15:
            return self.exceptions.get(number)

        # Regular Conversions
        if len(number) >= 4:
            text += self._thousands_to_text(reversed_num[3])
        if len(number) >= 3:
            text += self._hundreds_to_text(reversed_num[2])
        if len(number) >= 2:
            text += self._tens_to_text(reversed_num[1])
            if int(number) > 30:
                text += ' y '

        text += self.ones.get(number[0])
        return text


    def _thousands_to_text(self, number:str):
        """Converts single thousands place digit to the appropriate Spanish word"""
        if number != '1':
            return self.ones.get(number) + ' mil'
        else:
            return 'mil'


    def _hundreds_to_text(self, number:str):
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


    def _tens_to_text(self, number:str):
        """Converts single tens place to appropriate Spanish word."""
        return self.tens.get(number)


    ####################
    # User Input
    ####################
    def _ask_parameters(self):
        print("What is the max number you want?")
        self.max_number = int(input())

        print("How many rounds do you want?")
        self.rounds = int(input())

    def _ask_number(self):
        integer = random.randint(1, self.max_number)
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

    ####################
    # Run Function
    ####################
    def run(self):
        print("Hola.  Welcome to Spanish Numbers")
        self._ask_parameters()

        while self.rounds > 0:
            self._ask_number()
            self.rounds -= 1

        correct = self.rounds - self.incorrect
        print('You scored', correct, 'out of', self.rounds)
        print('Adios')
        input()



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
# Testing Suite
# Correct double digit numbers  (10s and 20s have no space but 31+ follow 'y num' format)

########
# Long Term
#######
# Add a GUI
# Create a GIT website page for it instead (if possible)