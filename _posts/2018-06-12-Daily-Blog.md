---
layout: post
title: Daily Blog
category: dev
date: 2018.06.21
---

This little blog is to help me track how things are going with the various
projects that I have on the go. Each day I'll try to add one or two lines.


2018.07.10
---
So this didn't take off. Ohwell.


2018.06.26
---
* Presented SimCADO documentation, progress with SpecCADO, SCAO FV PSFs, 
and roadmap for SimCADO until FDR, at the the MICADO CM#11


2018.06.25
---
Spent the day attacking the radiometry of SimMETIS with Leo. We have the 
background looking good. We removed a couple of redundant keywords, but at the
end of the day we couldn't find any issues with the radiometry.


2018.06.22
---
* Meeting with Werner about what has been done in the last 3 months and what the 
roadmap for the next year should be.
* Wrote the beginnings of two new PSF classes which only pull in PSFs when 
needed. This avoids loading and resamping 150 MB constantly in memory.



2018.06.20
---
* 2 hour group meeting discussing Loop 1 and whether all the major dust clouds
that we see are all part of the same shell. Gaia should help us to get the 
distances to these clouds. See the work by Andre & Andre.
* 4 hour meeting with Oliver to discuss everything related to SimCADO. Namely:
    * A plan for the PDR Documentation
    * How to add Speccado
    * Setting a freeze on the current version of the imaging mode
    * What to add for the 1.0 release
    * Concept of downloadable instrument packages for the different modes
    * How to incorporate an instrument reference database


2018.06.18
---
* 3 hour coding session with NL to try to get SimMETIS N-band imager running.
    * We found that there are some issues with the Sirius spectrum.
    * The issue with the mirror emission is still unresolved.

    
2018.06.14
---
* Started thinking about the field varying SCAO PSF problem. Created a PSF cube 
for each of the broadband filters with a new format. For each wavelength the 
cube contains a table relating position on the FPA to an extension containing 
the relevant PSF image.

    
2018.06.13
---
* Set up the Jekyll now as a way of keeping track of what I do from day to day.
    
    
    
    
