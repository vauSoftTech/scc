#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 May. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : SCC
    Script Name  : choghadiya.py
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

from datetime import datetime as dttm, timedelta as td

import info as ci


class Choghadiya:
    """
        This is main Choghadiya Class.

        It contains each single Choghadiya as an Inner class called Choghadiyu.
    """

    class Choghadiyu:
        """
            This is inner class that represents a single Choghadiyu
        """

        def __init__(self, idx, start, end, ch_name):
            # x = "Choghadiyu __init__  start {}, " \
            #     "{:%H:%M}, {:%H:%M}, {}".format(
            #     idx, start, end, ch_name)
            # utils.log_debug(x)
            self.idx = idx
            self.start = start
            self.end = end
            self.ch_name = ch_name
            # utils.log_debug("Choghadiyu __init__ ended.")

        def __repr__(self):
            x = "Choghadiyu({}, {},{}, {})".format(self.idx, self.start,
                                                   self.end,
                                                   self.ch_name)
            return x

        def __str__(self):
            x = "{:>02} {:7.7s} " \
                "{:%H:%M}-{:%H:%M}".format(self.idx, self.ch_name, self.start,
                                           self.end)
            return x

        def is_running_at(self, this_dttm=dttm.now()):
            return self.start <= this_dttm <= self.end

        @property
        def mid_point(self):
            return self.start + ((self.end - self.start) / 2)

        def elapsed(self, this_dttm=dttm.now()):
            if self.is_running_at(this_dttm):
                return ((this_dttm - self.start) /
                        (self.end - self.start)) * 100
            else:
                if self.start < self.end < this_dttm:
                    return 100
                elif this_dttm < self.start:
                    return 0
                else:
                    return -1

        @property
        def ruling_planet(self):
            return ci.Info.get_ruling_planet(self.ch_name)

        @property
        def ch_type(self):
            return ci.Info.get_type(self.ch_name)

        @property
        def good_for(self):
            return ci.Info.get_good_for(self.ch_name)

        @property
        def gujarati_name(self):
            return ci.Info.get_gujarati_name(self.ch_name)

    ############################################################################
    #
    # OUTER CLASS
    #
    ############################################################################
    def __init__(self, for_date, sunrise_time, sunset_time, next_sunrise=None):
        def merge_date_and_time(dt_part, tm_part):
            return dttm(dt_part.year, dt_part.month, dt_part.day,
                        tm_part.hour, tm_part.minute, tm_part.second,
                        tm_part.microsecond)

        # x = "Choghadiya __init__ start:  {:%Y-%m-%d %H:%M}," \
        #     "{:%H:%M}, """.format(sunrise_dttm, sunset_dttm)
        # utils.log_debug(x)

        if next_sunrise is None:
            next_sunrise = sunset_time
        self.st_dttm = merge_date_and_time(for_date, sunrise_time)
        self.md_dttm = merge_date_and_time(for_date, sunset_time)
        self.en_dttm = merge_date_and_time(for_date + td(days=1),
                                           next_sunrise)

        if self.st_dttm < self.md_dttm < self.en_dttm:
            pass
        else:
            raise ValueError("Invalid parameter Chronology.")

        self._ch = {i: None for i in range(1, 17)}
        self.ready = False
        self._prepare_slots_()
        # utils.log_debug("Choghadiya __init__ done.")

    def __repr__(self):
        return "Choghadiya({0:%Y-%m-%d}, {0:%H:%M}, {1:%H:%M}, {2:%H:%M})" \
            .format(self.st_dttm, self.md_dttm, self.en_dttm)

    def __str__(self):
        return "Choghadiya for Vedic day {:%A}".format(self.st_dttm)

    def _prepare_slots_(self):
        if self.ready:
            return

        wk_day_no = self.st_dttm.isoweekday()
        ch_list = list(ci.Info.choghadiya_names_gen(wk_day_no))

        st = self.st_dttm
        ln = self.day_choghadiya_length
        en = st + ln
        for i in range(1, 9):
            self._ch[i] = Choghadiya.Choghadiyu(i, st, en, ch_list[i - 1])
            st, en = en, en + ln

        st = self.md_dttm
        ln = self.night_choghadiya_length
        en = st + ln

        for i in range(9, 17):
            self._ch[i] = Choghadiya.Choghadiyu(i, st, en,
                                                ch_list[i - 1])
            st, en = en, en + ln

        self.ready = True
        return None

    def get_choghadiyu(self, idx):
        return self._ch[idx]

    def current_choghadiyu(self, curr_time=dttm.now()):
        if not self.ready:
            return None
        result = list(self.get_choghadiyu(i)
                      for i in range(1, 17)
                      if self.get_choghadiyu(i).is_running_at(curr_time))
        return result[0] if len(result) >= 1 else None

    @property
    def vedic_weekday_name(self):
        return "{:%A}".format(self.st_dttm)

    @property
    def vedic_weekday_duration(self):
        return self.en_dttm - self.st_dttm

    @property
    def day_choghadiya_length(self):
        return (self.md_dttm - self.st_dttm) / 8

    @property
    def night_choghadiya_length(self):
        return (self.en_dttm - self.md_dttm) / 8

    @property
    def first_choghadiyu_for_daytime(self):
        return self.get_choghadiyu(1)

    @property
    def last_choghadiyu_for_daytime(self):
        return self.get_choghadiyu(8)

    @property
    def first_choghadiyu_for_nighttime(self):
        return self.get_choghadiyu(9)

    @property
    def last_choghadiyu_for_nighttime(self):
        return self.get_choghadiyu(16)

    @property
    def auspicious(self):
        return [self.get_choghadiyu(i)
                for i in range(1, 17)
                if self.get_choghadiyu(i).ch_type == "Auspicious"]

    @property
    def inauspicious(self):
        return [self.get_choghadiyu(i)
                for i in range(1, 17)
                if self.get_choghadiyu(i).ch_type == "Inauspicious"]

    def print_choghadiya(self):
        nw = dttm.now()
        print(" Choghadiya for {:%Y-%b-%d} ".format(self.st_dttm).center(59, "="))
        print(" Vedic day {} ".format(self.vedic_weekday_name).center(59, "="))

        print(" Starts at {:%H:%M} and ends at {:%H:%M} next day "
              .format(self.first_choghadiyu_for_daytime.start,
                      self.last_choghadiyu_for_nighttime.end).center(59, "."))

        c = self.current_choghadiyu(nw)
        if c is not None:
            nm = c.ch_name
            gdfr = c.good_for
            ruler = c.ruling_planet
            txt1 = "Current Choghadiyu is \"{}\". ".format(nm)
            txt2 = "It is ruled by \"{}\". ".format(ruler)
            txt3 = "It is considered good for \"{}\".".format(gdfr)
            txt = txt1 + txt2 + txt3
            print(txt)

        print("-" * 59)
        for i in range(1, 9):
            c1 = self._ch[i]
            c2 = self._ch[i + 8]
            x1 = f"{c1}"
            if c1.is_running_at(nw):
                x1 = x1 + " *"
                x1 = x1 + f"{c1.elapsed(nw):3.0f}%"
            x1 = f"{x1:<28.28s}"

            x2 = f"{c2}"
            if c2.is_running_at(nw):
                x2 = x2 + " *"
                x2 = x2 + f"{c2.elapsed(nw):3.0f}%"
            x2 = f"{x2:<28.28s}"
            print(f"{x1} | {x2}")

        print("".center(59, "="))

        lst1 = self.auspicious
        lst2 = self.inauspicious

        print("All Auspicious".center(28), "|", "All Inauspicious".center(28))
        for item in zip(lst1, lst2):
            print(str(item[0]).center(28), "|", str(item[1]).center(28))


def main():
    """

    :rtype: None
    """
    # utils.python_version_check()
    # utils.do_not_run_this(__file__)
    return None


if __name__ == '__main__':
    main()
