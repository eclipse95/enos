import textwrap


class EnosError(Exception):
    pass


class EnosFailedHostsError(EnosError):
    def __init__(self, hosts):
        self.hosts = hosts


class EnosUnreachableHostsError(EnosError):
    def __init__(self, hosts):
        self.hosts = hosts


class EnosFilePathError(EnosError):
    def __init__(self, filepath, msg=''):
        super(EnosFilePathError, self).__init__(msg)
        self.filepath = filepath


class EnosUnknownProvider(EnosError):
    def __init__(self, provider_name):
        super(self.__class__, self).__init__(textwrap.dedent(f''' \
          The provider '{provider_name}' could not be found.

          Please refer to https://beyondtheclouds.github.io/enos/provider/
          to use a provider that exists.
        '''))
        self.provider_name = provider_name
