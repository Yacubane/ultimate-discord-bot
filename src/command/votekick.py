class Votekick:
    db = {}

    def run(self, args):
        if not args.mentions:
            return "Podaj kogo mam kiknąć, np, @zajma"
        voted_user = args.mentions[0]
        if not (voted_user.id in self.db):
            self.db[voted_user.id] = 0
        self.db[voted_user.id] += 1
        counter = self.db[voted_user.id]
        return f'<@!{voted_user.id}> voted kick nr: {counter}'

    def stats(self):
        if not self.db:
            return "nikogo nie trzeba kiknąć"
        return "\n".join([f'<@!{user_id}> voted kick nr: {counter}' for user_id, counter in self.db.items()])
