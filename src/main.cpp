#include <fmt/core.h>
#include <zmqpp/zmqpp.hpp>

int main(int, char **) {
    fmt::print("Hello!\n");
    zmqpp::context context;  // Comment to compile successfully
}

