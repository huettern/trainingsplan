#!/bin/bash

set -e

mkdir -p /tmp/trainingsplan-pub
cp -rv web/* /tmp/trainingsplan-pub/
git checkout gh-pages
rm -r *
cp -rv /tmp/trainingsplan-pub/* .
git add .
git commit
git push

git checkout main
