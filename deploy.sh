#!/usr/bin/env bash

fswatch -o /Users/jasonbenn/code/colorizer | xargs -n1 -I{} rsync -uar ~/code/colorizer/* ml-box-sourceress:/home/jason/code/colorizer