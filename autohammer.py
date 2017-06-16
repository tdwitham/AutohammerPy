#!/usr/bin/python3# 
# (c) 2016,2017 - Timothy D. Witham tim.wookie.witham@gmail.com
# Licensed under BSD 2-Clause

__author__ = 'wookie'
import os
from sys import argv
from xml.etree.ElementTree import iterparse

from components.auto_xml import *
from components.infrastructure import validateCommand
from components.FileOps import makeTrace

def hammerit(filename):
    """

    :rtype : none
    """
    validateCommand(len(argv))
    cFile = os.getcwd() + os.sep + argv[1] + os.sep + 'run_config.xml'
    for event, elem in iterparse(cFile, events=('start', 'end')):
        if (ckheader(event, elem.tag, elem.text)):
            if event == 'start':
                thisSection = elem.tag
                makeTrace("Starting Section {}".format(thisSection))
            else:
                makeTrace("Exiting section {}".format(thisSection))
                finishSection(thisSection)
                thisSection = None
        else:
            if event == 'end':
                makeTrace("\tAt parameter {}  with value {}".format(elem.tag, elem.text))
                doSection(thisSection, event, elem.tag, elem.text)


def putSectionParms(thisSection, secParms):
    for k, v in secParms.items():
        writeLog('\t' + k + " : " + v)


if __name__ == '__main__':
    validateCommand(len(argv))
    hammerit(argv[1])
