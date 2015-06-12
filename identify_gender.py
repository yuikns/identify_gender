#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class IdentifyGender(object):
    """docstring for IdentifyGender"""
    def __init__(self):
        super(IdentifyGender, self).__init__()
        self.datapath = './data/'
        self.names = {}
        self.names['us_male'] = {}
        self.names['us_female'] = {}
        self.names['gr_male'] = {}
        self.names['gr_female'] = {}
        self.names['in_male'] = {}
        self.names['in_female'] = {}
        self.names['kr_male'] = {}
        self.names['kr_female'] = {}
        self.names['jp_male'] = {}
        self.names['jp_female'] = {}
        self.names['fr_male'] = {}
        self.names['fr_female'] = {}
        self.names['it_male'] = {}
        self.names['it_female'] = {}
        self.names['cn_male'] = {}
        self.names['cn_female'] = {}
        self.names['es_male'] = {}
        self.names['es_female'] = {}

        self.UpdateHash('us','male')
        self.UpdateHash('us','female')
        self.UpdateHash('gr','male')
        self.UpdateHash('gr','female')
        self.UpdateHash('in','male')
        self.UpdateHash('in','female')
        self.UpdateHash('kr','male')
        self.UpdateHash('kr','female')
        self.UpdateHash('jp','male')
        self.UpdateHash('jp','female')
        self.UpdateHash('fr','male')
        self.UpdateHash('fr','female')
        self.UpdateHash('it','male')
        self.UpdateHash('it','female')
        self.UpdateHash('cn','male')
        self.UpdateHash('cn','female')
        self.UpdateHash('es','male')
        self.UpdateHash('es','female')

    def UpdateHash(self, nation, gender):
        name = nation + '_' + gender
        with open(self.datapath + nation + '/' + name + '.txt') as f:
            lines = f.read().splitlines()
            for line in lines:
                self.names[name][line] = 1
            #print(self.names[name])

    def Test(self, name):
        name = name.lower()
        tmp = {}
        tmp['male'] = 0
        tmp['female'] = 0
        for key, value in self.names.items():
            if name in value:
                tmp[key.split('_')[1]] += 1
                #print('Maybe: ' + key)

        if tmp['male'] == 0:
            if tmp['female'] >= 1:
                ans = 'female'
            else:
                ans = 'no_records'
        elif tmp['female'] == 0:
            ans = 'male'
        else:
            ans = 'both'

        return ans

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print("\t usage: " + sys.argv[0] + " input_file output_file")
        print("for example:\n\t" + sys.argv[0] + " name_list.txt result.txt")
    else :
        print("input file:" + sys.argv[1] + "\t output file:" + sys.argv[2])
        with open(sys.argv[2], 'w') as outfile:
            with open(sys.argv[1], 'r') as infile:
                IG = IdentifyGender()
                for line in infile:
                    fullname = line.strip()
                    name = line.strip().split()
                    if name:
                        print(fullname + '\t' + IG.Test(name[0]), file = outfile)
