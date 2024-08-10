from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class ProductLabel(models.Model):

    _name = "product.label"

    name =  fields.Char(String="nombre de la etiqueta")
    description = fields.Text(string="Descripción")

