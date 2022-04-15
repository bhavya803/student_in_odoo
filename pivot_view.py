from odoo import api, fields, models

class pivot_view(models.Model):
	_name='pivot.view'
	_description='pivot_view'

	name=fields.Char('name')
	stage_id=fields.Integer('stage_id')