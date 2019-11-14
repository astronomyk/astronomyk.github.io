# Using spectrophotometric techniques to determine in-situ soil carbon abundances 

## Keywords
Climate change, blockchain, regenerative agriculture, internet of things, infrared spectroscopy, swarm data transfer


## Main ideas

1. Large growth in corporate and consumer level demand for verifiable CO2 offsets and removal certificates  
2. [nori.com](https://nori.com/) and [puro.earth](https://puro.earth/) trade carbon removal certificates transparently 
   on the blockchain
3. Regenerative farming practices sequester carbon from the atmosphere in the soil
4. Farmers can earn money **IF** they can verify an increase in soil organic carbon
5. Near infrared spectroscopy is a robust method for verifying soil composition (Nayak+ 2019)
6. Visual and infrared LEDs enable narrow-band low resolution (R~10) reflectance spectroscopy (spectro-photometry) over
   a wavelength range of [350, 1700]nm 
7. Internet of things enabled devices (arduino, esp8266) allow compact low energy wireless communications
8. Swarm communication protocols enable rapid data transfer through spatially distributed hub-less systems   
9. Astronomers have decades of experience with population model fitting to spectro-photometric data sets

By combining the knowledge bases of astronomers, soil scientists, and farmers, with modern advances in cheap 
electronics, infrared LEDs, and the internet of things (IoT), it should be possible for swarms of in-situ sensors
to transfer soil composition data autonomously and in real time, thereby enabling transparent and continuous monitoring 
and verification of the soil composition (i.e. carbon content) across farmland.

A cheap and easily deployable sensor for continuous in-situ soil carbon measurements may be the final piece needed for 
farmers to profit from the free-market based mechanisms (i.e. carbon removal certificates), thus providing the
financial incentives to encourage the widespread adoption of (urgently needed) regenerative agricultural practices.  

## Methods

1. Build a prototype sensor using the ESP8266 board and the 55 LEDs covering the 350-1700nm range from Ushio-Optics
2. Build a library of soil composition and spectral profiles using laboratory NIR and mass spectrographs for a range of
   soil conditions (if not already available).
3. Compare soil reflectance data from the sensor to the spectral library
4. Deploy sensors on several test fields/farms to collect real data for a year
5. Periodically make mass-spectroscopy measurements of soil samples for comparison with the photometric sensor data
6. Develop a model for translating sensor data to soil composition for a list of the most interesting / useful compounds 
7. If this works, apply for more funding and scale up the project.

## Links

### Technologies
* [Nori](https://nori.com/) - Blockchain based carbon removal market (USA)
* [Puro](https://puro.earth/) - Carbon removal market (EU, Finland)
* [SCiO](https://www.consumerphysics.com/business/technology/#) - miniature handheld 12-channel NIR spectrophotometer
* [Ushio OptoSemi](https://www.ushio-optosemi.com/en/products/led/std/standard/mold_type.html) - list of currently 
  available visual and NIR LEDs
* [ESP8266](https://en.wikipedia.org/wiki/ESP8266) - Wifi/Bluetooth enabled micro Arduino board

### Literature
* [Review: Carbon Sequestration Potential on Agricultural Lands - Kane+15](https://sustainableagriculture.net/wp-content/uploads/2015/12/Soil_C_review_Kane_Dec_4-final-v4.pdf)  
  This project would address points 4, 5, and 6 in the research agenda section of this review.

   
* [Review: Soil carbon estimation techniques - Nayak+19](https://www.sciencedirect.com/science/article/pii/S0048969719306138)
* [Stable isotope amount ratio analysis by using high-resolution continuum source graphite furnace molecular absorption 
spectrometry](https://www.bam.de/Content/EN/News-announcements/2017/2017-11-14-bam-isas-and-salsa-research-on-isotopes.html)


## Funding possibilities
[FWF 1000 ideas application](fwf_1000_ideas.rst)  - Deadline 15.01.2020 @ 14:00 CET


## Contacts

Uni Wien
* [Kieran Leschinski](kieran.leschinski@univie.ac.at)
* [Anastassiya Tchaikovsky](anastassiya.tchaikovsky@univie.ac.at)

BOKU (Tulln)
* [Univ.Prof. Dipl.-Ing. Dr.nat.techn. Walter Wenzel](walter.wenzel@boku.ac.at)
* [Priv.-Doz. Dr. Markus Puschenreiter](markus.puschenreiter@boku.ac.at)
 