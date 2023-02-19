#include <stdio.h>
#include <ros.h>
#include <std_msgs/Int16.h>

using namespace std;

class Ultrasonic{
private:
    ros::NodeHandle nh;
    std_msgs::Int16 distance;
public:
    Ultrasonic (ros::Publisher ultrasonicPub, int sensor_name, int rate){
        cout<<sensor_num<<" has been successfully initiated."<<endl;
        ros::Publisher ultrasonicPub =  nh.advertise<std_msgs::Int16>("ultrasonic_distance");
        nh.initNode();
        ros::Rate loop_rate(rate);
    }

    Ultrasonic::send_data(ros::Publisher distance){
        ultrasonicPub.publish(distance);
    }
}
