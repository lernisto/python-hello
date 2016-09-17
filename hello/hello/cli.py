#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import click

DEBUG = False


@click.command()
@click.option('--verbose', '-v', default=DEBUG)
@click.argument('who', default='World')
def greet(verbose, who):
    if verbose:
        with open('debug.log', 'a') as fo:
            fo.write(sys.version)
    click.echo('Hello, {}.'.format(who))

main = greet
