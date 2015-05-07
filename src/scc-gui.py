#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 May. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : SCC
    Script Name  : scc-gui.py
    License      : GNU General Public License v3.0


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import os
import argparse as ap
from pathlib import Path
from datetime import datetime as dttm, time as tm, timedelta as td

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb

from sccdateentry import DateEntry
from scctimeentry import TimeEntry

import vau
import scc


class CSSApp(Frame):

    def __init__(self, parent=None, app_title=None, app_icon=None, app_height=-1, app_width=-1):

        def create_sub_frames(container):
            container.result_win = None
            return

        def create_widgets(container):
            container.de = DateEntry(container, " Date : ")
            container.de.hide_hints()
            container.de.set(date_value=dttm.now())
            container.de.grid(row=0, column=0, padx=(10, 5), pady=(5, 0),
                              sticky=(W, E))

            container.sr = TimeEntry(container, " Sunrise Time :")
            container.sr.hide_hints()
            container.sr.set(time_value=tm(hour=6, minute=30, second=0))
            container.sr.grid(row=1, column=0, padx=(10, 5), pady=(0, 0),
                              sticky=(W, E))

            container.ss = TimeEntry(container, " Sunset Time :")
            container.ss.hide_hints()
            container.ss.set(time_value=tm(hour=18, minute=30, second=0))
            container.ss.grid(row=2, column=0, padx=(10, 5), pady=(0, 0),
                              sticky=(W, E))

            container.nsr = TimeEntry(container, " Next Sunrise Time :")
            container.nsr.hide_hints()
            container.nsr.set(time_value=tm(hour=6, minute=30, second=0))
            container.nsr.grid(row=3, column=0, padx=(10, 5), pady=(0, 0),
                               sticky=(W, E))

            container.cf = TimeEntry(container, " Calculate for time :")
            container.cf.hide_hints()
            container.cf.set(time_value=dttm.now())
            container.cf.grid(row=4, column=0, padx=(10, 5), pady=(0, 5),
                              sticky=(W, E))

            container.calc_full_btn = Button(container,
                                             text=" Calculate Choghadiya for full day",
                                             command=container.calculate_full)
            container.calc_full_btn.grid(row=0, column=1, rowspan=4,
                                         padx=(0, 10), pady=(0, 0),
                                         sticky=W + E + S + N)

            container.calc_btn = Button(container,
                                        text=" Calculate Choghadiya for this moment",
                                        command=container.calculate)
            container.calc_btn.grid(row=4, column=1, padx=(0, 10), pady=(0, 5),
                                    sticky=W + E + S + N)
            return

        if parent is not None:
            self.parent = parent
        else:
            self.parent = Tk()

        super(CSSApp, self).__init__(parent)
        if app_title is None:
            self.master.title(f"Simple Choghadiya Calculator by VAU")
        else:
            self.master.title(f"{app_title} by VAU")

        create_sub_frames(self)
        create_widgets(self)

        if app_icon is None:
            spn = vau.get_script_filepath(__file__)
            logo_file_name = spn / Path('config/logo.png')
            if os.path.exists(logo_file_name):
                photo = PhotoImage(file=logo_file_name)
                self.master.iconphoto(False, photo)
            else:
                print('logo file not found.')
        else:
            if os.path.exists(app_icon):
                photo = PhotoImage(file=app_icon)
                self.master.iconphoto(False, photo)
            else:
                print('{} file not found.'.format(app_icon))
        self.pack()
        self.master.protocol("WM_DELETE_WINDOW", self.client_exit)
        return

    def client_exit(self):
        if self.ask("Decide", "Are you sure to exit?") == 'yes':
            self.master.destroy()
        else:
            self.show_message('Return', 'Ok then, you will now return to the application screen.')
        return

    def run(self):
        self.parent.mainloop()
        return

    def ask(self, title, question):
        self.bell()
        return mb.askquestion(title, question)

    def show_message(self, title, message):
        self.bell()
        mb.showinfo(title, message)
        return

    def disable_all_btn(self):
        self.calc_btn.config(state='disabled')
        self.calc_full_btn.config(state='disabled')
        return

    def enable_all_btn(self):
        self.calc_btn.config(state='normal')
        self.calc_full_btn.config(state='normal')
        return

    def calculate_full(self):
        d1 = self.de.get
        d2 = self.sr.get
        d3 = self.ss.get
        d4 = self.nsr.get
        answer = scc.calculate(d1, d2, d3, d4)
        self.bell()
        self.show_choghadiya(answer)
        return

    def calculate(self):
        self.disable_all_btn()
        d1 = self.de.get
        d2 = self.sr.get
        d3 = self.ss.get
        d4 = self.nsr.get
        d5 = self.cf.get

        answer = scc.calculate_for_specific_time(d1, d2, d3, d4, d5)

        text_ans = """Currently, at {0:%X}, on {1:} {4:} Choghadiyu is running. 
It started at {5:%X} and will last till {6:%X}.
        """.format(d5, *answer)
        self.bell()
        self.show_message("Result ...", text_ans)
        self.cf.set(dttm.now())
        self.enable_all_btn()
        return

    def show_choghadiya(self, ch_dict):
        self.disable_all_btn()
        self.result_win = Toplevel(self.master)
        self.result_win.protocol("WM_DELETE_WINDOW", self.close_result_win)

        ttl = "Choghadiya for Vedic day \"{:%A}\"".format(self.de.get)
        self.result_win.title(ttl)

        day_title = Label(self.result_win, text="Day Choghadiya")
        day_title.grid(row=0, column=0, columnspan=4)
        night_title = Label(self.result_win, text="Night Choghadiya")
        night_title.grid(row=0, column=6, columnspan=4)

        close_btn = Button(self.result_win, text="Close this window",
                           command=self.close_result_win)
        close_btn.grid(row=10, column=0, columnspan=10, sticky=(W, E))

        for k, v in ch_dict.items():
            for sk, sv in v.items():
                this_row = sk
                this_col = 0 if k == "D" else 6
                this_ch_nm = sv["N"]
                this_st_tm = "{:%X}".format(sv["S"])
                this_en_tm = "{:%X}".format(sv["E"])
                l1 = Label(self.result_win, text=sk)
                l1.grid(row=this_row + 1, column=this_col,
                        padx=(5, 0), pady=(5, 5), sticky=E)
                l2 = Label(self.result_win, text=this_ch_nm)
                l2.grid(row=this_row + 1, column=this_col + 1,
                        padx=(5, 5), pady=0, sticky=W)
                l3 = Label(self.result_win, text=this_st_tm)
                l3.grid(row=this_row + 1, column=this_col + 2,
                        padx=(5, 5), pady=0, sticky=E)
                l4 = Label(self.result_win, text=this_en_tm)
                if this_col == 0:
                    l4.grid(row=this_row + 1, column=this_col + 3,
                            padx=(5, 15), pady=0, sticky=W)
                else:
                    l4.grid(row=this_row + 1, column=this_col + 3,
                            padx=(5, 5), pady=0, sticky=W)

        vertical_sep = Separator(self.result_win, orient=VERTICAL)
        vertical_sep.grid(row=0, column=5, rowspan=10, sticky=(N, S))

        self.result_win.mainloop()
        return

    def close_result_win(self):
        self.enable_all_btn()
        self.result_win.destroy()
        return

    def setdate(self, new_value):
        if new_value is not None:
            self.de.set(new_value)
        return

    def setsunrise(self, new_value):
        if new_value is not None:
            self.sr.set(new_value)
        return

    def setsunset(self, new_value):
        if new_value is not None:
            self.ss.set(new_value)
        return

    def setnextsunrise(self, new_value):
        if new_value is not None:
            self.nsr.set(new_value)
        return

    def setcalcat(self, new_value):
        if new_value is not None:
            self.cf.set(new_value)

def main(arg1=None, arg2=None, arg3=None, arg4=None, arg5=None):
    app = CSSApp()
    app.setdate(arg1)
    app.setsunrise(arg2)
    app.setsunset(arg3)
    app.setnextsunrise(arg4)
    app.setcalcat(arg5)
    app.run()
    return


if __name__ == '__main__':
    scc_gui_parser = ap.ArgumentParser(prog='SCC',
                                       usage='%(prog)s [options]',
                                       description='Simple Choghadiya Calculator.',
                                       epilog="Simple and easy way to calculate "
                                              "Choghadiya that is part of Sanaatan "
                                              "Panchang."
                                       )
    scc_gui_parser.add_argument('-v', '--version', action='version',
                                version='%(prog)s 0.0.1 (Unstable Alpha)')

    date_group = scc_gui_parser.add_argument_group('date_group', 'Date Group')
    date_group.add_argument('-d', "--date",
                            help="Date - format YYYY-MM-DD",
                            required=False,
                            type=vau.date_type_validation,
                            default="{:%Y-%m-%d}".format(dttm.today()))

    events_group = scc_gui_parser.add_argument_group('events_group',
                                                     'Sun related events Group')
    events_group.add_argument("--sunrise",
                              help="Sunrise Time - format HH:MM[:SS]",
                              required=False,
                              type=vau.time_type_validation)
    events_group.add_argument("--sunset",
                              help="Sunset Time - format HH:MM[:SS]",
                              required=False,
                              type=vau.time_type_validation)
    events_group.add_argument("--next-sunrise",
                              help="Next Sunrise Time - format HH:MM[:SS]",
                              required=False,
                              type=vau.time_type_validation)
    scc_gui_parser.add_argument("--calc-at",
                                help="Calc for Time - format HH:MM[:SS]",
                                required=False,
                                type=vau.time_type_validation,
                                default="{:%H:%M:%S}".format(dttm.now().time()))
    args = scc_gui_parser.parse_args()

    if args.next_sunrise is None:
        args.next_sunrise = args.sunrise

    if args.calc_at is None:
        args.calc_at = dttm.now().time()
    main(args.date, args.sunrise, args.sunset, args.next_sunrise, args.calc_at)
