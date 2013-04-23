from zope.interface import alsoProvides, implements, Interface
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from collective.productbehaviors import MessageFactory as _
from util import context_property


class IWeighted(form.Schema):
    ""
    weight = schema.Decimal(
        title=_(u'label_weight', default=u'Weight'),
        required=False
    )

alsoProvides(IWeighted,IFormFieldProvider)

class Weighted(object):
    """Adapter for weight"""

    implements(IWeighted)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    weight = context_property("weight")


class IDimensioned(form.Schema):
    """Marker/Form interface for Physical Info"""

    length = schema.Decimal(
        title=_(u'label_length', default=u'Length'),
        required=False
    )

    width = schema.Decimal(
        title=_(u'label_width', default=u'Width'),
        required=False
    )

    height = schema.Decimal(
        title=_(u'label_height', default=u'Height'),
        required=False
    )

    # -*- Your Zope schema definitions here ... -*-

alsoProvides(IDimensioned,IFormFieldProvider)


class Dimensioned(object):
    """Adapter for dimensions"""

    implements(IDimensioned)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context


    # -*- Your behavior property setters & getters here ... -*-

    length = context_property("length")
    width = context_property("width")
    height = context_property("height")
