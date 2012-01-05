from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from domsense.homeboxes import homeboxMessageFactory as _


class IHomeBox_PreView(Interface):
    """
    homebox_preview view interface
    """

    def test():
        """ test method"""


class HomeBox_PreView(BrowserView):
    """
    homebox_preview browser view
    """
    implements(IHomeBox_PreView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def isManager(self):
        pm = getToolByName(self.context, 'portal_membership')
        return pm.checkPermission('Manage portal', self.context)
