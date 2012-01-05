# -*- coding: utf-8 -*-
from AccessControl.SecurityInfo import ModuleSecurityInfo

PROJECTNAME = "domense.homeboxes"
security = ModuleSecurityInfo(PROJECTNAME)

security.declarePublic('ManageSettings')
ManageSettings = PROJECTNAME + ': Manage Homeboxes settings'