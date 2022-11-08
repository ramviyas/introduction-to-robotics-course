After downloading this package. Compile your workspace.

Install dependencies: sudo apt-get install ros-noetic-turtlebot3-description ros-noetic-turtlebot3-gazebo

Then, add the following lines in your ~/.bashrc file so that GAZEBO will load these models correctly.
Replace "your_workspace" with the name of your workspace and make sure the full path of the "maze_simulation" package is correct.

export GAZEBO_PLUGIN_PATH=path_to_your_workspace/src/maze_simulation/lib:${GAZEBO_PLUGIN_PATH}

export GAZEBO_MODEL_PATH=path_to_your_workspace/src/maze_simulation/models:${GAZEBO_MODEL_PATH}

export GAZEBO_RESOURCE_PATH=path_to_your_workspace/src/maze_simulation/models:${GAZEBO_RESOURCE_PATH}



Then, resource your bashrc file (or open a new terminal)

export TURTLEBOT3_MODEL=burger

roslaunch maze_simulation maze_world_1.launch (or try out the other maze_world_2.launch)


