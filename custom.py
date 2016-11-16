import os
import sys
import platform
import subprocess

# set these variables
arnold_dir = ""
arnold_dir_changed = False
depn_dir = ""
depn_dir_changed = False

try:
   with open("custom.cache", "r") as f:
      for l in f.readlines():
         spl = map(lambda x: x.strip(), l.split("="))
         if len(spl) == 2:
            if spl[0] == "DEPS_DIR" and os.path.isdir(spl[1]):
               depn_dir = spl[1]
            elif spl[0] == "ARNOLD_DIR" and os.path.isdir(spl[1]):
               arnold_dir = spl[1]
except:
   pass

for arg in sys.argv[1:]:
   if arg.startswith("DEPS_DIR="):
      tmp = arg[len("DEPS_DIR="):]
      if os.path.isdir(tmp):
         depn_dir = tmp
         depn_dir_changed = True
   elif arg.startswith("ARNOLD_DIR="):
      tmp = arg[len("ARNOLD_DIR="):]
      if os.path.isdir(tmp):
         arnold_dir = tmp
         arnold_dir_changed = True

if depn_dir_changed or arnold_dir_changed:
   with open("custom.cache", "w") as f:
      f.write("DEPS_DIR=%s\n" % depn_dir)
      f.write("ARNOLD_DIR=%s\n" % arnold_dir)
      f.write("\n")

print("Using DEPS_DIR=%s" % depn_dir)
print("Using ARNOLD_DIR=%s" % arnold_dir)

if platform.system() == "Darwin":
    # OSX specific setup
    CXXFLAGS = ["-Wno-unused-local-typedefs"]

# depn dirs
dep_lib = depn_dir + "/lib"
dep_include = depn_dir + "/include"

# include path
TBB_INCLUDE_PATH = dep_include
BOOST_INCLUDE_PATH = dep_include
OPENEXR_INCLUDE_PATH = dep_include
ILMBASE_INCLUDE_PATH = dep_include
JPEG_INCLUDE_PATH = dep_include
PNG_INCLUDE_PATH = dep_include
TIFF_INCLUDE_PATH = dep_include
FREETYPE_INCLUDE_PATH = dep_include + "/freetype2"
OSL_INCLUDE_PATH = dep_include
OIIO_INCLUDE_PATH = dep_include
GLEW_INCLUDE_PATH = dep_include + "/GL"
ALEMBIC_INCLUDE_PATH = dep_include
HDF5_INCLUDE_PATH = dep_include
APPLESEED_INCLUDE_PATH = depn_dir + "/appleseed/include"

# lib path
TBB_LIB_PATH = dep_lib
BOOST_LIB_PATH = dep_lib
OPENEXR_LIB_PATH = dep_lib
ILMBASE_LIB_PATH = dep_lib
JPEG_LIB_PATH = dep_lib
PNG_LIB_PATH = dep_lib
TIFF_LIB_PATH = dep_lib
FREETYPE_LIB_PATH = dep_lib
OSL_LIB_PATH = dep_lib
OIIO_LIB_PATH = dep_lib
GLEW_LIB_PATH = dep_lib
ALEMBIC_LIB_PATH = dep_lib
HDF5_LIB_PATH = dep_lib
APPLESEED_LIB_PATH = depn_dir + "/appleseed/lib"

# suffix
TBB_LIB_SUFFIX = ""
BOOST_LIB_SUFFIX = ""
OPENEXR_LIB_SUFFIX = ""
PNG_LIB_SUFFIX = ""
GLEW_LIB_SUFFIX = ""
ALEMBIC_LIB_SUFFIX = ""
HDF5_LIB_SUFFIX = ""

# arnold
ARNOLD_ROOT = arnold_dir

# with gl
WITH_GL = True

# build dir
INSTALL_PREFIX = os.path.abspath("dist")
BUILD_CACHEDIR = os.path.abspath("build")

cwd = os.getcwd()
gcc_atomic = "%s/include/boost/atomic/detail/gcc-atomic.hpp" % depn_dir
patch = "%s/gcc-atomic.patch" % cwd
patch_cmd = "patch -p1 < %s" % patch

os.chdir(os.path.dirname(gcc_atomic))
p = subprocess.Popen(patch_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
out, _ = p.communicate()
if p.returncode == 0:
   print("=== Patching gcc-atomic.hpp ===")
   print(out)
os.chdir(cwd)
