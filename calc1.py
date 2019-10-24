# Calculator 
#
# EOF (End of file) token is used to indicate that
# that is no more input left for lexical analysis.
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        #token type: int, plus, or eof
        self.type = type
        #token value, 0,1,2.,3,4,5,6,7,8,8,'+', or none
        self.value = value

    def __str__(self):
        """ string rep of class instanxe
        examples: token(int, 3)token(plus '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )
    
    def__repr__(self):
        type=self.type,
        value=repr(self.value)
    
class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an an index into self.text
        self.pos = 0
        #current token instance
        self.current_token = none
    
    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """ lexical analyser (tokenizer, scanner)
        this method is reponsible for breaking a 
        sentence apart into tokens. One token at a time.
        """
        text = self.text
        # if self.pos index past the end of the self.text?
        # if so, then return EOF token because there is no
        # mpre input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character.
        # lots of comments, writing them all would take forever
        current_char = text[self.pos]

        #####
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(INTEGER, int (current_char))
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        ####
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
            else:
                self.error()

# fyi, where i have put '####' it means there were orignally
# blocks of comments to be added.

    def expr(self):
        ####
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)
        op = self.current_token
        self.eat(PLUS)
        right = self.current_token
        self.eat(INTEGER)
        result = left.value + right.value
        return result

def main():
    while True:
        try:
            # to run under python 3 replace raw_input call
            # with input
            text = raw_input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        Interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()