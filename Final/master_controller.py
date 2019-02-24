import bls_data_frame as b
#read in the Match_Indeed_to_skill module
import Match_Indeed_to_skill as mi

df_bls = b.get_df_bls()
job_list = b.get_job_list(df_bls)

skill_list = mi.get_skill_list()


