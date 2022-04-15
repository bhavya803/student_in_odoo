# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /home/bhavya/python/v15/third_party_handler(models.Model):
#     _name = '/home/bhavya/python/v15/third_party_handler./home/bhavya/python/v15/third_party_handler'
#     _description = '/home/bhavya/python/v15/third_party_handler./home/bhavya/python/v15/third_party_handler'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
