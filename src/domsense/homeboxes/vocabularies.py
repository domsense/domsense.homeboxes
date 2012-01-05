# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.schema import vocabulary
from zope import component

try:
    from zope.app.schema.vocabulary import IVocabularyFactory
except:
    from zope.schema.interfaces import IVocabularyFactory

from Products.CMFCore.utils import getToolByName

from domsense.homeboxes.browser.interfaces import IHomeBoxRenderer


class BaseVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []
        for term in self.terms:
            terms.append(vocabulary.SimpleVocabulary.createTerm(term[0],
                                                                term[0],
                                                                term[1]))
        return vocabulary.SimpleVocabulary(terms)

    @property
    def terms(self):
        return []

    def get_dict(self):
        return dict(self.terms)


class HomeboxesList(BaseVocabulary):

    @property
    def terms(self):
        gsm = component.getGlobalSiteManager()
        # XXX: is this the best way???
        items = [(x.name,x.factory.name)
                 for x in gsm.registeredAdapters()
                 if x.provided == IHomeBoxRenderer]
        return sorted(items,key=lambda x: x[1])
