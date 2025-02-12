# Examples for Nabu

This repository contains the likelihood models presented in the paper and instructions how to replicate the results using nabu package. Below we describe how to run each of the analysis. Each model can be loaded and used via following prescription

```python
import nabu
likelihood_model = nabu.Likelihood.load("PATH/TO/MODEL.nabu")
generated_samples = likelihood_model.sample(100)
```

where the last line shows how to generate samples from the likelihood model.

## [ATLAS](https://inspirehep.net/literature/2791852)

ATLAS model used in the paper is included in `ATLAS/atlas-model.nabu` including the transformation information. In order to replicate the results one can use the following command

```bash
nabu-fit-to-data -dp ATLAS/atlas-dataset.npz -e 600 -t rqs -k 12 -int 1e-6 1 -tfrac 0.2990332256 -w 512 -l 8 -d 1 -perm random -lr 0.01 -mlr 1.0e-06
```

## [LHCb](https://lhcbproject.web.cern.ch/Publications/LHCbProjectPublic/LHCb-PAPER-2020-025.html)

LHCb model used in the paper is included in `LHCb/lhcb-model.nabu` including the transformation information. In order to replicate the results one can use the following command

```bash
nabu-fit-to-data -dp LHCb/lhcb-dataset.npz -e 600 -t rqs -k 12 -int 1e-6 1 -w 64 -l 8 -d 2 -lr 0.001 -mlr 1.0e-08
```

## [WET](http://dx.doi.org/10.5281/zenodo.8027015)

WET model used in the paper is included in `WET/wet-model.nabu` including the transformation information. In order to replicate the results one can use the following command

```bash
nabu-fit-to-data -dp WET/wet-dataset.npz -e 600 -w 64 -l 2 -d 3 -lr 0.001 -mlr 0.0001
```
