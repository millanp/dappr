from django.contrib import admin, messages
from dappr.models import RegistrationProfile

# Register your models here.
def validate_selection(modeladmin, request, queryset):
    if queryset.filter(identity_confirmed=False).exists():
        modeladmin.message_user(request, 
                                "One or more of the selected users have not confirmed their identity", 
                                level=messages.ERROR)
        return
    # Do not allow if anything is already approved
    if queryset.filter(approved=True).exists():
        modeladmin.message_user(request,
                                "One or more registration profiles have already been approved",
                                level=messages.ERROR)
        return


def approve_requests(modeladmin, request, queryset):
    validate_selection(modeladmin, request, queryset)
    # Activate all associated users
    queryset.update(approved=True)
    queryset.update(active=False)
    for profile in queryset:
        profile.user.is_active = True
        profile.user.save()
        profile.send_approval_notification()
approve_requests.short_description = "Approve selected account request(s)"


def reject_requests(modeladmin, request, queryset):
    validate_selection(modeladmin, request, queryset)
    queryset.update(active=False)
    for profile in queryset:
        profile.user.delete()
        profile.send_rejection_notification()
reject_requests.short_description = "Reject selected account request(s)"


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'identity_confirmed', 'confirmation_key', 'approved')
    actions = (approve_requests, reject_requests)
admin.site.register(RegistrationProfile, RegistrationAdmin)
