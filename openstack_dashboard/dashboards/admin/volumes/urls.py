# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf.urls import include  # noqa
from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from openstack_dashboard.dashboards.admin.volumes.extras \
    import urls as extras_urls
from openstack_dashboard.dashboards.admin.volumes import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create_type$', views.CreateVolumeTypeView.as_view(),
        name='create_type'),
    url(r'^(?P<volume_id>[^/]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<type_id>[^/]+)/extras/',
        include(extras_urls, namespace='extras')),
)
