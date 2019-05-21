import sys
from os.path import abspath, join, dirname
sys.path.append(abspath(dirname(__file__)+'/../'))
from common.layers import ConvNorm

print("|||module Tacotron2/tacotron2/model.py")

class Tacotron2:
    def __init__(self):
        print("|||class Tacotron2/tacotron2/model/Tacotron2")
