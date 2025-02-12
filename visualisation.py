import argparse
import pandas as pd
import hist
import numpy as np

import matplotlib.pyplot as plt
import mplhep
mplhep.style.use("CMS")

parser = argparse.ArgumentParser()
parser.add_argument('data', type=str)
args = parser.parse_args()

assert(args.data in ['LHCb', 'ATLAS', 'WET'])

if args.data == 'LHCb':
    fname = 'LHCb/lhcb-dataset.npz'
    columns = ["mKD", "mDD"]
    labels = [r"$m'(K^+D^-)$", r"$m'(D^+D^-)$"]
    ranges = [[-0.05,1.05]]*2
elif args.data == 'ATLAS':
    fname = 'ATLAS/atlas-dataset.npz'
    columns = ["pT", "y", "pT1", "eta", "phi"]
    labels = [r"$p_T^{\mu\mu}$",r"$y^{\mu\mu}$",r"$p_T^{\mu_1}$",r"$\Delta \eta_{12}^2$",r"$\Delta \phi_{12}^2$"]
    ranges = [[-0.05,1.05]]*5
elif args.data == 'WET':
    fname = 'WET/wet-dataset.npz'
    columns = ["VL", "VR", "SL", "SR", "T"]
    labels = [  r"${\rm Re}{\cal C}_{V_R}^{\bar{u}b\bar{e}\nu_e}$",
                r"${\rm Re}{\cal C}_{V_L}^{\bar{u}b\bar{e}\nu_e}$",
                r"${\rm Re}{\cal C}_{S_R}^{\bar{u}b\bar{e}\nu_e}$",
                r"${\rm Re}{\cal C}_{S_L}^{\bar{u}b\bar{e}\nu_e}$",
                r"${\rm Re}{\cal C}_{T}^{\bar{u}b\bar{e}\nu_e}$"]
    ranges = [[-1.8, 1.8], [-1.8, 1.8], [-2.8, 2.8], [-2.8, 2.8], [-2.8, 2.8]]

data = np.load(fname)
X_train = pd.DataFrame(data['X_train'], columns=columns)
X_test = pd.DataFrame(data['X_test'], columns=columns)
data = pd.concat([X_train, X_test], ignore_index=True)

f = plt.figure()
fig, ax = plt.subplots(len(columns),len(columns),figsize=(f.get_size_inches()[0]*len(columns)/2,f.get_size_inches()[1]*len(columns)/2),gridspec_kw={'hspace': 0, 'wspace': 0})

for i in range(0,len(columns)):
    ymin, ymax = ranges[i][0], ranges[i][1]
    for j in range(0,i):
        print(i,j)
        xmin, xmax = ranges[j][0], ranges[j][1]

        h, xedges, yedges = np.histogram2d(data[columns[j]],data[columns[i]],bins=50,range=((xmin,xmax),(ymin,ymax)))
        datac = ax[i,j].contourf(h.T, extent=[xedges.min(),xedges.max(),yedges.min(),yedges.max()], cmap="YlOrRd", levels=10)
        # add contour lines
        # ax[i,j].contour(datac,colors="k",linewidths=1,alpha=0.5)

        # set limits
        ax[i,j].set_xlim(xmin, xmax)
        ax[i,j].set_ylim(xmin, xmax)

        # make upper right invisible
        ax[j,i].set_visible(False)

    # plot histograms in diagonal
    H = hist.Hist(hist.axis.Regular(50, ymin, ymax))
    H.fill(data[columns[i]])
    mplhep.histplot(H, ax=ax[i,i], color="black", histtype="errorbar", density=True, xerr=True, yerr=True)

    # set limits
    ax[i,i].set_xlim(ymin, ymax)
    ax[i,i].set_ylim(0,)

    ax[i,i].set_yticks([]) # remove yticks from diagonal
    ax[len(columns)-1,i].set_xlabel(labels[i]) # set bottom row xlabels
    # set left column ylabels with fixed offset from edge
    ax[i,0].yaxis.set_label_coords(-0.15,0.5)
    ax[i,0].set_ylabel(labels[i]) # set left column ylabels
    # # remove yticklabels from all but the left column
    if i!=0:
        for j in range(0,len(columns)):
            ax[j,i].set_yticklabels([])
plt.tight_layout()
plt.savefig(f"{args.data}.png")
plt.close()