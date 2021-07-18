import wx

from chessclassic_out import BaseGameFrame, BaseMenuFrame


class MenuFrame(BaseMenuFrame):
    ...


class GameFrame(BaseGameFrame):
    ...


class ChessClassicApp(wx.App):
    def __init__(self, *args, **kwargs):
        self.menu_frame = None
        self.game_frames = []

        super().__init__(*args, **kwargs)

    def OnInit(self):
        self.menu_frame = MenuFrame(None, wx.ID_ANY, 'ChessClassic Menu')

        self.SetTopWindow(self.menu_frame)
        self.menu_frame.Show()

        return True
