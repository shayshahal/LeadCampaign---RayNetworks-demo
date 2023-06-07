import os
import time
from facebook_business.adobjects.ad import Ad
from api.models import db
from api.models.lead import Lead


def get_leads_resolver(_, info):
    fields = ['id', 'created_time', 'field_data']
    params = {
        'filtering': [{'field': 'time_created', 'operator': 'GREATER_THAN', 'value': time.time()-86400}],
    }
    leads = Ad(os.environ['AD_ID']).get_leads(fields=fields, params=params)
    leadsData = []
    for lead in leads:
        leadData = Lead(
            id=lead['id'],
            created_time=lead['created_time'],
            fieldData=lead['field_data'],
        )
        leadsData.append(leadData)
        db.session.add(leadData)
    db.session.commit()
    return leadsData
