# Backup State Sensor
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs) ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/hombrelab/home-assistant-backup-state) ![GitHub commit activity](https://img.shields.io/github/last-commit/hombrelab/home-assistant-backup-state) 

The [backup_state](https://github.com/hombrelab/home-assistant-backup-state) custom component for [home-assistant](https://www.home-assistant.io) is created to show the status of a backup.  
But it can obviously be used for anything that you want to publish a status to home-assistant 'the easy way'...  
### Preparations
I have a (backup) script running before and after a backup is made.  
The script publishes a JSON object to my MQTT server.
```shell script
  # $1 = state     = ON or OFF
  # $2 = timestamp = ON/OFF state timestamp
  # $3 = runtime   = OFF state timestamp - ON state timestamp
  # $display       = formatted runtime hh:mm:ss

  display=$(date -d@$3 -u +%H:%M:%S)

  mosquitto_pub -h $BROKER -m "{\"state\":\"$1\", \"timestamp\":$2, \"runtime\":$3, \"display\":\"$display\"}" -t $topic
```
### Installation
Copy this folder to `<config_dir>/custom_components/backup_state/` or use [hacs](https://github.com/custom-components/hacs) and point it to this [GitHub repository](https://github.com/hombrelab/home-assistant-backup-state).  

Setup is done through the integration page:  
- **name**: _required_ (you can have more than one setup so choose a unique name)  
- **topic**: _required_ MQTT topic the component has to subscribe to

After setting up the component you can create sensor templates to display the values nicely:
```yaml
---
# Server backup state
- platform: template
sensors:
  server_backup_state:
    friendly_name: "Server Backup State"
    value_template: >-
      {% set timestamp = states('sensor.server_backup_state_timestamp') | int | timestamp_custom('%a %H:%M', true) %}
      {% if is_state('sensor.server_backup_state_state', 'on') %}
        {{timestamp}} (started)
      {% elif is_state('sensor.server_backup_state_state', 'off') %}
        {{timestamp}} ({{states('sensor.server_backup_state_display')}})
      {% else %}
        -
      {% endif %}
```