# -*- coding: utf-8 -*-
# from odoo import http


# class AcountMove(http.Controller):
#     @http.route('/acount_move/acount_move', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acount_move/acount_move/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('acount_move.listing', {
#             'root': '/acount_move/acount_move',
#             'objects': http.request.env['acount_move.acount_move'].search([]),
#         })

#     @http.route('/acount_move/acount_move/objects/<model("acount_move.acount_move"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acount_move.object', {
#             'object': obj
#         })
