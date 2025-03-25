# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class Purchase(metaclass=PoolMeta):
    __name__ = 'purchase.purchase'
    business_hours = fields.Char('Business Hours')

    @fields.depends('party')
    def on_change_party(self):
        super().on_change_party()
        if self.party:
            self.business_hours = self.party.business_hours
