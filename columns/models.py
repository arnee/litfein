from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.models import MediaFileContent

Page.register_extensions(
    'feincms.module.page.extensions.navigation',
    'feincms.module.page.extensions.titles',
    'feincms.module.extensions.seo',
    'feincms.module.extensions.featured',
    'feincms.module.page.extensions.excerpt',
    #'feincms.module.extensions.translations',
    'feincms.module.extensions.datepublisher',
    ) # Example set of extensions


Page.register_templates(
    {
        'key': 'one-col',
        'title': _('One column template'),
        'path': 'one_column_page.html',
        'regions': (
            ('col1', _('Main column')),
        ),
    },
    {
        'key': 'two-cols',
        'title': _('Two columns template'),
        'path': 'two_columns_page.html',
        'regions': (
            ('coll', _('Left column')),
            ('colr', _('Right column')),
        ),
    },

)

Page.create_content_type(RichTextContent)
Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
    ('lightbox', _('lightbox')),
))


