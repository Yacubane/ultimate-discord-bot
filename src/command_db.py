from src.command.test_cmd import TestCMD
from src.command.votekick_zajma import VotekickZajma
from src.command.bajo_jajo import bajo_jajo
from src.command.help import print_help
from src.command.votekick import Votekick
from src.command.run_code import run_code
from src.command.ciri import Ciri
from src.command.decide import decide
from src.command.voice import Voice
from src.command.cppify import cppify

test_cmd = TestCMD()
votekick_zajma = VotekickZajma()
votekick = Votekick()
ciri = Ciri()
voice = Voice()

context_free_command_db = {
    '+test': lambda context, client: test_cmd.run(),
    '+votekick zajma': lambda context, client: votekick_zajma.run(),
    '+bajo jajo': lambda context, client: bajo_jajo(),
    '+help': lambda context, client: print_help(),
    '+votekick stats': lambda context, client: votekick.stats(),
    '+ciri': lambda context, client: ciri.run(),
}

start_with_command_db = {
    '+votekick': lambda args: votekick.run(args),
    '+run': lambda args: run_code(args),
    '+czy': lambda args: decide(),
    '+cppify': lambda args: cppify(args)
}

async_command_db = {
    '+płotnik': voice.run,
}
