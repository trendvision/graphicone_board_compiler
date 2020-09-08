from sqlalchemy.orm import Session
from sqlalchemy import and_, case, literal, or_

import graphicone_models as models


def get_user_status(db: Session, current_username: str, requested_username: str):

    true = literal(True)
    false = literal(False)
    null = literal(None)

    unblock = db.query(true).filter(and_(
        models.BlockedUser.id_blocked_user == requested_username,
        models.BlockedUser.id_blocking_user == current_username
    )).label('Unblock')

    blocked = db.query(true).filter(and_(
        models.BlockedUser.id_blocked_user == current_username,
        models.BlockedUser.id_blocking_user == requested_username
    )).label('Blocked')

    accept_status = db.query(models.Follower.accept_status).filter(and_(
        models.Follower.follower == current_username,
        models.Follower.following == requested_username
    )).label('accept_status')

    r = db.query(case(
        [
            (blocked == true, 'Blocked'),
            (unblock == true, 'Unblock'),
            (accept_status == true, 'Unfollow'),
            (or_(accept_status == false, accept_status == null), 'Request send')
        ], else_='Follow'
    ).label('status')).first()

    return r[0]
