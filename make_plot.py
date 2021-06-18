import numpy as np
import matplotlib.pyplot as plt
import corner
import matplotlib.lines as mlines

#### KILONOVA #####
samples_kn = np.load('LC_bns_beta_brightUV_incloptical.npy')
length_kn = len(samples_kn)
times = samples_kn[:,0]
lightcurves = samples_kn[:,2]
peak_mag_unfiltered = np.min(lightcurves,axis=1)
mag_2hours_unfiltered = lightcurves[:,14] # ~2 hours
peak_idx = np.zeros(length_kn)
sample_idx = []
peak_mag = []
mag_2hours = []
for i in range(length_kn):
    index_unfiltered=np.where(lightcurves[i]==peak_mag_unfiltered[i])[0]
    if len(index_unfiltered)==1:
        peak_idx[i]=index_unfiltered
        sample_idx.append(i)
        peak_mag.append(peak_mag_unfiltered[i])
        mag_2hours.append(mag_2hours_unfiltered[i])
     
peak_times = []
for i in sample_idx:
    peak_times.append(samples_kn[i,0,int(peak_idx[i])])

#### SHOCK ####
t = np.geomspace(0.02,1)
samples_sh = np.load('LC_shock.npy')
length_sh = len(samples_sh)
lightcurves_sh = samples_sh[:,0]
peak_mag_sh = np.min(lightcurves_sh,axis=1)
peak_times_sh = np.zeros(length_sh)
mag_2hours_sh = lightcurves_sh[:,18]
for i in range(length_sh):
    index=np.where(lightcurves_sh[i]==peak_mag_sh[i])[0]
    peak_times_sh[i] = t[index]
    
    
##### PEAK TIME LOWER LIMITS ###############
peak_times_sh_limited = np.where(peak_times_sh>(2/24),peak_times_sh,2/24)
peak_times_limited = np.where(np.asarray(peak_times)>(2/24),peak_times,2/24)

### peaks plot ###
# fig,ax = plt.subplots(1,1)
# corner.hist2d(np.asarray(peak_times_sh)*24,np.asarray(peak_mag_sh),ax=ax,color='tab:blue',no_fill_contours=False,plot_density=True,plot_datapoints=False)
# corner.hist2d(np.asarray(peak_times)*24,np.asarray(peak_mag),ax=ax,color='tab:orange',no_fill_contours=False,plot_density=True,plot_datapoints=False,newfig=False)
# ax.invert_yaxis()
# ax.set_ylim([-12,-18.5])
# ax.set_xlim([0,10])
# ax.set_xlabel('Time to peak (hours)',fontsize=15)
# ax.set_ylabel('Peak absolute magnitude (AB)',fontsize=15)
# ax.set_title('Distribution of peaks in Dorado band',fontsize=15)
# shock = mlines.Line2D([],[], color='tab:blue',linestyle='-',label='Shock Interaction model peaks')
# nucleo = mlines.Line2D([],[], color='tab:orange',linestyle='-',label='Nucleosynthesis model peaks')
# #ax.legend(handles=[shock, nucleo],loc='lower right')
# fig.savefig('Doradoband_peaks_distribution.png',dpi=300,pad_inches=0.3,bbox_inches='tight')

##### plot at 2 hours ########
fig,ax = plt.subplots(1,1)

corner.hist2d(np.asarray(peak_times_sh_limited)*24,np.asarray(mag_2hours_sh),ax=ax,color='tab:blue',no_fill_contours=False,plot_density=True,plot_datapoints=False)
corner.hist2d(np.asarray(peak_times_limited)*24,np.asarray(mag_2hours),ax=ax,color='tab:orange',no_fill_contours=False,plot_density=True,plot_datapoints=False,newfig=False)

#ax.plot(peak_times_sh_limited*24,mag_2hours_sh,'x')
#ax.plot(peak_times_limited*24,mag_2hours,'x',alpha=0.2)

ax.invert_yaxis()
ax.set_ylim([-12,-18.5])
ax.set_xlim([0,10])
ax.set_xlabel('Time to peak (hours)',fontsize=15)
ax.set_ylabel(r'Abs. mag. at 2 hours',fontsize=15)
shock = mlines.Line2D([],[], color='tab:blue',linestyle='-',label='Shock Interaction model peaks')
nucleo = mlines.Line2D([],[], color='tab:orange',linestyle='-',label='Nucleosynthesis model peaks')
fig.savefig('Doradoband_ABmag_2hours_2hlimit.png',dpi=300,pad_inches=0.3,bbox_inches='tight')
