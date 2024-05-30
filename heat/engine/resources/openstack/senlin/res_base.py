#    Copyright 2015 IBM Corp.
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

from heat.common.i18n import _
from heat.engine.resources.openstack.heat import none_resource
from heat.engine import support


class BaseSenlinResource(none_resource.NoneResource):
    """A base class for Senlin resources."""

    support_status = support.SupportStatus(
        version='23.0.0',
        status=support.HIDDEN,
        message=_('Senlin project was retired'),
        previous_status=support.SupportStatus(
            version='22.0.0',
            status=support.DEPRECATED,
            message=_('Senlin project was marked inactive'),
            previous_status=support.SupportStatus(
                version='6.0.0',
                )))
