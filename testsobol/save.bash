#!/bin/bash
filename=`date +%Y%m%d`".dat"
python manage.py printmodels 2>$filename

