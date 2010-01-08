# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory
from zope.interface import moduleProvides

mf = MessageFactory("dolmen.app.security")

from content import *
from content import IContentPermissions

from roles import *
from roles import IDolmenRoles


class IDolmenSecurity(IContentPermissions, IDolmenRoles):
    """A public Dolmen security API
    """


moduleProvides(IDolmenSecurity)
__all__ = list(IDolmenSecurity)
