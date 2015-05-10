#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 May. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : SCC
    Script Name  : info.py
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


class Info:
    """
    This class manages basic Choghadiya information.

    Choghadiya Name : English Transliterated name of the Choghadiyu.
    Gujarati Name : Unicode Gujarati name of the Choghadiyu.
    Choghadiya Type : Auspicious, Inauspicious, or Neutral.
    Ruling Planet : One of the celestial bodies from the Sun, the Moon,
                    Mercury, Venus, Jupiter, Saturn etc...
    Good For :  What kinds of tasks can be undertaken : Mentions the
                types of tasks that can be undertaken when a particular
                choghadiyu is running.
    """

    """Some Constants declarations for Choghadiya names"""
    CH_UD = "Udveg"
    CH_CH = "Char"
    CH_LB = "Laabh"
    CH_AM = "Amrut"
    CH_KL = "Kal"
    CH_SB = "Shubh"
    CH_RG = "Rog"

    info_dict = {
        CH_UD: {
            "gu_nm": "ઉદ્વેગ",
            "type": "Inauspicious",
            "ruler": "Sun",
            "goodfor": "government related work"
        },
        CH_CH: {
            "gu_nm": "ચર",
            "type": "Neutral",
            "ruler": "Venus",
            "goodfor": "travel related work"
        },
        CH_LB: {
            "gu_nm": "લાભ",
            "type": "Auspicious",
            "ruler": "Mercury",
            "goodfor": "all kinds of gain related work"
        },
        CH_AM: {
            "gu_nm": "અમૃત",
            "type": "Auspicious",
            "ruler": "Moon",
            "goodfor": "all kinds of work"
        },
        CH_KL: {
            "gu_nm": "કાળ",
            "type": "Inauspicious",
            "ruler": "Saturn",
            "goodfor": "wealth accumulation"
        },
        CH_SB: {
            "gu_nm": "શુભ",
            "type": "Auspicious",
            "ruler": "Jupiter",
            "goodfor": "marriage & association"
        },
        CH_RG: {
            "gu_nm": "રોગ",
            "type": "Inauspicious",
            "ruler": "Mars",
            "goodfor": "defeat enemy"
        }
    }

    def __new__(cls):
        """
        We do not want to allow creation of the instances of this class. but it
        we do not mind if someone later on inherits from this class and creates
        instances of that  new class.
        :param :
        """
        if cls is Info:
            print(f"Creating an instance of the class {cls} is not allowed.")
            return None
        return object.__new__(cls)

    @staticmethod
    def _get_list():
        # AVOID CALLING THIS METHOD FROM ANYWHERE OUT OF THIS UNIT,
        # Having discovered that there are only seven Choghadiya and there is a
        # certain patten associated with  their occurrence, here we are doing
        # away with that large dictionary in scc.py that holds all the
        # Choghadiya for whole week.
        return list(Info.info_dict.keys()) * 5

    @staticmethod
    def get_ruling_planet(ch_nm):
        if ch_nm in Info.info_dict.keys():
            return Info.info_dict[ch_nm]["ruler"]
        else:
            return "Unknown planet"

    @staticmethod
    def get_type(ch_nm):
        """
        :param ch_nm: str - A valid choghadiyu name
        :return: str
        """
        if ch_nm in Info.info_dict.keys():
            return Info.info_dict[ch_nm]["type"]
        else:
            return "Unknown type"

    @staticmethod
    def get_good_for(ch_nm):
        """
        A static method that returns a string describing what that
        choghadiyu is good for.

        :param ch_nm: name of a Choghadiyu
        :return:
        """
        if ch_nm in Info.info_dict.keys():
            return Info.info_dict[ch_nm]["goodfor"]
        else:
            return "Nothing!"

    @staticmethod
    def get_gujarati_name(ch_nm):
        """
        A static method that returns a string describing Gujarati Language
        name of the choghadiyu.

        :param ch_nm: name of a Choghadiyu
        :return:
        """
        return Info.info_dict[ch_nm]["gu_nm"]

    @staticmethod
    def choghadiya_names_gen(weekday_number):
        """
        Earlier, we had a dictionary to hold hard-coded list of Choghadiya. but
        there is a pattern in occurrence of Choghadiya therefore it can be
        replaced with a generator.

        This function returns a generator object generates a full list of
        all the Choghadiya for a day passed to this function as an argument.

        :param weekday_number: iso week day number is expected
        :return: A generator object if argument provided is a valid iso week
            day number or a None.
        """
        if 0 <= weekday_number <= 7:
            lst = Info._get_list()
            offsets = (0, 3, 6, 2, 5, 1, 4, 0)
            this_offset = offsets[weekday_number]
            this_range = lst[this_offset:this_offset + 8] + \
                lst[this_offset + 5:this_offset + 21:2][::-1]
            for ch in this_range:
                yield ch
        else:
            return None


def main():
    from datetime import datetime as dttm
    xdt = dttm.now()
    idx = dttm.isoweekday(xdt)
    print("-"*61)
    print("Choghadiya for the week day number: {:} ({:%A})".format(idx, xdt))
    print("-"*61)
    x = list(Info.choghadiya_names_gen(idx))
    for i in range(0, 16):
        nm = x[i]
        good_for = (Info.get_good_for(nm)).capitalize()
        gj_nm = Info.get_gujarati_name(nm)
        print(f"{i + 1:>02}). {nm} \t{good_for:30.30s} \t{gj_nm}")
    return


if __name__ == '__main__':
    main()
