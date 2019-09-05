import http.client
from TUC.data.SettingsInfo import SettingsInfo


def modify_consul_config(path,value):
    conn = http.client.HTTPConnection(host="localhost", port=8500)
    conn.request(method="PUT", url=path, body=value)
    try:
        r1 = conn.getresponse()
    except Exception as e:
        raise e
    if int(r1.status) == 200:
        SettingsInfo().TestLog.info("Modify consul with key {} and value {}".format(path,value))
    else:
        raise Exception("Fail to enable MarkPushed.")