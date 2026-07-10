cmake_minimum_required(VERSION 3.16)

project(QtKickstart LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)

qt_standard_project_setup()

qt_add_executable(QtKickstart
    main.cpp
)

target_link_libraries(QtKickstart
    PRIVATE Qt6::Widgets
)
