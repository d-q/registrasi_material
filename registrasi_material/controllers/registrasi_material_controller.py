from odoo import models, http, fields, api, _
from odoo.exceptions import UserError

from odoo.http import request, Response, route
import json

class RegistrasiMaterialController(http.Controller):

    @http.route('/material', type='json', auth='public', methods=['GET'])
    def get_material(self):
        material = request.env['registrasi.material'].sudo().search([])
        list_material = []
        for rec in material:
            vals = {
                'id': rec.id,
                'code': rec.code,
                'name': rec.name,
                'type': rec.type,
                'price': rec.price,
                'supplier': {
                    'id': rec.supplier.id,
                    'name': rec.supplier.name
                }
            }
            list_material.append(vals)
        data = {'success': True, 'response': list_material, 'message': 'Berhasil'}
        return data 

    @http.route('/material', type='json', auth='public', methods=['POST'])
    def post_create_material(self, **rec):
        type = ['fabric','jeans','cotton']
        if request.jsonrequest:
            if str(rec['type']) not in type:
                return {'success': False, 'message': 'Material Type tidak sesuai'}
            elif int(rec['price']) < 100:
                return {'success': False, 'message': 'Material Buy Price tidak boleh di bawah 100'}
            else:
                vals = {
                    'code': rec['code'],
                    'name': rec['name'],
                    'type': rec['type'],
                    'price': rec['price'],
                    'supplier': rec['supplier'],
                }
                material = request.env['registrasi.material'].sudo().create(vals)
                args = {'success': True, 'message': 'Berhasil', 'ID': material.id}
                return args

    @http.route('/material/<int:id>', type='json', auth='public',  methods=['GET'])
    def get_detail_material(self, id):
        material = request.env['registrasi.material'].sudo().search([('id','=',id)])
        list_material = []
        if material.id:
            for rec in material:
                vals = {
                    'id': rec.id,
                    'code': rec.code,
                    'name': rec.name,
                    'type': rec.type,
                    'price': rec.price,
                    'supplier': {
                        'id': rec.supplier.id,
                        'name': rec.supplier.name
                    }
                }
                list_material.append(vals)
            data = {'success': True, 'response': list_material, 'message': 'Berhasil'}
            return data
        else:
            data = {'success': False, 'message': 'Data tidak ditemukan'}
            return data

    @http.route('/material/<int:id>', type='json', auth='public', methods=['POST'])
    def post_write_material(self, id, **rec):
        type = ['fabric','jeans','cotton']
        if request.jsonrequest:
            if str(rec['type']) not in type:
                return {'success': False, 'message': 'Material Type tidak sesuai'}
            elif int(rec['price']) < 100:
                return {'success': False, 'message': 'Material Buy Price tidak boleh di bawah 100'}
            else:
                vals = {
                    'code': rec['code'],
                    'name': rec['name'],
                    'type': rec['type'],
                    'price': rec['price'],
                    'supplier': rec['supplier'],
                }
                material = request.env['registrasi.material'].sudo().search([('id','=',id)])
                if material.id:
                    material.sudo().write(vals)
                    data = {'success': True, 'message': 'Berhasil', 'ID': material.id}
                    return data
                else:
                    data = {'success': False, 'message': 'Data tidak ditemukan'}
                    return data

    @http.route('/unlink_material/<int:id>', type='json', auth='public', methods=['POST'])
    def unlink_product(self, id, **rec):
        if request.jsonrequest:
            material = http.request.env['registrasi.material'].sudo().search([('id','=',id)])
            if material.id:
                material.unlink()
                data = {'success': True, 'message': 'Data berhasil dihapus'}
                return data
            else:
                data = {'success': False, 'message': 'Data tidak ditemukan'}
                return data