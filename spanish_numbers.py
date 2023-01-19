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
