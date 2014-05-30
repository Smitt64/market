from django.template        import Library
from django.template.loader import render_to_string

from django.contrib         import messages


register = Library()

from ..forms import GetPhoneForm

@register.simple_tag(takes_context=True)
def getcall_form(context):
    request = context['request']
    #messages.info(request, "user:"+request.user.last_name)
    form = GetPhoneForm(request.user)
    return render_to_string("own_forms/own_forms.html",{'get_call_form': form}, context_instance=context)