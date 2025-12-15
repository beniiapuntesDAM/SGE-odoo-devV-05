# -*- coding: utf-8 -*-
# from odoo import http


# class AbjFloristeria(http.Controller):
#     @http.route('/abj_floristeria/abj_floristeria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abj_floristeria/abj_floristeria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abj_floristeria.listing', {
#             'root': '/abj_floristeria/abj_floristeria',
#             'objects': http.request.env['abj_floristeria.abj_floristeria'].search([]),
#         })

#     @http.route('/abj_floristeria/abj_floristeria/objects/<model("abj_floristeria.abj_floristeria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abj_floristeria.object', {
#             'object': obj
#         })

