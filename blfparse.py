#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      madhav
#
# Created:     03-10-2012
# Copyright:   (c) madhav 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Scanner(object):
    '''starship scanned info, it is list of 12 elements each'''
    ''' slime torpedo is a list of 9 characters each'''
    def __init__(self):
        self.starship = []
        self.torpedo = []
        self.env = []
        self.scan_env()
        self.scan_starship()
        self.scan_torpedo()

    def scan_starship(self):
        file_handle= open("Starship.blf", "r")
        row = []
        for line in file_handle:
            for character in line:
                if character == '\n': break
                row.append(character)
            self.starship.append(row)

    def scan_torpedo(self):
        file_handle= open("SlimeTorpedo.blf", "r")
        row = []
        for line in file_handle:

            for character in line:
                if character == '\n': break
                row.append(character)
            self.torpedo.append(row)



    def scan_env(self):
        file_handle = open("TestData.blf", "r")
        row = []
        for line in file_handle:

            for character in line:
                if character == '\n': break
                row.append(character)
            self.torpedo.append(row)

