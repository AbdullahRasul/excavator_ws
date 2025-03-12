import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # Declare launch arguments for simulation (is_sim)
    is_sim_arg = DeclareLaunchArgument(
        "is_sim",
        default_value="True",
        description="Flag to indicate if the robot is running in simulation"
    )

    is_sim = LaunchConfiguration("is_sim")

    # Define the robot description parameter (URDF)
    robot_description = ParameterValue(
        Command(
            [
                "xacro ",
                os.path.join(
                    get_package_share_directory("excavator_description"),  # Updated to your excavator package
                    "urdf",
                    "excavator.urdf.xacro",  # Updated URDF file name for the excavator
                ),
            ]
        ),
        value_type=str,
    )

    # Robot state publisher node for simulation (if not using simulation, skip it)
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        condition=UnlessCondition(is_sim),
        parameters=[{"robot_description": robot_description}],
    )

    # Joint state broadcaster spawner node
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
    )

    # Arm controller spawner node
    arm_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["arm_controller", "--controller-manager", "/controller_manager"],
    )

    return LaunchDescription(
        [
            is_sim_arg,
            robot_state_publisher_node,
            joint_state_broadcaster_spawner,
            arm_controller_spawner,
        ]
    )
