# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:25:06 2021

@author: super
"""

import numpy as np
import matplotlib.pyplot as plt
import corner


#### KILONOVA #####
samples_kn = np.load('input_files/LC_nucleo2.npy')
length_kn = len(samples_kn)
times = samples_kn[:,0]
nuc = samples_kn[:,3]
nuc_120min_unfiltered = np.zeros(len(times))
for i in range(len(times)):
    nuc_120min_unfiltered[i] = np.interp(2/24,times[i],nuc[i])



# nuc_120min = nuc_120min_unfiltered[nuc_120min_unfiltered!=0] 

# nuc_210min_unfiltered = nuc[:,22]
# nuc_210min = nuc_210min_unfiltered[nuc_210min_unfiltered!=0] 
# nuc_delta_m = nuc_210min-nuc_120min

####### SHOCK #######
# t_sh = np.geomspace(0.02,1)
# samples_sh = np.load('input_files/LC_shock.npy')
# sh_120min = samples_sh[0:2501,0,18]
# sh_210min = samples_sh[0:2501,0,25]
# sh_delta_m = sh_210min-sh_120min

# import matplotlib.lines as mlines

###### GRADIENT PLOT ##############
# fig,ax=plt.subplots(1,1)

# corner.hist2d(nuc_delta_m,nuc_120min,ax=ax,color='tab:orange',no_fill_contours=False,plot_density=True,plot_datapoints=False,newfig=True,label='Shock Interaction')
# corner.hist2d(sh_delta_m,sh_120min,ax=ax,color='tab:blue',no_fill_contours=False,plot_density=True,plot_datapoints=False,new_fig=False,label='Nucleosynthesis')
# shock = mlines.Line2D([],[], color='tab:blue',linestyle='-',label='Shock Interaction')
# nucleo = mlines.Line2D([],[], color='tab:orange',linestyle='-',label='Nucleosynthesis')
# ax.legend(handles=[shock,nucleo],loc='lower right') 

# ax.set_ylabel(r'Abs. mag. at 2 hours',fontsize=15)
# ax.set_xlabel(r'$\Delta m_{\rm90 min}$ ($m_{\rm 3.5 hours} - m_{\rm 2 hours}$)',fontsize=15)
# ax.invert_yaxis()
#fig.savefig('gradient.png',dpi=300,pad_inches=0.3,bbox_inches='tight')


##### HIST PLOT ##############
# fig,ax=plt.subplots(1,1)
# ax.hist(sh_120min,bins=50,label='Shock Interaction')
# ax.hist(nuc_120min,bins=50,alpha=0.5,label='Nucleosynthesis')
# ax.set_xlabel(r'Absolute magnitude (AB) at 2 hours',fontsize=15)
# ax.set_ylabel(r'$n_{\rm samples}$',fontsize=15)
# ax.invert_xaxis()
# ax.legend()
# fig.savefig('histogram_2hours.png',dpi=300,pad_inches=0.3,bbox_inches='tight')

