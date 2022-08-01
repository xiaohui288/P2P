#!/usr/bin/python
# -*- coding:utf-8 -*-

file = open('shanghai_tech_part_a_test.list', mode='w')
for i in range(1, 183):
    file.write('test_data/images/IMG_' + str(i) + '.jpg ')
    file.write('test_data/ground_truth/GT_IMG_' + str(i) + '.mat\n')
file.close()
