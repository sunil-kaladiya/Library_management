from odoo import models, fields,api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    image = fields.Image('Img')
    author = fields.Many2one("res.partner",'Author',)
    isbn = fields.Char('ISBN')
    total = fields.Integer('Total Copies')
    available_copies = fields.Integer('Available Copies')
    state = fields.Selection([
        ('available', 'Available'),
        ('out_of_stock', 'Out Of Stock'),
        ],compute="_compute_state", default='available')


    @api.depends('available_copies')
    def _compute_state(self):
        for book in self:
            if book.available_copies > 0:
                book.state = 'available'
            else:
                book.state = 'out_of_stock'




















































    # # branch_id  = fields.Many2one('library.branch', string='Branch')
    # company_id = fields.Many2one('res.company', string='Company',
    #                               default=lambda self: self.env.company)
    # cost_price = fields.Float(string='Cost Price')  # Managers only
    # state      = fields.Selection([
    #     ('available', 'Available'),
    #     ('borrowed', 'Borrowed'),
    #     ('damaged', 'Damaged'),
    # ], default='available')
    #
    #
    # def read(self, fields_list=None, load='_classic_read'):
    #     result = super().read(fields_list, load)
    #
    #     if not self.env.user.has_group('library_management.group_library_manager'):
    #         for record in result:
    #             if 'cost_price' in record:
    #                 record['cost_price'] = 0.0
    #     return result
    #
    # @api.model
    # def fields_get(self, allfields=None, attributes=None):
    #     fields = super().fields_get(allfields, attributes)
    #     if not self.env.user.has_group('library_management.group_library_manager'):
    #         fields.pop('cost_price', None)
    #     return fields
    #


