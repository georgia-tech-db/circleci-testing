# coding=utf-8
# Copyright 2018-2023 EVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging

__all__ = ["logger"]


LOG_handler = logging.StreamHandler()
LOG_formatter = logging.Formatter(
    fmt="%(asctime)-15s %(levelname)-6s"
    "[%(module)s:%(filename)s:%(funcName)s:%(lineno)04d] %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S",
)
LOG_handler.setFormatter(LOG_formatter)

logger = logging.getLogger(__name__)
logger.addHandler(LOG_handler)
logger.setLevel(logging.WARN)
