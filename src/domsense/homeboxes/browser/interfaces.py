from plone.theme.interfaces import IDefaultPloneLayer
from zope.viewlet.interfaces import IViewletManager
from zope.interface import Interface


class IHomeBoxLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "agile_skin" theme, this interface must be its layer
       (in theme2011/viewlets/configure.zcml).
    """
    
class IHomeboxManager(IViewletManager):
    """ [A description of your viewlet manager goes here]  """
    
class IHomeBoxRenderer(Interface):
    """
    """
