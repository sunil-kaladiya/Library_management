from odoo import models, fields, api


class LibraryBulkReturnWizard(models.TransientModel):
    _name = 'library.bulk.return.wizard'
    _description = 'Library Bulk Return Wizard'

    return_date = fields.Date("Return Date", default=fields.Date.context_today, required=True)

    def action_bulk_return(self):

        active_ids = self.env.context.get('active_ids', [])
        rents = self.env['library.rent'].browse(active_ids)

        rents.write({
            'state': 'returned',
            'return_date': self.return_date,
        })
        return {'type': 'ir.actions.act_window_close'}