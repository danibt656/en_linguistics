"""
This module provides the word generation functions.
"""
import random


class Word:
    def gen_verbs(self):
        """generate verbs list"""
        with open("dicc/verbs.txt") as vfile:
            return [line.strip() for line in vfile]

    def gen_adverbs(self):
        """generate adverbs list"""
        with open("dicc/adverbs.txt") as advfile:
            return [line.strip() for line in advfile]

    def gen_adjectives(self):
        """generate adjectives list"""
        with open("dicc/adjectives.txt") as adjfile:
            return [line.strip() for line in adjfile]

    def gen_nouns(self):
        """generate nouns list"""
        with open("dicc/nouns.txt") as nfile:
            return [line.strip() for line in nfile]
