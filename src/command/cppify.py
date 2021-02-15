import re
import random


def cppify(message):
    transformed = message.content.lower().replace("+cppify ", '')
    if random.randint(0, 1) % 2:
        transformed = transformed.title()
        if random.randint(0, 1) % 2:
            transformed = transformed[:1].lower() + transformed[1:]
    else:
        vowels = "aąeęiouy"
        transformed = re.sub(r'[' + vowels + '\s*]', '', transformed)
    for diacritic, replacement in [('ą', 'a'), ('ę', 'e'), ('ś', 's'),
                                   ('ż', 'z'), ('ć', 'c'), ('ń', 'n'),
                                   ('ó', 'o'), ('ł', 'l')]:
        transformed = transformed.replace(diacritic, replacement)
    transformed = re.sub(r"[^a-zA-Z0-9_]", "", transformed, 0, re.MULTILINE)
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
