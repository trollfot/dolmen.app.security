# -*- coding: utf-8 -*-

import grok
from zope.interface import Interface, Attribute, moduleProvides

from dolmen.app.security import mf as _


class CanAddContent(grok.Permission):
    grok.name('dolmen.content.Add')
    grok.title(_(u"Add content"))


class CanEditContent(grok.Permission):
    grok.name('dolmen.content.Edit')
    grok.title(_(u"Edit content"))


class CanViewContent(grok.Permission):
    grok.name('dolmen.content.View')
    grok.title(_(u"View content"))


class CanListContent(grok.Permission):
    grok.name('dolmen.content.List')
    grok.title(_(u"List the container content"))


class CanDeleteContent(grok.Permission):
    grok.name('dolmen.content.Delete')
    grok.title(_(u"Delete content"))


class CanCopyContent(grok.Permission):
    grok.name('dolmen.content.Copy')
    grok.title(_(u"Copy content to the clipboard"))


class CanCutContent(grok.Permission):
    grok.name('dolmen.content.Cut')
    grok.title(_(u"Cut content to the clipboard"))


class CanPasteContent(grok.Permission):
    grok.name('dolmen.content.Paste')
    grok.title(_(u"Paste content from the clipboard"))

    
class CanReviewContent(grok.Permission):
    grok.name('dolmen.control.Review')
    grok.title(_(u"Review and annotate content"))


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
