#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

print "#################################################################"
print "# Herencia es una aplicacion para generar Modulo para Odoo      #"
print "# www.falconsolutions.cl                                        #"
print "# Autor: Marlon Falcon Herandez                                 #"
print "# mail: mfalcon@falconsolutions.cl                              #"
print "#################################################################"

# Entramos el nombre del módulo
name = raw_input("Entre el Nombre del Modulo a Heredar:")
module = name
name = name.replace(".", '_')
name = "herencia_" + name
form = raw_input("Dame el ID Formulario:")
pos_campos = raw_input("Dame el nombre Campo de referencia:")
cant_campos = int(raw_input("Cantidad de Campos a Insertar:"))
print ""
print "###############  Campos  ##############################"
print ""
print ""
# Creamos la carpeta del módulo
os.makedirs(name)
os.makedirs(name+"/views")
os.makedirs(name+"/models")

# Creamos los ficheros en la raiz
# Creamos el __init__.py
file = open(name + '/__init__.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('import models \n')
file.close()


# Creamos el __manifest__.py
file = open(name + '/__manifest__.py','w')
file.write('# -*- coding: utf-8 -*-\n')
file.write('##############################################################################\n')
file.write('#\n')
file.write('#    OpenERP, Open Source Management Solution\n')
file.write('#    This module copyright (C) 2017 Marlon Falcón Hernandez\n')
file.write('#    (<http://www.falconsolutions.cl>).\n')
file.write('#\n')
file.write('#    This program is free software: you can redistribute it and/or modify\n')
file.write('#    it under the terms of the GNU Affero General Public License as\n')
file.write('#    published by the Free Software Foundation, either version 3 of the\n')
file.write('#    License, or (at your option) any later version.\n')
file.write('#\n')
file.write('#    This program is distributed in the hope that it will be useful,\n')
file.write('#    but WITHOUT ANY WARRANTY; without even the implied warranty of\n')
file.write('#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n')
file.write('#    GNU Affero General Public License for more details.\n')
file.write('#\n')
file.write('#    You should have received a copy of the GNU Affero General Public License\n')
file.write('#    along with this program.  If not, see <http://www.gnu.org/licenses/>.\n')
file.write('#\n')
file.write('##############################################################################\n')
file.write('{\n')
file.write('    \'name\': \'' + name + ' MFH\',\n')
file.write('    \'version\': \'10.0.0.1.0\',\n')
file.write('    \'author\': "Falcón Solutions, Marlon Falcón...",\n')
file.write('    \'maintainer\': \'Falcon Solutions\',\n')
file.write('    \'website\': \'http://www.falconsolutions.cl\',\n')
file.write('    \'license\': \'AGPL-3\',\n')
file.write('    \'category\': \'account.payment\',\n')
file.write('    \'summary\': \'Ejemplo de un módulo by FalconSolutions.\',\n')
file.write('    \'depends\': [\'account\',\'account_accountant\'],\n')
file.write('    \'description\': """\n')
file.write('Modulo basado en FalconSolutions\n')
file.write('===================================================== \n')
file.write('Éste módulo permite selecionar \n')
file.write('""",\n')
file.write('    \'demo\': [],\n')
file.write('    \'test\': [],\n')
file.write('    \'data\': [\'views/'+ name + '_view.xml\',],\n')
file.write('    \'installable\': True,\n')
file.write('    \'auto_install\': False,\n')
file.write('}\n')
file.close()

# Creamos el Modelo
file = open(name + '/models/__init__.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('import '+name+' \n')
file.close()

# Creamos el Modelo
file = open(name + '/models/'+name+'.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('# Part of Odoo. See LICENSE file for full copyright and licensing details. \n')
file.write('from odoo import api, fields, models \n')
file.write('from datetime import datetime \n')
file.write('\n')
file.write('class '+name+'(models.Model): \n')
file.write('    _inherit = "' + module + '" \n')
arreglo = []
for num in range(1,cant_campos+1):
    fname = raw_input("Nombre del Campo:")
    print "Char,Text,Boolean,Datetime,Integer"
    ftipo = raw_input("Tipo de Campo:")
    print "-----------------------------------"
    print ""
    print ""
    file.write('    '+fname+' = fields.'+ftipo+'(string=\''+fname+'\', required=True) \n')
    file.write(' \n')
    arreglo.append(fname)
file.close()


# Creamos el _views.xml
file = open(name + '/views/'+ name + '_view.xml','w')
file.write('<?xml version="1.0" encoding="UTF-8"?> \n')
file.write('<odoo> \n')
file.write('<!-- Comentario en la Views --> \n')
file.write('     <record id="view_ej_' + name + '_form" model="ir.ui.view"> \n')
file.write('        <field name="name">ej.' + name + '.form</field> \n')
file.write('        <field name="model">' + module + '</field> \n')
file.write('        <field name="inherit_id" ref="' + form + '"/> \n')
file.write('        <field name="arch" type="xml"> \n')
file.write('        <field name="' + pos_campos + '" position="after" >\n')
for fname in arreglo:
    file.write('          <field name="'+fname+'"/> \n')
file.write('        </field> \n')
file.write('        </field> \n')
file.write('    </record> \n')

file.write('</odoo> \n')
file.close()

print "Se a creado el Modulo:" + name





