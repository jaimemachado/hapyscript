from typing import Any, Literal
from datetime import datetime
from pyscript_builtins import StateVal

class _automation_state(StateVal):
    current: int
    id: str
    last_triggered: datetime
    mode: str

    def trigger(self, skip_condition: bool):
        ...

    def toggle(self):
        ...

    def turn_on(self):
        ...

    def turn_off(self, stop_actions: bool):
        ...

class automation:
    webhookpyscript: _automation_state
    new_automation: _automation_state

    @staticmethod
    def trigger(*, entity_id: str, skip_condition: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str, stop_actions: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def reload():
        ...

class backup:

    @staticmethod
    def create_automatic():
        ...

class _binary_sensor_state(StateVal):
    ...

class binary_sensor:
    ax7501_b1_wan_status: _binary_sensor_state
    zigbee2mqtt_bridge_connection_state: _binary_sensor_state
    zigbee2mqtt_bridge_connection_state_2: _binary_sensor_state
    ax7501_b1_wan_status_2: _binary_sensor_state

class _button_state(StateVal):

    def press(self):
        ...

class button:
    zigbee2mqtt_bridge_restart: _button_state
    zigbee2mqtt_bridge_restart_2: _button_state

    @staticmethod
    def press(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class camera:

    @staticmethod
    def enable_motion_detection(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def disable_motion_detection(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def snapshot(*, entity_id: str, filename: str):
        """

        Args:
            entity_id: Entity ID
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.jpg"""
        ...

    @staticmethod
    def play_stream(*, entity_id: str, media_player: str, format: Literal['', 'hls']='hls'):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def record(*, entity_id: str, filename: str, duration: int=30, lookback: int=0):
        """

        Args:
            entity_id: Entity ID
            filename:  Example: /tmp/snapshot_{{ entity_id.name }}.mp4"""
        ...

class cast:

    @staticmethod
    def show_lovelace_view(*, entity_id: str, view_path: str, dashboard_path: str | None=None):
        """

        Args:
            view_path:  Example: downstairs
            dashboard_path:  Example: lovelace-cast"""
        ...

class climate:

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_hvac_mode(*, entity_id: str, hvac_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_preset_mode(*, entity_id: str, preset_mode: str):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: away"""
        ...

    @staticmethod
    def set_temperature(*, entity_id: str, temperature: float | None=None, target_temp_high: float | None=None, target_temp_low: float | None=None, hvac_mode: Literal['', 'off', 'auto', 'cool', 'dry', 'fan_only', 'heat_cool', 'heat'] | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_humidity(*, entity_id: str, humidity: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_fan_mode(*, entity_id: str, fan_mode: str):
        """

        Args:
            entity_id: Entity ID
            fan_mode:  Example: low"""
        ...

    @staticmethod
    def set_swing_mode(*, entity_id: str, swing_mode: str):
        """

        Args:
            entity_id: Entity ID
            swing_mode:  Example: on"""
        ...

    @staticmethod
    def set_swing_horizontal_mode(*, entity_id: str, swing_horizontal_mode: str):
        """

        Args:
            entity_id: Entity ID
            swing_horizontal_mode:  Example: on"""
        ...

class cloud:

    @staticmethod
    def remote_connect():
        ...

    @staticmethod
    def remote_disconnect():
        ...

class conversation:

    @staticmethod
    def process(*, text: str, language: str | None=None, agent_id=None, conversation_id: str | None=None) -> dict[str, Any]:
        """

        Args:
            text:  Example: Turn all lights on
            language:  Example: NL
            agent_id:  Example: homeassistant
            conversation_id:  Example: my_conversation_1"""
        ...

    @staticmethod
    def reload(*, language: str | None=None, agent_id=None):
        """

        Args:
            language:  Example: NL
            agent_id:  Example: homeassistant"""
        ...

class counter:

    @staticmethod
    def increment(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def decrement(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def reset(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: float):
        """

        Args:
            entity_id: Entity ID"""
        ...

class cover:

    @staticmethod
    def open_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_cover_position(*, entity_id: str, position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_cover(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def open_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_cover_tilt_position(*, entity_id: str, tilt_position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle_cover_tilt(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class _event_state(StateVal):
    event_type: str
    event_types: list
    restored: bool
    supported_features: int

class event:
    backup_automatic_backup: _event_state
    xiaomibuttom01_action: _event_state
    xiaomibuttom01_action_2: _event_state

class fan:

    @staticmethod
    def turn_on(*, entity_id: str, percentage: int | None=None, preset_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: auto"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def increase_speed(*, entity_id: str, percentage_step: int | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def decrease_speed(*, entity_id: str, percentage_step: int | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def oscillate(*, entity_id: str, oscillating: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_direction(*, entity_id: str, direction: Literal['', 'forward', 'reverse']):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_percentage(*, entity_id: str, percentage: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_preset_mode(*, entity_id: str, preset_mode: str):
        """

        Args:
            entity_id: Entity ID
            preset_mode:  Example: auto"""
        ...

class ffmpeg:

    @staticmethod
    def start(*, entity_id: str | None=None):
        ...

    @staticmethod
    def stop(*, entity_id: str | None=None):
        ...

    @staticmethod
    def restart(*, entity_id: str | None=None):
        ...

class file:

    @staticmethod
    def read_file(*, file_name: str | None=None, file_encoding: Literal['', 'JSON', 'YAML'] | None=None) -> dict[str, Any]:
        """

        Args:
            file_name:  Example: www/my_file.json
            file_encoding:  Example: JSON"""
        ...

class frontend:

    @staticmethod
    def set_theme(*, name, mode: Literal['', 'dark', 'light']='light'):
        """

        Args:
            name:  Example: default"""
        ...

    @staticmethod
    def reload_themes():
        ...

class hassio:

    @staticmethod
    def addon_start(*, addon):
        """

        Args:
            addon:  Example: core_ssh"""
        ...

    @staticmethod
    def addon_stop(*, addon):
        """

        Args:
            addon:  Example: core_ssh"""
        ...

    @staticmethod
    def addon_restart(*, addon):
        """

        Args:
            addon:  Example: core_ssh"""
        ...

    @staticmethod
    def addon_stdin(*, addon):
        """

        Args:
            addon:  Example: core_ssh"""
        ...

    @staticmethod
    def host_shutdown():
        ...

    @staticmethod
    def host_reboot():
        ...

    @staticmethod
    def backup_full(*, name: str | None=None, password: str | None=None, compressed: bool=True, location=None, homeassistant_exclude_database: bool=False):
        """

        Args:
            name:  Example: Backup 1
            password:  Example: password
            location:  Example: my_backup_mount"""
        ...

    @staticmethod
    def backup_partial(*, homeassistant: bool | None=None, homeassistant_exclude_database: bool=False, addons: Any | None=None, folders: Any | None=None, name: str | None=None, password: str | None=None, compressed: bool=True, location=None):
        """

        Args:
            addons:  Example: ['core_ssh', 'core_samba', 'core_mosquitto']
            folders:  Example: ['homeassistant', 'share']
            name:  Example: Partial backup 1
            password:  Example: password
            location:  Example: my_backup_mount"""
        ...

    @staticmethod
    def restore_full(*, slug: str, password: str | None=None):
        """

        Args:
            password:  Example: password"""
        ...

    @staticmethod
    def restore_partial(*, slug: str, homeassistant: bool | None=None, folders: Any | None=None, addons: Any | None=None, password: str | None=None):
        """

        Args:
            folders:  Example: ['homeassistant', 'share']
            addons:  Example: ['core_ssh', 'core_samba', 'core_mosquitto']
            password:  Example: password"""
        ...

class homeassistant:

    @staticmethod
    def save_persistent_states():
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop():
        ...

    @staticmethod
    def restart():
        ...

    @staticmethod
    def check_config():
        ...

    @staticmethod
    def update_entity(*, entity_id: str):
        ...

    @staticmethod
    def reload_core_config():
        ...

    @staticmethod
    def set_location(*, latitude: float, longitude: float, elevation: float | None=None):
        """

        Args:
            latitude:  Example: 32.87336
            longitude:  Example: 117.22743
            elevation:  Example: 120"""
        ...

    @staticmethod
    def reload_custom_templates():
        ...

    @staticmethod
    def reload_config_entry(*, entity_id: str, entry_id: str | None=None):
        """

        Args:
            entity_id: Entity ID
            entry_id:  Example: 8955375327824e14ba89e4b29cc3ec9a"""
        ...

    @staticmethod
    def reload_all():
        ...

class input_boolean:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class input_button:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def press(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class input_datetime:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def set_datetime(*, entity_id: str, date: str | None=None, time: str | None=None, datetime: str | None=None, timestamp: float | None=None):
        '''

        Args:
            entity_id: Entity ID
            date:  Example: "2019-04-20"
            time:  Example: "05:04:20"
            datetime:  Example: "2019-04-20 05:04:20"'''
        ...

class input_number:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: float):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def increment(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def decrement(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class input_select:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def select_first(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_last(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_next(*, entity_id: str, cycle: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_option(*, entity_id: str, option: str):
        '''

        Args:
            entity_id: Entity ID
            option:  Example: "Item A"'''
        ...

    @staticmethod
    def select_previous(*, entity_id: str, cycle: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_options(*, entity_id: str, options: str):
        """

        Args:
            entity_id: Entity ID
            options:  Example: ["Item A", "Item B", "Item C"]"""
        ...

class input_text:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """

        Args:
            entity_id: Entity ID
            value:  Example: This is an example text"""
        ...

class light:

    @staticmethod
    def turn_on(*, entity_id: str, transition: int | None=None, rgb_color: tuple[int, int, int] | None=None, color_temp_kelvin: int | None=None, brightness_pct: int | None=None, brightness_step_pct: int | None=None, effect: str | None=None, rgbw_color: Any | None=None, rgbww_color: Any | None=None, color_name: Literal['', 'homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'] | None=None, hs_color: Any | None=None, xy_color: Any | None=None, color_temp: int | None=None, brightness: int | None=None, brightness_step: int | None=None, white=None, profile: str | None=None, flash: Literal['', 'long', 'short'] | None=None):
        """

        Args:
            entity_id: Entity ID
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str, transition: int | None=None, flash: Literal['', 'long', 'short'] | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str, transition: int | None=None, rgb_color: tuple[int, int, int] | None=None, color_temp_kelvin: int | None=None, brightness_pct: int | None=None, effect: str | None=None, rgbw_color: Any | None=None, rgbww_color: Any | None=None, color_name: Literal['', 'homeassistant', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'navyblue', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'] | None=None, hs_color: Any | None=None, xy_color: Any | None=None, color_temp: int | None=None, brightness: int | None=None, white=None, profile: str | None=None, flash: Literal['', 'long', 'short'] | None=None):
        """

        Args:
            entity_id: Entity ID
            rgb_color:  Example: [255, 100, 100]
            rgbw_color:  Example: [255, 100, 100, 50]
            rgbww_color:  Example: [255, 100, 100, 50, 70]
            hs_color:  Example: [300, 70]
            xy_color:  Example: [0.52, 0.43]
            profile:  Example: relax"""
        ...

class lock:

    @staticmethod
    def unlock(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def lock(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

    @staticmethod
    def open(*, entity_id: str, code: str | None=None):
        """

        Args:
            entity_id: Entity ID
            code:  Example: 1234"""
        ...

class logbook:

    @staticmethod
    def log(*, name: str, message: str, entity_id: str | None=None, domain: str | None=None):
        """

        Args:
            name:  Example: Kitchen
            message:  Example: is being used
            domain:  Example: light"""
        ...

class logger:

    @staticmethod
    def set_default_level(*, level: Literal['', 'debug', 'info', 'warning', 'error', 'fatal', 'critical'] | None=None):
        ...

    @staticmethod
    def set_level():
        ...

class matter:

    @staticmethod
    def water_heater_boost(*, entity_id: str, duration: float=3600, emergency_boost: bool=False, temporary_setpoint: int=65):
        """

        Args:
            entity_id: Entity ID"""
        ...

class _media_player_state(StateVal):
    supported_features: int

    def turn_on(self):
        ...

    def turn_off(self):
        ...

    def toggle(self):
        ...

    def volume_up(self):
        ...

    def volume_down(self):
        ...

    def media_play_pause(self):
        ...

    def media_play(self):
        ...

    def media_pause(self):
        ...

    def media_stop(self):
        ...

    def media_next_track(self):
        ...

    def media_previous_track(self):
        ...

    def clear_playlist(self):
        ...

    def volume_set(self, volume_level: int):
        ...

    def volume_mute(self, is_volume_muted: bool):
        ...

    def media_seek(self, seek_position: float):
        ...

    def join(self, group_members: str):
        """

        Args:
            group_members:  Example: - media_player.multiroom_player2
                - media_player.multiroom_player3
                """
        ...

    def select_source(self, source: str):
        """

        Args:
            source:  Example: video1"""
        ...

    def select_sound_mode(self, sound_mode: str | None):
        """

        Args:
            sound_mode:  Example: Music"""
        ...

    def play_media(self, *, media, enqueue: Literal['', 'play', 'next', 'add', 'replace'] | None=None, announce: bool | None=None):
        """

        Args:
            media:  Example: {"media_content_id": "https://home-assistant.io/images/cast/splash.png", "media_content_type": "music"}
            announce:  Example: true"""
        ...

    def browse_media(self, *, media_content_type: str | None=None, media_content_id: str | None=None) -> dict[str, Any]:
        """

        Args:
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles"""
        ...

    def search_media(self, *, search_query: str, media_content_type: str | None=None, media_content_id: str | None=None, media_filter_classes: str | None=None) -> dict[str, Any]:
        """

        Args:
            search_query:  Example: Beatles
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles
            media_filter_classes:  Example: ['album', 'artist']"""
        ...

    def shuffle_set(self, shuffle: bool):
        ...

    def unjoin(self):
        ...

    def repeat_set(self, repeat: Literal['', 'off', 'all', 'one']):
        ...

class media_player:
    lg_webos_tv_oled65b26la: _media_player_state
    lg_webos_tv_oled55b26la: _media_player_state

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_up(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_down(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_play_pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_play(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_stop(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_next_track(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_previous_track(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clear_playlist(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_set(*, entity_id: str, volume_level: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def volume_mute(*, entity_id: str, is_volume_muted: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def media_seek(*, entity_id: str, seek_position: float):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def join(*, entity_id: str, group_members: str):
        """

        Args:
            entity_id: Entity ID
            group_members:  Example: - media_player.multiroom_player2
                - media_player.multiroom_player3
                """
        ...

    @staticmethod
    def select_source(*, entity_id: str, source: str):
        """

        Args:
            entity_id: Entity ID
            source:  Example: video1"""
        ...

    @staticmethod
    def select_sound_mode(*, entity_id: str, sound_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID
            sound_mode:  Example: Music"""
        ...

    @staticmethod
    def play_media(*, entity_id: str, media, enqueue: Literal['', 'play', 'next', 'add', 'replace'] | None=None, announce: bool | None=None):
        """

        Args:
            entity_id: Entity ID
            media:  Example: {"media_content_id": "https://home-assistant.io/images/cast/splash.png", "media_content_type": "music"}
            announce:  Example: true"""
        ...

    @staticmethod
    def browse_media(*, entity_id: str, media_content_type: str | None=None, media_content_id: str | None=None) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles"""
        ...

    @staticmethod
    def search_media(*, entity_id: str, search_query: str, media_content_type: str | None=None, media_content_id: str | None=None, media_filter_classes: str | None=None) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            search_query:  Example: Beatles
            media_content_type:  Example: music
            media_content_id:  Example: A:ALBUMARTIST/Beatles
            media_filter_classes:  Example: ['album', 'artist']"""
        ...

    @staticmethod
    def shuffle_set(*, entity_id: str, shuffle: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def unjoin(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def repeat_set(*, entity_id: str, repeat: Literal['', 'off', 'all', 'one']):
        """

        Args:
            entity_id: Entity ID"""
        ...

class mqtt:

    @staticmethod
    def publish(*, topic: str, payload=None, evaluate_payload: bool=False, qos: Literal['', '0', '1', '2']=0, retain: bool=False):
        """

        Args:
            topic:  Example: /homeassistant/hello
            payload:  Example: The temperature is {{ states('sensor.temperature') }}"""
        ...

    @staticmethod
    def dump(*, topic: str | None=None, duration: int=5):
        """

        Args:
            topic:  Example: OpenZWave/#"""
        ...

    @staticmethod
    def reload():
        ...

class notify:

    @staticmethod
    def send_message(*, entity_id: str, message: str, title: str | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def persistent_notification(*, message: str, title: str | None=None, data: Any | None=None):
        """

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            data:  Example: platform specific"""
        ...

    @staticmethod
    def notify(*, message: str, title: str | None=None, target: Any | None=None, data: Any | None=None):
        """Sends a notification message using the notify service.

        Args:
            message:  Example: The garage door has been open for 10 minutes.
            title:  Example: Your Garage Door Friend
            target:  Example: platform specific
            data:  Example: platform specific"""
        ...

class _number_state(StateVal):
    max: float
    min: float
    mode: str
    step: float
    unit_of_measurement: str

    def set_value(self, value: str):
        """

        Args:
            value:  Example: 42"""
        ...

class number:
    powerplug01_countdown: _number_state

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """

        Args:
            entity_id: Entity ID
            value:  Example: 42"""
        ...

class persistent_notification:

    @staticmethod
    def create(*, message: str, title: str | None=None, notification_id: str | None=None):
        """

        Args:
            message:  Example: Please check your configuration.yaml.
            title:  Example: Test notification
            notification_id:  Example: 1234"""
        ...

    @staticmethod
    def dismiss(*, notification_id: str):
        """

        Args:
            notification_id:  Example: 1234"""
        ...

    @staticmethod
    def dismiss_all():
        ...

class _person_state(StateVal):
    device_trackers: list
    editable: bool
    id: str
    user_id: str

class person:
    jaime_machado: _person_state

    @staticmethod
    def reload():
        ...

class pyscript:

    @staticmethod
    def hello():
        """A more complex service."""
        ...

    @staticmethod
    def main():
        """A more complex service."""
        ...

    @staticmethod
    def reload(*, global_ctx: str | None=None):
        """Reloads all available pyscripts and restart triggers

        Args:
            global_ctx: Only reload this specific global context (file or app) Example: file.example"""
        ...

    @staticmethod
    def generate_stubs() -> dict[str, Any]:
        """Build a stub files combining builtin helpers with discovered entities and services."""
        ...

    @staticmethod
    def jupyter_kernel_start(*, key: str, kernel_name: str='pyscript', shell_port: int | None=None, iopub_port: int | None=None, stdin_port: int | None=None, control_port: int | None=None, hb_port: int | None=None, ip: str='127.0.0.1', transport: Literal['', 'tcp', 'udp']='tcp', signature_scheme: Literal['', 'hmac-sha256']='hmac-sha256'):
        """Starts a jupyter kernel for interactive use; Called by Jupyter front end and should generally not be used by users

        Args:
            key: Used for signing Example: 012345678-9abcdef023456789abcdef
            kernel_name: Kernel name Example: pyscript
            shell_port: Shell port number Example: 63599
            iopub_port: IOPub port number Example: 63598
            stdin_port: Stdin port number Example: 63597
            control_port: Control port number Example: 63596
            hb_port: Heartbeat port number Example: 63595
            ip: IP address to connect to Jupyter front end Example: 127.0.0.1
            transport: Transport type Example: tcp
            signature_scheme: Signing algorithm Example: hmac-sha256"""
        ...

class recorder:

    @staticmethod
    def purge(*, keep_days: int | None=None, repack: bool=False, apply_filter: bool=False):
        ...

    @staticmethod
    def purge_entities(*, entity_id: str | None=None, domains: Any | None=None, entity_globs: Any | None=None, keep_days: int=0):
        """

        Args:
            domains:  Example: sun
            entity_globs:  Example: domain*.object_id*"""
        ...

    @staticmethod
    def enable():
        ...

    @staticmethod
    def disable():
        ...

    @staticmethod
    def get_statistics(*, start_time: datetime, statistic_ids, period: Literal['', '5minute', 'hour', 'day', 'week', 'month'], types: Literal['', 'change', 'last_reset', 'max', 'mean', 'min', 'state', 'sum'], end_time: datetime | None=None, units: Any | None=None) -> dict[str, Any]:
        """

        Args:
            start_time:  Example: 2025-01-01 00:00:00
            statistic_ids:  Example: ['sensor.energy_consumption', 'sensor.temperature']
            period:  Example: hour
            types:  Example: ['mean', 'sum']
            end_time:  Example: 2025-01-02 00:00:00
            units:  Example: {'energy': 'kWh', 'temperature': '°C'}"""
        ...

class scene:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def apply(*, entities: Any, transition: int | None=None):
        """

        Args:
            entities:  Example: light.kitchen: "on"
                light.ceiling:
                  state: "on"
                  brightness: 80
                """
        ...

    @staticmethod
    def create(*, scene_id: str, entities: Any | None=None, snapshot_entities: str | None=None):
        """

        Args:
            scene_id:  Example: all_lights
            entities:  Example: light.tv_back_light: "on"
                light.ceiling:
                  state: "on"
                  brightness: 200
                
            snapshot_entities:  Example: - light.ceiling
                - light.kitchen
                """
        ...

    @staticmethod
    def delete(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str, transition: int | None=None):
        """

        Args:
            entity_id: Entity ID"""
        ...

class schedule:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def get_schedule(*, entity_id: str) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...

class script:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class _select_state(StateVal):
    options: list

    def select_first(self):
        ...

    def select_last(self):
        ...

    def select_next(self, cycle: bool):
        ...

    def select_option(self, option: str):
        '''

        Args:
            option:  Example: "Item A"'''
        ...

    def select_previous(self, cycle: bool):
        ...

class select:
    zigbee2mqtt_bridge_log_level: _select_state
    zigbee2mqtt_bridge_log_level_2: _select_state
    powerplug01_power_outage_memory: _select_state
    powerplug01_indicator_mode: _select_state

    @staticmethod
    def select_first(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_last(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_next(*, entity_id: str, cycle: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def select_option(*, entity_id: str, option: str):
        '''

        Args:
            entity_id: Entity ID
            option:  Example: "Item A"'''
        ...

    @staticmethod
    def select_previous(*, entity_id: str, cycle: bool=True):
        """

        Args:
            entity_id: Entity ID"""
        ...

class _sensor_state(StateVal):
    options: list
    restored: bool
    state_class: str
    supported_features: int
    unit_of_measurement: str

class sensor:
    sun_next_dawn: _sensor_state
    sun_next_dusk: _sensor_state
    sun_next_midnight: _sensor_state
    sun_next_noon: _sensor_state
    sun_next_rising: _sensor_state
    sun_next_setting: _sensor_state
    backup_backup_manager_state: _sensor_state
    backup_next_scheduled_automatic_backup: _sensor_state
    backup_last_successful_automatic_backup: _sensor_state
    backup_last_attempted_automatic_backup: _sensor_state
    ax7501_b1_external_ip: _sensor_state
    ax7501_b1_download_speed: _sensor_state
    ax7501_b1_upload_speed: _sensor_state
    xiaomibuttom01_battery: _sensor_state
    xiaomibuttom01_voltage: _sensor_state
    zigbee2mqtt_bridge_version: _sensor_state
    zigbee2mqtt_bridge_version_2: _sensor_state
    powerplug01_power: _sensor_state
    powerplug01_current: _sensor_state
    powerplug01_voltage: _sensor_state
    powerplug01_energy: _sensor_state
    powerplug01_linkquality: _sensor_state
    xiaomibuttom01_battery_2: _sensor_state
    xiaomibuttom01_voltage_2: _sensor_state
    ax7501_b1_external_ip_2: _sensor_state
    ax7501_b1_download_speed_2: _sensor_state
    ax7501_b1_upload_speed_2: _sensor_state

class shell_command:

    @staticmethod
    def pyscript_git_pull() -> dict[str, Any]:
        ...

class shopping_list:

    @staticmethod
    def add_item(*, name: str):
        """

        Args:
            name:  Example: Beer"""
        ...

    @staticmethod
    def remove_item(*, name: str):
        """

        Args:
            name:  Example: Beer"""
        ...

    @staticmethod
    def complete_item(*, name: str):
        """

        Args:
            name:  Example: Beer"""
        ...

    @staticmethod
    def incomplete_item(*, name: str):
        """

        Args:
            name:  Example: Beer"""
        ...

    @staticmethod
    def complete_all():
        ...

    @staticmethod
    def incomplete_all():
        ...

    @staticmethod
    def clear_completed_items():
        ...

    @staticmethod
    def sort(*, reverse: bool=False):
        ...

class _switch_state(StateVal):

    def turn_off(self):
        ...

    def turn_on(self):
        ...

    def toggle(self):
        ...

class switch:
    zigbee2mqtt_bridge_permit_join: _switch_state
    zigbee2mqtt_bridge_permit_join_2: _switch_state
    powerplug01: _switch_state
    powerplug01_child_lock: _switch_state

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class system_log:

    @staticmethod
    def clear():
        ...

    @staticmethod
    def write(*, message: str, level: Literal['', 'debug', 'info', 'warning', 'error', 'critical']='error', logger: str | None=None):
        """

        Args:
            message:  Example: Something went wrong
            logger:  Example: mycomponent.myplatform"""
        ...

class timer:

    @staticmethod
    def reload():
        ...

    @staticmethod
    def start(*, entity_id: str, duration: str | None=None):
        """

        Args:
            entity_id: Entity ID
            duration:  Example: 00:01:00 or 60"""
        ...

    @staticmethod
    def pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def cancel(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def finish(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def change(*, entity_id: str, duration: str=0):
        """

        Args:
            entity_id: Entity ID
            duration:  Example: 00:01:00, 60 or -60"""
        ...

class _todo_state(StateVal):
    supported_features: int

    def add_item(self, *, item: str, due_date: datetime | None=None, due_datetime: datetime | None=None, description: str | None=None):
        """

        Args:
            item:  Example: Submit income tax return
            due_date:  Example: 2023-11-17
            due_datetime:  Example: 2023-11-17 13:30:00
            description:  Example: A more complete description of the to-do item than that provided by the summary."""
        ...

    def update_item(self, *, item: str, rename: str | None=None, status: Literal['', 'needs_action', 'completed'] | None=None, due_date: datetime | None=None, due_datetime: datetime | None=None, description: str | None=None):
        """

        Args:
            item:  Example: Submit income tax return
            rename:  Example: Something else
            status:  Example: needs_action
            due_date:  Example: 2023-11-17
            due_datetime:  Example: 2023-11-17 13:30:00
            description:  Example: A more complete description of the to-do item than that provided by the summary."""
        ...

    def remove_item(self, item: str):
        """

        Args:
            item:  Example: Submit income tax return"""
        ...

    def get_items(self, status: Literal['', 'needs_action', 'completed']) -> dict[str, Any]:
        """

        Args:
            status:  Example: needs_action"""
        ...

    def remove_completed_items(self):
        ...

class todo:
    shopping_list: _todo_state

    @staticmethod
    def add_item(*, entity_id: str, item: str, due_date: datetime | None=None, due_datetime: datetime | None=None, description: str | None=None):
        """

        Args:
            entity_id: Entity ID
            item:  Example: Submit income tax return
            due_date:  Example: 2023-11-17
            due_datetime:  Example: 2023-11-17 13:30:00
            description:  Example: A more complete description of the to-do item than that provided by the summary."""
        ...

    @staticmethod
    def update_item(*, entity_id: str, item: str, rename: str | None=None, status: Literal['', 'needs_action', 'completed'] | None=None, due_date: datetime | None=None, due_datetime: datetime | None=None, description: str | None=None):
        """

        Args:
            entity_id: Entity ID
            item:  Example: Submit income tax return
            rename:  Example: Something else
            status:  Example: needs_action
            due_date:  Example: 2023-11-17
            due_datetime:  Example: 2023-11-17 13:30:00
            description:  Example: A more complete description of the to-do item than that provided by the summary."""
        ...

    @staticmethod
    def remove_item(*, entity_id: str, item: str):
        """

        Args:
            entity_id: Entity ID
            item:  Example: Submit income tax return"""
        ...

    @staticmethod
    def get_items(*, entity_id: str, status: Literal['', 'needs_action', 'completed']='needs_action') -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID
            status:  Example: needs_action"""
        ...

    @staticmethod
    def remove_completed_items(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class _tts_state(StateVal):

    def speak(self, *, media_player_entity_id: str, message: str, cache: bool=True, language: str | None=None, options: Any | None=None):
        """

        Args:
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...

class tts:
    google_translate_en_com: _tts_state

    @staticmethod
    def speak(*, entity_id: str, media_player_entity_id: str, message: str, cache: bool=True, language: str | None=None, options: Any | None=None):
        """

        Args:
            entity_id: Entity ID
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...

    @staticmethod
    def clear_cache():
        ...

    @staticmethod
    def cloud_say(*, entity_id: str, message: str, cache: bool=False, language: str | None=None, options: Any | None=None):
        """Say something using text-to-speech on a media player with cloud.

        Args:
            message:  Example: My name is hanna
            language:  Example: ru
            options:  Example: platform specific"""
        ...

class _update_state(StateVal):
    auto_update: bool
    display_precision: int
    entity_picture: str
    in_progress: bool
    installed_version: str
    latest_version: str
    release_summary: Any
    release_url: str
    skipped_version: Any
    supported_features: int
    title: str
    update_percentage: Any

    def install(self, *, version: str | None=None, backup: bool | None=None):
        """

        Args:
            version:  Example: 1.0.0"""
        ...

    def skip(self):
        ...

    def clear_skipped(self):
        ...

class update:
    home_assistant_supervisor_update: _update_state
    home_assistant_core_update: _update_state
    home_assistant_operating_system_update: _update_state
    matter_server_update: _update_state
    studio_code_server_update: _update_state
    esphome_device_builder_update: _update_state
    get_hacs_update: _update_state
    hacs_update: _update_state
    onedrive_backup_update: _update_state
    mushroom_update: _update_state
    mushroom_dashboard_strategy_update: _update_state
    pyscript_update: _update_state
    powerplug01: _update_state
    advanced_ssh_web_terminal_update: _update_state
    tailscale_update: _update_state

    @staticmethod
    def install(*, entity_id: str, version: str | None=None, backup: bool | None=None):
        """

        Args:
            entity_id: Entity ID
            version:  Example: 1.0.0"""
        ...

    @staticmethod
    def skip(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clear_skipped(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class vacuum:

    @staticmethod
    def start(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def pause(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def return_to_base(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def clean_spot(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def locate(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_fan_speed(*, entity_id: str, fan_speed: str):
        """

        Args:
            entity_id: Entity ID
            fan_speed:  Example: low"""
        ...

    @staticmethod
    def send_command(*, entity_id: str, command: str, params: Any | None=None):
        """

        Args:
            entity_id: Entity ID
            command:  Example: set_dnd_timer
            params:  Example: { "key": "value" }"""
        ...

class valve:

    @staticmethod
    def open_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def close_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_valve_position(*, entity_id: str, position: int):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def stop_valve(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

class water_heater:

    @staticmethod
    def turn_on(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_away_mode(*, entity_id: str, away_mode: bool):
        """

        Args:
            entity_id: Entity ID"""
        ...

    @staticmethod
    def set_temperature(*, entity_id: str, temperature: float, operation_mode: str | None=None):
        """

        Args:
            entity_id: Entity ID
            operation_mode:  Example: eco"""
        ...

    @staticmethod
    def set_operation_mode(*, entity_id: str, operation_mode: str):
        """

        Args:
            entity_id: Entity ID
            operation_mode:  Example: eco"""
        ...

class _weather_state(StateVal):
    attribution: str
    cloud_coverage: float
    dew_point: float
    humidity: int
    precipitation_unit: str
    pressure: float
    pressure_unit: str
    supported_features: int
    temperature: float
    temperature_unit: str
    uv_index: float
    visibility_unit: str
    wind_bearing: float
    wind_speed: float
    wind_speed_unit: str

    def get_forecasts(self, type: Literal['', 'daily', 'hourly', 'twice_daily']) -> dict[str, Any]:
        ...

class weather:
    forecast_home: _weather_state

    @staticmethod
    def get_forecasts(*, entity_id: str, type: Literal['', 'daily', 'hourly', 'twice_daily']) -> dict[str, Any]:
        """

        Args:
            entity_id: Entity ID"""
        ...

class zone:

    @staticmethod
    def reload():
        ...