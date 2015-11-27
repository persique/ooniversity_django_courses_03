from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'email', 'skype')
	search_fields = ['surname', 'name']
	list_filter = ['courses']
	fieldsets = (
		('Personal info', {
			'fields': ('name', 'surname', 'date_of_birth')
		}), 
		('Contact info', {
			'fields': ('email', 'phone', 'address', 'skype')
		}),
		(None, {
			'fields': ('courses', ),
		}), 
	)

	def full_name(self, obj):
		return "%s %s" % (obj.surname, obj.name)

admin.site.register(Student, StudentAdmin)