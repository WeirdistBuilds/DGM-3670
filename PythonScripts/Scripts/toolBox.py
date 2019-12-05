import maya.cmds as cmds


class ToolBox():
    def __init__(self):
        self.window_name = 'kh_toolbox'

    def create(self):
        self.delete()
        self.window_name = cmds.window(self.window_name)
        self.m_column = cmds.columnLayout(p=self.window_name, adj=True)
        self.color_field = cmds.textField(p=self.m_column,
                                          label='color_field',
                                          placeholderText='Enter color name...')

        cmds.button(p=self.m_column,
                    label='color_button',
                    c=lambda *args: self.color_button())
        cmds.button(p=self.m_column,
                    label='select_everything_button',
                    c=lambda *args: self.select_button())
        cmds.button(p=self.m_column,
                    label='ball',
                    c=lambda *args: self.ball_button())

        cmds.showWindow(self.window_name)

    def delete(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)

    def ball_button(self):
        from tools import ball
        ball()

    def select_button(self):
        from tools import select_all
        select_all()

    def color_button(self):
        value = cmds.textField(self.color_field, query=True, text=True)
        self.color_changer(value)
        cmds.textField(self.color_field, e=True, text='')

    def color_changer(self, color):
        this_color = {
            'yellow': lambda: 16,
            'red': lambda: 12,
            'blue': lambda: 5,
            'green': lambda: 13,
            'purple': lambda: 7,
            'orange': lambda: 11,
            'black': lambda: 1,
            'white': lambda: 15
        }.get(color, lambda: 6)()

        selection = cmds.ls(sl=True)
        shapes = cmds.listRelatives(selection, shapes=True, children=True)
        for shape in shapes:
            cmds.setAttr('%s.overrideEnabled' % shape, True)
            cmds.setAttr('%s.overrideColor' % shape, this_color)
