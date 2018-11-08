#! /usr/bin/env python
'''
author: Danny Rakita
website: http://pages.cs.wisc.edu/~rakita/
email: rakita@cs.wisc.edu
last update: 11/4/18

PLEASE DO NOT CHANGE CODE IN THIS FILE.  IF TRYING TO SET UP RELAXEDIK, PLEASE REFER TO start_here.py INSTEAD
AND FOLLOW THE STEP-BY-STEP INSTRUCTIONS THERE.  Thanks!
'''
######################################################################################################

import os
from RelaxedIK.Utils.colors import bcolors
from start_here import info_file_name, urdf_file_name, fixed_frame, joint_names, joint_ordering, ee_fixed_joints, starting_config, \
    collision_file_name

path_to_src = os.path.dirname(__file__)

if info_file_name == '':
    print bcolors.FAIL + 'info_file_name is a required field in start_here.py.  Please fill that in and run again.' + bcolors.ENDC
    exit(-1)

out_file = open(path_to_src + '/RelaxedIK/Config/info_files/' + info_file_name, 'w')
out_file.write('path_to_src: \"{}\"\n'.format(path_to_src))

if urdf_file_name == '':
    print bcolors.FAIL + 'urdf_file_name is a required field in start_here.py.  Please fill that in and run again.' + bcolors.ENDC
    exit(-1)
else:
    out_file.write('urdf_file_name: \"{}\"\n'.format(urdf_file_name))

if fixed_frame == '':
    print bcolors.FAIL + 'fixed_frame is a required field in start_here.py.  Please fill that in and run again.' + bcolors.ENDC
    exit(-1)
else:
    out_file.write('fixed_frame: \"{}\"\n'.format(fixed_frame))

if len(joint_names) == 0:
    print bcolors.FAIL + 'joint_names is a required field in start_here.py.  Please fill that in and run again.' + bcolors.ENDC
    exit(-1)
else:
    num_chains = len(joint_names)
    chains_str = ''
    for i in range(num_chains):
        chains_str += '[ '
        for j in range(len(joint_names[i])):
            chains_str += '\"' + joint_names[i][j] + '\"'
            if not j == len(joint_names[i]) -1:
                chains_str += ', '
        chains_str += ' ]'
        if not i == num_chains - 1:
            chains_str += ', '
    out_file.write('joint_names: [ {} ]\n'.format(chains_str))


if len(joint_ordering) == 0:
    print bcolors.FAIL + 'joint_ordering is a required field in start_here.py.  Please fill that in and run again.' + bcolors.ENDC
    exit(-1)
else:
    ordering_str = '[ '
    for i in range(len(joint_ordering)):
        ordering_str += '\"{}\"'.format(joint_ordering[i])
        if not i == len(joint_ordering) -1:
            ordering_str += ', '
    ordering_str += ' ]'
    out_file.write('joint_ordering: {}\n'.format(ordering_str))

if len(ee_fixed_joints) == 0:
    print bcolors.FAIL + 'ee_fixed_joints is a required field in start_here.py.  Please fill that in and run again.' + bcolors.ENDC
    exit(-1)
else:
    ee_str = '[ '
    for i in range(len(ee_fixed_joints)):
        ee_str += '\"{}\"'.format(ee_fixed_joints[i])
        if not i == len(ee_fixed_joints) -1:
            ee_str += ', '
        ee_str += ' ]'
    out_file.write('ee_fixed_joints: {}\n'.format(ee_str))


if len(starting_config) == 0:
    print bcolors.FAIL + 'starting_config is a required field in start_here.py.  Please fill that in and run again.' + bcolors.ENDC
    exit(-1)
else:
    st_str = '[ '
    for i in range(len(starting_config)):
        st_str += '{}'.format(str(starting_config[i]))
        if not i == len(starting_config) -1:
            st_str += ', '
    st_str += ' ]'
    out_file.write('starting_config: {}\n'.format(st_str))



if collision_file_name == '':
    print bcolors.FAIL + 'collision_file_name is a required field in start_here.py.  Please fill that in and run again.' + bcolors.ENDC
    exit(-1)
else:
    out_file.write('collision_file_name: \"{}\"\n'.format(collision_file_name))


out_file.close()



in_file = open(path_to_src + '/RelaxedIK/Config/info_files/' + info_file_name, 'r')

import yaml

y = yaml.load(in_file)







