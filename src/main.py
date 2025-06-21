import json
from pulses import Pulse
import plots 

def get_config(file_name):
    with open(file_name) as file:
        config = json.load(file)
        return config

def main():
    config_laser = get_config("config/param_laser.json")
    pulse = Pulse(config_laser)
    nu, intensity = pulse.get_spectrum()
    plots.spectrum(nu, intensity)

if __name__ == '__main__':
    main()