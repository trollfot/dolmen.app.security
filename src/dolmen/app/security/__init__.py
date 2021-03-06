# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory
from zope.interface import moduleProvides

mf = MessageFactory("dolmen.app.security")

from dolmen.app.security.permissions import *
from dolmen.app.security.permissions import IContentPermissions

from dolmen.app.security.roles import *
from dolmen.app.security.roles import IDolmenRoles


class IDolmenSecurity(IContentPermissions, IDolmenRoles):
    """A public Dolmen security API
    """


moduleProvides(IDolmenSecurity)
__all__ = list(IDolmenSecurity)
