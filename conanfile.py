from conan import ConanFile
from conan.tools.cmake import cmake_layout


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("abseil/20230125.3")
        self.requires("fmt/10.2.1")
        self.requires("gtest/1.14.0")
        self.requires("nlohmann_json/3.11.3")
        self.requires("spdlog/1.14.1")
        self.requires("zlib/1.3.1")
        self.requires("catch2/3.6.0")
        self.requires("doctest/2.4.11")
        self.requires("eigen/3.4.0")
        self.requires("boost/1.85.0")
        self.requires("cpputest/4.0")
        self.requires("bzip2/1.0.8")
        # self.requires("boost/1.80.0")
        self.requires("protobuf/3.21.12")
        self.requires("grpc/1.54.3")
        self.requires("tensorflow-lite/2.12.0")
        self.requires("opencv/4.9.0")
        self.requires("libcurl/8.6.0")
        self.requires("gsl/2.7.1")
        self.requires("poco/1.13.3")
        self.requires("sdl/2.30.3")
        self.requires("glfw/3.4")
        self.requires("freeglut/3.4.0")
        self.requires("glm/cci.20230113")
        self.requires("flatbuffers/23.3.3")
        self.requires("cista/0.15")
        self.requires("dlib/19.24.2")
        self.requires("zstd/1.5.5")
        #self.requires("openblas/0.3.26")
    def layout(self):
        cmake_layout(self)