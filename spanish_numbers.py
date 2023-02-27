import random
import json


class SpanishNumbers:
    def __init__(self):
        path = 'Desktop/git-projects/spanish_numbers/number_dict.json'
        with open(path) as file:
            data = json.load(file)
        self.ones = data['ones']
        self.tens = data['tens']
        self.exceptions = data['exceptions']

        self.max_number = 9999
        self.rounds = 0
        self.incorrect = 0

    ####################
    # Conversions
    ####################
    def number_to_text(self, number: str):
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
            if number == '100':
                return 'cien'
            else:
                text += self._hundreds_to_text(reversed_num[2])
        if len(number) >= 2:
            text += self._tens_to_text(reversed_num[1])
            if int(number) > 30 and int(number)%10 != 0:
                text += ' y '

        text += self.ones.get(reversed_num[0])
        return text


    def _thousands_to_text(self, number: str):
        """Converts single thousands place digit to Spanish string."""
        if number != '1':
            return self.ones.get(number) + ' mil'
        else:
            return 'mil'


    def _hundreds_to_text(self, number: str):
        """Converts single hundreds place digit to Spanish string."""
        match number:
            case '5':
                return 'quinientos '
            case '1':
                return 'ciento '
            case '0':
                return ''
            case other:
                return self.ones.get(number) + 'cientos '


    def _tens_to_text(self, number: str):
        """Converts single tens place to appropriate Spanish word."""
        return self.tens.get(number)


    ####################
    # User Input
    ####################
    def _validate_input(self, prompt):
        while True:
            try:
                print(prompt)
                value = int(input())
                break
            except ValueError:
                print("Invalid input.  Please select a number")
        return value
    
    def _ask_parameters(self):
        prompt = "What is the max number you want?"
        while True:
            self.max_number = self._validate_input(prompt)
            if self.max_number > 9999:
                print("Please select a number less than 9999.")
            else:
                break

        prompt = "How many rounds do you want?"
        self.rounds = self._validate_input(prompt)


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
        while True:
            self._ask_parameters()
            total_rounds = self.rounds

            while self.rounds > 0:
                self._ask_number()
                self.rounds -= 1

            # Results
            correct = total_rounds - self.incorrect
            print('You scored', correct, 'out of', total_rounds)
            
            # Try Again
            print("Try again?")
            answer = input()
            if not answer.lower().startswith('y'):
                print('Adios')
                break


def main():
    game = SpanishNumbers()
    game.run()


if __name__ == '__main__':
    main()


####### 
# MVP Goals
#######
# Try again option
# May be able to refactor exceptions such as 100 to to more nicely into pattern

########
# Long Term
#######
# Add a GUI
# Create a GIT website page for it instead (if possible)