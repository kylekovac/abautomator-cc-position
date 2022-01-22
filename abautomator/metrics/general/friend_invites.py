from dataclasses import dataclass
from sqlalchemy.schema import Table
from sqlalchemy.sql.selectable import Selectable

from abautomator.metrics import BaseMetric
from abautomator import utils

@dataclass
class FriendInvitesMetric(BaseMetric):
    name: str = "friend_invites"
    table_name: str = "fct_share_completes_installs"
    table_col: str = "id"

    def add_where_clause(self, query: Selectable, table: Table, dt_range: utils.DateRange):
        query = utils.add_time_frame(query, table, dt_range)
        return query.where(
            table.c.general_type == "Invite"
        )
