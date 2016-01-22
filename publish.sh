#!/bin/bash

GITDIR=`git rev-parse --show-toplevel`
DOCDIR=docs
CODEDIR=mini

cd $GITDIR
git checkout gh-pages
find ./* -maxdepth 1 -not -name ".*" -delete
git checkout master $DOCDIR $CODEDIR
git reset HEAD
cd docs
make html
mv -fv _build/html/* ../
cd $GITDIR
rm -rf $DOCDIR $CODEDIR
touch .nojekyll
git add .
git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`"
git push origin gh-pages
git checkout master
