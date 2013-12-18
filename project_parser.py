import csv
import unicodedata
#import unicodecsv

with open('projects.csv', 'rb') as csvfile:
    rcreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    project_list = open('project_list.py', "wa")
    counter = 1
    projects = []

    for row in rcreader:
        project_list.write("p" + str(counter) + " = {\n")
        project_list.write("\t" + "'AC_ID': \"%s\", \n" % row[2])
        project_list.write("\t" + "'NAME': \"%s\", \n" % row[1])
        project_list.write("\t" + "'DESCRIPTION': \"%s\", \n" % row[6])
        project_list.write("\t" + "'MEMBER': \"%s\", \n" % row[8])
        project_list.write("\t" + "'MEMBER_EMAIL': \"%s\", \n" % row[9])
        project_list.write("\t" + "'SRC_CODE': \"%s\", \n" % row[11])
        project_list.write("}" + "\n")
        projects.append("p" + str(counter))

        counter += 1
        
    project_list.write("projects = %s\n" % str(projects).replace("'", ""))
    project_list.close()

"""        
        print row[1]            # project name
        print row[2]            # ac_id
        print row[6]            # project desc
        
        print "Member: %s" % row[8]            # member(s)
        print row[9]                           # member email
        print row[11]                          # github src_code
        
"""        

"""    
    #coordinators_list.write("# -*- coding: utf-8 -*-\n")
    for row in rcreader:
        coordinators_list.write("c" + str(counter) + " = {\n")
        coordinators_list.write("\t" + "'USERNAME': \"%s\",\n" % row[4].replace(" ","").lower())
        coordinators_list.write("\t" + "'PASSWORD': \"rc\",\n")
        coordinators_list.write("\t" + "'FIRSTNAME': \"%s\",\n" % row[4].split()[0].strip(' '))
        coordinators_list.write("\t" + "'LASTNAME': \"%s\",\n" % row[4].split()[-1].strip(' '))
        coordinators_list.write("\t" + "'CONTACT': %s,\n" % row[7].strip(' '))
        coordinators_list.write("\t" + "'EMAIL': \"%s\",\n" % row[6].strip(' '))
        coordinators_list.write("\t" + "'PHOTO': \"\",\n")
        coordinators_list.write("}" + "\n")
        users.append("c" + str(counter))
        
        rc_list.write("rc" + str(counter) + " = {\n")
        rc_list.write("\t" + "'RC_ID': %s,\n" % row[0].strip(' '))
        rc_list.write("\t" + "'NAME': \"%s\",\n" % row[1].strip(' '))
        rc_list.write("\t" + "'CITY': \"%s\",\n" % row[2].strip(' '))
        rc_list.write("\t" + "'STATE': \"%s\",\n" % row[3].strip(' '))
        rc_list.write("\t" + "'COORDINATOR': \"%s\",\n" % row[4].replace(" ","").lower())
        rc_list.write("}" + "\n")
        rcs.append("rc" + str(counter))

        counter += 1
        
    coordinators_list.write("users = %s\n" % str(users).replace("'", ""))
    coordinators_list.close()
    rc_list.write("rcs = %s\n" % str(rcs).replace("'", ""))
    rc_list.close()


        print "'RC_ID': %s" % row[0]
        print "'NAME': \"%s\"" % row[1]
        print "'CITY': \"%s\"" % row[2]
        print "'STATE': \"%s\"" % row[3]
        print "'COORDINATOR': \"%s\"" % row[4].split()[0]
        print "'STATUS': \"%s\"" % row[5]
        print "'EMAIL': \"%s\"" % row[6]
        print "'CONTACT': %s" % row[7]
        #print ', '.join(row)
"""
