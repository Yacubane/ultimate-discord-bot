from src.command.test_cmd import TestCMD
from src.command.bajo_jajo import bajo_jajo
from src.command.help import print_help
from src.command.votekick import Votekick
from src.command.run_code import run_code
from src.command.ciri import Ciri
from src.command.decide import decide
from src.command.voice import Voice
from src.command.cppify import cppify


class CommandDB:
    test_cmd = TestCMD()
    ciri = Ciri()
    vote_kick = None
    voice = None

    context_free_command_db = {}
    start_with_command_db = {}
    async_command_db = {}

    def __init__(self, client):
        self.voice = Voice(client)
        self.vote_kick = Votekick(client)
        self.context_free_command_db = {
            '+test': lambda context, client: self.test_cmd.run(),
            '+bajo jajo': lambda context, client: bajo_jajo(),
            '+help': lambda context, client: print_help(),
            '+votekick stats': lambda context, client: self.vote_kick.stats(),
            '+ciri': lambda context, client: self.ciri.run(),
        }

        self.start_with_command_db = {
            '+run': lambda args: run_code(args),
            '+czy': lambda args: decide(),
            '+cppify': lambda args: cppify(args)
        }

        self.async_command_db = {
            '+płotnik': self.voice.run,
            '+votekick': self.vote_kick.run
        }
