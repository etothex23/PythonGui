import tkinter
import PySimpleGUI as Sg
from datetime import datetime, timedelta


class DateCalculator:

    def __init__(self) -> None:
        self.d_format = '%m / %d / %Y'
        self.current_date = datetime.now()
        self.days_to_add = 0
        self.future_date = datetime.now()
        self.past_date = datetime.now()
        self.add_or_sub = True
        self.icon = "wm-logo.ico"
        self.r_font = ('Verdana', 12)
        self.h_font = ('Arial bold', 20)
        self.e = None
        self.v = None
        self.calc_layout = [[Sg.Text('Current Date: ', text_color='#e2f0c6', background_color='#323232',
                                     pad=(10, 10), border_width=0, expand_x=True),
                             Sg.Text(self.getsdate(), text_color='#ecf5da', background_color='#323232',
                                     pad=(10, 10), key='cdate', border_width=2, relief='sunken')],
                            [Sg.Text(' Days to +/-: ', text_color='#e2f0c6', background_color='#323232',
                                     pad=(10, 10), border_width=0, expand_x=True),
                             Sg.InputText(0, 5, key='-INPUT-', enable_events=True, pad=(10, 10),
                                          background_color='#ffffff',
                                          border_width=1, justification='right', do_not_clear=True)],
                            [Sg.Text('Past Date: ', text_color='#e2f0c6', background_color='#323232',
                                     pad=(10, 10), border_width=0, expand_x=True),
                             Sg.Text(self.getsdate('p'), text_color='#ecf5da', background_color='#323232', pad=(10, 10),
                                     key='pdate', border_width=2, relief='sunken')],
                            [Sg.Text('Future Date: ', text_color='#e2f0c6', background_color='#323232',
                                     pad=(10, 10), border_width=0, expand_x=True),
                             Sg.Text(self.getsdate('f'), text_color='#ecf5da', background_color='#323232', pad=(10, 10),
                                     key='fdate', border_width=2, relief='sunken')]]
        self.layout = [[Sg.Text('Date Calculator', justification='c', font=self.h_font, size=(15, 1),
                                relief='ridge', border_width=2, text_color='#cde59e', background_color='#323232')],
                       [Sg.Frame(title='Calculate date:', title_color='#cde59e', title_location=Sg.TITLE_LOCATION_TOP,
                                 layout=self.calc_layout, border_width=2, pad=(10, 10),
                                 background_color='#3a3a3a', element_justification='right', expand_x=True)],
                       [Sg.Button('Calc', key='calc', button_color=("#eeeeee", "#3a3a3a")),
                        Sg.Exit(button_color=("#eeeeee", "#3a3a3a"))]]
        self.calculator = Sg.Window('Calculator', self.layout, icon=self.icon, background_color='#5c5c5c',
                                    element_justification='center', element_padding=(10, 10),
                                    margins=(10, 10), font=self.r_font, finalize=True)

    def focus_text(self):
        self.calculator['-INPUT-'].Widget.selection_range(0, tkinter.END)

    def getsdate(self, t='c'):
        if t == 'p':
            return datetime.strftime(self.past_date, self.d_format)
        elif t == 'f':
            return datetime.strftime(self.future_date, self.d_format)
        else:
            return datetime.strftime(self.current_date, self.d_format)

    def set_and_calc(self):
        self.future_date = self.current_date + timedelta(days=self.days_to_add)
        self.past_date = self.current_date + timedelta(days=-self.days_to_add)
        self.calculator['fdate'].update(self.getsdate('f'))
        self.calculator['pdate'].update(self.getsdate('p'))

    def Update(self, value=None, disabled=None, select=None, visible=None):
        select = True

    def exec_calc(self) -> None:
        self.calculator['-INPUT-'].Widget.selection_range(0, tkinter.END)
        while True:  # The Event Loop
            self.e, self.v = self.calculator.read()
            temp = self.v['-INPUT-']
            print(temp.isdigit())
            print(self.e)
            print(self.v)
            if self.e == Sg.WIN_CLOSED or self.e == 'Exit':
                break
            elif self.e == '-INPUT-' and not temp.isdigit():
                print('fuck')
                self.calculator['-INPUT-'].update(value='0')
                self.calculator['-INPUT-'].Widget.selection_range(0, tkinter.END)
            elif temp.isdigit():
                # self.calculator['-INPUT-'].Widget.config(insertbackgroundcolor='#d2ff93')
                self.calculator['-INPUT-'].Widget.config(background='#d2ff93')
                self.days_to_add = int(self.v['-INPUT-'])
                self.set_and_calc()
            print(self.days_to_add)
            print(self.future_date)

        self.calculator.close()


DateCalculator().exec_calc()
