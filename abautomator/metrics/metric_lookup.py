from abautomator.metrics.general import user_sessions, incident_views, incident_share_completes, friend_invites
from abautomator.metrics.protect import trial_starts, protect_cancellations
from abautomator.metrics.activation import (
    granted_location, entered_phone, granted_notifs, signup_complete, granted_contacts,
    viewed_shs,
)


METRIC_LOOKUP = {
    # general
    "friend_invites": friend_invites.FriendInvitesMetric(),
    "incident_share_completes": incident_share_completes.IncidentShareCompletesMetric(),
    "incident_views": incident_views.IncidentViewsMetric(),
    "all_sessions": user_sessions.AllSessionsMetric(),
    "organic_sessions": user_sessions.OrganicSessionsMetric(),
    "push_driven_sessions": user_sessions.PushDrivenSessionsMetric(),

    # protect
    "protect_cancellations" : protect_cancellations.ProtectCancellationsMetric(),
    "trial_starts": trial_starts.TrialStartsMetric(),

    # activation
    "granted_location": granted_location.GrantedLocationMetric(),
    "entered_phone": entered_phone.EnteredPhoneMetric(),
    "granted_notifs": granted_notifs.GrantedNotifsMetric(),
    "signup_complete": signup_complete.SignupCompleteMetric(),
    "granted_contacts": granted_contacts.GrantedContactsMetric(),
    "viewed_SHS": viewed_shs.ViewedShsMetric(),

}
