#  Copyright (c) 2021 Hombrelab <me@hombrelab.com>

# Constants for the Backup State component

DOMAIN = "backup_state"
UUID = "f1e28691-9aa0-4b25-8350-ecf5128f8cd2"
SW_MANUFACTURER = "Hombrelab"
SW_NAME = "Backup State"
SW_VERSION = "2.0.006"

# labels
NAME = "name"
TOPIC = "topic"

# default values
DEFAULT_NAME = "backup-state"
DEFAULT_TOPIC = "home-assistant/backup-state"

# list of entities
ENTITIES = [
    [
        'Backup State state',
        'mdi:state-machine',
        None,
        'state'
    ],
    [
        'Backup State timestamp',
        'mdi:update',
        None,
        'timestamp'
    ],
    [
        'Backup State runtime',
        'mdi:run',
        None,
        'runtime'
    ],
    [
        'Backup State display',
        'mdi:run',
        None,
        'display'
    ]
]