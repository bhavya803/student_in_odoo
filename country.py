from odoo import api, fields, models

class Country(models.Model):
	_name='country.info'
	_description='country_name'
	_rec_name='country_id'
	_table ='none'

	country_id = fields.Many2one('res.country', string='Country', help='Select Country')    
	state_id=fields.Many2one('res.country.state','country_id',domain="[('country_id', '=', country_id)]")
	