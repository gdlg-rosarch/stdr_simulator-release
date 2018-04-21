# Script generated with Bloom
pkgdesc="ROS - A simple, flexible and scalable 2D multi-robot simulator."
url='http://stdr-simulator-ros-pkg.github.io'

pkgname='ros-kinetic-stdr-simulator'
pkgver='0.3.2_1'
pkgrel=1
arch=('any')
license=('GPLv3'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-stdr-gui'
'ros-kinetic-stdr-launchers'
'ros-kinetic-stdr-msgs'
'ros-kinetic-stdr-parser'
'ros-kinetic-stdr-resources'
'ros-kinetic-stdr-robot'
'ros-kinetic-stdr-samples'
'ros-kinetic-stdr-server'
)

conflicts=()
replaces=()

_dir=stdr_simulator
source=()
md5sums=()

prepare() {
    cp -R $startdir/stdr_simulator $srcdir/stdr_simulator
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

