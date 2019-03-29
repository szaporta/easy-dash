from datadog import initialize, api
import argparse

# parser = argparse.ArgumentParser()
# group_origin = parser.add_argument_group('Keys for Origininating DD account (where the dashboard lives)')
# group_origin.add_argument('--origapikey', help='Enter the origin API key')
# group_origin.add_argument('--origappkey', help='Enter the origin APP key')
# group_dest = parser.add_argument_group('Keys for the Destination DD account (where the dashboard is going')
# group_dest.add_argument('--destapikey', help='Enter the destination API key')
# group_dest.add_argument('--destappkey', help='Enter the destination APP key')
# group_dashboard = parser.add_argument_group('Dashboard to copy')
# group_dashboard.add_argument('--dash', help='ID of the dashboard you want to clone ex: 442-3kr-k68')
# args = parser.parse_args()



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
    parser.add_argument('--origapikey', help='Enter the origin API key')
    parser.add_argument('--origappkey', help='Enter the origin APP key')
    parser.add_argument('--destapikey', help='Enter the destination API key')
    parser.add_argument('--destappkey', help='Enter the destination APP key')
    parser.add_argument('--dash', help='ID of the dashboard you want to clone ex: 442-3kr-k68')


#     parser.add_argument('square', help='displace a square of a given number', type=int)
#     parser.add_argument("x", type=int, help="the base")
#     parser.add_argument("y", type=int, help="the exponent")
#     parser.add_argument('-v', '--verbosity', help='increase output verbosity', action='count', default=0)
    args = parser.parse_args()
#     answer = args.x**args.y
#     if args.verbosity >= 2:
#             print("{} to the power {} equals {}".format(args.x, args.y, answer))
#     elif args.verbosity >= 1:
#             print("{}^{} == {}".format(args.x, args.y, answer))
#     else:
#             print(answer)
#     for arg in args:
#             print("Arg: ", arg)
    print(args)
    print(args.dash)
    print(args.origapikey)
    print(args.origappkey)
    print(args.destapikey)
    print(args.destappkey)


    dashboard = get_original_dashboard(
        
        args.origapikey,           # <=== Replace this with the API key of the account with the dashboard you want to clone
        args.origappkey,           # <=== Replace this with the APP key of the account with the dashboard you want to clone
        args.dash       # <=== Replace this with the ID of the dashboard you want to clone ex: '442-3kr-k68'
        
        )
    
    create_new_dashboard(
        
        args.destapikey,             # <=== Replace this with the API key of your own account            
        args.destappkey,             # <=== Replace this with the APP key of your own account
        dashboard
        
        )
