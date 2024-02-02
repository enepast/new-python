#!/usr/bin/env python3
"""Tests for new.py"""

import os
import random
import string
from subprocess import getstatusoutput
from new import get_defaults

PRG = os.path.abspath(os.path.join(os.path.dirname(__file__), 'new.py'))


def test_exists():
    """Verifies that we can find the file"""
    assert os.path.isfile(PRG)


def test_get_defaults():
    """
    Generates random settings, writes it in a file ~/.new.py and
    verifies that get_defaults() from new.py reads them correctly
    """
    expected = {
        random_string(): random_string()
        for _ in range(random.randint(3, 7))
    }
    text = '\n'.join(f'{k}={v}' for k, v in expected.items())
    with open(os.path.expanduser('~/.new.py'), 'w') as f:
        f.write(text)
    assert get_defaults() == expected
    assert set(get_defaults().keys()) == set(expected.keys())


def test_usage():
    """Executes new.py -h and new.py --help to verify that returns a message
    """
    for flag in ['-h', '--help']:
        retval, out = getstatusoutput(f'{PRG} {flag}')
        assert retval == 0
        assert out.lower().startswith('usage')


def test_ok(tmp_path):
    """
    Changes the temp, executes new.py with a random name and verifies
    that the state is 0 and that the script was created
    """
    os.chdir(tmp_path)
    basename = random_string()
    name = basename + '.py'
    retval, out = getstatusoutput(f'{PRG} {name}')
    print(out)  # Add this line to print the error message
    assert retval == 0
    assert os.path.isfile(name)
    assert out == f'Done, see new script "{name}."'


def random_string():
    """Generate a random string"""
    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
