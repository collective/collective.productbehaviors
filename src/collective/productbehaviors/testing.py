from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectiveproductbehaviorsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.productbehaviors
        xmlconfig.file(
            'configure.zcml',
            collective.productbehaviors,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.productbehaviors:default')

COLLECTIVE_PRODUCTBEHAVIORS_FIXTURE = CollectiveproductbehaviorsLayer()
COLLECTIVE_PRODUCTBEHAVIORS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_PRODUCTBEHAVIORS_FIXTURE,),
    name="CollectiveproductbehaviorsLayer:Integration"
)
COLLECTIVE_PRODUCTBEHAVIORS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_PRODUCTBEHAVIORS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectiveproductbehaviorsLayer:Functional"
)
