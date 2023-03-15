# Moja Global's Land Sector Dataset Description

In most files, there is a field called <a id ='geometry'><b>geometry </b></a>. This field is vector geometry; the spatial components of geographic features with discrete boundaries.

**DECLARATION: Any field already described in a current section is ignored in the subsequent sections to avoid field description redundancy.**

There are five main categories of the Land Sector Dataset; which are:

1. [Administrative](https://datasets.mojaglobal.workers.dev/0:/Administrative/)
2. [Biodiversity, AgroClimatic, and Ecological Zones](https://datasets.mojaglobal.workers.dev/0:/Bioclimatic&EcologicalZones/)
3. [Climate](https://datasets.mojaglobal.workers.dev/0:/Climate/)
4. [Land Cover](https://datasets.mojaglobal.workers.dev/0:/LandCover/)
5. [Soil](https://datasets.mojaglobal.workers.dev/0:/Soil/)

# 1. Administritive

The administrative directory has three subdirectories as explained below.

## 1.1 Boundaries

In this directory, files are containing political boundaries. These documents are the dividing lines between countries, states, provinces, counties, and cities. People create these lines, usually called boundaries, to separate areas under the jurisdiction of different groups. Sometimes, political boundaries follow boundaries, but most of the time you can’t see them.

The boundaries are in two levels.

### 1.1.1 Boundaries Level 2

The directories with Level 2 contain boundaries at the country level including the Global Ecological Zone boundaries for each country as well as the World Soil Resources' boundaries:

- The general notation of files is **COUNTRY_AL2_country.json**( implying the country code followed by Administrative Level 2, followed by the country name).

The files are made up of twelve (12) important fields: as explained below:

1.  <b><a id ='country'>country:</b> refers to the name of the country </a>
2.  **ISO3166_2:** (ISO standard codes of administrative divisions and subdivisions) In other words - Administrative Divisions of Countries
3.  **name:** name of the level 2 country
4.  **enname:** English name of the country
5.  **locname:** Local name of the country
6.  **offname:** official name
7.  **boundary:** type of boundary
8.  **wikidata:** Wikidata code
9.  **wikimedia:** Wikimedia name
10. **timestamp** the time the data was collected
11. **adnminlevel:** administrative level 2
12. **geometry:**

- The notation of files with the general form- **COUNTRY_AL2_country_GEZ.json** (Implying country code followed by administrative level 2, followed by country name; with GEZ: Global Economic Zone). The files have 08 fields. Some of which are:

1. **gez_name:** Global Economic Zone name
2. **gez_code:** Global Economic Zone standard code
3. **gez_abbrev:** Global Economic Zone standard abbreviation

- The notation of files with the general form- **COUNTRY_AL2_country_WSR.json**(implying country code followed by administrative level 2, followed by country name; with WSR: World Soil Resources). The files have 08 fields

1.   <b><a href ='#country'>country:</b> refers to the name of the country </a>
2.  **ISO3166_2:** (ISO standard codes of administrative divisions and subdivisions) In other words - Administrative Divisions of Countries
3.  **name:** name of the level 4 state
4.  **SNAME:** soil name standard code
5.  **mg_code:** the soil major group code
6.  **IPCC:** soil names(The Intergovernmental Panel on Climate Change)
7.  **adnminlevel:** administrative level
8.  **geometry:**
### 1.1.2 Boundaries Level 4 

Level 4 directory contains the boundaries of each state grouped by country, as well as the boundaries of each state's ecological zone and the boundaries of the world's soil resources. At Level 4:

- The general notation of files is **COUNTRY_AL4_STATE-NAME.json**( implying the country name followed by Administrative Level 4, followed by the state name).
  The files are made up of eight (08) fields( **country, ISO3166_2, name, SNAME, mg_code, IPCC, adminlevel, geometry**)

- The notation of files with the general form: **COUNTRY_AL4_STATE-NAME_GEZ.json**(implying country name followed by administrative level 4, followed by state name; with GEZ: Global Economic Zone). The files have 08 fields(**country, ISO3166_2, name, gez_name, gez_code, gez_abbrev, adminlevel geometry**)

- The notation of files with the general form- **COUNTRY_AL4_STATE-NAME_WSR.json**(implying country name followed by administrative level 4, followed by state name; with WSR: World Soil Resources). The files have 08 fields( **country, ISO3166_2, name, SNAME, mg_code, IPCC, adminlevel, geometry**)

- The general notation of files is **COUNTRY_AL4_STATE-NAME.json**( implying the country name followed by Administrative Level 4, followed by the state name).
  The files are made up of eight (08) important fields: as explained below:

1.  **country:** refers to the name of the country
2.  **ISO3166_2:** (ISO standard codes of administrative divisions and subdivisions) In other words - Administrative Divisions of Countries
3.  **name:** name of the level 4 state
4.  **SNAME:** soil name standard code
5.  **mg_code:** the soil major group code
6.  **IPCC:** soil names(The Intergovernmental Panel on Climate Change)
7.  **adnminlevel:** administrative level
8.  **geometry:**

- The notation of files with the general form **COUNTRY_AL4_STATE-NAME_GEZ.json**(implying country name followed by administrative level 4, followed by state name; with GEZ: Global Economic Zone). The files have 08 fields. Some of which are:

1.  **gez_name:** Global Economic Zone name
2.  **gez_code:** Global Economic Zone standard code
3.  **gez_abbrev:** Global Economic Zone standard abbreviation

- The notation of files with the general form- **COUNTRY_AL4_STATE-NAME_WSR.json**(implying country name followed by administrative level 4, followed by state name; with WSR: World Soil Resources). The files have 08 fields( **country, ISO3166_2, name, SNAME, mg_code, IPCC, adminlevel, geometry**)

We also have two files that contain the world's country boundaries and the world's states boundaries respectively.

## 1.2 Protected Areas

This directory contains the boundary dataset for the **World Database of Protected Areas WDPA** especially data on Other Effective Area-Based Conservation Measures (WDOECM). A detailed description of the files within can be found[ here](http://wdpa.s3.amazonaws.com/WDPA_Manual/English/WDPA_Manual_1_4_EN_FINAL.pdf).

## 1.3 Roads

This directory combines the best available roads data by country into a global roads coverage, using the UN Spatial Data Infrastructure Transport (UNSDI-T) version 2 as a common data model. All country road networks are joined topologically at the borders, and many countries are edited for internal topology. Source data for each country are provided in the [documentation](https://sedac.ciesin.columbia.edu/downloads/docs/groads/groads-v1-documentation.pdf).

# 2. Biodiversity, AgroClimatic, and Ecological Zones.

This directory contains two sub-directories and five files. The five files are:

### 2.1.1 CI_BiodiversityHotspots.geojson:

This file contains global conservation international Biodiversity Hotspots. It has 06 fields:

1. **OBJECTID**: the object identifier
2. **NAME**: Standard name of Hotzone
3. **Type**: type of hot zone with outer limit or hotspot area
4. **shape_Length**: represents the length of the polygon
5. **Shape_Area** represents the area of the polygon
6. **geometry:**

### 2.1.2 GlobalCriticalHabitatScreening.tif:

This screening layer shows the global spatial distribution of likely or potential Critical Habitat, as defined by the International Finance Corporation’s Performance Standard 6 (IFC PS6) criteria.

### 2.1.3 HoldridgeLifeZones.json:

The Holdridge life zones system is a global bioclimatic scheme for the classification of land areas. This file contains:

1. **FID**:
2. **AREA**:
3. **PERIMETER**:
4. **HOLDRIG\_**:
5. **HOLDRIG_ID**:
6. **ZONE**:
7. **CASE\_**:
8. **FREQUENCY**:
9. **SYMBOL**:
10. **geometry:**

### 2.1.4 TerrestrialEcoregionsoftheWorld_WWF.geojson:

This file contains Terrestrial Ecological Regions of the world and has the following fields:

    OBJECTID_1	OBJECTID	AREA	ECO_NAME	REALM	BIOME	ECO_NUM	ECO_ID	ECO_SYM	GBL_STAT	G200_REGIO	G200_NUM	G200_BIOME	G200_STAT	area_km2	eco_code	BIOME_1	GBL_STAT_1	REALM_1	Shape_Length	Shape_Area	geometry
   
1. **OBJECTID**: Internal feature number
2. **AREA**: Area of each polygon in square km.
3. **ECO_NAME**: The name of the Terrestial eco region
4. **REALM**: Biogeographical realm
5. **BIOME**: Biome
6. **ECO_NUM**: A unique number of each region within each biome nested within each realm
7. **ECO_ID**: A unique numeric id for each ecoregion
8. **ECO_SYM**: Ecoregion symbol
9. **GBL_STAT**: Global status
10. **G200_REGIO**: Global 200 Name (The Global 200 is the list of ecoregions identified by the World Wide Fund for Nature (WWF), the global conservation organization, as priorities for conservation.)
11. **G200_NUM**: Global 200 Number
12. **G200_BIOME**: Global 200 Biome
13. **G200_STAT**: Global status
14. **area_km2**: Area of the ecoregion (km2)
15. **eco_code**: An alphanumeric code. The first 2 codes are the realm the ecoregion is in. The second 2 codes are the bioe and the last 2 are the ecoregion number.
16. **geometry:**

### 2.1.5 WorldDrylandDataset_2007_UNCCD_CBD_2014.json: empty file

There are two subdirectories:

## 2.2 Global AgroEcological Zones:

This directory contains 12 GeoTiff files with various Land Resources(cultivated, domestic land cover, forest land), Protected areas(restricted agro areas, types), Soil resources(dominant soils, nutrient availability, rain-fed terrain suitability, rooting conditions), Terrain slope index and Water scarcity. files
and 3 subdirectories. The 03 subdirectories:

### 2.2.1 Agro Climate

Contains GeoTiff files for growing period length, temperature growing period, thermal climate, and thermal zones.

### 2.2.2 Fisher 2008 GAEZ

Contains GeoTiff files about Barren sparsely vegetated land, buildup land, irrigated cultivated land, rainfed cultivated land, total cultivated land, forest land, grass shrub woodland, and water bodies. The ASC directory contains ASCII Raster files(.asc) variants of some of the GeoTiff files.

### 2.2.3 Originals

This directory contains the zipped(compressed) files versions of the GeoTiff and/or .asc files.

## 2.3 Global Ecological Zones

This directory contains a global ecological zone file and 02 subdirectories, which contain JSON files of ecological zones grouped by country and state. The attributes of the file in this section are the same as those of the GEZ file in section 1.1.1.

# 3. Climate

The Climate directory contains the Koppen Geiger climate shift from 1901 to 2100. The files within this subdirectory have the following attributes:

    OBJECTID	ID	GRIDCODE	Shape_Length	Shape_Area	geometry

some files within the subdirectory have the suffixes:

A1FI (fossil fuel intensive),

A1 ( new and efficient technologies),

A2 (a very heterogenic world with a focus on family values and local traditions),

B1 (a world without materialism and launch of clean technologies),

B2 (a world with a focus on local solutions for economic and ecological sustainability),

Within the climate directory the files:

**IPCC_ClimateZoneMap.tif:** Contains the GeoTiff IPCC climate zone map.

**IPCC_ClimateZoneMap_Vector.geojson:** contains the vectorised format fo the GeoTiff IPCC climate zone map. This file has the properties:

    CLASS_NAME	geometry

**KoppenGeigerClimateShifts.zip**: This file contains the zips of the Koppen Geiger Climate shifts.

# 4. Land Cover

The Land cover directory has four principal subdirectories:

## 4.1 Biomass Carbon

The Biomass Carbon is further subdivided into:

### 4.1.1 Above Ground Live Biomass:

This directory contains a zip file (AboveGroundLiveBiomassTiles.zip), which contains a data set of all living biomass above the soil, including stems, stumps, branches, bark, seeds, and leaves.


### 4.1.2 Avitabile Pan Tropical Biomass

This directory contains Avitabile's Above ground biomass GeoTiff and zip files

### 4.1.3 Geo Carbon Global Forest Biomass Maps

Contains geo carbon GeoTiff and zip file maps(global forest biomass, above-ground biomass, and forest above-ground biomass)

### 4.1.4 Global Biomass

This directory has 03 global biomass subdirectories containing tiles for above-ground biomass, growing stock volumes, and originals. The file names in these subdirectories directly imply the tiles of interest.

## 4.2 Forest

This directory contains subdirectories:

### 4.2.1 Managed Forest Concessions

Within this directory, files are containing managed forest concessions of 10 countries including the global GeoJSON file for managed forest concessions. These files have the following properties.
**id, OBJECTID, country, name, company, group_comp, group_coun, legal_term, status, province, source, last_updat, Shape_Leng, AREA_GEO, Shape_Length, Shape_Area, and geometry**

### 4.2.2 PanTropical Forest Strata

Contains GeoTiff files of Pantropical forest strata for Africa(AFR), South America(SAM), and Southeast Asia(SEA) as well as their relative zip files.

### 4.2.3 Planted forests

This data is from the Spatial Database of Planted Trees(SDPT). It contains data on 43 countries. Each file has the following properties:
**final_id, iso, country, org_name, common_name, species, species_simp, plant_ag, timber_ag, ever_dec, conifer_broad, hard_soft, size, source, year, geometry**

### 4.2.4 Wood Fiber Concessions

This directory contains files on the wood fiber concessions of 03 countries and 01 file for the world. The files have the following properties:
**OBJECTID\*1. OBJECTID. group_comp. NAME, type, COUNTRY, area_ha, source, Last_updat, gfwid, Shape_Leng, source_typ, year, FID\*, source_t_1, Shape_Le_1,, Shape_Le_2, Shape_Length, Shape_Area, geometry.**

## 4.3 Forest Loss

Forest Loss contains three subdirectories:

### 4.3.1 Hansen Global Forest Change

This directory contains four principal subdirectories(**datamask, gain, lossy year, and tree cover**). In these directories are GeoTiff tiles with the names implying the interest

### 4.3.2 Intact Forest Landscapes

This directory contains zips and GeoJSON files for Intact forest landscapes. The notation of the files carries the year of recording.

### 4.3.3 Terra i Forest Loss

It contains the terra i forest loss data for the country Uganda.

## 4.4 Land Use

This directory contains Global Food Security-Support Analysis Data. The subdirectories contain tiled files with GFSAD Global Crop Land Crop Extent data. These files notations contain the year as well as the regions of interest which are:

- Africa (GFSAD30AFCE_2015_resampledTiles),
- Australia-New_Zealand-China-Mongolia( GFSAD30AUNZCNMOCE_2015_resampledTiles),
- Europe-Centra_Asia-Russia-Middle_East( GFSAD30EUCEARUMECE_2015_resampledTiles),
- North America( GFSAD30NACE_2010_resampledTiles),
- South America( GFSAD30SACE_2015_resampledTiles) and
- Southeast-and-Northeast Asia( GFSAD30SEACE_2015_resampledTiles).

# 5. Soil

This directory contains 03 subdirectories and 02 files( Global soil organic carbon). The three subdirectories are:

## 5.1 Harmonised World Soil Database (HWSD)

This directory contains data tables with the following properties:

ID MU_GLOBAL MU_SOURCE1 MU_SOURCE2 ISSOIL SHARE SEQ SU_SYM74 SU_CODE74 SU_SYM85 SU_CODE85 SU_SYM90 SU_CODE90 T_TEXTURE DRAINAGE REF_DEPTH AWC_CLASS PHASE1 PHASE2 ROOTS IL SWR ADD_PROP T_GRAVEL T_SAND T_SILT T_CLAY T_USDA_TEX_CLASS T_REF_BULK_DENSITY T_BULK_DENSITY T_OC T_PH_H2O T_CEC_CLAY T_CEC_SOIL T_BS T_TEB T_CACO3 T_CASO4 T_ESP T_ECE S_GRAVEL S_SAND S_SILT S_CLAY S_USDA_TEX_CLASS S_REF_BULK_DENSITY S_BULK_DENSITY S_OC S_PH_H2O S_CEC_CLAY S_CEC_SOIL S_BS S_TEB S_CACO3 S_CASO4 S_ESP S_ECE

## 5.2 Soil Quality Crop Production

Contains a zip file of the HWSD Soil Quality Crop Production.

## 5.3 World Soil Resources (WSR)

This directory contains 02 subdirectories:

### 5.3.1 WSR by Country:

Contains files whose notation indicates the country of interest. 
 The files have 08 fields

1.  **country:** refers to the name of the country
2.  **ISO3166_2:** (ISO standard codes of administrative divisions and subdivisions) In other words - Administrative Divisions of Countries
3.  **name:** name of the level 4 state
4.  **SNAME:** soil name standard code
5.  **mg_code:** the soil major group code
6.  **IPCC:** soil names(The Intergovernmental Panel on Climate Change)
7.  **adnminlevel:** administrative level
8.  **geometry**

### 5.3.2 WSR by State

Contains files of states' soil resources. 
The files have 08 fields( **country, ISO3166_2, name, SNAME, mg_code, IPCC, adminlevel, geometry**)

