# -*- coding: utf-8 -*-

from dolmen.app.security import roles
from dolmen.app.security import IContentPermissions, IDolmenRoles
from dolmen.security import components
from grokcore.component import testing
from zope.testing.cleanup import cleanUp
from zope.component import getUtilitiesFor
from zope.securitypolicy.interfaces import IRole
from zope.security.interfaces import IPermission


def setup_module(module):
    testing.grok("dolmen.security.components.meta")
    testing.grok("grokcore.security.meta")
    testing.grok("dolmen.app.security")


def teardown_module(module):
    cleanUp()


def iface_attrs(iface):
    return set([name for name, attr in iface.namesAndDescriptions()])


def get_permissions(role):
    return components.permissions.bind().get(role)
    

def test_registered_roles():
    
    roles = set([str(role.__class__.__name__)
                 for id, role in getUtilitiesFor(IRole)])
    assert roles == iface_attrs(IDolmenRoles)


def test_permissions_for_roles():

    assert get_permissions(roles.Member) == [
        'dolmen.content.View',
        'dolmen.content.Copy',
        ]
         
    assert get_permissions(roles.Reviewer) == [
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.control.Review',
        ]

    assert get_permissions(roles.Owner) == [
        'dolmen.content.Add',
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.content.Cut',
        'dolmen.content.Copy',
        'dolmen.content.Paste',
        'dolmen.content.Delete',
        ]

    assert get_permissions(roles.Contributor) == [
        'dolmen.content.Add',
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.content.Cut',
        'dolmen.content.Copy',
        'dolmen.content.Paste',
        'dolmen.content.Delete',
        ]
    

def test_registered_permissions():

    perms = set([str(perm.__class__.__name__)
                 for id, perm in getUtilitiesFor(IPermission)])
    assert perms == iface_attrs(IContentPermissions)
