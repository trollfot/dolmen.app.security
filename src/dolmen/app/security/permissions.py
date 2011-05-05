# -*- coding: utf-8 -*-

from dolmen.app.security import mf as _
from dolmen.security import components as security
from zope.interface import Interface, Attribute, moduleProvides


class CanAddContent(security.Permission):
    security.name('dolmen.content.Add')
    security.title(_(u"Add content"))


class CanEditContent(security.Permission):
    security.name('dolmen.content.Edit')
    security.title(_(u"Edit content"))


class CanViewContent(security.Permission):
    security.name('dolmen.content.View')
    security.title(_(u"View content"))


class CanListContent(security.Permission):
    security.name('dolmen.content.List')
    security.title(_(u"List the container content"))


class CanDeleteContent(security.Permission):
    security.name('dolmen.content.Delete')
    security.title(_(u"Delete content"))


class CanCopyContent(security.Permission):
    security.name('dolmen.content.Copy')
    security.title(_(u"Copy content to the clipboard"))


class CanCutContent(security.Permission):
    security.name('dolmen.content.Cut')
    security.title(_(u"Cut content to the clipboard"))


class CanPasteContent(security.Permission):
    security.name('dolmen.content.Paste')
    security.title(_(u"Paste content from the clipboard"))


class CanReviewContent(security.Permission):
    security.name('dolmen.control.Review')
    security.title(_(u"Review and annotate content"))


class IContentPermissions(Interface):
    """Public Dolmen content centric permissions
    """
    CanAddContent = Attribute("Add content")
    CanEditContent = Attribute("Edit content")
    CanViewContent = Attribute("View content")
    CanListContent = Attribute("List the container content")
    CanDeleteContent = Attribute("Delete content")
    CanCopyContent = Attribute("Copy content to the clipboard")
    CanCutContent = Attribute("Cut content to the clipboard")
    CanPasteContent = Attribute("Paste content from the clipboard")
    CanReviewContent = Attribute("Review and annotate content")


moduleProvides(IContentPermissions)
__all__ = list(IContentPermissions)
