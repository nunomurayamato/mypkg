import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    Memorypublisher = launch_ros.actions.Node(
                      package='mypkg',
                      executable='Memorypublisher',
                      )

    return launch.LaunchDescription([Memorypublisher])
