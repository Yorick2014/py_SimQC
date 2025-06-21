import math
import numpy as np

from constants import Constants as Const

class Pulse:
    def __init__(self, config_laser: dict[str, float, int]):
        value_wavelength  = float(config_laser.get("central_wavelength"))
        value_duration = float(config_laser.get("pulse_duration"))
        
        if value_wavelength is None or value_duration is None:
                    raise ValueError("Invalid config")

        self._central_wavelength = value_wavelength
        self._pulse_duration = value_duration
        self._number_points = int(config_laser.get("number_points"))

    def get_spectrum(self):
          wavelength = self._central_wavelength
          duration = self._pulse_duration

          nu0 = Const.SPEED_LIGHT / wavelength
          
          # Стандартное отклонение во времени
          sigma_t = duration / (2 * math.sqrt(2 * math.log(2)))
          # Стандартное отклонение в частотной области
          sigma_nu = 1 / (2 * math.pi * sigma_t)
          delta_nu = Const.GAUS_K * (1 / duration)

          nu_min = nu0 - 5 * delta_nu
          nu_max = nu0 + 5 * delta_nu
          nu = np.linspace(nu_min, nu_max, self._number_points)
          intensity = np.exp(-((nu - nu0)**2) / (2 * sigma_nu**2))

          return nu, intensity