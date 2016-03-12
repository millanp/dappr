from django.contrib import admin, messages
from dappr.models import RegistrationProfile

def selection_valid(modeladmin, request, queryset):
    """
    Verify that the selected registration profiles are ready for action
    
    Args:
        modeladmin: the current admin interface
        request: request object sent with admin action
        queryset: queryset of objects selected
    Returns:
        boolean, indicating whether selection is valid
    """
    # Check whether selection contains profiles of people whose identity has not been confirmed.
    if queryset.filter(identity_confirmed=False).exists():
        modeladmin.message_user(request, 
                                "One or more users have not confirmed their identity", 
                                level=messages.ERROR)
        return False
    # Check whether selection contains inactive (dealt with) registration profiles
    if queryset.filter(active=False).exists():
        modeladmin.message_user(request,
                                "One or more registration profiles are inactive (already dealt with)")
        return False
    return True
def approve_requests(modeladmin, request, queryset):
    """
    Approve selected requests, and send email notification to users
    
    Args:
        modeladmin: the current admin interface
        request: request object sent with admin action
        queryset: queryset of objects selected
    """
    if not selection_valid(modeladmin, request, queryset): return
    
    # Update selected registration profiles to the "approved" state
    queryset.update(approved=True)
    queryset.update(active=False)
    
    # Activate all users associated with selected registration profiles 
    # and send email notifications
    for profile in queryset:
        profile.user.is_active = True
        profile.user.save()
        profile.send_approval_notification()
approve_requests.short_description = "Approve selected account request(s)"


def reject_requests(modeladmin, request, queryset):
    """
    Reject selected requests, and send email notification to users
    
    Args:
        modeladmin: the current admin interface
        request: request object sent with admin action
        queryset: queryset of objects selected
    """
    if not selection_valid(modeladmin, request, queryset): return
    queryset.update(active=False)
    for profile in queryset:
        profile.user.delete()
        profile.send_rejection_notification()
reject_requests.short_description = "Reject selected account request(s)"


class RegistrationAdmin(admin.ModelAdmin):
    """
    Simple modeladmin for RegistrationProfile, 
    displaying the fields "user", "identity_confirmed", "confirmation_key", 
    and "approved".
    """
    list_display = ('user', 'identity_confirmed', 'confirmation_key', 'approved')
    actions = (approve_requests, reject_requests)
admin.site.register(RegistrationProfile, RegistrationAdmin)
