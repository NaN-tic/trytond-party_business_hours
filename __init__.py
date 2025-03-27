# This file is part party_business_hours module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import party, sale, purchase

def register():
    Pool.register(
        party.Party,
        party.Address,
        module='party_business_hours', type_='model')
    Pool.register(
        sale.Sale,
        depends=['sale'],
        module='party_business_hours', type_='model')
    Pool.register(
        purchase.Purchase,
        depends=['purchase'],
        module='party_business_hours', type_='model')
