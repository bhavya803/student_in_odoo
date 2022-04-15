from odoo import api, fields, models
from datetime import datetime

class calander_view(models.Model):
	_name='calander.view'
	_description='claander_view'

	name=fields.Char('name')
	date_deadline=fields.Date('date')