#!/usr/bin/env bash
# Aether Project
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
Aether Project
Alphagriffin.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""

# this pushes to both dirs
for r in $(git remote); do git push $r master; done

# this submits for pypy
# python setup.py register

# this pushs to pypy
# python setup.py sdist upload
