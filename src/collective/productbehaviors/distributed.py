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
from util import context_property


class IDistributed(Interface):
    "marker interface for delivery information"


class IDistributionInfo(form.Schema):
    "delivery information"

    manufacturer = schema.TextLine(
        title=_(u'label_manufacturer', default=u'Manufacturer'),
        required=False
    )

    oems = schema.List(
        title=_(u'label_oems', default=u'OEMs'),
        description = _(u'help_oems', default=u'Original equipment manufacturers'),
        required=False
    )

    importers = schema.List(
        title=_(u'label_importers', default=u'Importers'),
        required=False
    )

    distributors = schema.List(
        title=_(u'label_distributors', default=u'Distributors'),
        required=False
    )

alsoProvides(IDistributionInfo,IFormFieldProvider)


class DistributionInfo(object):
    """
       Adapter for distribution info
    """
    implements(IDistributionInfo)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    manufacturer = context_property("manufacturer")
    oems = context_property("oems")
    importers = context_property("importers")
    distributors = context_property("distributors")
