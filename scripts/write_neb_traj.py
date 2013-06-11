#!/usr/bin/env python

from ase.all import *
import ase
from ase.calculators.vasp import xdat2traj
import pickle
import os

atoms = read('00/POSCAR')
out = ase.io.trajectory.PickleTrajectory('neb.traj', mode='w')
out.write_header(atoms)

for line in open('INCAR').read_lines():
    if line.rfind('IMAGES'):
        images = int(line.split('=')[-1])


print images
