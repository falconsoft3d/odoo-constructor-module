#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

print("#################################################################")
print("# Simple es una aplicacion para generar Modulo para Odoo ERP    #")
print("# www.falconsolutions.cl                                        #")
print("# Autor: Marlon Falcon Herandez                                 #")
print("# mail: mfalconsoft@gmal.com   ......                           #")
print("#################################################################")

# Entramos el nombre del módulo
name = raw_input("Entre el Nombre del Modulo:")
cant_campos = int(raw_input("Cantidad de Campos:"))
print("")
print("###############  Campos  ##############################")
print("")
print("")
# Creamos la carpeta del módulo
os.makedirs(name)
os.makedirs(name+"/views")
os.makedirs(name+"/models")
os.makedirs(name+"/security")

# Creamos los ficheros en la raiz
# Creamos el __init__.py
file = open(name + '/__init__.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('from . import models \n')
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
file.write('    \'version\': \'13.0.0.1.0\',\n')
file.write('    \'author\': "Marlon Falcón Herández",\n')
file.write('    \'maintainer\': \'Ynext\',\n')
file.write('    \'website\': \'http://www.ynext.cl\',\n')
file.write('    \'license\': \'AGPL-3\',\n')
file.write('    \'category\': \'account.payment\',\n')
file.write('    \'summary\': \'Ejemplo de un módulo by Ynext.\',\n')
file.write('    \'depends\': [\'base\',\'stock\'],\n')
file.write('    \'description\': """\n')
file.write('Modulo basado en Ynext\n')
file.write('===================================================== \n')
file.write('Éste módulo permite selecionar \n')
file.write('""",\n')
file.write('    \'demo\': [],\n')
file.write('    \'test\': [],\n')
file.write('    \'data\': [\'views/'+ name + '_view.xml\', \'security/ir.model.access.csv\'],\n')
file.write('    \'installable\': True,\n')
file.write('    \'auto_install\': False,\n')
file.write('}\n')
file.close()

# Creamos el Modelo
file = open(name + '/models/__init__.py','w')
file.write('# -*- coding: utf-8 -*- \n')
file.write('from . import '+name+' \n')
file.close()

# Creamos el Modelo
file = open(name + '/models/'+name+'.py','w')
file_security = open(name + '/security/ir.model.access.csv','w')
file_security.write('id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n')
file_security.write('access_'+name+',access.'+name+',model_ej_'+name+',,1,1,1,1')
file.write('# -*- coding: utf-8 -*- \n')
file.write('# Part of Odoo. See LICENSE file for full copyright and licensing details. \n')
file.write('from odoo import api, fields, models \n')
file.write('from datetime import datetime \n')
file.write('\n')
file.write('class '+name+'(models.Model): \n')
file.write('    _name = \'ej.'+name+'\' \n')
arreglo = []
for num in range(1,cant_campos+1):
    fname = raw_input("Nombre del Campo:")
    print("Char,Text,Boolean,Datetime,Integer")
    ftipo = raw_input("Tipo de Campo:")
    print("-----------------------------------")
    print("")
    print("")
    file.write('    '+fname+' = fields.'+ftipo+'(string=\''+fname+'\', required=True) \n')
    file.write(' \n')
    arreglo.append(fname)
file.close()
file_security.close()



# Creamos el _views.xml
file = open(name + '/views/'+ name + '_view.xml','w')
file.write('<?xml version="1.0" encoding="UTF-8"?> \n')
file.write('<odoo> \n')
file.write('<!-- Comentario en la Views --> \n')
file.write('     <record id="view_ej_' + name + '_form" model="ir.ui.view"> \n')
file.write('        <field name="name">ej.' + name + '.form</field> \n')
file.write('        <field name="model">ej.' + name + '</field> \n')
file.write('        <field name="arch" type="xml"> \n')
file.write('            <form string="Listado de '+name.capitalize()+'"> \n')
file.write('                <group> \n')
for fname in arreglo:
    file.write('                    <field name="'+fname+'"/> \n')
file.write('                </group> \n')
file.write('            </form> \n')
file.write('        </field> \n')
file.write('    </record> \n')

file.write('     <record id="view_tree_' + name +'" model="ir.ui.view"> \n')
file.write('        <field name="name">ej.' + name + '.tree</field> \n')
file.write('        <field name="model">ej.' + name + '</field> \n')
file.write('        <field name="arch" type="xml"> \n')
file.write('           <tree> \n')
for fname in arreglo:
    file.write('                    <field name="'+fname+'"/> \n')
file.write('           </tree> \n')
file.write('        </field> \n')
file.write('    </record> \n')

# Colocamos la acción
file.write('    <record model="ir.actions.act_window" id="act_ej_' + name + '"> \n')
file.write('        <field name="name">' + name + '</field> \n')
file.write('        <field name="res_model">ej.' + name + '</field> \n')
file.write('        <field name="view_mode">tree,form</field> \n')
file.write('        <field name="view_id"  ref="view_tree_'+name+'" /> \n')
file.write('    </record> \n')

# Colocamos el Menú
file.write('<!--  Declaramos los menu --> \n')
file.write('<menuitem id="ej_' + name + '_menu" name="' + name.capitalize() + '" web_icon="stock,static/description/icon.png" sequence="10"/> \n')
file.write('<menuitem id="submenu_ej_' + name + '_menu" name="'+ name.capitalize() +'" sequence="10" parent="ej_' + name + '_menu"/> \n')
file.write('<menuitem id="submenu_ej_' + name + '_action" name="'+ name.capitalize() + '" sequence="10" parent="submenu_ej_' + name + '_menu" action="act_ej_' + name + '"/> \n')

file.write('</odoo> \n')
file.close()

print("Se a creado el Modulo:" + name)





