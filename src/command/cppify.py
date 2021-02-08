import re
import random


def cppify(message):
    transformed = message.content.lower()\
        .replace("+ccpify ", '')\
        .replace("'\".//\\`~!@#$%^&*()_+{}|:,.<>?", '')
    if random.randint(0, 1) % 2:
        transformed = transformed.title()
        if random.randint(0, 1) % 2:
            transformed = transformed[:1].lower() + transformed[1:]
    else:
        vowels = "aąeęiouy"
        transformed = re.sub(r'[' + vowels + '\s*]', '', transformed)
    transformed = transformed.replace(" ", '')
    output = ""
    if random.randint(0, 1) % 2:
        output = 'const '
    output += 'void '
    if random.randint(0, 1) % 2:
        output += '*'
    if random.randint(0, 1) % 2:
        output += '*'
    if random.randint(0, 1) % 2:
        output += '*'
    if random.randint(0, 1) % 2:
        output += ' _'
    output += transformed
    output += '('
    if random.randint(0, 1) % 2:
        output += 'const'
        if random.randint(0, 1) % 2:
            output += ' __ptr_void'
        if random.randint(0, 1) % 2:
            output += ' *'
        elif random.randint(0, 1) % 2:
            output += ' **'
        output += ' _smf'
    output += ')'
    return f'`{output}`'