# Copyright (c) 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

VERSION = (4, 4, "0a4")
__version__ = ".".join([str(s) for s in VERSION])

__title__ = "platformio"
__description__ = (
    "A professional collaborative platform for embedded development. "
    "Cross-platform IDE and Unified Debugger. "
    "Static Code Analyzer and Remote Unit Testing. "
    "Multi-platform and Multi-architecture Build System. "
    "Firmware File Explorer and Memory Inspection. "
    "IoT, Arduino, CMSIS, ESP-IDF, FreeRTOS, libOpenCM3, mbedOS, Pulp OS, SPL, "
    "STM32Cube, Zephyr RTOS, ARM, AVR, Espressif (ESP8266/ESP32), FPGA, "
    "MCS-51 (8051), MSP430, Nordic (nRF51/nRF52), NXP i.MX RT, PIC32, RISC-V, "
    "STMicroelectronics (STM8/STM32), Teensy"
)
__url__ = "https://platformio.org"

__author__ = "PlatformIO"
__email__ = "contact@platformio.org"

__license__ = "Apache Software License"
__copyright__ = "Copyright 2014-present PlatformIO"

__apiurl__ = "https://api.platformio.org"

__accounts_api__ = "https://api.accounts.platformio.org"
__registry_api__ = "https://api.registry.platformio.org"
__pioremote_endpoint__ = "ssl:host=remote.platformio.org:port=4413"
