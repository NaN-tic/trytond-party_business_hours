# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'
    business_hours = fields.Char('Business Hours')

    @fields.depends('party', 'business_hours', 'shipment_address')
    def set_business_hours(self):
        if self.shipment_address and self.shipment_address.business_hours:
            self.business_hours = self.shipment_address.business_hours
        elif self.party and not self.business_hours:
            self.business_hours = self.party.business_hours

    @fields.depends(methods=['set_business_hours'])
    def on_change_party(self):
        super().on_change_party()
        self.set_business_hours()

    @fields.depends(methods=['set_business_hours'])
    def on_change_shipment_address(self):
        self.set_business_hours()
