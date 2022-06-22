#!/usr/bin/env python

import json
import pandas as pd
import numpy as np
import argparse
import re

def search(df: pd.DataFrame, substring: str, case: bool = False) -> pd.DataFrame:
    mask = np.column_stack([df[col].astype(str).str.contains(substring, case=case, na=False) for col in df])
    return df.loc[mask.any(axis=1)]

def formated(ws):
        if len(ws) > 1:
            j =""
            count = 0
            for i in ws:
                count = count + 1
                if count == 1:
                    j = j + i
                elif count != len(ws):
                    j = j + ", " + i
                else:
                    j = j + " and " + i
            return j
        else:
            return ws[0]

def map_remove(df,c):
    if len(c)>0:
        c =sorted(c,reverse = True)
        for i in c:
            del df[i]
    return df

parser = argparse.ArgumentParser(description="Command Line Options")
parser.add_argument('pattern', type=str)
parser.add_argument('file', type=str)
group = parser.add_mutually_exclusive_group()
group.add_argument('-k', action='store_true')
group.add_argument('-v', action='store_true')
parser.add_argument("-x", default=False, action="store_true")
parser.add_argument("-i", default=False, action="store_true")
parser.add_argument("-c", default=False, action="store_true")
parser.add_argument("-d", default=False, action="store_true")

args = parser.parse_args()

with open(args.file, "r", encoding='ISO-8859-1') as f:
    res = f.read().split("\n")
    res = [x for x in res if x]

l=[]
c =[]   
gen_string=[]
for i in range(0,len(res)):
    if res[i].startswith('{'):
        gen_string.append(res[i])
    else:
        l.append(i+1)
        c.append(i)    
cleaned_string =','.join(gen_string)    
json_data = json.loads("["+cleaned_string+"]")
df = pd.json_normalize(json_data)

if args.k:
    df = df.columns.values
    if args.i:
        res = filter(lambda a: args.pattern.casefold() in a.casefold(), df)
    else:    
        res = filter(lambda a: args.pattern in a, df)
    if args.c:
        print(len(list(res)))
    else:
        if args.d:
            res = list(set(df) - set(res))
        res = list(res)
        if len(res)>0:
            print("".join(res))         
else:
    if args.i:
        res1 = search(df,args.pattern)
    else:
        res1 = search(df,args.pattern,True)
    
    if args.c:
        print(len(res1.index))
    else:    
        index_res1 = res1.dropna(axis=1).index.values
        res = map_remove(res,c)
        if args.d:
            res_list = map_remove(res,index_res1)
            # list(res[index_res1])
        else:    
            res = pd.Series(res)
            res_list = list(res[index_res1])
        if len(res_list)>0:
            print("\n".join(res_list))
if not args.x:
    if len(l) > 0:
        print(f"Invalid JSON on line number {formated(l)}")


#####################################################################################################################

# COMMAND LINE OPERATIONS WHICH ARE PERFORMED BELOW:

# 1) python json_grep.py complete-request json_sample.log
# 2) python json_grep.py Java json_sample.log
# 3) python json_grep.py -x Java json_sample_err.log
# 4) python json_grep.py -v port json_sample.log
# 5) python json_grep.py -v 8088 json_sample.log
# 6) python json_grep.py -k 8088 json_sample.log
# 7) python json_grep.py -i Provakil json_sample_err.log
# 8) python json_grep.py -c -x -i provakil json_sample_err.log
# 9) python json_grep.py -d tmUpdates json_sample.log