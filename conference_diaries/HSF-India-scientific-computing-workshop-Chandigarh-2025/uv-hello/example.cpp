#include <pybind11/pybind11.h>

PYBIND11_MODULE(example, m) {
 m.def("add", [](int i, int j){return i + j;}); }