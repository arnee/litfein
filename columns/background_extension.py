from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms.module.medialibrary.fields import MediaFileForeignKey
from feincms.module.medialibrary.models import MediaFile

from feincms import extensions


class Extension(extensions.Extension):

    def handle_model(self):
        self.model.add_to_class(
            'background_image', MediaFileForeignKey(MediaFile, blank=True, null=True, verbose_name='backgroud_image'),
        )

        if hasattr(self.model, 'cache_key_components'):
            self.model.cache_key_components.append(lambda page: page.background_image_id)

    def handle_modeladmin(self, modeladmin):
        modeladmin.add_extension_options(_('Background image'), {
            'fields': ('background_image',),
            'classes': ('collapse',),
        })
