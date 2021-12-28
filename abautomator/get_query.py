from datetime import date

from sqlalchemy import case
from sqlalchemy.engine import *
from sqlalchemy.schema import Table, MetaData
from sqlalchemy.sql import func, select
from sqlalchemy.sql.selectable import Selectable

from abautomator.collector import Collector
from abautomator.metric import Metric

def get_users_query(engine: Engine, coll: Collector):
  table = Table(f'echelon.{coll.event}', MetaData(bind=engine), autoload=True)

  result = select(
      table.c.echelon_user_id,
      getattr(table.c, coll.event_prop).label("exp_cond"),
  ).where(
      getattr(table.c, coll.event_prop).in_(coll.conds)
  ).group_by(
      table.c.echelon_user_id, 
      getattr(table.c, coll.event_prop),
  )
  # Ommitting first_event_datetime for now

  result = add_time_frame(result, table, coll.start_dt, coll.end_dt)
  return result

def get_metric_query(engine: Engine, coll: Collector, metric: Metric):
  table = Table(f'echelon.{metric.table_name}', MetaData(bind=engine), autoload=True)

  result = select(
      table.c.echelon_user_id,
      func.count(getattr(table.c, metric.table_col)).label(metric.n_label),
      case(
        (
          func.count(getattr(table.c, metric.table_col)) > 0, 1
        ),
        else_=0
      ).label(metric.pct_label),
  ).group_by(
      table.c.echelon_user_id,
  )
  result = add_time_frame(result, table, coll.start_dt, coll.end_dt)

  return result

def add_time_frame(query: Selectable, table: Table, start_dt: date = None, end_dt: date = None):
  if start_dt:
    query = query.where(
      table.c.event_date >= start_dt
    )
  if end_dt:
    query = query.where(
      table.c.event_date <= end_dt
    )
  return query