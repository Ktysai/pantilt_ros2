# pantilt_ros2

Pachet pentru laborator introductiv ROS 2, pregatit pentru Humble/Jazzy.
Sintaxa Python/XML verificata; lansarea nu a fost testata intr-un mediu ROS 2.

## Instalare
Intr-un terminal cu mediul ROS 2 activat:

sudo apt update
sudo apt install python3-colcon-common-extensions ros-$ROS_DISTRO-xacro ros-$ROS_DISTRO-robot-state-publisher ros-$ROS_DISTRO-joint-state-publisher-gui ros-$ROS_DISTRO-rviz2

Extrageti folderul pantilt_ros2 in ~/ros2_ws/src/.

cd ~/ros2_ws
colcon build --symlink-install --packages-select pantilt_ros2
source install/setup.bash
ros2 launch pantilt_ros2 pantilt_ros2_launch.py

Implicit: 08_pantilt_simple.urdf, cu geometrie primitiva in loc de STL.
Cinematica originala este pastrata; forma pieselor STL nu este reprodusa exact.

## Model cu STL
Copiati baza.STL, pan_stalp.STL si tilt_stalp.STL in meshes/.
Reconstruiti pachetul, apoi:
ros2 launch pantilt_ros2 pantilt_ros2_launch.py model:=08_pantilt.urdf

In modelul original s-au schimbat doar referintele package://pantilt_ros/ in package://pantilt_ros2/.

## Activitati
1. Miscati cursoarele pan_joint si tilt_joint.
2. Intr-un alt terminal cu acelasi mediu ROS activat:
   ros2 node list
   ros2 topic list
   ros2 topic echo /joint_states
3. Identificati numele articulatiilor si valorile unghiurilor.
4. Activati TF in RViz pentru a vedea reperele.
5. Modificati o culoare in URDF-ul simplificat si reporniti lansarea.

Cursor -> /joint_states -> robot_state_publisher -> /tf -> RViz.
Pan: -3.14 ... 3.14 rad; tilt: 0 ... 3.14 rad.
Vizualizare cinematica, nu simulare dinamica sau comanda hardware.
Nu porniti un al doilea publisher pentru aceleasi articulatii simultan.
Metadatele de autor si licenta trebuie completate inainte de redistribuire publica.
