#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#----------------------------------------------------------------------------------
# Name:        AXPath.py
#
# Purpose:
#
# Version:     1.1
#
# Author:      automationteam
#
# Created:     03/26/2019
# Updated:     
#
# Copyright:   (c) TMA Solution
#
# Todo:         Used to mark directories on disk as Python package directories
#----------------------------------------------------------------------------------
"""
#Python default packages used in this lib.

import sys,os,time,logging

class AXPath():

    def __init__(self):
        #Avaya IX Workplace
        self.AvayaEquinox           = "/AXApplication[@AXTitle='Avaya IX Workplace']"

        #self.MainWindowIdentifier   = self.AvayaEquinox + "/AXWindow[@AXTitle='Avaya IX Workplace' and @AXIdentifier='UCC3MainWindowIdentifier' and @AXSubrole='AXStandardWindow']"
        self.MainWindowIdentifier   = self.AvayaEquinox + "/AXWindow[@AXTitle='Avaya IX Workplace']"
        #self.LogInWindowIndentifier = self.AvayaEquinox + "/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier' and @AXSubrole='AXStandardWindow']"
        self.LogInWindowIndentifier = self.AvayaEquinox + "/AXWindow[@AXIdentifier='UCC3LoginWindowIdentifier']"
        self.AvayaEquinoxmenuBar    = self.AvayaEquinox + "/AXMenuBar"
        self.absoluteAvayaEquinox	= self.AvayaEquinoxmenuBar + "/AXMenuBarItem[@AXTitle='Avaya IX Workplace']"
        self.WindowUnKnown          = self.AvayaEquinox + "/AXWindow[@AXSubrole='AXUnknown']"
        #self.ConfiguretionWindow    = self.AvayaEquinox + "/AXWindow[@AXTitle='Avaya IX Workplace Settings' and @AXIdentifier='UCC3ConfigurationWindowIdentifier' and @AXSubrole='AXStandardWindow']"
        self.ConfiguretionWindow    = self.AvayaEquinox + "/AXWindow[@AXTitle='Avaya IX Workplace Settings']"

        #Conference window
        self.ConferenceWindowIdentifier     = self.AvayaEquinox + "/AXWindow[@AXIdentifier='UCC3ConferenceWindowIdentifier']"
        self.StandardConferenceWindow       = self.AvayaEquinox + "/AXWindow[@AXIdentifier='UCC3ConferenceWindowIdentifier']"   
        self.ContactListContextMenuWindowTableViewIdentifier = self.WindowUnKnown + "/AXScrollArea[0]/AXTable[@AXIdentifier='UCC3AutomationContactListContextMenuWindowTableViewIdentifier']"
        self.AlertViewEndIdentifier                     = self.ConferenceWindowIdentifier + "/AXSheet[@AXIdentifier='UCC3AlertWindowIdentifier']/AXLayoutArea[@AXIdentifier='UCC3AutomationAlertViewEndIdentifier']"
        self.ConferenceRosterParticipantTableIdentifier = self.ConferenceWindowIdentifier + "/AXScrollArea[0]/AXTable[@AXIdentifier='UCC3AutomationConferenceRosterParticipantTableIdentifier']"
        self.Conference_AlertWindow                     = self.ConferenceWindowIdentifier + "/AXSheet[@AXIdentifier='UCC3AlertWindowIdentifier']"
        self.ALertMainWindowIndentifier                 = self.MainWindowIdentifier + "/AXSheet[@AXIdentifier='UCC3AlertWindowIdentifier']"

        #My Meeting Details Window
        #self.MyMeetingDetailsWindow = self.AvayaEquinox + "/AXWindow[@AXTitle='Avaya IX Workplace' and @AXIdentifier='UCC3MainWindowIdentifier' and @AXSubrole='AXStandardWindow']"
        self.MyMeetingDetailsWindow = self.AvayaEquinox + "/AXWindow[@AXTitle='Avaya IX Workplace']"

        #Notification
        self.NotificationCenter             = "/AXApplication[@AXTitle='Notification Center']/AXWindow[@AXSubrole='AXNotificationCenterBanner']"

        #Chat Private
        self.ConfigurationComboBoxTableView = self.WindowUnKnown + "/AXScrollArea[1]/AXTable[@AXIdentifier='UCC3AutomationConfigurationComboBoxTableViewIdentifier']"
        self.StandardWindow                 = self.AvayaEquinox + "/AXWindow[@AXSubrole='AXStandardWindow']"
        self.AlertWindowIdentifier         = self.StandardWindow  + "/AXSheet[@AXIdentifier='UCC3AlertWindowIdentifier']"

        #Application
        self.Application_share_your_screen  = "/AXApplication[@AXTitle='Google Chrome']/AXWindow[@AXSubrole='AXStandardWindow']"

        #SignInPage
        #self.SignInPageAcion    = self.AvayaEquinox + "/AXWindow[@AXTitle='Avaya IX Workplace' and @AXIdentifier='UCC3MainWindowIdentifier' and @AXSubrole='AXStandardWindow']"
        self.SignInPageAcion    = self.AvayaEquinox + "/AXWindow[@AXTitle='Avaya IX Workplace']"
    # Dashboard Locators
    def AvayaEquinoxAXPath(self):
        return self.AvayaEquinox
    def MainWindowIdentifierAXPath(self):
        return self.MainWindowIdentifier
    def AvayaEquinoxmenuBarAXPath(self):
        return self.AvayaEquinoxmenuBarAXPath
    def absoluteAvayaEquinoxAXPath(self):
        return self.absoluteAvayaEquinox
    def LogInWindowIndentifierAXPath(self):
        return self.LogInWindowIndentifier
    def ConfiguretionWindowAXPath(self):
        return self.ConfiguretionWindow
    def AlertWindowIndentifierAXPath(self):
        return self.AlertWindowIdentifier
    def AConferenceWindowIdentifierAXPath(self):
        return self.ConferenceWindowIdentifier
    def ContactListContextMenuWindowTableViewIdentifierAXPath(self):
        return self.ContactListContextMenuWindowTableViewIdentifier
    #get notification
    def ConferenceRosterParticipantTableIdentifierAXPath(self):
        return self.ConferenceRosterParticipantTableIdentifier
    #Gertting windown unknown
    def WindowUnKnownAXPath(self):
        return self.WindowUnKnown
    #Chat Private
    def ConfigurationComboBoxTableViewAXPath(self):
        return self.ConfigurationComboBoxTableView
    #Chat Private
    def StandardWindowAXPath(self):
        return self.StandardWindow
    def mainwindow_alertWindowIndentifierAXPath(self):
        return self.ALertMainWindowIndentifier

    
