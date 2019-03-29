from datadog import initialize, api
import argparse

def get_original_dashboard(api_key, app_key, dashboard_id):

    options = { 'api_key': api_key, 'app_key': app_key }
    initialize(**options)
    
    og_dash = api.Dashboard.get(dashboard_id)
    
    return og_dash

def create_new_dashboard(api_key, app_key, dashboard_template):
    
    options = { 'api_key': api_key, 'app_key': app_key }
    initialize(**options)
    
    title = dashboard_template['title']
    widgets = dashboard_template['widgets']
    layout_type = dashboard_template['layout_type']
    description = dashboard_template['description']
    is_read_only = dashboard_template['is_read_only']
    notify_list = dashboard_template['notify_list']
    template_variables = dashboard_template['template_variables']

    api.Dashboard.create(
        
        title=title,
        widgets=widgets,
        layout_type=layout_type,
        description=description,
        is_read_only=is_read_only,
        notify_list=notify_list,
        template_variables=template_variables
        
        )
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--srcapikey', help='Enter the source API key')
    parser.add_argument('--srcappkey', help='Enter the source APP key')
    parser.add_argument('--dstapikey', help='Enter the destination API key')
    parser.add_argument('--dstappkey', help='Enter the destination APP key')
    parser.add_argument('--dash', help='ID of the dashboard you want to clone ex: 442-3kr-k68')
    args = parser.parse_args()

    dashboard = get_original_dashboard(
        
        args.srcapikey,           # <=== Replace this with the API key of the account with the dashboard you want to clone
        args.srcappkey,           # <=== Replace this with the APP key of the account with the dashboard you want to clone
        args.dash       # <=== Replace this with the ID of the dashboard you want to clone ex: '442-3kr-k68'
        
        )
    
    create_new_dashboard(
        
        args.dstapikey,             # <=== Replace this with the API key of your own account            
        args.dstappkey,             # <=== Replace this with the APP key of your own account
        dashboard
        
        )
