#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 May. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : SCC
    Script Name  : timeentry.py (Called from scc-gui.py)
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
from datetime import datetime as dttm
from datetime import time as tm
from tkinter import *
from tkinter.ttk import *


class TimeEntry(Frame):

    def __init__(self, parent, text_label):
        super(TimeEntry, self).__init__(parent)

        self.hh_values = tuple(x for x in range(0, 24))
        self.mm_values = tuple(x for x in range(0, 60))
        self.ss_values = tuple(x for x in range(0, 60))

        self.hh_var = IntVar()
        self.mm_var = IntVar()
        self.ss_var = IntVar()

        self.hh_var.set(2)
        self.mm_var.set(37)
        self.ss_var.set(10)

        self.hints = True
        self.lh = Label(self, text=" Hour ")
        self.lh.grid(row=0, column=1, padx=(0, 5))
        self.lm = Label(self, text=" Minute ")
        self.lm.grid(row=0, column=2, padx=(5, 5))
        self.ls = Label(self, text=" Second ")
        self.ls.grid(row=0, column=3, padx=(5, 0))

        self.l1 = Label(self, text=text_label)
        self.l1.grid(row=1, column=0, padx=(5, 5), pady=(5, 5))

        self.e1 = Spinbox(self, width=2, increment=1, wrap=True,
                          textvariable=self.hh_var, validate="focusout",
                          state='readonly', values=self.hh_values)
        self.e1.grid(row=1, column=1)
        self.e1.bind("<<Increment>>", lambda _: print("<<Increment>>"))
        self.e1.bind("<<Decrement>>", lambda _: print("<<Decrement>>"))

        self.e2 = Spinbox(self, width=2, increment=1, wrap=True,
                          textvariable=self.mm_var, state='readonly',
                          values=self.mm_values)
        self.e2.grid(row=1, column=2)

        self.e3 = Spinbox(self, width=2, from_=1000, to=3000, increment=1,
                          wrap=True, textvariable=self.ss_var, state='readonly',
                          values=self.ss_values)
        self.e3.grid(row=1, column=3)

        self.bind('<FocusIn>', self.focus_in)
        self.bind('<FocusOut>', self.focus_out)
        self.configure(relief="groove", borderwidth=3)
        return

    @property
    def get(self):
        # print(tm(self.hh_var.get(), self.mm_var.get(), self.ss_var.get()))
        return tm(self.hh_var.get(), self.mm_var.get(), self.ss_var.get())

    def set(self, time_value):
        self.hh_var.set(time_value.hour)
        self.mm_var.set(time_value.minute)
        self.ss_var.set(time_value.second)
        return

    def focus_in(self, event):
        # print(event, "occurred.")
        self.e1.focus_force()
        return

    def focus_out(self, event):
        # print(event, "occurred.")
        try:
            x = self.get
            print(x)
        except ValueError as e:
            print(e)
            self.set(dttm.now().time())
        return

    def show_hints(self):
        self.lh.grid(row=0, column=1)
        self.lm.grid(row=0, column=2)
        self.ls.grid(row=0, column=3)
        self.hints = True
        return

    def hide_hints(self):
        self.lh.grid_forget()
        self.lm.grid_forget()
        self.ls.grid_forget()
        self.hints = False
        return

    def toggle_hints(self):
        if self.hints:
            self.hide_hints()
        else:
            self.show_hints()
        return


def main():
    root = Tk()
    de = TimeEntry(root, "Enter Time : ")
    de.grid(padx=50, pady=50)
    de.set(dttm.now().time())
    b = Button(root, text="Toggle Hints", command=de.toggle_hints)
    b.grid(padx=50, pady=50)
    root.mainloop()
    print(de.get)


if __name__ == '__main__':
    main()
