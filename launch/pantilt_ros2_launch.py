from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command, FindExecutable
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    share = Path(get_package_share_directory('pantilt_ros2'))
    model = PathJoinSubstitution([str(share), 'urdf', LaunchConfiguration('model')])
    return LaunchDescription([
        DeclareLaunchArgument('model', default_value='01_pantilt.urdf'),
        Node(package='robot_state_publisher', executable='robot_state_publisher',
             parameters=[{'robot_description': ParameterValue(
                 Command([FindExecutable(name='xacro'), ' ', model]), value_type=str)}]),
        Node(package='joint_state_publisher_gui', executable='joint_state_publisher_gui'),
        Node(package='rviz2', executable='rviz2',
             arguments=['-d', str(share / 'rviz' / 'pantilt.rviz')]),
    ])
