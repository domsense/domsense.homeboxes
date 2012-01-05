from zope.site.hooks import getSite

from zope import interface

from domsense.homeboxes.interfaces import IHomeBoxContainer
from domsense.homeboxes.config import CONTAINER_DEFAULT_ID
from domsense.homeboxes.config import CONTAINER_DEFAULT_TITLE


def setupVarious(context):

    if context.readDataFile('domsense.homeboxes.import_various.txt') is None:
        return

    site = getSite()
    if not hasattr(site,CONTAINER_DEFAULT_ID):
        site.invokeFactory('Folder',
                           CONTAINER_DEFAULT_ID,
                           title=CONTAINER_DEFAULT_TITLE)
        folder = getattr(site,CONTAINER_DEFAULT_ID)
        folder.markCreationFlag()
        interface.alsoProvides(folder,IHomeBoxContainer)

        # omit from nav
        folder.getField('excludeFromNav').set(folder,True)
        folder.reindexObject()

        # set constrain on type
        if not folder.getConstrainTypesMode():
            folder.setConstrainTypesMode(1)
        # flush allowed types
        folder.setLocallyAllowedTypes(())
        # set proper type
        folder.setLocallyAllowedTypes(['HomeBox',])






