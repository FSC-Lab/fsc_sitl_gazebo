cmake_minimum_required(VERSION 3.0.2)
project(personal_sitl_gazebo)

find_package(catkin REQUIRED)

catkin_package()

include_directories()

catkin_install_python(PROGRAMS scripts/ground_truth_relative DESTINATION
                      ${CATKIN_PACKAGE_BIN_DESTINATION})
