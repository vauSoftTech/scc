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
from pathlib import Path
from datetime import datetime as dttm, time as tm, timedelta as td

import vau
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb

from sccdateentry import DateEntry
from scctimeentry import TimeEntry
import scc


class CSSApp(Frame):

    def __init__(self, parent=None, app_title=None, app_icon=None, app_height=-1, app_width=-1):

        def create_sub_frames(container):
            return

        def create_widgets(container):
            container.de = DateEntry(container, " Date : ")
            container.de.hide_hints()
            container.de.set(date_value=dttm.now())
            container.de.grid(row=0, column=0, padx=50, pady=(5, 0), sticky=W)

            container.sr = TimeEntry(container, " Sunrise Time :")
            container.sr.hide_hints()
            container.sr.set(time_value=tm(hour=6, minute=30, second=0))
            container.sr.grid(row=1, column=0, padx=50, pady=(0, 0), sticky=W)

            container.ss = TimeEntry(container, " Sunset Time :")
            container.ss.hide_hints()
            container.ss.set(time_value=tm(hour=18, minute=30, second=0))
            container.ss.grid(row=2, column=0, padx=50, pady=(0, 0), sticky=W)

            container.nsr = TimeEntry(container, " Next Sunrise Time :")
            container.nsr.hide_hints()
            container.nsr.set(time_value=tm(hour=6, minute=30, second=0))
            container.nsr.grid(row=3, column=0, padx=50, pady=(0, 5), sticky=W)

            container.cf = TimeEntry(container, " Calculate for time :")
            container.cf.hide_hints()
            container.cf.set(time_value=dttm.now())
            container.cf.grid(row=4, column=0, padx=50, pady=(0, 5), sticky=W)

            container.calc_full_btn = Button(container, text=" Calculate Choghadiya for full day",
                                             command=container.calculate_full)
            container.calc_full_btn.grid(row=0, column=1, rowspan=4, padx=5, pady=(5, 0),
                                         sticky=W + E + S + N)

            container.calc_btn = Button(container, text=" Calculate Choghadiya for this moment",
                                        command=container.calculate)
            container.calc_btn.grid(row=4, column=1, padx=5, pady=(5, 0),
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
        self.calc_full_btn.config(state='disabled')
        self.calc_btn.config(state='disabled')
        return

    def enable_all_btn(self):
        self.calc_btn.config(state='normal')
        self.calc_full_btn.config(state='normal')
        return

    def calculate_full(self):
        self.disable_all_btn()
        d1 = dttm(self.de.get.year, self.de.get.month, self.de.get.day,
                  self.sr.get.hour, self.sr.get.minute, self.sr.get.second)
        # print(d1)
        d2 = dttm(self.de.get.year, self.de.get.month, self.de.get.day,
                  self.ss.get.hour, self.ss.get.minute, self.ss.get.second)
        # print(d2)
        d3 = dttm(self.de.get.year, self.de.get.month, self.de.get.day,
                  self.nsr.get.hour, self.nsr.get.minute, self.nsr.get.second)
        d3 = d3 + td(days=1)
        # print(d3)
        txt = "{} {}, {}".format(d1, d2, d3)
        self.show_message("Calculate for ...", txt)
        answer = scc.calculate(d1, d2, d3)
        self.show_message("Result ...", repr(answer))
        self.enable_all_btn()
        return

    def calculate(self):
        self.disable_all_btn()
        d1 = dttm(self.de.get.year, self.de.get.month, self.de.get.day,
                  self.sr.get.hour, self.sr.get.minute, self.sr.get.second)
        # print(d1)
        d2 = dttm(self.de.get.year, self.de.get.month, self.de.get.day,
                  self.ss.get.hour, self.ss.get.minute, self.ss.get.second)
        # print(d2)
        d3 = dttm(self.de.get.year, self.de.get.month, self.de.get.day,
                  self.nsr.get.hour, self.nsr.get.minute, self.nsr.get.second)
        d3 = d3 + td(days=1)

        d4 = dttm(self.de.get.year, self.de.get.month, self.de.get.day,
                  self.cf.get.hour, self.cf.get.minute, self.cf.get.second)

        d5 = d3.replace(hour=0, minute=0, second=0)

        if d1 <= d4 < d5:
            pass
        else:
            d4 = d4.replace(d5.year, d5.month, d5.day)

        print(d4)

        answer = scc.calculate_for_specific_time(d1, d2, d3, d4)

        text_ans = """Currently, at {0:%X}, on {1:} {4:} Choghadiyu is running. 
It started at {5:%X} and will last till {6:%X}.
        """.format(d4, *answer)
        self.show_message("Result ...", text_ans)
        self.cf.set(dttm.now())
        self.enable_all_btn()
        return


def main():
    app = CSSApp()
    app.run()
    return


if __name__ == '__main__':
    main()
