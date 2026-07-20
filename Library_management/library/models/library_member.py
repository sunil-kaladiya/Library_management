from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char("Name", required=True)
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    membership_number = fields.Char("Membership Number",required=True)
    active_rent_count = fields.Integer("Active Rent Count",compute="_compute_active_rent_count", store=True)

    rent_ids = fields.One2many('library.rent','member_id',"Rent Records")

    @api.depends('rent_ids.state')
    def _compute_active_rent_count(self):
        for partner in self:
            partner.active_rent_count = len(partner.rent_ids.filtered(
                lambda r: r.state in ['rented', 'overdue']
            ))

    @api.constrains('active_rent_count')
    def _check_active_rent_limit(self):
        for partner in self:
            if partner.active_rent_count > 3:
                raise ValidationError(
                    f"Member '{partner.name}' cannot have more than 3 active rents at once! "
                    f"Currently active rents: {partner.active_rent_count}"
                )

