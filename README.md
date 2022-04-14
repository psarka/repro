## Build steps

```
conan install . -if=build -pr:h=emscripten.profile -pr:b=default --build=missing
source build/activate.sh
cmake -B build -S .
cmake --build build/ -- -j 4
```

## See result

```
python3 -m http.server
# navigate to build
# see Hello! in the dev tools
```