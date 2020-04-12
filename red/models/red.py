# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class red(models.Model): 
    _name = 'ej.red' 
    nombre = fields.Char(string='nombre', required=True) 
 
