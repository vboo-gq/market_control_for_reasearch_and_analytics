"""Database models"""

from sqlalchemy import Column, ForeignKey, Integer, String, \
    DateTime, BigInteger, SmallInteger, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Model for state"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Region(Base):
    """Model for region"""
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Player(Base):
    """Model for player"""
    __tablename__ = 'player'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    nation = Column(String)
    registration_date = Column(Date)


class MarketTrack(Base):
    """Model for market track"""
    __tablename__ = 'market_track'
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)


class PlayerMarketStat(Base):
    """Model for market stat"""
    __tablename__ = 'player_market_stat'
    id = Column(Integer, primary_key=True)
    item_type = Column(SmallInteger)
    price = Column(Integer)
    amount = Column(BigInteger)
    total_offers = Column(Integer)

    player_id = Column(Integer, ForeignKey('player.id'))
    player = relationship(
        'Player',
        backref=backref('player_market_stats', lazy='dynamic')
    )

    market_track_id = Column(Integer, ForeignKey('market_track.id'))
    market_track = relationship(
        'MarketTrack',
        backref=backref('player_market_stats', lazy='dynamic')
    )


class StateMarketStat(Base):
    """Model for market stat"""
    __tablename__ = 'state_market_stat'
    id = Column(Integer, primary_key=True)
    item_type = Column(SmallInteger)
    price = Column(Integer)
    amount = Column(BigInteger)

    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship(
        'State',
        backref=backref('state_market_stats', lazy='dynamic')
    )

    market_track_id = Column(Integer, ForeignKey('market_track.id'))
    market_track = relationship(
        'MarketTrack',
        backref=backref('state_market_stats', lazy='dynamic')
    )
