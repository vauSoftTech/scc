#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 May. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : SCC
    Script Name  : scc-cli.py
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
import argparse as ap
from datetime import datetime as dttm
import vau
import scc


def input_number(txt_msg, min_no, max_no, default_no):
    try:
        result = int(input(txt_msg))

        if result < min_no:
            print("Minimum allowed value is {}.".format(min_no))
            result = min_no
        if result > max_no:
            print("Maximum allowed value is {}.".format(max_no))
            result = max_no

    except ValueError:
        result = default_no

    return result


# def date_type_validation(argument):
#     try:
#         return dttm.strptime(argument, "%Y-%m-%d")
#     except ValueError:
#         raise ap.ArgumentTypeError("Not a valid date: '{0}'.".format(argument))
#
#
# def time_type_validation(argument):
#     try:
#         return dttm.strptime(argument, "%H:%M:%S")
#     except ValueError:
#         try:
#             return dttm.strptime(argument, "%H:%M")
#         except ValueError:
#             raise ap.ArgumentTypeError("Not a valid time: '{0}'.".format(argument))


def main(gd, srt, sst, nsrt, gt):
    x = scc.calculate_for_specific_time(gd, srt, sst, nsrt, gt)

    print("{} {} {} {} {:%Y%m%d%H%M} {:%H:%M:%S} {:%Y%m%d%H%M}".
          format(x[0], x[1], x[2], x[3], x[4], gt, x[5]))
    return


if __name__ == '__main__':
    scc_cli_parser = ap.ArgumentParser(prog='SCC',
                                       usage='%(prog)s [options]',
                                       description='Simple Choghadiya Calculator.',
                                       epilog="Simple and easy way to calculate "
                                              "Choghadiya that is part of Sanaatan "
                                              "Panchang."
                                       )
    scc_cli_parser.add_argument('-v', '--version', action='version',
                                version='%(prog)s 0.0.1 (Unstable Alpha)')

    date_group = scc_cli_parser.add_argument_group('date_group', 'Date Group')
    date_group.add_argument('-d', "--date",
                            help="Date - format YYYY-MM-DD",
                            required=False,
                            type=vau.date_type_validation,
                            default="{:%Y-%m-%d}".format(dttm.today()))

    events_group = scc_cli_parser.add_argument_group('events_group',
                                                     'Sun related events Group')
    events_group.add_argument("--sunrise",
                              help="Sunrise Time - format HH:MM[:SS]",
                              required=True,
                              type=vau.time_type_validation)
    events_group.add_argument("--sunset",
                              help="Sunset Time - format HH:MM[:SS]",
                              required=True,
                              type=vau.time_type_validation)
    events_group.add_argument("--next-sunrise",
                              help="Next Sunrise Time - format HH:MM[:SS]",
                              required=False,
                              type=vau.time_type_validation)
    scc_cli_parser.add_argument("--calc-at",
                                help="Calc for Time - format HH:MM[:SS]",
                                required=False,
                                type=vau.time_type_validation,
                                default="{:%H:%M:%S}".format(dttm.now().time()))
    args = scc_cli_parser.parse_args()

    if args.next_sunrise is None:
        args.next_sunrise = args.sunrise

    if args.calc_at is None:
        args.calc_at = dttm.now().time()

    main(args.date, args.sunrise.time(), args.sunset.time(),
         args.next_sunrise.time(), args.calc_at.time())
