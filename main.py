"""Controller to quarantine target computer."""
import sys

import quarantineComputer

def main():
        # Get Target Computer Name from stdin
        if len(sys.argv) > 1 :
                target_computer_name = sys.argv[1]
        else:
                raise InterruptedError
                sys.exit()

        # Tanium API Account Information
        try:
                import settings
                if settings.getId():
                        id_value = settings.getId()
                        hostname = id_value['url']
                        api_token = id_value['api_token']
        except:
                raise ImportError('There are no settings')

        # modify the json to quarantine target computer
        group_defined_info = quarantineComputer.parseQuestion(
                api_token, 
                hostname
        )
        group_defined_info['filters'][0]['value'] = target_computer_name

        quarantine_tanium_packages = quarantineComputer.getPackages(
                api_token, 
                hostname
        )
        quarantineComputer.quarantine(
                api_token, 
                group_defined_info, 
                quarantine_tanium_packages, 
                hostname, 
                target_computer_name
        )

if __name__ == '__main__':
        main()