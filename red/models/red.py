# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class red(models.Model): 
    _name = 'ej.red' 
    name = fields.Char(string='name', required=True) 
 
    Edad = fields.Integer(string='Edad', required=True) 
 
