#!/usr/bin/env python
'''
Compare two GENIE spline files with formatting circa 2.8.N.
Usage:
    python spl_comp.py spline1.xml spline2.xml

The script will look for matching spline entries and then check to see
if the cross sections are identical. Note - it does not do any clever
interpolation, it just checks knot by knot for energy and cross section
equivalence. It is _not_ a check of physics model equivalence. Two splines
with the same physics but a different number of knots will not be identical.
'''

from __future__ import print_function
import sys
from xml.etree import ElementTree as ET


def decode_flavor(flavor):
    """
    Change the PDG code into a string.
    """
    return {
        '-16': 'tau_antineutrino',
        '-14': 'muon_antineutrino',
        '-12': 'electron_antineutrino',
        '12': 'electron_neutrino',
        '14': 'muon_neutrino',
        '16': 'tau_neutrino'
    }.get(flavor, 'unknown')


def get_neutrino_description(description):
    """
    Take a GENIE description string like:
        'genie::ReinSeghalCOHPiPXSec/Default/nu:-14;tgt:1000060120;
         proc:Weak[CC],COH;hmult:(p=0,n=0,pi+=0,pi-=1,pi0=0);'
    and return:
    {'algorithm': 'ReinSeghalCOHPiPXSec',
     'flavor': 'muon_antineutrino',
     'hmult': '(p=0,n=0,pi+=0,pi-=1,pi0=0)',
     'proc': 'Weak[CC],COH',
     'tgt': '1000060120'}
    """
    components = description.split(';')
    alg_flavor = components[0].split('/')
    alg = alg_flavor[0].split(':')[-1]
    flavor = decode_flavor(alg_flavor[-1].split(':')[-1])
    ddict = {'algorithm': alg, 'flavor': flavor}
    components = components[1:]
    for component in components:
        elem = component.split(':')
        if len(elem) > 1:
            ddict[elem[0]] = elem[1]

    return ddict


def process_spline(spline):
    """
    Transform a spline (object) from an ElementTree retrieval
    into a dictionary containing the relevant information.
    """
    knots = spline.findall('./knot')
    xsecs = []
    for knot in knots:
        e = knot.find('./E')
        x = knot.find('./xsec')
        xsecs.append((float(e.text), float(x.text)))
    description = get_neutrino_description(spline.get('name'))
    return {'description': description, 'xsecs': xsecs}


def xml_to_list_of_dicts(xml_file_name):
    """
    Take an xml file and return a list of dictionaries, where each dictionary
    contains a description and a list of tuples for energy and cross section.
    The description key is 'description' and the cross sections key is 'xsecs'.
    """
    xsec_xml = ET.parse(xml_file_name)
    splines = xsec_xml.findall('./spline')
    neutrino_xsecs = []

    for spline in splines:
        xsec_dict = process_spline(spline)
        neutrino_xsecs.append(xsec_dict)

    return neutrino_xsecs


if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv:
        print(__doc__)
        sys.exit(1)

    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)

    xml_file1 = sys.argv[1]
    xml_file2 = sys.argv[2]
    
    # Create a list of cross-sections, where each cross section is represented
    # by a dictionary containing a description and the numerical x-sections.
    list_of_dicts1 = xml_to_list_of_dicts(xml_file1)
    list_of_dicts2 = xml_to_list_of_dicts(xml_file2)

    # Compare all the dictionries in the first list to those in the second.
    for d1 in list_of_dicts1:
        for d2 in list_of_dicts2:
            if d1['description'] == d2['description']:
                print("Found matching descriptions for %s", d1['description'])
                if d1['xsecs'] == d2['xsecs']:
                    print("  Cross sections match!")
                else:
                    print("  Cross sections DO NOT match!")
