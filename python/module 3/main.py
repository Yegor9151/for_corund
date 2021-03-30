from first_engine.game import Game


class FirstGame(Game):

    def run(self) -> None:

        while self.runner:
            for event in self.events():
                self.close(event)


FirstGame(width=600, height=400).run()
