from django.contrib import admin
from base.models import *
# Register your models here.

#base
admin.site.register(Galery)
admin.site.register(Contact)
admin.site.register(Settings)

#pages
admin.site.register(Error)
admin.site.register(About)
admin.site.register(Coming)
admin.site.register(Faq)
admin.site.register(Terms)

#index pages
admin.site.register(SettingsTwo)
admin.site.register(SettingsThree)
admin.site.register(SettingsFour)
admin.site.register(SettingsFive)

#forms
admin.site.register(HelpMessage)
admin.site.register(Reservation)