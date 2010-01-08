# -*- coding: utf-8 -*-

import grok
from zope.interface import Interface, Attribute, moduleProvides

from dolmen.app.security import mf as _


class Member(grok.Role):
    grok.name('dolmen.Member')
    grok.title(_(u"Member"))
    grok.description(_(u"A basic member."))
    grok.permissions(
        'dolmen.content.View',
        'dolmen.content.Copy',
        )


class Owner(grok.Role):
    grok.name('dolmen.Owner')
    grok.title(_(u"Owner"))
    grok.description(_(u"The owner of an object."))
    grok.permissions(
        'dolmen.content.Add',
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.content.Cut',
        'dolmen.content.Copy',
        'dolmen.content.Paste',
        'dolmen.content.Delete',
        )
    

class Contributor(grok.Role):
    grok.name('dolmen.Contributor')
    grok.title(_(u"Contributor"))
    grok.description(_(u"A content contributor."))
    grok.permissions(
        'dolmen.content.Add',
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.content.Cut',
        'dolmen.content.Copy',
        'dolmen.content.Paste',
        'dolmen.content.Delete',
        )


class Reviewer(grok.Role):
    grok.name('dolmen.Reviewer')
    grok.title(_(u"Reviewer"))
    grok.description(_(u"A content reviewer."))
    grok.permissions(
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.control.Review',
        )


class IDolmenRoles(Interface):
    """The public Dolmen roles
    """
    Owner = Attribute("The owner of an object.")
    Member = Attribute("A basic member.")
    Reviewer = Attribute("A content reviewer.")
    Contributor = Attribute("A content contributor.")
    

moduleProvides(IDolmenRoles)
__all__ = list(IDolmenRoles)
