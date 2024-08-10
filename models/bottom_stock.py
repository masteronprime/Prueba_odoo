from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
           
class BotonSmart(models.Model):
    _inherit = "product.template"

    order_line_ids = fields.Many2many(
        'sale.order.line',
        string="Líneas de Orden de Venta",
        compute="_compute_order_lines"
    )
    count_orders = fields.Integer(string="Número de Órdenes", compute="_compute_orders")
    label_ids = fields.Many2many('product.label', string='Etiqueta producto')

    @api.depends('order_line_ids')
    def _compute_orders(self):
        for product in self:
            product.count_orders = len(product.order_line_ids)

    @api.depends('product_variant_ids')
    def _compute_order_lines(self):
        for product in self:
            order_lines = self.env['sale.order.line'].search([('product_id', 'in', product.product_variant_ids.ids)])
            product.order_line_ids = order_lines

    def action_view_orders(self):
        self.ensure_one()
        sale_orders = self.env['sale.order.line'].search([('product_id', 'in', self.product_variant_ids.ids)])
        action = self.env.ref('sale.action_orders').read()[0]
        action['domain'] = [('id', 'in', sale_orders.mapped('order_id').ids)]
        action['context'] = dict(self.env.context, default_product_id=self.id)
        return action   

    def action_print_report_product(self):
        return self.env.ref('prueba.action_report_product_details').report_action(self)