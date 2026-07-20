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
