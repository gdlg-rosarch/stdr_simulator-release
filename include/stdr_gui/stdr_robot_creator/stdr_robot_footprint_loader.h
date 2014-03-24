/******************************************************************************
   STDR Simulator - Simple Two DImensional Robot Simulator
   Copyright (C) 2013 STDR Simulator
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software Foundation,
   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
   
   Authors : 
   * Manos Tsardoulias, etsardou@gmail.com
   * Aris Thallas, aris.thallas@gmail.com
   * Chris Zalidis, zalidis@gmail.com 
******************************************************************************/

#ifndef STDR_ROBOT_FOOTPRINT_LOADER
#define STDR_ROBOT_FOOTPRINT_LOADER

#include "ui_robotFootprint.h"
#include "stdr_gui/stdr_tools.h"

/**
@namespace stdr_gui
@brief The main namespace for STDR GUI
**/ 
namespace stdr_gui
{
  /**
  @class CRobotPropertiesLoader
  @brief Implements the low level functionalities of the robot footprint widget. Inherits form QWidget and Ui_RobotFootprint (auto created from ui file)
  **/ 
  class CRobotFootprintLoader : 
    public QWidget, 
    public Ui_RobotFootprint
  {
    //------------------------------------------------------------------------//
    private:
      //!< Number of input arguments
      int   argc_;
      //!< Input arguments
      char**  argv_;
    //------------------------------------------------------------------------//
    public:
      /**
      @brief Default contructor
      @param argc [int] Number of input arguments
      @param argv [char**] Input arguments
      @return void
      **/
      CRobotFootprintLoader(int argc, char **argv);
  };  
}

#endif
