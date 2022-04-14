cmake_minimum_required(VERSION 3.15)
project(repro CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

find_package(fmt REQUIRED)
find_package(zmqpp REQUIRED)

add_executable(repro src/main.cpp)
target_link_libraries(repro fmt::fmt zmqpp::zmqpp)

set_target_properties(repro PROPERTIES SUFFIX ".html" LINK_FLAGS "--emrun")
file(COPY src/index.html DESTINATION "${CMAKE_CURRENT_BINARY_DIR}")

set(CMAKE_CXX_FLAGS "-fstack-protector-all")  # <- this does something, but not enough
