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
import blfparse

class match(object):
    def row_find(self, noise, torpedo_row, env_row, expected_column_count,):
        '''torpedo has 9 chars on each row'''

        columnstate = 0
        temp_noise = noise

        found = 0

        for row in env_row:
            i=0; j = 0
            for element in torpedo_row:

                if (element[i] == env_row[j]) or temp_noise:
                    i += 1
                    j += 1
                    if element[i] != env_row[j]:
                        if temp_noise:
                            temp_noise -= 1
                    columnstate +=1
                    if columnstate == expected_column_count:
                        found = 1
                        break
                else:
                    columnstate = 0
                    j += 1


            if found == 1:
                return 'OK', element[j-9]

            return 'FAIL', '0'

    def find(self, noise, env, torpedo, expected_column_count, expected_row_count):
        ''' Torpado has 11 rows'''

        #co-ordinates, env row and env column where tarpedo starts
        x = y = -1

        env_row_num = -1
        for row in env:
            env_row_num += 1
            torpedo_row_state == 0 #has 11 rows


            for torpedo_row in torpedo:

                list_returned = self.row_find(noise, torpedo_row, row, expected_column_count,)
                if list_returned[0] == 'OK':

                    if torpedo_row_state == 0:
                        x = env_row_num
                        y = list_returned[1]

                    torpedo_row_state +=1

                    if list_returned[1] != y:
                        x, y = -1
                        #the row matches, but they do start at exact 'y' coordinates
                        torpedo_row_state = 0
                        break

                    if torpedo_row_state == expected_row_count:
                        #wow, we found a tarpedo, print its location and search for next
                        print x, y
                        x, y = 0
                        torpedo_row_state = 0
                        break

                else:
                    torpedo_row_state = 0
                    x = y = -1

    pass

def main():
    scanner = blfparse.Scanner()
    match = Match()
    noise = 2 #i.e. 20 % noise in test data i.e. outof 10 pixels atleast 8 should macth.

    #below prints the x, y cordinates on test data where pattern of left top coordinate of tarpedo starts
    expected_column_count = 8
    expected_row_count = 11
    match.find(noise, scanner.torpedo, scanner.env, expected_column_count, expected_row_count)

    #below prints the x, y cordinates on test data where pattern of left top coordinate of starship starts
    expected_column_count = 12
    expected_row_count = 9
    match.find(noise, scanner.torpedo, scanner.env, expected_column_count, expected_row_count)

if __name__ == '__main__':
    main()
