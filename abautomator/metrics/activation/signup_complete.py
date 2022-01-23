from dataclasses import dataclass
from sqlalchemy.schema import Table
from sqlalchemy.sql.selectable import Selectable

from abautomator.metrics import BaseMetric
from abautomator import utils

@dataclass
class SignupCompleteMetric(BaseMetric):
    name: str = "signup_complete"
    table_name: str = "dim_user_onboardings"
    table_col: str = "echelon_user_id"

    def add_where_clause(self, query: Selectable, table: Table, dt_range: utils.DateRange):
        query = utils.add_time_frame(query, table, dt_range)
        return query.where(
            table.c.signup_completed.isnot(None)
        )
