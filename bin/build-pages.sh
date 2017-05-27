#!/bin/bash
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
Aether Project
Alphagriffin.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""

# references: github sleeper?
set -e

cd "`dirname $0`/.."
rm -r build/sphinx || true
python setup.py build_sphinx

git checkout gh-pages
git fetch origin gh-pages
git merge --ff-only origin/gh-pages
git rm `git ls-files`
git checkout HEAD CNAME
git checkout HEAD .nojekyll
cp -r build/sphinx/html/. .
git add `find build/sphinx/html | cut -c 19-`
git status
