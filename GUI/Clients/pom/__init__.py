#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Used to mark directories on disk as Python package directories """

"""
#------------------------------------------------------------------
# Name:        __init__.py
#
# Purpose:
#
# Version:     1.1
#
# Author:      nmdong
#
# Created:     11/30/2018
# Updated:     
#
# Copyright:   (c) TMA Solution
#
# Todo:         Used to mark directories on disk as Python package directories
#------------------------------------------------------------------
"""

#Python default packages used in this lib.
import sys,os,time,logging

##Get framework base path from environment variable
##which is set in user .basrhrc file.

base_path = os.environ['PHOENIX_BASE_PATH']
##Lib PATH SET