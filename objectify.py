#!/usr/bin/env python

"""
Creates and returns a device-info object using DNACenter API (credentials stored in lehost.py) for parsing. -MG, 10.15.25
"""

from dnacentersdk import api
from lehost import host, x, y

def objectify():
    object = api.DNACenterAPI(
        base_url=host,
        username=x,
        password=y,
        verify=False, 
    )
    return object

def main():
    objectify() 

if __name__ == "__main__":
    main()
    