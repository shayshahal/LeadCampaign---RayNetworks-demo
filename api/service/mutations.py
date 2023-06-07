from facebook_business.adobjects.page import Page
import os


def create_leadgenForm_resolver(_, info):
    page = Page(os.environ['PAGE_ID'])
    print(page.get_lead_gen_forms(['data']))
    fields = ['id', 'ad_id']
    params = {
        'name': 'leads-campaign-ariadne20', 'questions': [{'type': 'EMAIL'}, {
            'type': 'FULL_NAME'}], 'privacy_policy': {'url': 'www.google.com'}, 'follow_up_action_url': 'www.google.com'}
    leadgenForm = page.create_lead_gen_form(fields=fields, params=params)
    print(leadgenForm)
    return leadgenForm
