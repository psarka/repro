conan install . -if=build -pr:h=emscripten.profile -pr:b=default --build=missing
source build/activate.sh
cmake -B build -S .
cmake --build build/ --verbose -- -j 4
