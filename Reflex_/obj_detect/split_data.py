import os
import splitfolders as spl

#defining paths

source_dir=r"D:\Coding_\Reflex_\dataset\Self-Driving-Car-3\export\dataset"
output_dir=r"D:\Coding_\Reflex_\dataset\Self-Driving-Car-3\export"


#splitting images at random

spl.ratio(source_dir,output=output_dir,seed=42, ratio=(0.8,0.2),group_prefix=None)



