import math
import numpy as np

pressure = 100658.1

dry_ball_hole = 12.71
wet_ball_hole = 12.12

dry_ball_indoor = 26.86
wet_ball_indoor = 19.01

pressure_diff = 25.9

water_vapor_pressure_hole = 0.621121 * np.exp((18.678 - wet_ball_hole/234.5) * (wet_ball_hole / (257.14 + wet_ball_hole))) * 1000
Ws_hole = 0.62198 * water_vapor_pressure_hole / (pressure - wet_ball_hole)
W_hole = ((2501 - 2.381 * wet_ball_hole) * Ws_hole - 1.006 * (dry_ball_hole - wet_ball_hole)) / (2501 + 1.805 * dry_ball_hole - 4.186 * wet_ball_hole)
specific_volumn_hole = 0.2871 * (dry_ball_hole + 273.15) * (1 + 1.6078 * W_hole) / (pressure / 1000)
enthalpy_hole = 1.006 * dry_ball_hole + W_hole * (2501 + 1.805 * dry_ball_hole)

water_vapor_pressure_indoor = 0.621121 * np.exp((18.678 - wet_ball_indoor/234.5) * (wet_ball_indoor / (257.14 + wet_ball_indoor))) * 1000
Ws_indoor = 0.62198 * water_vapor_pressure_indoor / (pressure - wet_ball_indoor)
W_indoor = ((2501 - 2.381 * wet_ball_indoor) * Ws_indoor - 1.006 * (dry_ball_indoor - wet_ball_indoor)) / (2501 + 1.805 * dry_ball_indoor - 4.186 * wet_ball_indoor)
# specific_volumn_indoor = 0.2871 * (dry_ball_indoor + 273.15) * (1 + 1.6078 * W_indoor) / (pressure / 1000)
enthalpy_indoor = 1.006 * dry_ball_indoor + W_indoor * (2501 + 1.805 * dry_ball_indoor)

wind_speed = math.sqrt(2 * 9.81 * pressure_diff * specific_volumn_hole)

spray_total = 0
for idx, item in enumerate(['4']):
    if '2p5' in item:
        spray_total = spray_total + math.pi * (2.5/2 ** 2)
    else:
        spray_total = spray_total + math.pi * ((float(item)/2) ** 2)

wind_volumn = wind_speed * 39.37 * spray_total
wind_volumn_m3 = wind_volumn * (0.0254 ** 3)

instrument_heat_loss = 0
ability = wind_volumn_m3 * (enthalpy_indoor - enthalpy_hole) / (specific_volumn_hole * (1 + W_hole)) * 1000 + instrument_heat_loss

print('specific_volumn_hole:', specific_volumn_hole)
print('wind_speed:', wind_speed)
print('wind_volumn:', wind_volumn)
print('ability', ability)