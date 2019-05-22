import os

import pytest


@pytest.fixture(scope='module')  # type: ignore
def bucket_name() -> str:
    return 'fststaging_nick_testing'
    #return 'voiceai-staging-public-test'


@pytest.fixture(scope='module')  # type: ignore
def creds() -> str:
    # TODO: bundle public creds into this repo
    return os.environ['GOOGLE_APPLICATION_CREDENTIALS']
