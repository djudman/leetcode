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
    template = """from typing import List, Optional

from leetcode.utils.tree import TreeNode, make_binary_tree


class Solution:
    def solve(self) -> None:
        pass
"""

    if re.match(r'^([a-z]+)://(.+)$', line):
        data = urlparse(line)
        name = data.path.strip(' \t/').split('/')[-1]
    else:
        name = line
    name = name.replace('-', '_')
    filename = realpath(join(dirname(__file__), 'solutions', f'{name}.py'))
    if not exists(filename):
        with open(filename, 'w') as f:
            f.write(template)
    os.system(f'{editor} {filename}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--new', metavar='URL|slug', type=str)
    args = parser.parse_args()
    if args.new:
        create_file(args.new)
    else:
        parser.print_help()
