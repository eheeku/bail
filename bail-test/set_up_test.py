def setUp(self):
    config = configparser.ConfigParser()
    config.read('./../config/config.ini')
    client_id = config['KORBIT']['client_id']
    client_secret = config['KORBIT']['client_secret']
    username = config['KORBIT']['username']
    password = config['KORBIT']['password']
    self.korbit_machine = KorbitMachine(mode="Prod",client_id = client_id,
            client_secret = client_secret,
            username=username,
            password=password)
    token = self.korbit_machine.set_token()
