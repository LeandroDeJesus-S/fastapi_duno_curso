from sqlalchemy import select

from fast_zero.models import User


def test_db_user(session):
    user = User(
        username='user123', password='pass123', email='email@email.com'
    )
    session.add(user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'user123'))

    assert user.username == 'user123'
