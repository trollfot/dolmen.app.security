# -*- coding: utf-8 -*-

from dolmen.app.security import mf as _
from dolmen.security import components as security
from zope.interface import Interface, Attribute, moduleProvides


class Member(security.Role):
    security.name('dolmen.Member')
    security.title(_(u"Member"))
    security.description(_(u"A basic member."))
    security.permissions(
        'dolmen.content.View',
        'dolmen.content.Copy',
        )


class Owner(security.Role):
    security.name('dolmen.Owner')
    security.title(_(u"Owner"))
    security.description(_(u"The owner of an object."))
    security.permissions(
        'dolmen.content.Add',
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.content.Cut',
        'dolmen.content.Copy',
        'dolmen.content.Paste',
        'dolmen.content.Delete',
        )


class Contributor(security.Role):
    security.name('dolmen.Contributor')
    security.title(_(u"Contributor"))
    security.description(_(u"A content contributor."))
    security.permissions(
        'dolmen.content.Add',
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.content.Cut',
        'dolmen.content.Copy',
        'dolmen.content.Paste',
        'dolmen.content.Delete',
        )


class Reviewer(security.Role):
    security.name('dolmen.Reviewer')
    security.title(_(u"Reviewer"))
    security.description(_(u"A content reviewer."))
    security.permissions(
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
