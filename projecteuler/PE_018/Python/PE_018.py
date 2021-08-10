#!/usr/bin/env  python
#  -*-  coding:  utf-8  -*-

'''
Project Euler: Maximum  path  sum  I

By  starting  at  the  top  of  the  triangle  below  and  moving  to  adjacent
numbers  on  the  row  below,  the  maximum  total  from  top  to  bottom  is  23.

          3
        7   4
      2   4   6
    8   5   9   3

That  is,  3  +  7  +  4  +  9  =  23.

Find  the  maximum  total  from  top  to  bottom  of  the  triangle  below:

                                75
                              95  64
                            17  47  82
                          18  35  87  10
                        20  04  82  47  65
                      19  01  23  75  03  34
                    88  02  77  73  07  63  67
                  99  65  04  28  06  16  70  92
                41  41  26  56  83  40  80  70  33
              41  48  72  33  47  32  37  16  94  29
            53  71  44  65  25  43  91  52  97  51  14
          70  11  33  28  77  73  17  78  39  68  17  57
        91  71  52  38  17  14  91  43  58  50  27  29  48
      63  66  04  68  89  53  67  30  73  16  69  87  40  31
    04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE:  As  there  are  only  16384  routes,  it  is  possible  to  solve  this
problem  by  trying  every  route.  However,  Problem  67,  is  the  same  challenge
with  a  triangle  containing  one-hundred  rows;  it  cannot  be  solved  by
brute  force,  and  requires  a  clever  method!  ;o)
'''

import  string


def  strip_string(str):
        all  =  string.maketrans('',  '')
        nodigs  =  all.translate(all,  string.digits)
        return  str.translate(all,  nodigs)


def  pyramid_file(filename):
        file  =  open(filename,  'r')
        pyramid  =  list()
        for  index,  line  in  enumerate(file):
                if  index  >  0:
                        pyramid.extend([[int(i)  for  i  in  line.split()]])
                else:
                        pyramid.extend([[int(strip_string(line))]])
        return  pyramid


def  path_pyramid(pyramid):
        layer  =  len(pyramid)-1
        pyramid_row_0  =  pyramid[layer-1]
        pyramid_row_1  =  pyramid[layer]
        chains  =  []
        for  i,  num  in  enumerate(pyramid_row_0):
                left  =  pyramid_row_1[i]
                right  =  pyramid_row_1[i+1]
                if  left  >  right:
                        chains.append([num,  left])
                else:
                        chains.append([num,  right])

        print  chains
        print

        for  k  in  range(2,  layer):
                temp_chains  =  []
                for  i,  num  in  enumerate(pyramid[layer-k]):
                        left  =  sum(chains[i])
                        right  =  sum(chains[i+1])
                        if  left  >  right:
                                chain  =  list(chains[i])
                                chain.insert(0,  num)
                                temp_chains.extend([chain])
                        else:
                                chain  =  list(chains[i+1])
                                chain.insert(0,  num)
                                temp_chains.extend([chain])
                chains  =  temp_chains

                print  chains
                print

        max_sum  =  0
        for  ch  in  chains:
                ch.insert(0,  pyramid[0][0])
        	if  sum(ch)  >  max_sum:
        		sols  =  ch
        return  sols


def  print_pyramid(pyramid,  solution):
        pyramid_row  =  len(pyramid)-1
        print  "================================================================================"
        for  index,  row  in  enumerate(pyramid):
                lin  =  ""
                for  i  in  row:
                        if  i  ==  solution[index]:
                                lin  +=  str([i])
                                lin  +=  "    "
                        elif  i  <  10:
                                lin  +=  "  "
                                lin  +=  str(i)
                                lin  +=  "      "
                        else:
                                lin  +=  str(i)
                                lin  +=  "      "
                print  lin.center(75)
        print  "==============================================================================="
        print  "Length  of  the  longest  path  =  "  +  str(sum(solution))
        print  "path  =  "  +  str(solution)
        print  "==============================================================================="

if  __name__  ==  '__main__':

        pyramid  =  pyramid_file('018.txt')

        sol  =  path_pyramid(pyramid)
        print_pyramid(pyramid,  sol)
