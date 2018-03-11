from django.conf.urls import include, url
from demo.views import index,testing, addDemo, getDemo, deleteDemos

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^testing/$', testing, name='testing'),
    url(r'^add/$', addDemo, name='add-demo'),
    url(r'^get/$', getDemo, name='get-demo'),
    url(r'^delete/$', deleteDemos, name='delete-demo'),

    # url(r'^blog/', include('blog.urls')),
 ]
