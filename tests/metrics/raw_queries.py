""" Raw queries for doing count comparisons w/ sqlalchemy queries """

RAW_QUERIES = {
    "friend_invites": """SELECT
        echelon_user_id
    FROM
        {dataset}.fct_share_completes_installs
    WHERE
        event_date >= '{start_dt}'
        and general_type = 'Invite'
    GROUP BY 1""",

    "incident_share_completes": """SELECT
        echelon_user_id
    FROM
        {dataset}.fct_share_completes_installs
    WHERE
        event_date >= '{start_dt}'
        and general_type = 'Incident Shares'
    GROUP BY 1""",

    "incident_share_attempts": """SELECT
        echelon_user_id
    FROM
        {dataset}.fct_share_attempts
    WHERE
        event_date >= '{start_dt}'
        AND (
          general_type = 'Screenshot' OR general_type LIKE '%Shared Button%'
        )
    GROUP BY 1""",

    "all_sessions": """SELECT
      echelon_user_id
    FROM
      {dataset}.fct_user_sessions
    WHERE
      event_date >= '{start_dt}'
    GROUP BY 1""",

    "organic_sessions": """SELECT
      echelon_user_id
    FROM
      {dataset}.fct_user_sessions
    WHERE
      event_date >= '{start_dt}'
      and not is_push_driven
    GROUP BY 1""",

    "push_driven_sessions": """SELECT
      echelon_user_id
    FROM
      {dataset}.fct_user_sessions
    WHERE
      event_date >= '{start_dt}'
      and is_push_driven
    GROUP BY 1""",

    "incident_views": """SELECT
      echelon_user_id
    FROM
      {dataset}.fct_incident_views
    WHERE
      event_date >= '{start_dt}'
    GROUP BY 1""",

    "trial_starts": """SELECT
      echelon_user_id
    FROM
      {dataset}.dim_purchased_subscriptions
    WHERE
      event_date >= '{start_dt}'
      and transaction_id = original_transaction_id
    GROUP BY 1""",

    "protect_payment_successful": """SELECT
      echelon_user_id
    FROM
      {dataset}.segment_protect_landing_page_payment_successful
    WHERE
      event_date >= '{start_dt}'
    GROUP BY 1""",

    "protect_cancellations": """SELECT
      echelon_user_id,
    FROM
      {dataset}.dim_purchased_subscriptions dps
    WHERE
      DATE(COALESCE(dps.last_cancel_datetime, dps.last_renewal_failure_datetime)) >= '{start_dt}'
    GROUP BY 1""",

  "granted_location": """SELECT
      echelon_user_id,
    FROM
      {dataset}.dim_user_onboardings dps
    WHERE
      event_date >= '{start_dt}'
      AND completed_location_prompt_permission in ('Always', 'While Use the App', 'While Using')
    GROUP BY 1""",
  
  "entered_phone": """SELECT
      echelon_user_id,
    FROM
      {dataset}.dim_user_onboardings dps
    WHERE
      event_date >= '{start_dt}'
      AND entered_phone_number IS NOT NULL
    GROUP BY 1""",

  "granted_notifs": """SELECT
      echelon_user_id,
    FROM
      {dataset}.dim_user_onboardings dps
    WHERE
      event_date >= '{start_dt}'
      AND completed_notification_prompt_permission = 'Granted'
    GROUP BY 1""",

  "signup_complete": """SELECT
      echelon_user_id,
    FROM
      {dataset}.dim_user_onboardings dps
    WHERE
      event_date >= '{start_dt}'
      AND signup_completed IS NOT NULL
    GROUP BY 1""",

  "granted_contacts": """SELECT
      echelon_user_id,
    FROM
      {dataset}.dim_user_onboardings dps
    WHERE
      event_date >= '{start_dt}'
      AND completed_contacts_preprompt_permission = 'granted'
    GROUP BY 1""",

  "viewed_SHS": """SELECT
      echelon_user_id,
    FROM
      {dataset}.dim_user_onboardings dps
    WHERE
      event_date >= '{start_dt}'
      AND viewed_shs IS NOT NULL
    GROUP BY 1""",

  "feed_views": """SELECT
      echelon_user_id,
    FROM
      {dataset}.segment_viewed_feed_item
    WHERE
      event_date >= '{start_dt}'
      AND section in ('mostImportant', 'forYou')
    GROUP BY 1""",

  "feed_taps": """SELECT
      echelon_user_id,
    FROM
      {dataset}.segment_tapped_feed_item
    WHERE
      event_date >= '{start_dt}'
      AND section in ('mostImportant', 'forYou')
    GROUP BY 1""",

  "feed_shares": """SELECT
      echelon_user_id,
    FROM
      {dataset}.segment_shared_feed_item
    WHERE
      event_date >= '{start_dt}'
      AND section in ('mostImportant', 'forYou')
    GROUP BY 1""",

  "all_feed_shares": """SELECT
      echelon_user_id,
    FROM
      {dataset}.fct_homescreen_shares
    WHERE
      tap_date >= '{start_dt}'
      AND section in ('mostImportant', 'forYou')
    GROUP BY 1""",

  "direct_feed_shares": """SELECT
      echelon_user_id,
    FROM
      {dataset}.fct_homescreen_shares
    WHERE
      tap_date >= '{start_dt}'
      AND section in ('mostImportant', 'forYou')
      AND share_source = 'Direct From Feed'
    GROUP BY 1""",

  "indirect_feed_shares": """SELECT
      echelon_user_id,
    FROM
      {dataset}.fct_homescreen_shares
    WHERE
      tap_date >= '{start_dt}'
      AND section in ('mostImportant', 'forYou')
      AND share_source != 'Direct From Feed'
    GROUP BY 1""",

  "chats": """SELECT
      echelon_user_id,
    FROM
      {dataset}.dim_incident_chats
    WHERE
      event_date >= '{start_dt}'
      AND is_deleted = False
    GROUP BY 1""",

  "signup_activation": """SELECT
      a.echelon_user_id,
    FROM
      {dataset}.fct_user_signups a
    LEFT JOIN
      {dataset}.fct_incident_views b
    ON
      a.echelon_user_id = b.echelon_user_id
      AND DATETIME_DIFF(b.event_datetime, a.join_datetime, MINUTE) BETWEEN 0 AND 1440
    WHERE
      join_date >= '{start_dt}'
    GROUP BY 1
    """,
}