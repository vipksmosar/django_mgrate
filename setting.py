import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_PROJECT = 'mytestsite'
DIR_WITH_DJANGO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/{}'.format(DJANGO_PROJECT)

