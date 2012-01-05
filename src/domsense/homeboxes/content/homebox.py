"""Definition of the HomeBox content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import folder

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import *

from Products.CMFCore.utils import getToolByName

from domsense.homeboxes import homeboxMessageFactory as _
from domsense.homeboxes.interfaces import IHomeBox
from domsense.homeboxes.config import PROJECTNAME

HomeBoxSchema = folder.ATFolderSchema.copy() + atapi.Schema((


    atapi.StringField(
        'style',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Style"),
            description=_(u"Choose the style of the box"),
        ),
        default=_(u"default"),
    ),

    atapi.StringField(
        'width',
        storage=atapi.AnnotationStorage(),
        vocabulary=(
                    ('normal','Normal'),
                    ('double','Double'),
                    ('triple','Triple'),
                    ('full','Full'),
                    ),
        widget=atapi.SelectionWidget(
            label=_(u"Width"),
            description=_(u"Choose the width of the box"),
        ),
        default=_(u"normal"),
    ),

    atapi.StringField(
        'height',
        storage=atapi.AnnotationStorage(),
        vocabulary=(
                    ('half','Half'),
                    ('normal','Normal'),
                    ('double','Double'),
                    ('triple','Triple'),
                    ('quad','Quad'),
                    ),
        widget=atapi.SelectionWidget(
            label=_(u"Height"),
            description=_(u"Choose the height of the box"),
        ),
        default=_(u"normal"),
    ),

    atapi.ReferenceField(
        'resource',
        storage=atapi.AnnotationStorage(),
        relationship='resource_link',
        widget=ReferenceBrowserWidget(
            label=_(u"Resources"),
            description=_(u"Resources to load"),
        ),
        multiValued = True,
    ),

    atapi.TextField(
        'text',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Text"),
            description=_(u"Field description"),
        ),
    ),

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'appearance',
        storage=atapi.AnnotationStorage(),
        vocabulary_factory='homeboxes_vocab',
        widget=atapi.SelectionWidget(
            label=_(u"Appearance"),
            description=_(u"Field description"),
        ),
    ),

    atapi.BooleanField(
        'showControls',
        storage=atapi.AnnotationStorage(),
        widget=atapi.BooleanWidget(
            label=_(u"Show controls"),
            description=_(u"Field description"),
        ),
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

HomeBoxSchema['title'].storage = atapi.AnnotationStorage()
HomeBoxSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(HomeBoxSchema, moveDiscussion=False)

class HomeBox(folder.ATFolder):
    """Description of the Example Type"""
    implements(IHomeBox)

    meta_type = "HomeBox"
    schema = HomeBoxSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    text = atapi.ATFieldProperty('text')
    style = atapi.ATFieldProperty('style')
    resource = atapi.ATReferenceFieldProperty('resource')
    appearance = atapi.ATFieldProperty('appearance')
    width = atapi.ATFieldProperty('width')
    height = atapi.ATFieldProperty('height')
    showControls = atapi.ATFieldProperty('showControls')


atapi.registerType(HomeBox, PROJECTNAME)
