import string
from collections import Counter


def tokenize(malecula_string):
    number = ''
    atom = ''
    for c in malecula_string:
        if c in string.digits:
            number += c
        elif number:
            yield int(number)
            number = ''

        if c in string.ascii_lowercase:
            atom += c
        elif c in string.ascii_uppercase:
            if atom:
                yield atom
            atom = c
        elif atom:
            yield atom
            atom = ''

        if c in ['(', '[', '{']:
            yield '('

        if c in [')', ']', '}']:
            yield ')'

    if number:
        yield int(number)

    if atom:
        yield atom


def counterize(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, int):
            bracket_counter = Counter()
            last = stack.pop()
            if last == ')':
                last = stack.pop()
                while last != '(':
                    for i in range(token):
                        bracket_counter += last
                    last = stack.pop()
            else:
                bracket_counter = last

            if not stack:
                yield bracket_counter
                break
            else:
                stack.append(bracket_counter)

        elif token == '(':
            stack.append('(')
        elif token == ')':
            stack.append(')')
        # atom
        else:
            stack.append(Counter({token: 1}))


def parse_molecule(formula):
    for token in tokenize(formula):
        print(token)
    # pass


water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremy_salt)            # return {K: 4, O: 14, N: 2, S: 4}
