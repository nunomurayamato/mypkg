import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    memorypublisher = launch_ros.actions.Node(
            package='mypkg',
            executable='memorypublisher',
            )

    return launch.LaunchDescription([memorypublisher])
