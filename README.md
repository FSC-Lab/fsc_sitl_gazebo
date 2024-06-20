# Personal sitl_gazebo

A repo of our own models (and launch files to run them in PX4-Gazebo simulation). Currently provides

- Model of a UAV that also broadcasts ground truth data
- Model of a UAV with a slung payload, with an downward facing camera to track the payload
- Camera model, inspired by the original `sitl_gazebo`'s *fpv_cam*, but with widened FOV and calibration parameters taken from `raspicam_node` (Actually TODO)

## Building this project

Clone this project into your workspace and run

``` bash
catkin build
```

No actual compilation takes place, and catkin merely loops this project into the ROS project registry with appropriate copying/linking. 

## Using this project

We recommend you use our project's `custom_posix_sitl.launch` file, which is a very thin wrapper over PX4's `mavros_posix_sitl.launch`.
Except it points the `GAZEBO_MODEL_PATH` environment variable to the `models` directory in this project

For example

``` bash
roslaunch fsc_sitl_gazebo custom_posix_sitl.launch custom_model:=iris_with_ground_truth
```
