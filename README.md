# SpaceAppsChallenge2015
Visualization of the Asteroid Skies

## Project

H&#333;k&#363;lele Hula

H&#333;k&#363;lele means "shooting star" in Hawaiian.  Our goal is
to produce a visualization of the asteroid impact hazard, emphasizing
the long-term threat over the next 100 years.


## Description

Like the Hula, a traditional Hawaiian dance narrating the interaction between the native Hawaiians and the Sea, our project aims at providing new ways to tell the story between asteroids (H&#333;k&#363;lele) and the Earth.

JPL maintains a current list of the most hazardous near-Earth
asteroids NEAs at its [Risk Page]:(http://neo.jpl.nasa.gov/risks/).
Instead of the standard approach of [visualizing the orbits](http://upload.wikimedia.org/wikipedia/commons/f/f6/Potentially_Hazardous_Asteroids_2013.png) of these
asteroids using a program such as [Celestia](ps1neos.png) we wanted
to produce a visualization of the immediate threat from all Risk
Page asteroids and show a snapshot of the 100-year risk outlook.

Our visualizations are the Impact Globe and the 100-Year Rose Plot.
The Impact Globe summarizes total impact threat over a window of
several years.  We tabulated the impact predictions from the JPL
risk page for all objects. Each "needle" on the Impact Globe
corresponds to a single asteroid's potential impact within a time
window.  A needle is given a color code according to the energy of
the potential impact (red is catastrophic, blue only a "light
scare"), and the length of the needle indicates the likelihood of an
impact.  The locations of the needles are not meaningful -- they are distributed from all directions regardless of true direction of impact. 

The Rose Plot shows the distance of a hazardous asteroid from Earth
over the next 100 years, showing the periodic close approaches and
potential impacts.  For all the Risk Page objects, we obtained
orbital elements from the <a href="http://www.minorplanetcenter.net">IAU
Minor Planet Center</a> and computed positions for all the asteroids
every day for 100 years into the future.  The Rose Plot shows the
distance from Earth for each asteroid over the next 100 years. The 
dashed lines show the Earth-Moon distance and Geosync satellite
altitude. Asteroids whose rose plot extends inside these dashed
circles have approaches closer than the moon and geosynchronous
satellite altitude, respectively.

The 2015 SpaceApps Challenge coincided with the University of
Hawaii's 2015 Open House, so we were able to solicit the input
of dozens of attendees who stopped by the 2015 SpaceApps 
Challenge room at the Open House.

## The Data

The data are the PHAs from [JPL Risk Page](http://neo.jpl.nasa.gov/risks/) and the [IAU Minor Planet Center](http://www.minorplanetcenter.net/).  These objects come closer than 0.05 astronomical units (AU) from Earth and about 140 meters or larger in diameter. We have extracted: the date, the probability of impact, the distance to the Earth and the Palermo scale that encodes the dangerosity of the asteroid and is related to the energy of the potential impact.

* Impact Globe

 - Complete list of Risk Page potential impacts
  - CSV
  - JSON

* Rose Plots
 - List of orbital elements for Risk page asteroids ([DES](http://ifa.hawaii.edu/users/jedicke/MOPS/docs/PSDC-530-004-02.DataExchangeStandard.pdf) format)
 - [OpenOrb](https://code.google.com/p/oorb/) orbit and ephemeris tool.  Extract the MJD/UTC1 and Delta columns from the output.
  

## Credits

* Google Chrome Experiments WebGL Globe

* JPL Risk Page

* IAU Minor Planet Center, orbital elements for JPL Risk Page objects

* Institute for Astronomy Open House, April 12, 2015
 - Phyllis Podolske
 - Allan Stone
 - Sierra Beaton
 - The Baldus & Lawrence 'Ohana
 - Connor and Debbie Frey

## Team Members

* Melody Wolk, Institute for Astronomy, University of Hawaii
* Istvan Svapudi, Institute for Astronomy, University of Hawaii
* Wu Po Feng, Institute for Astronomy, University of Hawaii
* Larry Denneau, Institute for Astronomy, University of Hawaii
* Curt Dodds, Institute for Astronomy, University of Hawaii
* Andrei Sherstyuk, Institute for Astronomy, University of Hawaii
* Robert Jedicke, Institute for Astronomy, University of Hawaii
* Serge Chastel, Institute for Astronomy, University of Hawaii
