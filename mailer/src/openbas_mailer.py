from typing import Dict

from contracts_mailer import TYPE, EmailContracts
from pyobas import OpenBAS
from pyobas._injectors.injector_helper import OpenBASInjectorHelper


class OpenBASEmail:
    def __init__(self):
        email_contracts = EmailContracts.build_contract()
        config = {
            "injector_id": "ba0003bc-4edc-45f3-b047-bda6c3b66f74",
            "injector_name": "Mailer injector",
            "injector_type": TYPE,
            "injector_contracts": email_contracts,
        }
        injector_config = {
            "connection": {
                "host": "192.168.2.36",
                "vhost": "/",
                "use_ssl": False,
                "port": 5672,
                "user": "guest",
                "pass": "guest",
            },
            "listen": "openbas_injector_openbas_mailer",
        }
        self.client = OpenBAS(
            url="http://localhost:3001/api",
            token="3207fa04-35d8-4baa-a735-17033abf101d",
        )
        self.helper = OpenBASInjectorHelper(self.client, config, injector_config)

    def _process_message(self, data: Dict) -> str:
        print(data)
        return "OK"

    # Start the main loop
    def start(self):
        self.helper.listen(message_callback=self._process_message)


if __name__ == "__main__":
    openBASEmail = OpenBASEmail()
    openBASEmail.start()
