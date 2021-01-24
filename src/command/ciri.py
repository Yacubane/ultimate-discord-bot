from src.utils.utils import rand_item


class Ciri:
    responses = [
        "- Puk puk.\n- Kto tam?\n- Napewno nie Ciri :/",
        "Zajmie umarła Ciri",
        "Zajma zabił Ciri",
        "Wiadomo kto, wiadomo kogo - Zajma, Ciri",
        "nk wytłumaczy dlaczego on ją zabił :/",
        "ej ej Kuba, czemu ją zabiłeś?",
        "Czemu Ciri nie zje dziś obiadku?\n- Bo nie żyje",
        "Cześć Kuba, widziałeś może dzieś Ciri?",
        "Zajma, co tam u Ciri?",
    ]

    def run(self):
        return rand_item(self.responses)
