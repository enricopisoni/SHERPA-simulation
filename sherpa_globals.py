'''
Created on Jul 14, 2015

define some global variables

@author: degraba
'''

# variabels for testing
# absolute emission per cell and macro sector
path_emission_cdf_test = './input/BC_emiss/yea/emep45_cams80_SecEmis.nc'

# netcdf with cells where reductions have to be applied (value between 0 and 1)
path_area_cdf_test = './input/reduction_areas/emiRedOn_emep45_cams80_Germany.nc'#London_emepCams_0_100_FLIP.nc'

path_reduction50all_txt_test = './input/reduction_perc/user_reduction_GNFR_all_PPM25.txt'#user_reduction_GNFR_all.txt'
# reductions per precursor and macro sector for module 3a and 3b
path_reduction_mod3a1P_txt_test = './input/reduction_perc//user_reduction_GNFR_all_PPM25_50p.txt'
path_reduction_mod3a2P_txt_test = './input/reduction_perc//user_reduction_GNFR_all_PPM25_50p.txt'
path_reduction_mod3b_txt_test = './input/reduction_perc//user_reduction_GNFR_all_PPM25_50p.txt'

# netcdf with model parameters per cell
path_model_cdf_test = '././input/SRR/yea/SR_SURF_ug_PM25_rh50.nc' 
# path_model_cdf_test = '././input/SRR/yea/SR_SURF_ug_PM10_rh50.nc' 
# path_model_cdf_test = '././input/SRR/yea/SR_SURF_ug_NO2.nc' 
# path_model_cdf_test = '././input/SRR/yea/SR_SURF_ppb_O3.nc' 
# path_model_cdf_test = '././input/SRR/yea/SR_SURF_ppb_SO2.nc' 

path_base_conc_cdf_test = './input/BC_concs/yea/BCconc_emepV45_cams80_SURF_ug_PM25_rh50.nc'
# path_base_conc_cdf_test = './input/BC_concs/yea/BCconc_emepV45_cams80_SURF_ug_PM10_rh50.nc'
# path_base_conc_cdf_test = './input/BC_concs/yea/BCconc_emepV45_cams80_SURF_ug_NO2.nc'
# path_base_conc_cdf_test = './input/BC_concs/yea/BCconc_emepV45_cams80_SURF_ppb_O3.nc'
# path_base_conc_cdf_test = './input/BC_concs/yea/BCconc_emepV45_cams80_SURF_ppb_SO2.nc'

# reductions per precursor and macro sector
path_reduction_txt_test = './input/reduction_perc/user_reduction_GNFR_all_PPM25.txt'
# path_reduction_txt_test = './input/reduction_perc/user_reduction_GNFR_all_PPM10.txt'

# folder where output will be put
path_result_cdf_test = './output/'

# ONLY FOR PM, INCLUDE A VARIABLE RELATED TO THE DOWNSCALING REQUEST
downscale_request = 0 # 0 if you do not need downscale, 1 if you need downscale but only for PM concentrations

# progress log is used when module 1 is called by another module
path_nuts0_cdf_test = './input_emep45_cams80/1_FINAL_INPUT/EMI_RED_ATLAS_NUTS_01005_Lv0_EdgarEmep.nc'
path_nuts1_cdf_test = './input_emep45_cams80/1_FINAL_INPUT/EMI_RED_ATLAS_NUTS_01005_Lv1_EdgarEmep.nc'
path_nuts2_cdf_test = './input_emep45_cams80/1_FINAL_INPUT/EMI_RED_ATLAS_NUTS_01005_Lv2_EdgarEmep.nc'
path_nuts3_cdf_test = './input_emep45_cams80/1_FINAL_INPUT/EMI_RED_ATLAS_NUTS_01005_Lv3_EdgarEmep.nc'

#for health
path_healthbl_test = './input_CAMS42_EMEP_01005/1_FINAL_INPUT/input/impacts/healthbl_nc.nc'
path_config_json_test = './input_CAMS42_EMEP_01005/1_FINAL_INPUT/sharedvariables.json'

fua_intersect_dir = './input_CAMS42_EMEP_01005/1_FINAL_INPUT/output_mod7/fua/'
nuts_intersect_dir = './input_CAMS42_EMEP_01005/1_FINAL_INPUT/output_mod7/nuts/'
dbf_dir = './input_CAMS42_EMEP_01005/1_FINAL_INPUT/output_mod7/'
target_list = './input_CAMS42_EMEP_01005/1_FINAL_INPUT/output_mod7/AM_targets.txt'
path_natural_dir_test = './input_CAMS42_EMEP_01005/1_FINAL_INPUT/output/'
aggr_zones='fua'
path_logo_test=''
aggrinp_txt=''
# list of precursors
# order important, it's the order in the alpha and omega arrays
# precursor_lst = ['NOx', 'NMVOC', 'NH3', 'PM25', 'SOx']  

# order important, it's the order in the alpha and omega arrays
sector_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]   #  

# fixed reduction percentage for potency calculation
alpha_potency = float(50)
