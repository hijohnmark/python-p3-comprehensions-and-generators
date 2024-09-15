#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [n for n in num_list if n % 2 == 0]
    return evens_list

def make_exclamation(sentence_list):
    exclamations_list = [sentence + "!" for sentence in sentence_list]
    return exclamations_list