from django.conf.urls.defaults import *

urlpatterns = patterns('intel.views',
    (r'^intel/?$', 'homepage'),
    (r'^intel/all\.?(?P<format>[a-zA-Z0-9\.].*)?/?$', 'all_mothers_report'),
    (r'^intel/risk\.?(?P<format>[a-zA-Z0-9\.].*)?/?$', 'hi_risk_report'),
    (r'^intel/details/?$', 'mother_details'),
    
    (r'^intel/chart/?$', 'chart'),
    
    (r'^intel/hq_chart/?$', 'hq_chart'),
    (r'^intel/hq_risk/?$', 'hq_risk'),
)