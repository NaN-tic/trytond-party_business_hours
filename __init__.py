# This file is part party_business_hours module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import party

def register():
    Pool.register(
        party.Party,
        module='party_business_hours', type_='model')
