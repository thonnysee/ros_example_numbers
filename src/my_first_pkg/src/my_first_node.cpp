#include<ros/ros.h>

int main(int argc, char **argv){
	ros::init(argc, argv, "my_first_cpp_node");
	ros::NodeHandle nh;
	ros::Rate rate(10);

	while(ros::ok){
	ROS_INFO_STREAM("Hello World");
	}
}
