# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Marlon Falcón Hernandez
#    (<http://www.falconsolutions.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'red MFH',
    'version': '13.0.0.1.0',
    'author': "Marlon Falcón Herández",
    'maintainer': 'Ynext',
    'website': 'http://www.ynext.cl',
    'license': 'AGPL-3',
    'category': 'account.payment',
    'summary': 'Ejemplo de un módulo by Ynext.',
    'depends': ['base','stock'],
    'description': """
Modulo basado en Ynext
===================================================== 
Éste módulo permite selecionar 
""",
    'demo': [],
    'test': [],
    'data': ['views/red_view.xml', 'security/ir.model.access.csv'],
    'installable': True,
    'auto_install': False,
}
