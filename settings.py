import re

def getId():
        id_value = {}
        with open('.env', 'r') as env:
                while True:
                        line = env.readline()

                        # account field name patterns
                        user_pattern = 'USER_NAME=(.*)'
                        password_pattern = 'PASSWORD=(.*)'
                        url_pattern = 'URL=(.*)'
                        api_token_pattern = '.*?API_TOKEN=(.*)'

                        # regular exression of above patterns
                        user_results = re.match(user_pattern, line)
                        password_results = re.match(password_pattern, line)
                        url_results = re.match(url_pattern, line)
                        api_token_results = re.match(api_token_pattern, line)

                        # store .env values in id_value dict
                        if user_results:
                                user = user_results.group().replace('USER_NAME=', '')
                                id_value['username'] = user
                        elif password_results:
                                password = password_results.group().replace('PASSWORD=', '')
                                id_value['password'] = password
                        elif url_results:
                                url = url_results.group().replace('URL=', '')
                                id_value['url'] = url
                        elif api_token_results:
                                api_token = api_token_results.group().replace('API_TOKEN=', '')
                                id_value['api_token'] = api_token
                        if not line:
                                return id_value
                                break