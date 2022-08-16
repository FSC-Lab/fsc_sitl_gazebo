<!--
 Copyright (c) 2022 hs293go
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# Personal sitl_gazebo

A repo of my own models (and launch files to run them in PX4-Gazebo simulation). Currently (at of 08/16/2022) provides

- Model of a UAV with a slung payload, with an downward facing camera to track the payload
- Camera model, inspired by the original `sitl_gazebo`'s *fpv_cam*, but with widened FOV and calibration parameters taken from `raspicam_node` (Actually TODO)
