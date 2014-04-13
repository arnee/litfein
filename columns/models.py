from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.models import MediaFileContent

import feincms_cleanse

from elephantblog.models import Entry
from feincms.content.application.models import ApplicationContent
from elephantblog.navigation_extensions import treeinfo
from form_designer.models import FormContent


Page.register_extensions(
    'feincms.module.page.extensions.navigation',
    #'feincms.module.page.extensions.titles',
    'feincms.module.extensions.seo',
    #'feincms.module.extensions.featured',
    #'feincms.module.page.extensions.excerpt',
    #'feincms.module.extensions.datepublisher',
    'columns.background_extension',
)


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
Page.create_content_type(FormContent)
Page.create_content_type(ApplicationContent, APPLICATIONS=(
    ('elephantblog.urls', 'Blog'),
))


Entry.register_extensions(
    'feincms.module.extensions.datepublisher',
)

Entry.register_regions(
    ('main', _('Main content area')),
)

Entry.create_content_type(
    RichTextContent,
    cleanse=feincms_cleanse.cleanse_html,
    regions=('main',)
)

Entry.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),

))
