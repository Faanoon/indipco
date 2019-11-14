# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns(filters)
	data=get_data(filters)
#        conditions=get_conditions(filters)
	return columns, data

def get_columns(filters):
 if filters.get("details"):
  if filters.get("details")=="More Details":
    return [
#      _("Process No") + ":Data:80",
      _("Item Code") + ":Link/Item:180",
      _("Item Name") + ":Data:270",
#      _("ROLLON Code") + ":Data:130",
      _("Item Group") + ":Data:130",
      _("UOM") + ":Data:100",
      _("Created By") + ":Data:180"
   ]
  else:
   return [
    _("Item Group") + ":Data:200",
    _("Abbreviation") + ":Data:120",
    _("Total Item Masters") + ":Float:150"
   ]

def get_data(filters):
 if filters.get("details"):
  if filters.get("details")=="More Details":
    if filters.get("item_group"):
     item_group=filters.get("item_group")
     return frappe.db.sql("""
      SELECT

      A.name,
      A.item_name,
 
      A.item_group,
      A.stock_uom,
      A.owner
  
      FROM
      `tabItem` AS A
  
      WHERE
      A.item_group = '%s'
      ORDER BY A.item_code DESC """ %(item_group), as_list=1)

    else:
     return frappe.db.sql("""
      SELECT
      
      A.name,
      A.item_name,
      
      A.item_group,
      A.stock_uom,
      A.owner
  
      FROM
      `tabItem` AS A
      ORDER BY A.item_code DESC """ ) 
  else:
    return frappe.db.sql("""
    SELECT DISTINCT
    A.item_group,
    B.naming_series_for_item,
    count(A.name)
    
    FROM
    `tabItem` AS A,
    `tabItem Group` AS B
    WHERE
    A.item_group=B.name
    GROUP BY A.item_group  """ )