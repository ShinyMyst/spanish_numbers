<<<<<<< HEAD
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
# Correct double digit numbrse (10s and 20s have no space but 31+ follow 'y num' format)

########
# Long Term
#######
# Add a GUI
# Create a GIT website page for it instead (if possible)
=======
# 5/4/2021

import random

ones = {'0':'','1':'uno', '2':'dos', '3':'tres', '4':'cuatro', '5':'cinco', '6':'seis', '7':'siete', '8':'ocho', '9':'nueve'}
tens = {'0':'','1':'dieci', '2':'veinte', '3':'treinta', '4':'cuarenta', '5':'cincuenta', '6':'sesenta', '7':'setenta', '8':'ochenta', '9':'noventa'}
exceptions = {'11':'once', '21':'doce', '31':'trece', '41':'catorce', '51':'quince'}  # Note that these are reversed to match the num2txt function
exceptions_num = ['11', '21', '31', '41', '51']  # Note that these are reversed to match the num2txt function


def num2txt(number):
    """Converts a number, up to 9999, to its text form, in Spanish"""
    spanish_num = str(number)[::-1]  # Reverse the number, so that [0] always refers to the ones place. 
    txt_thousands = ""
    txt_hundreds = ""
    txt_tens = ""
    txt_ones = ""

    # Thousands Place
    if len(spanish_num) == 4:
        if spanish_num[3] != 1:
            txt_thousands = ones.get(spanish_num[3]) + ' mil'
        else:
            txt_thousands = 'mil'
                
    # Hundreds Place
    if len(spanish_num) >= 3:
        if spanish_num[2] == '5':
            txt_hundreds = 'quinientos'
        elif spanish_num[2] == '1':
            txt_hundreds = 'cientos'
        elif spanish_num[2] == '0':
            pass
        else:
            txt_hundreds = ones.get(spanish_num[2]) + 'cientos'

                
    # Tens Place
    if len(spanish_num) >= 2:
        # If it's 11-15
        if spanish_num[0:2] in exceptions_num:
            txt_tens = exceptions.get(spanish_num[0:2])
        # If it's not
        else:
            txt_tens = tens.get(spanish_num[1])
            
    # Ones Place (This is nexted under the else because the exception over-rides it otherwise)
            if spanish_num[0] == '0':
                txt_ones = ""
            else:
                txt_ones = 'y ' + ones.get(spanish_num[0])
                        
    return (txt_thousands + ' ' + txt_hundreds + ' ' + txt_tens + ' ' + txt_ones)
        


def number_loop():
    """Hosts the loop that iterations through the number questions and offers to repeat the questions."""
    print('Hola.  How many numbers will you be trying today?')
    attempts = int(input())
    counter = 0
    correct = 0

    while attempts > counter:
        spanish_num = str(random.randint(1,9999))
        print('Que es' , num2txt(spanish_num) , '?')
        answer = input()
        if answer == spanish_num:
            print('Si.  Correct.')
            correct += 1
        else:
            print('No. ' + spanish_num + ' Try again.')
        counter += 1

    print('You scored', correct, 'out of', attempts)

def main_loop():
    """Main program.  Runs the number loop and continues to reactivate number loop for replays until quitting."""
    loop = True
    while loop is True:
        number_loop()
        print('Continue?')
        answer = input()
        if answer != 'y':
            loop = False
    print('Goodbye')

main_loop()
>>>>>>> origin/main
