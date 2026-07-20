from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta


class LibraryRent(models.Model):
    _name = 'library.rent'
    _description = 'Library Rent'


    book_id = fields.Many2one('library.book',"Book",required=True)
    member_id = fields.Many2one('library.member',"Member",required=True)
    rent_date = fields.Date("Rent Date",required=True,default=fields.Date.today,copy=False)
    due_date = fields.Date("Due Date",compute="_compute_due_date",store=True,readonly=True,copy=False)
    return_date = fields.Date("Return Date",copy=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('rented', 'Rented'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue')
    ],"Status", default='draft')

    user_id = fields.Many2one('res.users', 'User')

    @api.depends('rent_date')
    def _compute_due_date(self):

        for record in self:
            if record.rent_date:
                record.due_date = record.rent_date + timedelta(days=14)
            else:
                record.due_date = False

    def action_confirm_rent(self):

        for record in self:
            if record.state != 'draft':
                raise UserError("only conform draft records.")

            if record.book_id.available_copies <= 0:
                raise UserError(f"Sorry! Is book ({record.book_id.name}) not available(Out-Of-Stock)")

            record.book_id.available_copies -= 1
            record.state = 'rented'


    def action_return(self):

        for record in self:
            if record.state not in ['rented', 'overdue']:
                raise UserError("only Rented and Overdue Records Returned")

            if record.state != 'returned':
                record.state = 'returned'
                record.return_date = fields.Date.today()

                if record.book_id:
                    record.book_id.available_copies += 1


    @api.onchange('book_id')
    def _onchange_book_id(self):

        if self.book_id and self.book_id.available_copies <= 0:
            raise UserError(f"Sorry! Is book ({self.book_id.name}) not available(Out-Of-Stock), Please Select Other Book.")

    @api.model
    def _check_overdue_rents(self):
        today = fields.Date.today(self)
        overdue_records = self.search([
            ('state', '=', 'rented'),
            ('due_date', '<', today)
        ])
        if overdue_records:
            overdue_records.write({'state': 'overdue'})





















