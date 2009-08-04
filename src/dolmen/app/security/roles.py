# -*- coding: utf-8 -*-

import grok


class MemberRole(grok.Role):
    grok.name('dolmen.Member')
    grok.permissions(
        'dolmen.content.View',
        'dolmen.content.Copy',
        )


class OwnerRole(grok.Role):
    grok.name('dolmen.Owner')
    grok.permissions(
        'dolmen.content.Add',
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.content.Cut',
        'dolmen.content.Copy',
        'dolmen.content.Paste',
        )
    

class ContributorRole(grok.Role):
    grok.name('dolmen.Contributor')
    grok.permissions(
        'dolmen.content.Add',
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.content.Cut',
        'dolmen.content.Copy',
        'dolmen.content.Paste',
        )


class ReviewerRole(grok.Role):
    grok.name('dolmen.Reviewer')
    grok.permissions(
        'dolmen.content.View',
        'dolmen.content.Edit',
        'dolmen.control.Review',
        )
