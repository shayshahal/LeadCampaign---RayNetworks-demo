from flask import Flask, request
import os
from dotenv import load_dotenv
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.page import Page

app = Flask(__name__)
my_app_id = os.getenv('APP_ID')
my_app_secret = os.getenv('APP_SECRET')
access_token = os.getenv('PAGE_TOKEN')
id = os.getenv('AD_ACCOUNT_ID')
FacebookAdsApi.init(my_app_id, my_app_secret, access_token)
load_dotenv()


@app.route('/leads-campaign', methods=['POST'])
def createLead():
    page = Page(page_id)
    page.create_lead_gen_form([], {'name': 'leads-campaign', 'questions': [{'type': 'EMAIL'}, {
                                        'type': 'FULL_NAME'}], 'privacy_policy': {'url': 'www.google.com'}, 'follow_up_action_url': 'www.google.com'})
    return 'success', 200

@app.route('/leads-campaign')
def getLeadsFromLast24H():
    page = Page(page_id)
    leadGens = page.get_lead_gen_forms(['id'], {'name': 'leads-campaign'})
    fields = ['id', 'created_time', 'field_data']
    params = {
        'filtering': [{'field': 'time_created', 'operator': 'GREATER_THAN', 'value': time.time()-86400}],
    }
    leads = LeadgenForm(leadGens[0]['id']).get_leads(
        fields=fields, params=params)

    for res in leads:
        fieldDataString = ','.join('{0}: {1}'.format(
            obj['name'], obj['values']) for obj in res['field_data'])
        lead = Lead(
            id=res['id'],
            created_time=res['created_time'],
            fieldData=fieldDataString
        )
        db.session.add(lead)
    db.session.commit()
    return 'success', 200


if __name__ == '__main__':
    app.run(debug=True, port=3000)
