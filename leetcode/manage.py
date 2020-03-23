#!/usr/bin/env python

import argparse
import os
import re
from pathlib import Path
from urllib.parse import urlparse
from os.path import dirname, join, realpath, exists


editor = 'charm'

file_types = {
    'python': 'py',
    'sql': 'sql',
    'bash': 'sh',
}


def create_python_solution(url: str, name: str, extension: str) -> None:
    filename = realpath(join(dirname(__file__), 'solutions', f'{name}.{extension}'))
    template = '' \
               f'from typing import List, Optional\n\n' \
               'from leetcode.utils.list import ListNode, make_linked_list\n' \
               'from leetcode.utils.tree import TreeNode, make_binary_tree\n\n\n' \
               f'# {url}\n' \
               'class Solution:\n' \
               '    def solve(self) -> None:\n' \
               '        """\n' \
               '        >>> solution = Solution()\n' \
               '        """\n' \
               '        pass\n'
    if not exists(filename):
        with open(filename, 'w') as f:
            f.write(template)
    os.system(f'{editor} {filename}:9')


def create_sql_solution(url: str, name: str, extension: str) -> None:
    filename = realpath(join(dirname(__file__), 'solutions', f'{name}.{extension}'))
    template = f'-- {url}\n'
    if not exists(filename):
        with open(filename, 'w') as f:
            f.write(template)
    os.system(f'{editor} {filename}:2')


def create_bash_solution(url: str, name: str, extension: str) -> None:
    filename = f'{name}.{extension}'
    dirpath = Path(dirname(__file__), 'solutions', name)
    template = f'#!/bin/bash\n# {url}\n\n'
    os.makedirs(dirpath.absolute())
    filepath = dirpath.joinpath(filename)
    with open(filepath, 'w') as f:
        f.write(template)
    open(dirpath.joinpath('file.txt'), 'w').close()
    os.system(f'{editor} {filepath}:4')


def create_file(line: str, file_type: str) -> None:
    """
    Create new file in `solutions` directory and open it in editor
    """
    if re.match(r'^([a-z]+)://(.+)$', line):
        data = urlparse(line)
        name = data.path.strip(' \t/').split('/')[-1]
    else:
        name = line
    url = f'https://leetcode.com/problems/{name}/'
    name = name.replace('-', '_')
    extension = file_types[file_type]
    handler_name = f'create_{file_type}_solution'
    globals()[handler_name](url, name, extension)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--new', metavar='URL|slug', type=str)
    parser.add_argument('--type', metavar='File type', type=str,
                        choices=file_types.keys(), default='python')
    args = parser.parse_args()
    if args.new:
        create_file(args.new, args.type)
    else:
        parser.print_help()
