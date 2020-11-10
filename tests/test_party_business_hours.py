# This file is part party_business_hours module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class PartyBusinessHoursTestCase(ModuleTestCase):
    'Test Party Business Hours module'
    module = 'party_business_hours'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            PartyBusinessHoursTestCase))
    return suite
