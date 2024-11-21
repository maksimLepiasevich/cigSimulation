from functions import *
from tqdm import tqdm
n_model = 2

extent = [0, 6400, 0, 6400, 0, 1280]
resolution=[25,25,5]

extent = [0, 128, 0, 128, 0, 64]
resolution=[16,16,8]


for i in tqdm(range(n_model)):
    model = GeoModel(extent=extent, resolution=resolution)
    model.add_vp()
    model.add_meandering_channel()
    # model.add_distributary_channel()
    model.add_submarine_channel()
    model.add_dipping()
    model.add_fold()
    model.resample_z()
