# Excavator Description

## Overview
This repository contains the URDF/Xacro model for an excavator, taken from a MATLAB example by MathWorks. The model is used for simulation and visualization in ROS2.

## Usage Instructions
Follow these steps to visualize and interact with the excavator model in ROS2.

### Source the Workspace
Before running any command, make sure to source your workspace, especially if you are using multiple terminals:

`source ~/excavator_ws/install/setup.bash`

### Publish the Robot State

`ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro /home/${USER}/excavator_ws/src/excavator_description/urdf/excavator.urdf.xacro)"`

### Run the Joint State Publisher GUI

`ros2 run joint_state_publisher_gui joint_state_publisher_gui`

### Launch RViz for Visualization

`ros2 run rviz2 rviz2`

### Set Up RViz
- **Fixed Frame:** Set to `base_link` in the **Global Options**.
- **Loading Configuration:** Load the predefined RViz configuration file located in the `rviz` folder.

## Notes
- Ensure all dependencies, including `xacro`, `robot_state_publisher`, and `rviz2`, are installed.
- If using multiple terminals, always source the workspace before running commands.
