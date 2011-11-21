from django import template
from django.http import HttpRequest
from django.template import RequestContext


register = template.Library()

@register.simple_tag
def url_for(request, format):
    ''' adds a .format to the URL, taking query string into account
        eg, convert '/intel/all?search=xy' to '/intel/all.csv?search=xy'
    '''
    path = request.path.rstrip('/')
    full_path = request.get_full_path()

    # if format already exists, do nothing
    if path.endswith(".%s" % format):
        return full_path
    else:
        return full_path.replace(path, path + "." + format, 1)
        
        
@register.simple_tag
def attr_name(attr):
    ''' "sampledata_some_crap" => "some crap" '''
    return attr.replace("sampledata_", "").replace("_", " ")

@register.simple_tag
def follow_up_attr_name(attr):
    ''' "safe_pregnancy_crap" => "some crap" '''
    return attr.replace("safe_pregnancy_", "").replace("case_update_", "").replace("_", " ")
