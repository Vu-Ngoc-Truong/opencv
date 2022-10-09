cmake_minimum_required(VERSION 3.0.2)
project(detect_marker_project)
find_package(OpenCV REQUIRED)

# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(detect_marker src/detect_marker.cpp)
target_link_libraries(detect_marker ${OpenCV_LIBS})