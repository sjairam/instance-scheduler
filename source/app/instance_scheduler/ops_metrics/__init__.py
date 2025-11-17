# SPDX-License-Identifier: Apache-2.0
from enum import Enum


class GatheringFrequency(str, Enum):
    UNLIMITED = "UNLIMITED"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
