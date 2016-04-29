from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
urlpatterns=[
		url(r'^$',views.index,name='index'),
		url(r'^about/$',views.about,name='about'),
		url(r'^about1/$',views.about1,name='about1'),
		url(r'^new/$',views.new,name='new'),
		url(r'^new1/$',views.new1,name='new1'),
		url(r'^page/$',views.page,name='page'),
		url(r'^search/$',views.search,name='search'),
		url(r'^search1/$',views.search1,name='search1'),
		url(r'^contact/$',views.contact,name='contact'),
		url(r'^contact1/$',views.contact1,name='contact1'),
		url(r'^contacts/$',views.contacts,name='contacts'),
		url(r'^login/$',views.login,name='login'),
		url(r'^searching/$',views.searching,name='searching'),
		url(r'^static/$',TemplateView.as_view(template_name="searching.html"),name='searching'),
		url(r'^serialjson/$',views.serialjson,name='serial'),
]

