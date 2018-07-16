---
layout: post
title: Interfacing the Illustris galaxies with SimCADO
---

Date 

Contributors: Sophie Abrahams, Kieran Leschinski

The [Illustris] cosmological simulation suite has a large database of the galaxies
that were produced and includes snapshots of these objects through out the 
history of the simulated universe. The mock images that they have are only for 
the current generation of telescopes (I think). However in preparation for the
next generation of 40m telescopes it would be interesting to see how many of
these galaxies will be observable, and indeed if there is a bias towards
observations of galaxies with certain parameters. 

Hence I would like to built a pipeline which links the [Illustris API] with 
SimCADO in order to generate mock observations that should be possible with 
MICADO on the ELT.

[Illustris]: http://www.illustris-project.org/
[Illustris API]: http://www.illustris-project.org/data/docs/api/
