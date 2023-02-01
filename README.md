# SHERPA-simulation

## Content of this repository

Here you find the code to run the SHERPA Source Receptor Relationship, for simulating the impact on air quality of emission reduction scenarios, in EU regions and cities.

The code is provided to show how SHERPA Graphical User Interface works behind the scene.

On top of this, there is also a Jupyter notebook ('how_to_run_module1.ipynb') explaining how to use the 'scenario analysis' module directly in python (explaining how to set-up a python environment, and then how to run the SHERPA scenario analysis).

## What is SHERPA
SHERPA (Screening for High Emission Reduction Potential on Air) is tool, which allows for a rapid exploration of potential air quality improvements resulting from national/regional/local emission reduction measures. The tool has been developed with the aim of supporting national, regional and local authorities in the design and assessment of their air quality plans.The tool is based on the relationships between emissions and concentration levels, and can be used to answer the following type of questions:

- What is the potential for local action in my domain?
- What are the priority activity, sectors and pollutants on which to take action and,
- What is the optimal dimension that my policy action domain (city, region…) should have to be efficient?"

The SHERPA tool is distributed with EU-wide data on emissions and source-receptor models (spatial resolution of roughly 6x6 km2), so that it is very easy to start working on any region/local domain in Europe.

More specifically, SHERPA logical pathway is implemented through the following steps:

- Source allocation: to understand how the air quality in a given area is influenced by different sources;
- Governance: to analyze how one should coordinate with the surrounding regions to optimally improve air quality;
- Scenario analysis: to simulate the impact on air quality of a specific emission reduction scenario (defined also through the previous two steps)

## Current existing modules
The python code in this repository is used in the SHERPA interface, available at https://aqm.jrc.ec.europa.eu/Section/Sherpa/Background.
The SHERPA interface uses emissions at 2015 (CAMSv4.2 emissions), EMEP air quality model to derive the source receptor relationships, and meteorology at 2015. The spatial resolution in the SHERPA interface is 0.1x0.1 degrees.

In particular, the SHERPA interface uses the code of the following modules:

-  Module 1 (scenario assessment): to simulate the impact on air quality of a specific emission reduction scenario
-  Module 3 (Source allocation): to understand how the air quality in a given area is influenced by different sources. This module runs in two modes: precursor-based source allocation, and sector-based one. Note that this module works running module 4 and module 1, in sequence.
-  Module 4: (Potency): this module computes potencies, and it is not directly launched by the user. On the contrary, it is used by Module 3.
-  Module 6 (Governance): to analyze how one should coordinate with the surrounding regions to optimally improve air quality;
-  Module 8 (health impact): to evaluate PM2.5 health-related impact, when running module 1
-  Module 9 (aggregation): to aggregate emissions and concentrations, at NUTS or FUAs level.
-  Module 10 (cost module): to compute costs of end-of-pipe technologies required to reach a given emission reduction target.

This python code can also be used outside the graphical user interface. For this, we provide a different SHERPA implementation than the one in the SHERPA interface. 
In particular, it is a more updated SHERPA implementation, based on emissions from CAMSv4.2 + condensables at 2015, with an improved spatial resoltuion (at 0.1x0.05). 
The python code as such can be used directly only with these two modules:

-  Module 1 (scenario assessment): to simulate the impact on air quality of a specific emission reduction scenario
-  Module 3 (Source allocation): to understand how the air quality in a given area is influenced by different sources. 

The data contained in this repository (in the input directory) refers to this implementation, at 0.1x0.05 resolution.

## STILL UNDER DEVELOPMENT: Preparing results for the downscaling module
In this branch I adapt the 0.1x0.1 deg resolutionSRR to work with a new downscaling module. This module requires a different structure of emissions and concentration files.

For emissions:

- a unique file for all air quality indexes, containing all precursors and (for PM) PPM2.5, PPMco, PPM10
- same content should be available for basecase (initial) emissions and delta (resulting from the SRR simulation) emissions 
- the code will work with 12 GNFR sectors
- note that PPM10 = PPM2.5 + PMco

For concentrations

- you also need basecase files for PPM2.5 and PPM10 concentrations
- the PPM2.5 basecase is directly extracted from the EMEP results, the PPM10 is on the contrary computed as the sum of PPM2.5 + PPMco
- not that the SRR for PM downscaling will be run twice: once to simulate total PM2.5 (or PM10) and once to simulate the PPM2.5 (or PPM10) reductions. This second run is performed only reducing PPM2.5 or PPM10 emissions.

Now the code uses different tagas for emissions definitions (PPM25 or PPM10, depending on emissions to be reduced). 
Also now a new variable has been added when running module1 (downscale_request). 
If the variable downscale_request=0, a run with normal reductions is done. If downscale_request=1 then a run is done only reducing PPM emissions. 
This second run creates concentrations change for the PPM component. Finally, now filename are automatically created, depending on the concentrations to be modelled.
But also depending on the downscale_request. When downscale_request=1 indeed a 'primary' tag is added to the module1 output file.

# Publications

- Bessagnet B, Pisoni E, Thunis P, Mascherpa A. 
Design and implementation of a new module to evaluate the cost of air pollutant abatement measures. 
(2022) Journal of Environmental Management;317:115486. 
https://pubmed.ncbi.nlm.nih.gov/35751296/ 

- Thunis, P., Clappier, A., De Meij, A., Pisoni, E., Bessagnet, B., & Tarrason, L.
Why is the city's responsibility for its air pollution often underestimated? A focus on PM2.5. 
(2021) Atmospheric Chemistry and Physics, 21(24), 18195-18212. 
https://acp.copernicus.org/articles/21/18195/2021/

- Degraeuwe, B., Pisoni, E., Thunis, P.
Prioritising the sources of pollution in European cities: Do air quality modelling applications provide consistent responses?
(2020) Geoscientific Model Development, 13 (11), pp. 5725-5736. 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85096928556&doi=10.5194%2fgmd-13-5725-2020&partnerID=40&md5=d4cb7a3413af75830b782af529db3727

- Sartini, L., Antonelli, M., Pisoni, E., Thunis, P.
From emissions to source allocation: Synergies and trade-offs between top-down and bottom-up information
(2020) Atmospheric Environment: X, 7, art. no. 100088, . 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85090038106&doi=10.1016%2fj.aeaoa.2020.100088&partnerID=40&md5=c41e93233b2f100e7dcda69e064a90ea

- Belis, C.A., Pisoni, E., Degraeuwe, B., Peduzzi, E., Thunis, P., Monforti-Ferrario, F., Guizzardi, D.
Urban pollution in the Danube and Western Balkans regions: The impact of major PM2.5 sources
(2019) Environment International, 133, art. no. 105158, . 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85073224266&doi=10.1016%2fj.envint.2019.105158&partnerID=40&md5=81f54f1ee6fc53184059b655797f3ffa

- Pisoni, E., Thunis, P., Clappier, A.
Application of the SHERPA source-receptor relationships, based on the EMEP MSC-W model, for the assessment of air quality policy scenarios
(2019) Atmospheric Environment: X, 4, art. no. 100047, . 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85072582264&doi=10.1016%2fj.aeaoa.2019.100047&partnerID=40&md5=34146ae8e90b2bc98ed4babfea0991a3

- Peduzzi, E., Pisoni, E., Clappier, A., Thunis, P.
Multi-level policies for air quality: implications of national and sub-national emission reductions on population exposure
(2018) Air Quality, Atmosphere and Health, 11 (9), pp. 1121-1135. 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85053388835&doi=10.1007%2fs11869-018-0613-1&partnerID=40&md5=ec09ca92720060078aac98a3408f85a5

- Monforti-Ferrario, F., Kona, A., Peduzzi, E., Pernigotti, D., Pisoni, E.
The impact on air quality of energy saving measures in the major cities signatories of the Covenant of Mayors initiative
(2018) Environment International, 118, pp. 222-234. 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85048115990&doi=10.1016%2fj.envint.2018.06.001&partnerID=40&md5=39ee982bcf359ed03505d2e3d33ec995

- Pisoni, E., Albrecht, D., Mara, T.A., Rosati, R., Tarantola, S., Thunis, P.
Application of uncertainty and sensitivity analysis to the air quality SHERPA modelling tool
(2018) Atmospheric Environment, 183, pp. 84-93. 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85045688029&doi=10.1016%2fj.atmosenv.2018.04.006&partnerID=40&md5=9432074fa33ac072995b6076f64cce3c

- Thunis, P.
On the validity of the incremental approach to estimate the impact of cities on air quality
(2018) Atmospheric Environment, 173, pp. 210-222. 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-85034083743&doi=10.1016%2fj.atmosenv.2017.11.012&partnerID=40&md5=f877863da1d86c9bb5d844870ce349aa

- Thunis, P., Degraeuwe, B., Pisoni, E., Ferrari, F., Clappier, A.
On the design and assessment of regional air quality plans: The SHERPA approach
(2016) Journal of Environmental Management, 183, pp. 952-958. 
https://www.scopus.com/inward/record.uri?eid=2-s2.0-84994012263&doi=10.1016%2fj.jenvman.2016.09.049&partnerID=40&md5=1561546680304fcf57e914bdf441d452
