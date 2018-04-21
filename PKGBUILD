# Script generated with Bloom
pkgdesc="ROS - Implements synchronization and coordination functionalities of STDR Simulator."
url='http://stdr-simulator-ros-pkg.github.io'

pkgname='ros-kinetic-stdr-server'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('GPLv3'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-catkin'
'ros-kinetic-map-server'
'ros-kinetic-nav-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-stdr-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
'yaml-cpp'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-map-server'
'ros-kinetic-nav-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-roscpp'
'ros-kinetic-stdr-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=stdr_server
source=()
md5sums=()

prepare() {
    cp -R $startdir/stdr_server $srcdir/stdr_server
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

