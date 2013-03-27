# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs
import logging

from openstack_dashboard import api


LOG = logging.getLogger(__name__)

class OverviewTab(tabs.Tab):
    name = _("Service")
    slug = "_service"
    template_name = "services.html"
    
    def get_context_data(self, request):
        return {"service_id": self.tab_group.kwargs['service_id']}

class LogsTab(tabs.Tab):
    name = _("Logs")
    slug = "_logs"
    template_name = "services.html"
    
    def get_context_data(self, request):
        return {"service_id": self.tab_group.kwargs['service_id']}


class WinServicesTabs(tabs.TabGroup):
    slug = "services_details"
    tabs = (OverviewTab,)
    sticky = True
