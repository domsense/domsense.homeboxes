from zope import interface
from zope import component

from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from domsense.homeboxes.browser.interfaces import IHomeBoxRenderer
from domsense.homeboxes.interfaces import IHomeBox
from domsense.homeboxes import _

TEMPLATES = dict(
    doc = ViewPageTemplateFile("box_doc.pt"),
    imgslide = ViewPageTemplateFile("box_imgslide.pt"),
    docslide = ViewPageTemplateFile("box_docslide.pt"),
    eventslide = ViewPageTemplateFile("box_eventslide.pt"),
)

class Base(object):

    interface.implements(IHomeBoxRenderer)
    component.adapts(IHomeBox)

    id = ""
    name = ""
    template_options = {}
    extra_css_class = ""

    def __init__(self, box):
        self.context = box
        # XXX: from Zope >= 2.12 ViewPageTemplateFile requires
        # an instance as 1st arg that provides
        # `request` and `context' attributes
        # see http://svn.zope.org/Zope/trunk/src/Products/Five/browser/pagetemplatefile.py
        self.request = box.REQUEST

    @property
    def template(self):
        return TEMPLATES.get(self.id)

    @property
    def template_options(self):
        raise NotImplementedError()

    def render(self):
        return self.template(self, **self.template_options)

    def getWrapperCssClass(self):
        klass = "homebox-wrapper homebox-%s" % self.id
        klass += " boxwidth-%s boxheight-%s" % (self.context.width,
                                                self.context.height)
        if self.extra_css_class:
            klass += " " + self.extra_css_class
        if not self.showControls():
            klass += " hidden-controls"
        return klass

    def getCssClass(self):
        return "homebox " + self.context.style

    @property
    def url(self):
        return self.context.absolute_url()

    @property
    def title(self):
        return self.context.Title()

    def showControls(self):
        return self.context.showControls

    @property
    def portal_transforms(self):
        return getToolByName(self.context, 'portal_transforms')

    def transform_text(self, text):
        convertTo = self.portal_transforms.convertTo
        # get rid if resolveUID links
        # thanks to plone.outputfilters
        text = convertTo('text/x-html-safe', text,
                         mimetype='text/html',
                         context=self.context).getData()
        return text


class Doc(Base):

    id = "doc"
    name = _("Single doc")

    def getText(self):
        text = self.context.getRawText()
        if not text:
            resource = self.context.getResource()[0]
            if resource.getRawText():
                text = resource.getRawText()
        text = self.transform_text(text)
        return text

    @property
    def template_options(self):
        text = self.getText()
        return dict(text=text,)


class BaseSlide(Base):

    extra_css_class = "slide"

    @property
    def template_options(self):
        contents = self.getContents()
        return dict(contents=contents,)


class ImgSlide(BaseSlide):

    id = "imgslide"
    name = _("Image slideshow")

class DocSlide(BaseSlide):

    id = "docslide"
    name = _("Doc slideshow")

    def getContents(self):
        result = []
        contents = self.context.objectValues()
        if not contents:
            contents = self.context.getResource()
        for i in contents:
            text = i.getRawText()
            text = self.transform_text(text)
            result.append(
                dict(uid=i.UID(),
                     title=i.Title(),
                     text=text,)
            )
        return result

class EventSlide(BaseSlide):

    id = "eventslide"
    name = _("Event slideshow")