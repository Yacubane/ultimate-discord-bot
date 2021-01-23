from src.command.test_cmd import TestCMD
from src.command.votekick_zajma import VotekickZajma

test_cmd = TestCMD()
votekick_zajma = VotekickZajma()

command_db = {
    '+test': lambda args: test_cmd.run(),
    '+votekick zajma': lambda args: votekick_zajma.run()
}
