from sqlalchemy.orm import Session
from sqlalchemy import and_, func

import graphicone_models as models


def get_board_by_id(db: Session, board_id: str):

    graphs_count = db.query(
        func.count(models.Graph.id)
    ).filter(and_(
        models.Graph.location == 'board',
        models.Graph.location_id == models.Board.id)
    ).label('graphs_count')

    records = db.query(models.Board, models.Account, graphs_count).join(models.Account).filter(
        models.Account.username == models.Board.owner
    ).filter(models.Board.id == board_id).all()

    if not records:
        return dict()

    for board, account, graphs_count in records:

        board_item = dict(
            id=board.id,
            name=board.name,
            members=board.members,
            preview_img_url=board.preview_img_url,
            privacy_type=board.privacy,
            status=board.privacy,
            graphs_count=graphs_count)

        board_item['author'] = {
            'username': account.username,
            'name': account.name,
            'email': account.email,
            'image_url': account.image_url
        }

        board = board_item

        return board
