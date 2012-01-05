from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class DomsenseHomeboxes(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import domsense.homeboxes
        xmlconfig.file('configure.zcml',
                       domsense.homeboxes,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'domsense.homeboxes:default')

DOMSENSE_HOMEBOXES_FIXTURE = DomsenseHomeboxes()
DOMSENSE_HOMEBOXES_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(DOMSENSE_HOMEBOXES_FIXTURE, ),
                       name="DomsenseHomeboxes:Integration")