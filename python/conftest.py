import pytest
import datetime
import pytz
@pytest.fixture(autouse=True)
def getdateantime():
    print(datetime.datetime.now(pytz.timezone('Asia/kolkata')))
