class PluralStateMachine:
    def __init__(self):
        self.current_state = 'start'
    def transition(self, input_char):
        if self.current_state == 'start':
            if input_char == 'y':
                self.current_state = 'y'
            elif input_char in ['s', 'x']:
                self.current_state = 'es'
            else:
                self.current_state = 's'
        elif self.current_state == 'y':
            if input_char.isalpha():
                self.current_state = 'ies'
            else:
                self.current_state = 's'
        elif self.current_state == 'es':
            self.current_state = 's'
        elif self.current_state == 'ies':
            self.current_state = 's'
        elif self.current_state == 's':
            pass
    def generate_plural(self, noun):
        self.current_state = 'start'
        for char in noun[::-1]:
            self.transition(char)
        if self.current_state == 's':
            return noun + 's'
        elif self.current_state == 'es':
            return noun + 'es'
        elif self.current_state == 'ies':
            return noun[:-1] + 'ies'
        else:
            return "Invalid noun or plural form not recognized"
def main():
    fsm = PluralStateMachine()

    while True:
        noun = input("Enter a singular noun (or type 'exit' to quit): ")
        if noun.lower() == 'exit':
            break
        plural = fsm.generate_plural(noun)
        print(f"The plural form of '{noun}' is '{plural}'.")
if __name__ == "__main__":
    main()
