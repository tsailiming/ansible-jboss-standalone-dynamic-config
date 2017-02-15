from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def run(self, system_type, variables=None, **kwargs):
        
        system_type = system_type[0]

        if system_type == 'ssh':
            return ['system']
        elif system_type == 'db':
            return ['db-password']
        else:
            return ['']
