from odoo import models, fields, api

class AssignTagWizard(models.TransientModel):
    _name = 'assign.tag.wizard'
    _description = 'Wizard para asignar etiquetas a productos'

    product_ids = fields.Many2many('product.template', string="Productos")
    tag_name = fields.Char(string="Etiqueta", required=True)

    def assign_tag(self):
        tag = self.env['product.tag'].search([('name', '=', self.tag_name)], limit=1)
        if not tag:
            tag = self.env['product.tag'].create({'name': self.tag_name})
        
        for product in self.product_ids:
            product.product_tag_ids = [(4, tag.id)]
