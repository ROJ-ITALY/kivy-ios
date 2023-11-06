# pure-python package, this can be removed when we'll support any python package
from kivy_ios.toolchain import PythonRecipe, shprint
from os.path import join
import sh
import os


class ProtobufRecipe(PythonRecipe):
    version = "3.18.3"
    url = "https://pypi.org/packages/source/p/protobuf/protobuf-{version}.tar.gz"
    depends = ["python"]

    def prebuild_arch(self, arch):
        if self.has_marker("patched"):
            return
        self.apply_patch("0001-fix-bug-attribute-list.patch")
        self.set_marker("patched")

    def install(self):
        arch = list(self.filtered_archs)[0]
        build_dir = self.get_build_dir(arch.arch)
        print("SGU build_dir: {}".format(build_dir))
        os.chdir(build_dir)
        hostpython = sh.Command(self.ctx.hostpython)
        build_env = arch.get_env()
        dest_dir = join(self.ctx.dist_dir, "root", "python3")
        print("SGU dest_dir: {}".format(dest_dir))
        build_env['PYTHONPATH'] = self.ctx.site_packages_dir
        print("SGU build_env: {}".format(build_env))

        shprint(hostpython, "setup.py", "build", _env=build_env)
        shprint(hostpython, "setup.py", "install", "--prefix", dest_dir, _env=build_env)


recipe = ProtobufRecipe()
