#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2015 May. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : scc
    Script Name  : vau.py
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
from pathlib import Path

"""
    In reference to this article, here mimicking Java is avoided 
    by avoiding creation of "Singleton Class". 
    
    Because "Python is not Java"
    That insightful article is here... 
    https://dirtsimple.org/2004/12/python-is-not-java.html
"""

################################################################################
#
# FOLDER MANAGEMENT ROUTINES
#
################################################################################


def run_from_folder(script_name):
    if isinstance(script_name, str):
        script_name = Path(script_name)
    return script_name.parent


def get_user_home():
    return Path.home()


def get_cwd():
    return Path.cwd()


def is_running_from_home_folder():
    return get_user_home() == get_cwd()


def is_running_from_script_folder(script_name):
    script_folder = get_script_filepath(script_name)
    return script_folder == get_cwd()


def is_running_from_subfolder_of_cwd(script_name):
    x = get_script_filepath(script_name)
    y = get_cwd()
    return str(x).startswith(str(y)), x.relative_to(y)


def get_script_filename(script_path_and_name=None):
    if script_path_and_name is not None:
        result = Path(script_path_and_name).resolve().name
    else:
        result = get_script_filepath(__file__)
    return result


def get_script_filepath(script_path_and_name=None):
    if script_path_and_name is not None and \
            script_path_and_name != "":
        x = Path(script_path_and_name)
        if x.exists() and x.is_file():
            result = Path(script_path_and_name).resolve().parent
        elif x.exists() and x.is_dir():
            result = x.resolve()
        else:
            result = x
    else:
        result = get_script_filepath(__file__)
    return result


def folder_tree(folder_name):
    if isinstance(folder_name, str):
        folder_name = Path(folder_name)

    print(f'+ {folder_name}')

    for a_path in sorted(folder_name.rglob('*')):
        depth = len(a_path.relative_to(folder_name).parts)
        spacer = '---' * depth
        spacer = '+' + spacer
        print(f'{spacer}+ {a_path.name}')


def running_from_scripts_own_folder(script_name):
    if isinstance(script_name, str):
        script_name = Path(script_name)
    script_name = script_name.resolve()
    if script_name.is_file():
        return script_name.parent == get_cwd()
    elif script_name.is_dir():
        return script_name == get_cwd()


def get_absolute_path_to_subfolder(script_path, subfolder_name):
    return script_path / subfolder_name


def main():
    txt = """
    VAU.PY by: VAU SOFTTECH 
    Author: A. R. Bhatt
    ======
    Misc Utility Script.
    This script is best used by importing it in to your code. 
    """
    print(txt)
    return


if __name__ == '__main__':
    main()
