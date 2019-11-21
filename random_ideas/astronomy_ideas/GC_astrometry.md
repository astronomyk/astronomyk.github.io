# The IMF of YMCs in the GC using the ELT and astrometry

The initial mass function of young massive clusters in the galactic centre
using the extremely large telescope and astronometry

![](https://scx2.b-cdn.net/gfx/news/hires/2013/theoriginoft.jpg) 
[](https://apod.nasa.gov/apod/image/1601/30dor_hubble_3939.jpg)

## Goals: 
1. To determine the lowest mass stars that will be observable in young clusters
   in the galactic center for a given star density.
2. To determine what percentage of cluster memberships based on proper motions 
   are true or false positives and what percentage are false negatives. (i.e. 
   how many should belong to the cluster but don't, and how many don't belong to 
   the cluster, but are included)
3. To combine these two results to determine the lowest reliably-observable mass
   for a star, which definitely has cluster membership. Hence where the
   reliability limit will be for future IMF studies in the galactic centre.
 
## Background

### IMF: Initial Mass Function

How many stars are formed of which mass during a star formation event. 
Important for all aspects of astronomy, from aliens to cosmology 

Literature: 
[Kroupa 2001](https://arxiv.org/abs/astro-ph/0102155), 
[Chabrier 2003](https://arxiv.org/abs/astro-ph/0304382)

### YMC: Young Massive Clusters

Tighty grouped clusters of stars, generally containing >10000 members. 
Young means all original members are still around, i.e. non have gone supernova.
Massive means the IMF will be well sampled in all mass regimes, i.e. M>10Msun and M<0.1Msun
These facts combine to give us a good picture of the end product of a star formation event

Examples: Westerlund 1, R136, Arches cluster, Quintuplet cluster, Trumpler 14

Literature: 
[Portegeis-Zwart+ 2010](https://arxiv.org/abs/1002.1961)

### GC: Galactic Centre

Current knowledge of the IMF is restricted to the solar neighbourhood where
the environment (metalicity) is more or less constant. 
The galactic centre has a very different environment
- Higher gravitational potential
- Lower metalicity
- Higher external radiation field
- Higher density of stars
Perfect for studying the effect of the environment on the IMF

Literature: 
[Genzel 2010](https://arxiv.org/abs/1006.0064)


### ELT: The Extremely Large Telescope

The first next generation 40m class telescope.
It will have the resolution and sensitivity needed to study the motions of 
individual stars in the galactic centre.

Literature:
[ELT wikipedia](https://de.wikipedia.org/wiki/Extremely_Large_Telescope),
[ESO website](https://www.eso.org/public/austria/teles-instr/elt/),
[Davies+ 2018 (MICADO paper )](https://arxiv.org/pdf/1807.10003.pdf),
[MICADO simulation tool in python](https://simcado.readthedocs.io/en/latest/)

### Astrometry: Detectable movements of stars over time

The motion of stars over time. This allows us to calculate trajectories and 
hence differentiate the members of bound groups from the background and 
foreground stars.
The line-of-sight volume towards the galactic centre is very densely populated.

Literature:
[Pott+ 2018](https://arxiv.org/ftp/arxiv/papers/1807/1807.07402.pdf),
[Masari+ 2016](https://arxiv.org/pdf/1607.04412.pdf)
  
  
## Tasks

1. Make a galactic centre cluster
   - Using Galpy create a model of a massive cluster in a galactic centre potential. 
   - Evolve this cluster over time to see what happens
   - Adjust the mass and velocity dispersion of the cluster to fit the observations
   - "Observe" this cluster with the ELT using SimCADO
   - **Find the lowest recoverable mass for a given set of observing conditions**

2. Track cluster members
   - Generate time snapshots for the positions of the stars as it evolves (dt~3 months)
   - Observe each snapshot
   - Extract the stars and determine relative position of the stars
   - Determine the percentage of stars that have detectable motions in each snapshot
   - **Find the time (snapshot) where >90% of the stars have detectable motions with respect to t=0**
   
3. Make a field of fore-/background stars with random motions (direction and velocity)
   - Generate a population of stars using a present-day mass function for the galactic centre 
   - Combine the field stars with the cluster 
   - Evolve with time
   - Observe each snapshot
   - Extract the star properties (luminosity, position, velocity)
   - Determine cluster members. Compare this list to the input list
   - **Determine percentage of false positives, false negatives based on velocity**
   
4. Get IMF for cluster members
   - Isolate only the cluster members
   - **Find mass bins where 90% of input stars have cluster membership**
   - **Find mass bins where 90% of input stars are detected**

