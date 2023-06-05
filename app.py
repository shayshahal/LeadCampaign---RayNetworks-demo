import time
import os
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.page import Page
from facebook_business.adobjects.leadgenform import LeadgenForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv('PAGE_TOKEN')
page_id = os.getenv('PAGE_ID')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite'
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)
FacebookAdsApi.init(access_token=access_token, api_version='v17.0')


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.String(), nullable=False)
    fieldData = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return 'lead: ' + self.created_time


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
