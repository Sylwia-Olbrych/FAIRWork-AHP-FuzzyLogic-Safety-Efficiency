import tkinter as tk
import flexfunc
#%%
#Update Gripper Choice according to Robot Mode
def update_gripper_choice_scale(slider, value):
    gripper_choice_scale.config(from_=6 if value == 2 else 1)
    gripper_choice_scale.config(to=10 if value == 2 else 5)
    if slider == "robot_scale":
        gripper_choice_scale.set(1)
#%%
def calculate_ratings():
    # Get current values of sliders
    robot_mode = robot_mode_var.get()
    cycle_time = cycle_time_scale.get()
    layout = layout_scale.get()
    robot_movement = robot_movement_scale.get()
    gripper_choice = gripper_choice_scale.get()
    space_requirement = space_requirement_scale.get()
    human_traffic = human_traffic_scale.get()
    automation_skill = automation_skill_scale.get()
    safety_requirements = safety_requirements_scale.get()
    quantity = quantity_scale.get()

    # Calculate efficiency and safety
    efficiency = flexfunc.calc_efficiency(cycle_time, automation_skill, quantity, human_traffic)
    safety = flexfunc.calc_safety(robot_mode, layout, robot_movement, gripper_choice, space_requirement, human_traffic, automation_skill, safety_requirements)

    # Display the overall rating in a new window
    output_window = tk.Toplevel()
    output_window.title("Rating")
    output_window.geometry("200x100")
    output_window.resizable(False, False)

     # Add some widgets to the window
    efficiency_label = tk.Label(output_window, text="Efficiency:")
    efficiency_label.grid(row=0, column=0, padx=10, pady=10)

    efficiency_rating = tk.Label(output_window, text=f"{efficiency:.2f}")
    efficiency_rating.grid(row=0, column=1, padx=10, pady=10)

    safety_label = tk.Label(output_window, text="Safety:")
    safety_label.grid(row=1, column=0, padx=10, pady=10)

    safety_rating = tk.Label(output_window, text=f"{safety:.2f}")
    safety_rating.grid(row=1, column=1, padx=10, pady=10)

    button = tk.Button(output_window, text="Close", command=output_window.destroy)
    button.grid(row=2, column=0, columnspan=2, pady=10)

#%%
# Create input window for sliders and calculate button
input_window = tk.Tk()
input_window.title("Input Parameters")


#Slider
# Add robot slider
#robot_label = tk.Label(input_window, text="Robot Mode:")
#robot_label.grid(row=0, column=0, padx=10, pady=10)
#robot_scale = tk.Scale(input_window, from_=1, to=2, orient=tk.HORIZONTAL, length=200, command=lambda x: update_gripper_choice_scale("robot_scale", int(x)))
#robot_scale.grid(row=0, column=1, padx=10, pady=10)
robot_label = tk.Label(input_window, text="Robot Mode:")
robot_label.grid(row=0, column=0, padx=10, pady=10)

robot_mode_var = tk.IntVar()
robot_mode_var.set(1)  # set the default value to 1

cooperative_rb = tk.Radiobutton(input_window, text="Cooperative", variable=robot_mode_var, value=1, command=lambda: update_gripper_choice_scale("robot_scale", 1))
cooperative_rb.grid(row=1, column=0)

collaborative_rb = tk.Radiobutton(input_window, text="Collaborative", variable=robot_mode_var, value=2, command=lambda: update_gripper_choice_scale("robot_scale", 2))
collaborative_rb.grid(row=1, column=1)


cycle_time_slider = tk.Label(input_window, text='Cycle Time:')
cycle_time_slider.grid(row=2, column=0, padx=10, pady=10)
cycle_time_scale = tk.Scale(input_window, from_=0, to=24, resolution=0.1, orient=tk.HORIZONTAL, length=200)
cycle_time_scale.grid(row=2, column=1, padx=10, pady=10)


layout_slider = tk.Label(input_window, text='Layout:')
layout_slider.grid(row=3, column=0, padx=10, pady=10)
layout_scale = tk.Scale(input_window, from_=1, to=10, orient=tk.HORIZONTAL, length=200)
layout_scale.grid(row=3, column=1, padx=10, pady=10)

robot_movement_slider = tk.Label(input_window, text='Robot Movement:')
robot_movement_slider.grid(row=4, column=0, padx=10, pady=10)
robot_movement_scale = tk.Scale(input_window, from_=1, to=10, orient=tk.HORIZONTAL, length=200)
robot_movement_scale.grid(row=4, column=1, padx=10, pady=10)

# Add gripper slider
gripper_choice_label = tk.Label(input_window, text="Gripper Choice:")
gripper_choice_label.grid(row=5, column=0, padx=10, pady=10)
gripper_choice_scale = tk.Scale(input_window, from_=1, to=5, orient=tk.HORIZONTAL, length=200)
gripper_choice_scale.grid(row=5, column=1, padx=10, pady=10)

space_requirement_slider = tk.Label(input_window, text='Space Requirement:')
space_requirement_slider.grid(row=6, column=0, padx=10, pady=10)
space_requirement_scale = tk.Scale(input_window, from_=1, to=10, orient=tk.HORIZONTAL, length=200)
space_requirement_scale.grid(row=6, column=1, padx=10, pady=10)

human_traffic_slider = tk.Label(input_window, text='Human Traffic:')
human_traffic_slider.grid(row=7, column=0, padx=10, pady=10)
human_traffic_scale = tk.Scale(input_window, from_=1, to=10, orient=tk.HORIZONTAL, length=200)
human_traffic_scale.grid(row=7, column=1, padx=10, pady=10)

automation_skill_slider = tk.Label(input_window, text='Automation Skill:')
automation_skill_slider.grid(row=8, column=0, padx=10, pady=10)
automation_skill_scale = tk.Scale(input_window, from_=1, to=10, orient=tk.HORIZONTAL, length=200)
automation_skill_scale.grid(row=8, column=1, padx=10, pady=10)

safety_requirements_slider = tk.Label(input_window, text='Safety Requirements:')
safety_requirements_slider.grid(row=9, column=0, padx=10, pady=10)
safety_requirements_scale = tk.Scale(input_window, from_=1, to=10, orient=tk.HORIZONTAL, length=200)
safety_requirements_scale.grid(row=9, column=1, padx=10, pady=10)

quantity_slider = tk.Label(input_window, text='Quantity:')
quantity_slider.grid(row=10, column=0, padx=10, pady=10)
quantity_scale = tk.Scale(input_window, from_=0, to=100000, resolution=1000, orient=tk.HORIZONTAL, length=200)
quantity_scale.grid(row=10, column=1, padx=10, pady=10)


# Create the calculate button
#calculate_button = tk.Button(root, text="Calculate", command=calculate_ratings)

# Add calculate button
calculate_button = tk.Button(input_window, text="Calculate", command=calculate_ratings)
calculate_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)


# Run the main loop
input_window.mainloop()


#%%
