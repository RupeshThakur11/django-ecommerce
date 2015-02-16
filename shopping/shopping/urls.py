from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/$', 'products.views.product_page'),
    (r'^media(?P<path>.*)$','django.views.static.serve', {'document_root':'C:/Users/Administrator/lwcShopping/shopping/static/media'}),
    (r'^static(?P<path>.*)$','django.views.static.serve', {'document_root':'C:/Users/Administrator/lwcShopping/shopping/static'}),
    (r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^products/(?P<slug>[-\w]+)/$', 'products.views.product_single'),
    url(r'^products/(?P<slug>[-\w]+)/add$', 'cart.views.add'),
    url(r'^$','products.views.home'),
    url(r'^contact/$', 'contact.views.contact'),
    url(r'^cart/$','cart.views.viewcart'),
    url(r'^cart/delete$','cart.views.deleteCart'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^accounts/', TemplateView.as_view('registration.backends.default.urls')),

    # url(r'^shopping/', include('shopping.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   
)
