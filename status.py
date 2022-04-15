from odoo import api, fields, models

class status(models.Model):
	_name='status.info'
	_rec_name='name'
	_description="resume status"

	name=fields.Many2one('applier.info','name',required=True)
	state = fields.Selection([('received', 'Received'), ('viewed', 'Viewed'), 
		('selected', 'Selected'), ('rejected', 'Rejected')],default='viewed',string='status')



