# Examples for Nabu

This repository contains the likelihood models presented in the paper and instructions on replicating the results using the nabu package. Below, we describe how to run each analysis. The following prescription allows each model to be loaded and used.

```python
import nabu
likelihood_model = nabu.Likelihood.load("PATH/TO/MODEL.nabu")
generated_samples = likelihood_model.sample(100)
```

where the last line shows how to generate samples from the likelihood model.

## [ATLAS](https://inspirehep.net/literature/2791852)

The ATLAS model utilised in the paper is included in `ATLAS/atlas-model.nabu`, which encompasses the transformation information. To replicate the results, one can use the following command:

```bash
nabu-fit-to-data -dp ATLAS/atlas-dataset.npz -e 600 -t rqs -k 12 -int 1e-6 1 -tfrac 0.2990332256 -w 512 -l 8 -d 1 -perm random -lr 0.01 -mlr 1.0e-06
```

The data file contains standardised version of $p_T^{\mu\mu}$, $y^{\mu\mu}$, $p_T^{\mu_1}$, $\Delta \eta_{12}^2$ and $\Delta \phi_{12}^2$, respectively.

## [LHCb](https://lhcbproject.web.cern.ch/Publications/LHCbProjectPublic/LHCb-PAPER-2020-025.html)

The LHCb model used in the paper is located in `LHCb/lhcb-model.nabu`, which includes the transformation information. To replicate the results, use the following command.

```bash
nabu-fit-to-data -dp LHCb/lhcb-dataset.npz -e 600 -t rqs -k 12 -int 1e-6 1 -w 64 -l 8 -d 2 -lr 0.001 -mlr 1.0e-08
```

The datafile contains standardised version of $m^2(K^+D^-)$ and $m^2(D^+D^-)$, respectively.

## [WET](http://dx.doi.org/10.5281/zenodo.8027015)

The WET model used in this paper is included in `WET/wet-model.nabu`, which contains the transformation information. To replicate the results, one can use the following command.

```bash
nabu-fit-to-data -dp WET/wet-dataset.npz -e 600 -w 64 -l 2 -d 3 -lr 0.001 -mlr 0.0001
```
The datafile contains standardised version of ${\rm Re}[C_{V_R}^{\bar{u}b\bar{e}\nu_e}]$, ${\rm Re}[C_{V_L}^{\bar{u}b\bar{e}\nu_e}]$, ${\rm Re}[C_{S_R}^{\bar{u}b\bar{e}\nu_e}]$, ${\rm Re}[C_{S_L}^{\bar{u}b\bar{e}\nu_e}]$ and ${\rm Re}[C_{T}^{\bar{u}b\bar{e}\nu_e}]$, respectively.

# Sample illustrations
The complexity of the different samples can be illustrated using
```bash
python visualisation.py {ATLAS,LHCb,WET}
```

Please note that in addition to the packages required in the main repo ([see here](requirements.txt)), the script uses `pandas`, `mplhep`, and `hist` which are available with `pip` and `conda`.

<table>
<tr>
  <th>Figure</th>
  <th>Caption</th>
</tr>
<tr>
  <td><img src="/ATLAS.png?raw=true" width="1000px" height="auto"></a></td>
  <td>One- and two-dimensional projections of the ATLAS example data set.</td>
</tr>
<tr>
  <td><img src="/LHCb.png?raw=true" width="1000px" height="auto"></a></td>
  <td>One- and two-dimensional projections of the LHCb example data set.</td>
</tr>
<tr>
  <td><img src="/WET.png?raw=true" width="1000px" height="auto"></a></td>
  <td>One- and two-dimensional projections of the WET example data set.</td>
</tr>
</table>

