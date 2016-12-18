# -*- coding: utf-8 -*-
from openerp import models, fields, _


class StockMove(models.Model):

    _inherit = 'stock.move'

    _order = 'sequence, date_expected desc, id'

    sequence = fields.Integer('Sequence', default=10)
    package_number = fields.Char('Package number')
