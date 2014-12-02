#!/usr/bin/env python

# This script reads in a GENIE xml spline file, assuming one channel
# and neutrino and antineutrino entries (muon type) and parses them
# into two text files for easier plotting with Python / R.

from __future__ import print_function
import sys
import re
import os


def get_filenames(txt_name):
    """
    Take a base name (no extension) and add the nu / nu-bar designation
    plus .txt. Check to see if the files exist and remove them if they
    do (since we will be appending).
    """
    nu_name = txt_name + "_nu.txt"
    nubar_name = txt_name + "_nubar.txt"

    if os.path.isfile(nu_name):
        os.remove(nu_name)

    if os.path.isfile(nubar_name):
        os.remove(nubar_name)

    return nu_name, nubar_name


def transform(xml_file_name):
    """
    Take the xml file name (basically, assume we're working in the same
    directory - there are no path handling bits) and read through it.
    If we find we're in a (muon) neutrino section, append to the muon
    neutrino file. If we're in an antineutrino section (again, muon),
    append to the antinu file.

    Splitting structure generally assumes a GENIE xml file circa 2.8.
    """
    with open(xml_file_name, "r") as xml_file:

        nu_name, nubar_name = get_filenames(xml_file_name.split(".")[0])

        is_neutrino = False
        is_antineutrino = False
        for line in xml_file:

            # nu vs nubar is identified in the "spline" block
            if re.match("<spline", line):
                pieces = line.split("/")
                labels = pieces[2].split(";")
                nuflav = labels[0].split(":")

                if nuflav[1] == '14':
                    is_neutrino = True
                    is_antineutrino = False
                    with open(nu_name, "a") as myfile:
                        myfile.write("#neutrino\n")
                        myfile.write("Energy CrossSection\n")

                    myfile.close()

                if nuflav[1] == '-14':
                    is_neutrino = False
                    is_antineutrino = True
                    with open(nubar_name, "a") as myfile:
                        myfile.write("#antineutrino\n")
                        myfile.write("Energy CrossSection\n")

                    myfile.close()

            if re.match("(.*)<knot", line):
                parts = line.split()
                vals = parts[2] + " " + parts[5] + "\n"

                if (is_neutrino):
                    with open(nu_name, "a") as myfile:
                        myfile.write(vals)

                    myfile.close()

                if (is_antineutrino):
                    with open(nubar_name, "a") as myfile:
                        myfile.write(vals)

                    myfile.close()

    xml_file.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("This script requires a filename argument.")
        sys.exit(2)

    transform(sys.argv[1])
