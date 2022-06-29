import numpy as np
def corr_metric_calc(F):
    s= F.shape
    if s == (14,120):
        pass
    elif s == (14,160):
        F = F[:,20:140]
        s= F.shape

    corr_array = np.empty((s[0],s[0]))

    for i0 in range(s[0]):
        for i1 in range(s[0]):
            corr_array[i0,i1] = np.corrcoef(F[i0,:],F[i1,:])[0][1]

    return np.nanmean(corr_array)