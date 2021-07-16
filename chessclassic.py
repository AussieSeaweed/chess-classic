import wx

from chessclassic_out import BaseGameFrame, BaseMenuFrame


class MenuFrame(BaseMenuFrame):
    ...


class GameFrame(BaseGameFrame):
    ...


class ChessClassicApp(wx.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.menu_frame = None
        self.game_frame = None

    def OnInit(self):
        self.menu_frame = MenuFrame(None, wx.ID_ANY, 'Menu')
        self.game_frame = GameFrame(None, wx.ID_ANY, 'Game')

        self.SetTopWindow(self.menu_frame)
        self.menu_frame.Show()

        return True
