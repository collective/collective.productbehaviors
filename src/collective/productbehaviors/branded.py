from zope.interface import alsoProvides, implements, Interface, implementer
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.app.content.interfaces import INameFromTitle

from collective.productbehaviors import MessageFactory as _

from interfaces import IProduct

class INameFromBrandInfo(INameFromTitle):
    "behavior"


class IBranded(Interface):
    "marker interface to attach INameFromBrandInfo to"


class NameFromBrandInfo(object):
    implements(INameFromBrandInfo)

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        return u"%s %s" % (self.context.brand, self.context.model)


class IBrandInfo(form.Schema):
    """Marker/Form interface for Brand Info"""

    brand = schema.TextLine(
        title=_(u'label_brand', default=u'Brand'),
        required=False
    )

    model = schema.TextLine(
        title=_(u'label_model', default=u'Model'),
        required=False
    )

alsoProvides(IBrandInfo,IFormFieldProvider)


def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class BrandInfo(object):
    """
       Adapter for Brand Info
    """
    implements(IBrandInfo)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    brand = context_property("brand")
    model = context_property("model")
