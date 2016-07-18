Name:           ros-jade-stdr-server
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS stdr_server package

Group:          Development/Libraries
License:        GPLv3
URL:            http://stdr-simulator-ros-pkg.github.io
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-map-server
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-nodelet
Requires:       ros-jade-roscpp
Requires:       ros-jade-stdr-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-visualization-msgs
Requires:       yaml-cpp-devel
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-map-server
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-stdr-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-visualization-msgs
BuildRequires:  yaml-cpp-devel

%description
Implements synchronization and coordination functionalities of STDR Simulator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Jul 18 2016 Chris Zalidis <zalidis@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Chris Zalidis <zalidis@gmail.com> - 0.3.0-0
- Autogenerated by Bloom

