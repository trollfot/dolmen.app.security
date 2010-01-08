===================
dolmen.app.security
===================

`dolmen.app.security` is a package providing a collection of basic roles and
permissions for a Dolmen application.

  >>> import dolmen.app.security
  >>> from dolmen.app.security import IDolmenSecurity
  >>> from dolmen.app.security.roles import IDolmenRoles
  >>> from dolmen.app.security.content import IContentPermissions
  
  >>> IDolmenSecurity.extends(IDolmenRoles)
  True
  >>> IDolmenSecurity.extends(IContentPermissions)
  True

  >>> IDolmenSecurity.providedBy(dolmen.app.security)
  True


Content centric permissions
===========================

  >>> import dolmen.app.security.content

  >>> IContentPermissions.providedBy(dolmen.app.security.content)
  True

  >>> for name, attr in sorted(IContentPermissions.namesAndDescriptions()):
  ...   print "%s: %s" % (name, attr.getDoc())
  CanAddContent: Add content
  CanCopyContent: Copy content to the clipboard
  CanCutContent: Cut content to the clipboard
  CanDeleteContent: Delete content
  CanEditContent: Edit content
  CanListContent: List the container content
  CanPasteContent: Paste content from the clipboard
  CanReviewContent: Review and annotate content
  CanViewContent: View content



Dolmen application roles
========================

  >>> import dolmen.app.security.roles

  >>> IDolmenRoles.providedBy(dolmen.app.security.roles)
  True

  >>> for name, attr in sorted(IDolmenRoles.namesAndDescriptions()):
  ...   print "%s: %s" % (name, attr.getDoc())
  Contributor: A content contributor.
  Member: A basic member.
  Owner: The owner of an object.
  Reviewer: A content reviewer.
