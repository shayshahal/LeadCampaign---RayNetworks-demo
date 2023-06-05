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

    return 'success', 200


if __name__ == '__main__':
    app.run(debug=True, port=3000)
