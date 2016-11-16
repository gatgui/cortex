import os
import sys
import platform

# set these variables
arnold_dir = ""
depn_dir = ""

for arg in sys.argv[1:]:
   if arg.startswith("DEPS_DIR="):
      tmp = arg[len("DEPS_DIR="):]
      if os.path.isdir(tmp):
         depn_dir = tmp
   elif arg.startswith("ARNOLD_DIR="):
      tmp = arg[len("ARNOLD_DIR="):]
      if os.path.isdir(tmp):
         arnold_dir = tmp

if platform.system() == "Linux":
    # Linux specific setup
    pass
else:
    # OSX specific setup (or windows?)
    pass

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

