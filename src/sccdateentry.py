#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 May. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : SCC
    Script Name  : dateentry.py (Called from scc-gui.py)
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
from tkinter import *
from tkinter.ttk import *
from datetime import datetime as dttm

import calendar


class DateEntry(Frame):

    def __init__(self, parent, text_label):
        super(DateEntry, self).__init__(parent)
        self.dd_var = IntVar()
        self.mm_var = StringVar()
        self.yy_var = IntVar()
        self.month_names = tuple(calendar.month_abbr)

        self.dd_var.set(1)
        self.mm_var.set('Jan')
        self.yy_var.set(1940)

        self.hints = True
        self.ld = Label(self, text="Day")
        self.ld.grid(row=0, column=1)
        self.lm = Label(self, text="Month")
        self.lm.grid(row=0, column=2)
        self.ly = Label(self, text="Year")
        self.ly.grid(row=0, column=3)

        self.l1 = Label(self, text=text_label)
        self.l1.grid(row=1, column=0, padx=(5, 5), pady=(5, 5))

        self.e1 = Spinbox(self, width=2, from_=1, to=31, increment=1, wrap=True,
                          textvariable=self.dd_var, validate="focusout",
                          validatecommand=self.dd_validate,
                          invalidcommand=self.dd_invalid,
                          state='readonly')
        self.e1.grid(row=1, column=1)
        self.e1.bind("<<Increment>>", lambda _: print("<<Increment>>"))
        self.e1.bind("<<Decrement>>", lambda _: print("<<Decrement>>"))

        self.e2 = Spinbox(self, width=4, increment=1, wrap=True,
                          textvariable=self.mm_var, state='readonly',
                          values=tuple(self.month_names))
        self.e2.grid(row=1, column=2)

        self.e3 = Spinbox(self, width=5, from_=1000, to=3000, increment=1, wrap=True,
                          textvariable=self.yy_var)
        self.e3.grid(row=1, column=3)

        self.bind('<FocusIn>', self.focus_in)
        self.bind('<FocusOut>', self.focus_out)
        self.configure(relief="groove", borderwidth=3)
        return

    @property
    def get(self):
        return dttm(self.yy_var.get(), self.month_names.index(self.mm_var.get()), self.dd_var.get())

    def set(self, date_value):
        self.yy_var.set(date_value.year)
        self.mm_var.set(self.month_names[date_value.month])
        self.dd_var.set(date_value.day)
        return

    def dd_validate(self):
        v = self.dd_var.get()
        # print(self.mm_var.get())
        x = self.month_names.index(self.mm_var.get())
        if (x in [1, 3, 5, 7, 8, 10, 12]) and (1 <= v <= 31):
            return True
        elif (x in [4, 6, 9, 11]) and (1 <= v <= 30):
            return True
        elif x == 2 and (1 <= v <= 29):
            return True
        else:
            return False

    def dd_invalid(self):
        v = self.dd_var.get()
        if v < 1:
            self.dd_var.set(1)
        elif v > 31:
            x = self.month_names.index(self.mm_var.get())
            if x in [1, 3, 5, 7, 8, 10, 12]:
                self.dd_var.set(31)
            elif x in [4, 6, 9, 11]:
                self.dd_var.set(30)
            else:
                self.dd_var.set(28)
        return True

    def dd_increment(self):
        # print(self.dd_var.get())
        return

    def dd_decrement(self):
        # print(self.dd_var.get())
        return

    def focus_in(self, event):
        # print(event, "event occurred.")
        self.e1.focus_force()
        return

    def focus_out(self, event):
        # print(event, "event occurred.")
        try:
            x = self.get
            print(x)
        except ValueError as e:
            print(e)
            x = dttm.now()
            self.set(x)
        return

    def show_hints(self):
        self.ld.grid(row=0, column=1)
        self.lm.grid(row=0, column=2)
        self.ly.grid(row=0, column=3)
        self.hints = True
        return

    def hide_hints(self):
        self.ld.grid_forget()
        self.lm.grid_forget()
        self.ly.grid_forget()
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
    de = DateEntry(root, "Enter a Date : ")
    de.grid(padx=50, pady=50)
    de.set(dttm.now())
    b = Button(root, text="Toggle Hints", command=de.toggle_hints)
    b.grid(padx=50, pady=50)
    root.mainloop()
    print(de.get)


if __name__ == '__main__':
    main()
