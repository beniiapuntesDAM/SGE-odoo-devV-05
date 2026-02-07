from odoo import models, fields, api

class abj_floristeria_flor(models.Model):
    _name = 'abj_floristeria.flor'
    _description = 'Flor'
    _rec_name = 'nombre'   # ← Odoo usará este campo como nombre visible

    tipo = fields.Selection([
        ('rosa', 'Rosa'),
        ('tulipan', 'Tulipán'),
        ('margarita', 'Margarita'),
        ('otro', 'Otro')
    ], string='Tipo', required=True)

    color = fields.Char(string='Color')
    precio = fields.Float(string='Precio', required=True)

    nombre = fields.Char(
        string="Nombre",
        compute="_compute_nombre",
        store=True
    )

    @api.depends('tipo', 'color')
    def _compute_nombre(self):
        for f in self:
            tipo = dict(self._fields['tipo'].selection).get(f.tipo, '')
            f.nombre = f"{tipo} {f.color or ''}".strip()
