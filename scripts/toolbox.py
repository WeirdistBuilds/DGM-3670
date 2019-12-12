import maya.cmds as cmds
import calculator as calc
import centerLocator as center
import colorChanger as color
import controlCreator as control
import randomSpawner as randspawn
import sequentialRenamer as rename


class Toolbox:
    def __init__(self):
        self.window_name = 'kh_toolbox'
        self.calc_column = 'kh_calc_column'
        self.calc_radio_buttons = 'kh_calc_radio_buttons'
        self.calc_radio_buttons_2 = 'kh_calc_radio_buttons_2'
        self.calc_number_field = 'kh_calc_number_field'
        self.calc_answer_field = 'kh_calc_answer_field'
        self.calc_button = 'kh_calc_button'
        self.center_column = 'kh_center_column'
        self.center_checkbox_group = 'kh_center_checkbox_group'
        self.center_button = 'kh_center_button'
        self.color_column = 'kh_color_column'
        self.color_field = 'kh_color_field'
        self.color_button = 'kh_color_button'
        self.control_column = 'kh_control_column'
        self.control_field = 'kh_control_field'
        self.control_button = 'kh_control_button'
        self.random_column = 'kh_random_column'
        self.random_amount_field = 'kh_random_amount_field'
        self.random_grow_checkbox = 'kh_random_grow_checkbox'
        self.random_range_field = 'kh_random_range_field'
        self.random_scale_lower_field = 'kh_random_scale_lower_field'
        self.random_scale_upper_field = 'kh_random_scale_upper_field'
        self.random_button = 'kh_random_button'
        self.rename_column = 'kh_rename_column'
        self.rename_field = 'kh_rename_field'
        self.rename_button = 'kh_rename_button'
        self.calc_title = 'kh_calc_title'
        self.calc_row_1 = 'kh_calc_row_1'
        self.calc_row_2 = 'kh_calc_row_2'
        self.calc_buffer = 'kh_calc_buffer'
        self.center_title = 'kh_center_title'
        self.center_row_1 = 'kh_center_row_1'
        self.center_row_2 = 'kh_center_row_2'
        self.center_individual_checkbox = 'kh_center_individual_checkbox'
        self.center_blank = 'kh_center_blank'
        self.center_rotation_checkbox = 'kh_rotation_checkbox'
        self.center_buffer = 'kh_center_buffer'
        self.color_title = 'kh_color_title'
        self.color_row_1 = 'kh_color_row_1'
        self.color_row_2 = 'kh_color_row_2'
        self.color_text = 'kh_color_text'
        self.color_buffer = 'kh_color_buffer'
        self.control_title = 'kh_control_title'
        self.control_row_1 = 'kh_control_row_1'
        self.control_row_2 = 'kh_control_row_2'
        self.control_text = 'kh_control_text'
        self.control_blank = 'kh_control_blank'
        self.control_buffer = 'kh_control_buffer'
        self.random_title = 'kh_random_title'
        self.random_row_1 = 'kh_random_row_1'
        self.random_row_2 = 'kh_random_row_2'
        self.random_row_3 = 'kh_random_row_3'
        self.random_row_4 = 'kh_random_row_4'
        self.random_row_5 = 'kh_random_row_5'
        self.random_text_1 = 'kh_random_text_1'
        self.random_blank_1 = 'kh_random_blank_1'
        self.random_text_2 = 'kh_random_text_2'
        self.random_text_3 = 'kh_random_text_3'
        self.random_text_4 = 'kh_random_text_4'
        self.random_buffer = 'kh_random_buffer'
        self.rename_title = 'kh_rename_title'
        self.rename_row = 'kh_rename_row'
        self.rename_text = 'kh_rename_text'
        self.rename_buffer = 'kh_rename_buffer'

    def create(self):
        self.delete()
        self.window_name = cmds.window(self.window_name)
        # calculator
        self.calc_column = cmds.columnLayout(p=self.window_name, adj=True)
        self.calc_title = cmds.text(label='CALCULATOR')
        self.calc_radio_buttons = cmds.radioButtonGrp(p=self.calc_column,
                                                      numberOfRadioButtons=4,
                                                      label='Calculator Functions',
                                                      labelArray4=['Add', 'Subtract', 'Multiply', 'Divide'])
        self.calc_radio_buttons_2 = cmds.radioButtonGrp(p=self.calc_column,
                                                        numberOfRadioButtons=4,
                                                        shareCollection=self.calc_radio_buttons,
                                                        label='',
                                                        labelArray4=['Power', 'Mean', 'Median', 'Mode'])
        self.calc_row_1 = cmds.rowLayout(p=self.calc_column, adj=True, numberOfColumns=2)
        self.calc_number_field = cmds.textField(p=self.calc_row_1,
                                                placeholderText='Enter numbers, separated by spaces and/or commas.')
        self.calc_row_2 = cmds.rowLayout(p=self.calc_column, adj=True, numberOfColumns=2)
        self.calc_button = cmds.button(p=self.calc_row_2,
                                       label='Calculate',
                                       c=lambda *args: self.calc_call())
        self.calc_answer_field = cmds.textField(p=self.calc_row_2,
                                                placeholderText='Answer appears here.')
        self.calc_buffer = cmds.text(p=self.calc_column, label='\n')
        # center locator
        self.center_column = cmds.columnLayout(p=self.window_name, adj=True)
        self.center_title = cmds.text(p=self.center_column, label='CENTER LOCATOR')
        self.center_row_1 = cmds.rowLayout(p=self.center_column, adj=True, numberOfColumns=2)
        self.center_individual_checkbox = cmds.checkBox(p=self.center_row_1, label='Give Individual Centers')
        self.center_rotation_checkbox = cmds.checkBox(p=self.center_row_1, label='Match Rotation')
        self.center_row_2 = cmds.rowLayout(p=self.center_column, adj=True, numberOfColumns=2)
        self.center_button = cmds.button(p=self.center_row_2,
                                         label='Locate Center(s)',
                                         c=lambda *args: self.center_call())
        self.center_buffer = cmds.text(p=self.center_column, label='\n')
        # color changer
        self.color_column = cmds.columnLayout(p=self.window_name, adj=True)
        self.color_title = cmds.text(p=self.color_column, label='COLOR CHANGER')
        self.color_row_1 = cmds.rowLayout(p=self.color_column, adj=True, numberOfColumns=2)
        self.color_text = cmds.text(p=self.color_row_1, label='Color:', width=150)
        self.color_field = cmds.textField(p=self.color_row_1,
                                          placeholderText='Enter red, blue, yellow, '
                                                          'green, purple, orange, black, or white.')
        self.color_row_2 = cmds.rowLayout(p=self.color_column, adj=True, numberOfColumns=2)
        self.color_button = cmds.button(p=self.color_row_2,
                                        label='Change Color',
                                        c=lambda *args: self.color_call())
        self.color_buffer = cmds.text(p=self.color_column, label='\n')
        # control creator
        self.control_column = cmds.columnLayout(p=self.window_name, adj=True)
        self.control_title = cmds.text(p=self.control_column, label='CONTROL CREATOR')
        self.control_row_1 = cmds.rowLayout(p=self.control_column, adj=True, numberOfColumns=2)
        self.control_text = cmds.text(p=self.control_row_1, label='Color:', width=150)
        self.control_field = cmds.textField(p=self.control_row_1,
                                            placeholderText='Enter red, blue, yellow, '
                                                            'green, purple, orange, black, or white.')
        self.control_row_2 = cmds.rowLayout(p=self.control_column, adj=True, numberOfColumns=2)
        self.control_button = cmds.button(p=self.control_row_2,
                                          label='Create Control(s)',
                                          c=lambda *args: self.control_call())
        self.control_buffer = cmds.text(p=self.control_column, label='\n')
        # random spawn
        self.random_column = cmds.columnLayout(p=self.window_name, adj=True)
        self.random_title = cmds.text(p=self.random_column, label='RANDOM SPAWNER')
        self.random_row_1 = cmds.rowLayout(p=self.random_column, adj=True, numberOfColumns=2)
        self.random_text_1 = cmds.text(p=self.random_row_1, label='Amount: ', width=150)
        self.random_amount_field = cmds.intField(p=self.random_row_1)
        self.random_row_2 = cmds.rowLayout(p=self.random_column, adj=True, numberOfColumns=2)
        self.random_text_2 = cmds.text(p=self.random_row_2, label='Move Range:', width=150)
        self.random_range_field = cmds.intField(p=self.random_row_2)
        self.random_row_3 = cmds.rowLayout(p=self.random_column, adj=True, numberOfColumns=2)
        self.random_text_3 = cmds.text(p=self.random_row_3, label='Lower Scale Bound:', width=150)
        self.random_scale_lower_field = cmds.intField(p=self.random_row_3)
        self.random_row_4 = cmds.rowLayout(p=self.random_column, adj=True, numberOfColumns=2)
        self.random_text_4 = cmds.text(p=self.random_row_4, label='Upper Scale Bound:', width=150)
        self.random_scale_upper_field = cmds.intField(p=self.random_row_4)
        self.random_row_5 = cmds.rowLayout(p=self.random_column, adj=True, numberOfColumns=2)
        self.random_grow_checkbox = cmds.checkBox(p=self.random_row_5, label='Mushroom-Style Growth')
        self.random_button = cmds.button(p=self.random_column,
                                         label='Randomly Spawn',
                                         c=lambda *args: self.random_call())
        self.random_buffer = cmds.text(p=self.random_column, label='\n')
        # sequential rename
        self.rename_column = cmds.columnLayout(p=self.window_name, adj=True)
        self.rename_title = cmds.text(p=self.rename_column, label='SEQUENTIAL RENAMER')
        self.rename_row_1 = cmds.rowLayout(p=self.rename_column, adj=True, numberOfColumns=2)
        self.rename_text = cmds.text(p=self.rename_row_1, label='Text Format:', width=150)
        self.rename_field = cmds.textField(p=self.rename_row_1,
                                           placeholderText='eg. Kyle_###_Geo')
        self.rename_row_2 = cmds.rowLayout(p=self.rename_column, adj=True, numberOfColumns=2)
        self.rename_button = cmds.button(p=self.rename_row_2,
                                         label='Sequentially Rename',
                                         c=lambda *args: self.rename_call())
        self.rename_buffer = cmds.text(p=self.rename_column, label='\n')
        # show window
        cmds.showWindow(self.window_name)

    def delete(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)

    def calc_call(self):
        current_calc = calc.Calculator()
        calc_values = cmds.textField(self.calc_number_field, query=True, text=True)
        nums = [float(x) for x in calc_values.split(",")]
        operation = cmds.radioButtonGrp(self.calc_radio_buttons, query=True, sl=True)
        if operation == 0:
            operation = cmds.radioButtonGrp(self.calc_radio_buttons_2, query=True, sl=True) + 4
        result = {
            1: lambda: calc.Calculator.add(current_calc, nums),
            2: lambda: calc.Calculator.subtract(current_calc, nums),
            3: lambda: calc.Calculator.multiply(current_calc, nums),
            4: lambda: calc.Calculator.divide(current_calc, nums),
            5: lambda: calc.Calculator.power(current_calc, nums),
            6: lambda: calc.Calculator.mean(current_calc, nums),
            7: lambda: calc.Calculator.median(current_calc, nums),
            8: lambda: calc.Calculator.mode(current_calc, nums)
        }.get(operation, lambda: "Invalid operation number")()
        cmds.textField(self.calc_answer_field, e=True, text=result)

    def center_call(self):
        give_individual = cmds.checkBox(self.center_individual_checkbox, query=True, value=True)
        match_rotation = cmds.checkBox(self.center_rotation_checkbox, query=True, value=True)
        center.center_locator(give_individual, match_rotation)

    def color_call(self):
        color_value = cmds.textField(self.color_field, query=True, text=True)
        color.color_changer(color_value)
        cmds.textField(self.color_field, e=True, text='')

    def control_call(self):
        control_value = cmds.textField(self.color_field, query=True, text=True)
        control.control_creator(control_value)
        cmds.textField(self.control_field, e=True, text='')

    def random_call(self):
        random_amount = cmds.intField(self.random_amount_field, query=True, value=True)
        random_grow = cmds.checkBox(self.random_grow_checkbox, query=True, value=True)
        random_range = cmds.intField(self.random_range_field, query=True, value=True)
        random_upper = cmds.intField(self.random_scale_upper_field, query=True, value=True)
        random_lower = cmds.intField(self.random_scale_lower_field, query=True, value=True)
        randspawn.random_spawner(random_amount, random_grow, random_range, random_lower, random_upper)

    def rename_call(self):
        name_format = str(cmds.textField(self.rename_field, query=True, text=True))
        rename.sequential_renamer(name_format)

# import toolbox
# myTB = toolbox.Toolbox()
# myTB.create()
