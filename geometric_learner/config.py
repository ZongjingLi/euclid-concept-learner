import torch
import argparse

device = "cuda:0" if torch.cuda.is_available() else "cpu"

parser = argparse.ArgumentParser()
parser.add_argument("--device",default = device, type = str, help = "the default running device will be on cuda is available")
parser.add_argument("--point_scale",default = 0.3, type = float, help = "the variance of the point like distribution")
parser.add_argument("--resolution", default = (64,64), type = tuple, help = "the global resolution of the input concept image")
model_opt= parser.parse_args(args = [])