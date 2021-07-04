from django import template
from ortodont.models import About, Contact, Services

register = template.Library()


@register.inclusion_tag('ortodont/menu.html')
def show_menu(menu_class='menu'):
    about = About.objects.all()
    contact = Contact.objects.all()
    services = Services.objects.all()
    return {"about": about, "contact": contact, "services": services, "menu_class": menu_class}





