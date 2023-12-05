import unittest
from building.flexfunc import calc_efficiency, calc_safety

class TestFlexFunc(unittest.TestCase):
    def test_calc_efficiency(self):
        # Test case 1
        result_1 = calc_efficiency(cycle_time=8, skill_level=6, quantity=55000, human_traffic=8)
        self.assertGreaterEqual(result_1, 0)

        # Test case 2
        result_2 = calc_efficiency(cycle_time=15, skill_level=2, quantity=30000, human_traffic=3)
        self.assertGreaterEqual(result_2, 0)


    def test_calc_safety(self):
        # Test case 1
        result_1 = calc_safety(mode=1, layout=7, robot_movement=9, gripper_choice=3, space_requirement=5,
                               human_traffic=7, automation_skill=8, safety_requirements=6)
        self.assertGreaterEqual(result_1, 0)

        # Test case 2
        result_2 = calc_safety(mode=2, layout=3, robot_movement=6, gripper_choice=8, space_requirement=4,
                               human_traffic=5, automation_skill=3, safety_requirements=9)
        self.assertGreaterEqual(result_2, 0)


if __name__ == '__main__':
    unittest.main()
