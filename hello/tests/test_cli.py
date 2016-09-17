#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from click.testing import CliRunner

from hello import cli


runner = CliRunner()

def test_cli_bare():
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'World' in result.output

def test_cli_who():
    result = runner.invoke(cli.main, ['Jason'])
    assert result.exit_code == 0
    assert 'Jason' in result.output

def test_cli_help():
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert re.search(r'--help\s+Show this message and exit[.]', help_result.output) is not None
