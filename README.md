# ros_example_numbers
ROS Example scripts for numbers project.

## Requirements

We need a Linux distribution for mor ease on install, in this case we will use Ubuntu 18.03.

[Ubuntu install guide](http://wiki.ros.org/melodic/Installation/Ubuntu)

Only difference is that we need CATKIN python tools so in this last command we need to add at the end of it the CATKIN.

```cmd
sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential python-catkin-tools
```

## Setup

Now after the install correctly we can create a workspace for our project. Also add an empty directory called **src**

```cmd
mkdir -p awesome_project_ws/src
```

Once created navigate to the new directory and inside run the catkin tools

```cmd
catkin build
```

This will prepare the project to be executed and you will have to rebuild it everytime a new file inside your packages is created.

After this you will need to add the source to the bash you are using and there are many ways to do it one is editing your file .bashrc and adding to the end the line:

```
source path/to/awesome_project_ws/devel/setup.bash
```

Or in the Linux CLI run the command:

```cmd
source path/to/awesome_project_ws/devel/setup.bash
```

## Creating package

To create a new package you need to execute the next command adding the libraries that you will use, in this example we will add ros python library, ros c++ library and the std_msgs library to be able to work with messages on ROS.

```cmd
catkin_create_pkg awesome_pkg rospy roscpp std_msgs
```

## Running the ROS Core

Once all of this is done you can simply execute the command:

```cmd
roscore
```

This will start the environment for it to be able to run the packages with their nodes.

## Important commands

```cmd
rosrun <package_name> <node/script> #execute the node or script of the package you choose
rosnode list #list all the active nodes running
rosnode info <node_name> #check the log of the node
rostopic list #list all topics available at the moment of execution
rostopic info <name_of_topic> #check log info on topic
rostopic pub -1 </name_of_topic> std_msgs/String "data: '<new message>'" #this will add a new message to all subscribers listening to the topic
rostopic pub -r 5 </name_of_topic> std_msgs/String "data: '<new message>'" #continuosly send 5 new messages to the subscribers of the topic
```

## Note on nodes

If you are adding scripts to the nodes you need to create a new directory inside src/awesome_package/ called **scripts** in this new directory you will add python scripts for the package. Also after creating them make them executables with the chmod command:

```cmd
chmod +x my_new_script.py
```

And then rebuild the project with catkin:

```cmd
catkin build
```

In case you using c++ you will use the **src** directory inside src/awesome_package/ for the c++ scripts be able to run. Also after doing this you need to make them executables but not in the same way as python you will need to edit the file called **CMakeLists.txt** inside your package. Here you will need to add the next lines of code after the comment of c++ executable declarations:

```
## Declare a C++ executable
add_executable(node_cpp src/my_cpp_node.cpp)
target_link_libraries(node_cpp ${catkin_LIBRARIES})
```
