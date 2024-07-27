from odoo import models,fields,api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Price')
    price_subtotal = fields.Float(string='Price Subtotal', compute='_compute_price_subtotal', store=True)

    @api.depends('quantity', 'price_unit', 'account_id')
    def _compute_price_subtotal(self):
        for rec in self:
            rec.price_subtotal = rec.quantity * rec.price_unit

