Name:           ros-kinetic-stdr-server
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS stdr_server package

Group:          Development/Libraries
License:        GPLv3
URL:            http://stdr-simulator-ros-pkg.github.io
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-map-server
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-stdr-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-map-server
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-stdr-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  yaml-cpp-devel

%description
Implements synchronization and coordination functionalities of STDR Simulator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jul 18 2016 Chris Zalidis <zalidis@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

