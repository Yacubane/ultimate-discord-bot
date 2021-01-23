from src.utils.utils import rand_item


class VotekickZajma:
    counter = 0
    responses = [
        lambda args: f'Zajma ogarnij się, to już dziś {args["counter"]} raz'
    ]

    def run(self):
        self.counter += 1
        return rand_item(self.responses)({'counter': self.counter})
