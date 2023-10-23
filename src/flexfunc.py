import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def calc_efficiency(cycle_time, skill_level, quantity, human_traffic, **kwargs) -> float:
    # Create the input variables
    ct = ctrl.Antecedent(np.arange(0, 25, 1), 'cycle_time')
    sl = ctrl.Antecedent(np.arange(0, 11, 1), 'skill_level')
    qt = ctrl.Antecedent(np.arange(0, 100001, 1000), 'quantity')
    ht = ctrl.Antecedent(np.arange(0, 11, 1), 'human_traffic')

    # Create the output variable
    efficiency = ctrl.Consequent(np.arange(0, 11, 1), 'efficiency')

    # Define membership functions for each input variable
    ct['very_short'] = fuzz.trimf(ct.universe, [0, 0, 2])  # 0-2 hours
    ct['short'] = fuzz.trimf(ct.universe, [0, 2, 6])  # 2-6 hours
    ct['medium'] = fuzz.trimf(ct.universe, [2, 8, 14])  # 6-14 hours
    ct['long'] = fuzz.trimf(ct.universe, [10, 18, 24])  # 14-24 hours

    sl['basic'] = fuzz.trimf(sl.universe, [0, 0, 5])
    sl['intermediate'] = fuzz.trimf(sl.universe, [0, 5, 10])
    sl['advanced'] = fuzz.trimf(sl.universe, [5, 10, 10])

    qt['very_low'] = fuzz.trimf(qt.universe, [0, 0, 20000])
    qt['low'] = fuzz.trimf(qt.universe, [20000, 30000, 60000])
    qt['medium'] = fuzz.trimf(qt.universe, [40000, 50000, 70000])
    qt['high'] = fuzz.trimf(qt.universe, [60000, 70000, 100000])

    ht['low'] = fuzz.trimf(ht.universe, [0, 0, 5])
    ht['medium'] = fuzz.trimf(ht.universe, [0, 5, 10])
    ht['high'] = fuzz.trimf(ht.universe, [5, 10, 10])

    # Define the membership functions for the consequent variable
    efficiency['low'] = fuzz.trapmf(efficiency.universe, [0, 0, 3, 5])
    efficiency['medium'] = fuzz.trimf(efficiency.universe, [3, 5, 7])
    efficiency['high'] = fuzz.trapmf(efficiency.universe, [5, 7, 10, 10])

    # Define the rules for the fuzzy inference system
    rule1 = ctrl.Rule(ct['long'] | sl['basic'] | qt['high'] | ht['high'], efficiency['low'])
    rule2 = ctrl.Rule(ct['medium'] | sl['intermediate'] | qt['medium'] | ht['medium'], efficiency['medium'])
    rule3 = ctrl.Rule(ct['short'] | sl['advanced'] | qt['low'] | ht['low'], efficiency['high'])
    # Rule 4: If cycle_time is very short OR skill_level is high AND quantity is high, then efficiency is very high.
    rule4 = ctrl.Rule(ct['very_short'] | sl['advanced'] & qt['high'], efficiency['high'])
    # Rule 5: If cycle_time is short OR skill_level is medium AND quantity is medium, then efficiency is high.
    rule5 = ctrl.Rule(ct['short'] | sl['intermediate'] & qt['medium'], efficiency['high'])
    # Rule 6: If cycle_time is medium AND skill_level is low OR quantity is low, then efficiency is moderate.
    rule6 = ctrl.Rule(ct['medium'] & sl['basic'] | qt['low'], efficiency['medium'])
    # Rule 7: If cycle_time is long OR skill_level is very low AND quantity is very low, then efficiency is low.
    rule7 = ctrl.Rule(ct['long'] | sl['basic'] & qt['very_low'], efficiency['low'])
    # Rule 8: If human_traffic is high, then efficiency is lower by a certain degree, based on the extent of human traffic.
    rule8 = ctrl.Rule(ht['high'], efficiency['low'])

    # Define the control system and add the rules
    eff_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])

    # Define the simulation and run it with the input values
    eff_sim = ctrl.ControlSystemSimulation(eff_ctrl)
    eff_sim.input['cycle_time'] = cycle_time
    eff_sim.input['skill_level'] = skill_level
    eff_sim.input['quantity'] = quantity
    eff_sim.input['human_traffic'] = human_traffic
    eff_sim.compute()

    # Return the output value, which is the performance score
    return round(eff_sim.output['efficiency'], 1)


def calc_safety(mode, layout, robot_movement, gripper_choice, space_requirement, human_traffic, automation_skill,
                safety_requirements, **kwargs) -> float:
    # Define weights
    if mode == 1:
        weights = [0.15, 0.10, 0.10, 0.10, 0.20, 0.10, 0.25]  # collaborative
    else:
        weights = [0.20, 0.15, 0.15, 0.20, 0.15, 0.10, 0.05]  # cooperativet

    # Define Gripper Safety Rating
    if gripper_choice in range(1, 6):  # collaborative
        gripper_rating = 3
    elif gripper_choice in range(6, 11):  # cooperative
        gripper_rating = 7

    # Define inputs    
    inputs = [layout, robot_movement, gripper_rating, space_requirement, human_traffic, automation_skill,
              safety_requirements]

    # Normalize weights
    weights_sum = sum(weights)
    normalized_weights = [weight / weights_sum for weight in weights]

    # Compute weighted sum of inputs
    weighted_sum = sum([input * weight for input, weight in zip(inputs, normalized_weights)])

    # Compute safety rating
    safety_rating = round(weighted_sum * 10) / 10

    return safety_rating
