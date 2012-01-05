from DateTime import DateTime

from zope.component import getMultiAdapter
from zope.component import queryAdapter

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets.common import ViewletBase

from Products.CMFCore.utils import getToolByName

from plone.memoize.instance import memoize

from domsense.homeboxes.interfaces import IHomeBox
from domsense.homeboxes.browser.interfaces import IHomeBoxRenderer


class HomeboxViewlet(ViewletBase):

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                            name=u'plone_portal_state')

        self.navigation_root_url = portal_state.navigation_root_url()

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    @memoize
    def boxes(self):
        query = {
            'portal_type':'HomeBox',
            'review_state': 'published',
            #'sort_on': 'getObjPositionInParent ',
        }
        if hasattr(self.context, 'homeboxes'):
            homeboxes_folder = getattr(self.context, 'homeboxes')
            query['path'] = '/'.join(homeboxes_folder.getPhysicalPath())
        return self.portal_catalog(query)

    @memoize
    def getBoxes(self):
        for brain in self.boxes:
            box = brain.getObject()
            # get renderer
            adapter = queryAdapter(box, IHomeBoxRenderer, name=box.appearance)
            if adapter:
                yield adapter

    def isHomeBox(self):
        return IHomeBox.providedBy(self.context)

    def isManager(self):
        pm = getToolByName(self.context, 'portal_membership')
        return pm.checkPermission('Manage portal', self.context)

