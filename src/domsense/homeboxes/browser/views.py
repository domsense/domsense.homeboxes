from zope import interface
from zope import component

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from domsense.homeboxes.interfaces import IHomeBoxContainer
from domsense.homeboxes import _


class Helpers(BrowserView):

    def enabled(self, context=None):
        context = context or self.context
        return IHomeBoxContainer.providedBy(context)


class HomeBox_PreView(BrowserView):
    """
    homebox_preview browser view
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def isManager(self):
        pm = getToolByName(self.context, 'portal_membership')
        return pm.checkPermission('Manage portal', self.context)
