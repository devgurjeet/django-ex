from django.conf.urls import include, url
from demo.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^blog/', include('blog.urls')),
 ]
