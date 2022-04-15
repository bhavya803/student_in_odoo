from odoo import api, fields, models

class graph_view(models.Model):
	_name='graph.view'
	_description='graph_view'

	name=fields.Char('name')
	salary=fields.Integer('salary')
