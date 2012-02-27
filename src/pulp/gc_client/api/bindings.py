# -*- coding: utf-8 -*-
#
# Copyright © 2012 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pulp.gc_client.api.repository import *


class Bindings(object):
    def __init__(self, pulp_connection):
        self.repo_api = RepositoryAPI(pulp_connection)
        self.repo_importer_api = RepositoryImporterAPI(pulp_connection)
        self.repo_distributor_api = RepositoryDistributorAPI(pulp_connection)
        self.repo_history_api = RepositoryHistoryAPI(pulp_connection)
        self.repo_actions_api = RepositoryActionsAPI(pulp_connection)
        self.repo_unit_search_api = RepositoryUnitSearchAPI(pulp_connection)

        