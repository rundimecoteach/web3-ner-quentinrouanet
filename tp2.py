#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:24:52 2018

@author: zeta
"""

import spacy
import xmltodict

data_dir = "recettes/T1/"

#Test de spacy, malheureusement les données étant en français, le résultat
#n'est pas convaincant
def spacyLoad(text):

    nlp = spacy.load('fr')

    doc = nlp(text)
    for token in doc:
        print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(
        token.text,
        token.idx,
        token.lemma_,
        token.is_punct,
        token.is_space,
        token.shape_,
        token.pos_,
        token.tag_
        ))
        
#Lit une recette ne XML en entrée et renvoie une version textuelle lisible
def cleanXml(filename):
    
    with open(data_dir + filename) as fd:
        doc = xmltodict.parse(fd.read())
    #ajout du titre
    titreIngredients = doc['recette']['titre'] + " : \n"
    #ajout des ingrédients
    for ingredient in doc['recette']['ingredients']['p']:
        titreIngredients = titreIngredients + "- " + ingredient + "\n"
    
    return titreIngredients

