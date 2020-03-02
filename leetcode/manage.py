#!/usr/bin/env python

import argparse
import os
import re
from urllib.parse import urlparse
from os.path import dirname, join, realpath, exists


def create_file(line: str) -> None:
    """
    Create new *.py file in `solutions` directory and open it in editor
    """
    editor = 'charm'
    if re.match(r'^([a-z]+)://(.+)$', line):
        data = urlparse(line)
        name = data.path.strip(' \t/').split('/')[-1]
    else:
        name = line
    url = f'https://leetcode.com/problems/{name}/'
    name = name.replace('-', '_')
    filename = realpath(join(dirname(__file__), 'solutions', f'{name}.py'))
    if not exists(filename):
        template = ''\
            f'from typing import List, Optional\n\n'\
            'from leetcode.utils.tree import TreeNode, make_binary_tree\n\n\n'\
            f'# {url}\n'\
            'class Solution:\n'\
            '    def solve(self) -> None:\n'\
            '        pass\n'
        with open(filename, 'w') as f:
            f.write(template)
    os.system(f'{editor} {filename}:9')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--new', metavar='URL|slug', type=str)
    args = parser.parse_args()
    if args.new:
        create_file(args.new)
    else:
        parser.print_help()
