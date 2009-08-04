# -*- coding: utf-8 -*-

import grok


class CanReviewContent(grok.Permission):
    grok.name('dolmen.control.Review')
    grok.title('dolmen: review content')
    
