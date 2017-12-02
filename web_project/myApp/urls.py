from django.conf.urls import url
from django.views.generic import TemplateView
from .import views
urlpatterns = [
    url('^$', views.home,name='home'),
    url('^results/$',views.results,name='results'),
    url(r'^register/$',views.register,name='register'),
    url(r'^add_school/$',views.add_school,name='add school'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_redir/$',views.login_redir,name='login_redir'),
    url(r'^logout/$',views.logout_,name='logout'),
    url(r'accounts/profile/(?P<USER>.+)/$',views.profile,name='profile'),
    url(r'^post/$',views.post,name='Post'),
]
