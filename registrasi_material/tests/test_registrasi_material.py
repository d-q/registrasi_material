from odoo import models, http, fields, api, _
from odoo.exceptions import UserError

from odoo.tests.common import TransactionCase

class TestRegistrasiMaterial(TransactionCase):
    def setUp(self):
        super(TestRegistrasiMaterial, self).setUp()

    def test_data(self):
        list_type = ['fabric','jeans','cotton']
        partner = self.env['res.partner'].search([])
        material = self.env['registrasi.material']
        existing = material.create({
            'code': 'kmerah',
            'name': 'kain warna merah',
            'type': 'cotton',
            'price': 101,
            'supplier': 14,
        })
        self.assertIn(existing.type, list_type, 'type ada didalam list_type')
        # self.assertNotIn(existing.type, list_type, 'type tidak ada didalam list_type')
        self.assertTrue(existing.price > 100, 'Test price sesuai')
        self.assertFalse(existing.price < 100, 'Test Material Buy Price tidak boleh di bawah 100')
        self.assertIn(existing.supplier.id, partner.ids, 'partner ada didalam partner.ids')
        # self.assertNotIn(existing.supplier.id, partner.ids, 'partner tidak ada didalam partner.ids')