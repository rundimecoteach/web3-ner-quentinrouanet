#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## par Bouchaud Maxine et Rouanet Quentin

import io
import os
import csv
import pprint

filename = "pasta.csv"

with open(filename, newline='') as file:
    r = csv.reader(file, delimiter=';', quotechar='|')
    recipe = {row[0]:row[1:] for row in r}
    pp = pprint.PrettyPrinter(indent=4)
    for key in recipe:
        i = 0
        for ing in recipe[key]:
            if (ing == "1.0"):
                recipe[key][i] = recipe["title"][i]
            i += 1
    del recipe["title"]
    for key in recipe:
        recipe[key] = [x for x in recipe[key] if x != "0.0"]

    meat = ["meat", "beef", "lamb", "duck", "chicken", "pork", "bacon", "turkey"]

    no_meat = []
    with_meat = []
    for key in recipe:
        if any([x in recipe[key] for x in meat]):
            with_meat.append(key)
        else :
            no_meat.append(key)
    pp.pprint(no_meat)
