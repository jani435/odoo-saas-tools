# -*- coding: utf-8 -*-
import openerp
from openerp import models, fields, api
from openerp.addons.saas_utils import connector, database
from openerp import http
from contextlib import closing

class SaasPricingPrice(models.Model):
    _name = 'saas_pricing.price'
    
    name = fields.Char('Price name')
    interval = fields.Char('Price interval')
    price = fields.Float('Price', digits=(16,2))
    stripe_planid = fields.Char('Stripe Plan id')
    stripe_currency = fields.Many2one('res.currency')
    trial_period_days = fields.Char('Stripe trial period days')
    
class SaasPricingPlan(models.Model):
    _inherit = 'saas_portal.plan'
    
    pricing_ids = fields.Many2many('saas_pricing.price', 'saas_pricing_plan')
    
    
