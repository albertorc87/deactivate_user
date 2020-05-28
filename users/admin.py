"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import User

# Esta función recibe un queryset con los usuarios seleccionados y lanzaremos un update para desactivarlos
def desactivar_usuarios(modeladmin, request, queryset):
    queryset.update(is_active=False)

desactivar_usuarios.short_description = 'Desactivar usuarios'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = ('pk', 'username', 'email','is_active','is_staff',)
    list_display_links = ('pk', 'username', 'email',)

    # En actions añadimos las funcionalidades extra
    actions = [desactivar_usuarios]