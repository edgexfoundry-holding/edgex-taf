"""
 @copyright Copyright (C) 2019 IOTech Ltd

 @license SPDX-License-Identifier: Apache-2.0

 @file edgex.py

 @brief This is a demo test file. This file includes setup and teardown routines called by robot to setup and teardown
     the test suite.

 @description
     This is a demo test file. This file includes setup and teardown routines called by robot to setup and teardown
     the test suite.

"""

import http.client
import time

from TUC.data.SettingsInfo import SettingsInfo

def check_services_startup(check_list):
    services = {
        "device-virtual": {"composeName": "device-virtual",
                           "port": SettingsInfo().constant.DEVICE_SERVICE_PORT,
                           "pingUrl": "/api/v1/ping"},
        "data": {"composeName": "data",
                 "port": SettingsInfo().constant.CORE_DATA_PORT,
                 "pingUrl": "/api/v1/ping"},
        "metadata": {"composeName": "metadata",
                     "port": SettingsInfo().constant.CORE_METADATA_PORT,
                     "pingUrl": "/api/v1/ping"},
        "command": {"composeName": "command",
                    "port": SettingsInfo().constant.CORE_COMMAND_PORT,
                    "pingUrl": "/api/v1/ping"},
        "support-logging": {"composeName": "logging",
                            "port": SettingsInfo().constant.SUPPORT_LOGGING_PORT,
                            "pingUrl": "/api/v1/ping"},
        "support-notifications": {"composeName": "notifications",
                                  "port": SettingsInfo().constant.SUPPORT_NOTIFICATION_PORT,
                                  "pingUrl": "/api/v1/ping"},
        "support-scheduler": {"composeName": "scheduler",
                              "port": SettingsInfo().constant.SUPPORT_SCHEDULER_PORT,
                              "pingUrl": "/api/v1/ping"},
        "support-rulesengine": {"composeName": "rulesengine",
                                "port": SettingsInfo().constant.SUPPORT_RULESENGINE_PORT,
                                "pingUrl": "/api/v1/ping"},
        "export-client": {"composeName": "export-client",
                          "port": SettingsInfo().constant.EXPORT_CLIENT_PORT,
                          "pingUrl": "/api/v1/ping"},
        "export-distro": {"composeName": "export-distro",
                          "port": SettingsInfo().constant.EXPORT_DISTRO_PORT,
                          "pingUrl": "/api/v1/ping"},
    }

    for item in check_list:
        if item in services:
            SettingsInfo().TestLog.info("Check service " + item + " is startup...")
            check_service_startup(services[item])


def check_service_startup(d):
    recheck_times = int(SettingsInfo().constant.SERVICE_STARTUP_RECHECK_TIMES)
    wait_time = int(SettingsInfo().constant.SERVICE_STARTUP_WAIT_TIME)
    for i in range(recheck_times):
        SettingsInfo().TestLog.info(
            "Ping service with port {} and request url {} ... ".format(str(d["port"]), d["pingUrl"]))
        conn = http.client.HTTPConnection(host=SettingsInfo().constant.BASE_URL, port=d["port"])
        conn.request(method="GET", url=d["pingUrl"])
        try:
            r1 = conn.getresponse()
        except:
            time.sleep(wait_time)
            continue

        SettingsInfo().TestLog.info(r1.status)
        if int(r1.status) == 200:
            SettingsInfo().TestLog.info("Service is startup.")
            return True
        else:
            time.sleep(wait_time)
            continue
    return False
