# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    business_hours = fields.Char('Business Hours')


class Address(metaclass=PoolMeta):
    __name__ = 'party.address'
    business_hours = fields.Char('Business Hours')
