# FAIRWork-AHP-and-FuzzyLogic
Developers: [Zi Xuan(Melody) Tung](https://github.com/melody-tung), [Alexander Nasuta](https://github.com/Alexander-Nasuta), Sylwia Olbrych


## About the project
This project calculates efficiency and safety ratings for your workspace.
Inputs such as robot mode, cycle time, layout, robot movement, gripper choice, space requirement, human traffic, automation skill of workers, safety requirements, and quantity are able to be customised. 

## Key Components

1. `flexfunc.py`: This Python module contains functions for calculating efficiency and safety. The efficiency calculation utilizes fuzzy logic, while the safety calculation involves a weighted sum approach. Here's a brief overview of the functions:

   - `calc_efficiency`: Calculates the efficiency of a workspace based on parameters such as cycle time, skill level, quantity, and human traffic.

   - `calc_safety`: Computes the safety rating of a workspace considering factors like robot mode, layout, robot movement, gripper choice, space requirement, human traffic, automation skill, and safety requirements.

2. `testbuilding.py`: This script serves as a user interface for inputting workspace parameters and obtaining efficiency and safety ratings. It utilizes the functions from `flexfunc.py` to perform the calculations. Users can interact with sliders to input values for various parameters, and the tool provides real-time feedback on efficiency and safety ratings.


## Usage

1. Clone the repository to your local machine.

```bash
git clone https://github.com/Sylwia-Olbrych/FAIRWork-AHP-FuzzyLogic-Safety-Efficiency.git
```

2. Navigate to the project directory
3. Run the application using Python 
4. The GUI window will open with sliders and options to customize your workspace inputs.
5. Adjust the sliders and options according to your workspace setup.
6. Click the "Calculate" button to get efficiency and safety ratings.
7. A new window will pop up displaying the efficiency and safety ratings for your workspace.
8. Close the output window when you are done reviewing the ratings.

## Additional Information
### Input Parameters
**Robot Mode**: Choose between "Cooperative" and "Collaborative" robot modes.<br />
**Cycle Time**: Set the cycle time for your workspace.<br />
**Layout**: Rate the layout of your workspace on a scale from 1 to 10.<br />
**Robot Movement**: Rate the robot movement in your workspace on a scale from 1 to 10.<br />
**Gripper Choice**: Choose a gripper type from the available options.<br />
**Space Requirement**: Rate the space requirement of your workspace on a scale from 1 to 10.<br />
**Human Traffic**: Rate the human traffic in your workspace on a scale from 1 to 10.<br />
**Automation Skill**: Rate the automation skill of your workers on a scale from 1 to 10.<br />
**Safety Requirements**: Rate the safety requirements of your workspace on a scale from 1 to 10.<br />
**Quantity**: Set the quantity of items to be produced or processed.<br />

### Output
The tool will display the following ratings:<br />

**Efficiency**: An efficiency rating based on the provided inputs.<br />
**Safety**: A safety rating based on the provided inputs.<br />

***

“This work has been supported by the FAIRWork project (www.fairwork-project.eu) and has been funded within the European Commission’s Horizon Europe Programme under contract number 101049499. This paper expresses the opinions of the authors and not necessarily those of the European Commission. The European Commission is not liable for any use that may be made of the information contained in this presentation.”

This project provides a graphical user interface (GUI) tool to calculate safety and efficiency ratings for your workspace setup. It takes various input parameters related to your workspace configuration and provides a rating based on those inputs.


Copyright © RWTH of FAIRWork Consortium
