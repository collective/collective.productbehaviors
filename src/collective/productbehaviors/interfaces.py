from zope.interface import Interface

from browser.viewlets import IProductViewletManager

class IProduct(Interface):
   ""

class IProductBehaviorsInstalled(Interface):
   "browser layer marker"


# markers for behaviors

class IDimensionable(Interface):
   ""

class IWeightable(Interface):
   ""

class IDistributable(Interface):
   ""