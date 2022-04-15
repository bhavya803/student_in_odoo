from odoo import api, fields, models,_
import re


class apply_info_wizard(models.TransientModel):
    _name = 'apply.info.wizard'
    _description = 'apply wizard'
    fname=fields.Char(string='first name')
    lname=fields.Char(string="last name")
    mail_id=fields.Char(string="email")
    

    # @api.model
    # def create(self, vals):
    #     print('success')
    #     if not vals.get('note'):
    #         vals['note']:'name'    
    #     res= super(apply_info_wizard,self).create(vals)
    #     return res
    
    # def create_otherModule_data(self):
    #     line_dic = {
    #         'default_name': name,
    #         'complete_name': self.complete_name,
    #         'code': code,
    #         'active': True, 
    #     }
    #     self.env['hr.view_hr_job_tree'].create(line_dic)

    def action_create_info(self):
        print('applied for position')
        vals = {
            'fname':self.fname,
            'lname':self.lname,
            'mail_id':self.mail_id,
        } 
        create_rec = self.env['student.basic'].create(vals)
        # return {
        #     "name":_("Create"),
        #     "type":'ir_actions.act_window',
        #     'view_mode':'form',
        #     'res_model':'student.basic',
        #     'res_id':create_rec.id,
        #     'target':'new',
        # }

        # message = {
        # 'type': 'ir.actions.client',
        # 'tag': 'display_notification',
        # 'params': {
        # 'title': ('message'),
        # 'message': 'thanks for applying',
        # 'sticky':False,
        #     }
        # }
        # return {'type': 'ir.actions.act_window_close'}
        # employee_data = {
        #         'default_name':apply_info_wizard.name,
                # 'default_mobile_no':apply_info_wizard.mobile_no,
                # 'default_gmail':apply_info_wizard.gmail,
                # 'default_expected_salary':apply_info_wizard.expected_salary,
                # 'default_previous_salary':apply_info_wizard.previous_salary,
                # 'default_previous_job_position':apply_info_wizard.previous_job_position,
                # 'default_previous_company':apply_info_wizard.previous_company
        # }
        # res = self.env['ir.actions.act_window']._for_xml_id('hr.view_hr_job_tree')
        # res['context']=employee_data
        # return res
        # vals['favorite_user_ids'] = vals.get('favorite_user_ids', []) + [(4, self.env.uid)]
        # new_job = super(Job, self).create(vals)
        # utm_linkedin = self.env.ref("utm.utm_source_linkedin", raise_if_not_found=False)
        # if utm_linkedin:
        #     source_vals = {
        #         'source_id': utm_linkedin.id,
        #         'job_id': new_job.id,
        #     }
        #     self.env['hr.recruitment.source'].create(source_vals)
        # return new_job
        # return self.env.ref('hr_recruitment.mt_applicant_new')
    