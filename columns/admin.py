from django.contrib import admin

from feincms.module.page.models import Page
from feincms.module.page.admin import PageAdmin

from feincms.module.medialibrary.models import Category, MediaFile
from feincms.module.medialibrary.modeladmins import\
    CategoryAdmin, MediaFileAdmin

from elephantblog.models import Category as EntryCategory
from elephantblog.models import CategoryTranslation as EntryCategoryTranslation
from elephantblog.modeladmins import CategoryAdmin as EntryCategoryAdmin

from .forms import EntryCategoryTranslationForm


admin.site.unregister(MediaFile)
admin.site.unregister(EntryCategory)


class MediaFileNoTransAdmin(MediaFileAdmin):
    inlines = []


class EntryCategoryNoTransInline(admin.StackedInline):
    extra = 1
    max_num = 1
    model = EntryCategoryTranslation
    prepopulated_fields = {
        'slug': ('title', )
    }
    form = EntryCategoryTranslationForm


class EntryCategoryNoTransAdmin(EntryCategoryAdmin):
    inlines = [EntryCategoryNoTransInline]


class PageAdminExtra(PageAdmin):
    raw_id_fields = PageAdmin.raw_id_fields + ["background_image",]


admin.site.register(MediaFile, MediaFileNoTransAdmin)
admin.site.register(EntryCategory, EntryCategoryNoTransAdmin)
admin.site.register(Page, PageAdminExtra)
