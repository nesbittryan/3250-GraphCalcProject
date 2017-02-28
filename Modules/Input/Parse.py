#!/usr/bin/python

import ConfigParser

#
#   readConfig
#   Read a configuration file and return the object.
#   IN: NONE.
#   OUT: (Dictionary) Object.
#
def readConfig():
    config = ConfigParser.ConfigParser()
    config.read('Assets/settings.ini')
    hTable = {}

    for sections,key in enumerate(config.sections()):
        for k,v in config.items(key):
            hTable[k] = v
    return hTable

#
#   writeConfig
#   Write a configuration file.
#   IN: Dictionary see note.
#   OUT: NONE.
#   NOTE: Pass a dictionary containing ['key', 'value'] to save.
#
def writeConfig(dict):
    config = ConfigParser.ConfigParser()
    config.add_section('settings')
    for k, v in dict.items():
	    config.set('settings', k, v)
    with open('../Assets/Settings.ini', 'w+') as configfile:    # save
        config.write(configfile)
