from processing_py import App


class ChessClassicApp(App):
    def __init__(self, settings):
        super().__init__(settings.WIDTH, settings.HEIGHT)
