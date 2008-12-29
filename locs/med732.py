'''This is a calibration file for data collected at Medicina, Italy,
in September.'''

import aipy as a, numpy as n

E = [-18.8875321, -10.8875321, -34.8875321, -26.8875321]
N = [6.804708, 20.414123, 34.023538, 47.632953, 
    61.242368, 74.851783, 88.461198, 102.070613]
topo_antpos = n.array([
    # EAST , NORTH , ELEV
    [E[0],N[0],0], [E[1],N[0],0], [E[2],N[0],0], [E[3],N[0],0],
    [E[0],N[1],0], [E[1],N[1],0], [E[2],N[1],0], [E[3],N[1],0],
    [E[0],N[2],0], [E[1],N[2],0], [E[2],N[2],0], [E[3],N[2],0],
    [E[0],N[3],0], [E[1],N[3],0], [E[2],N[3],0], [E[3],N[3],0],
    [E[0],N[4],0], [E[1],N[4],0], [E[2],N[4],0], [E[3],N[4],0],
    [E[0],N[5],0], [E[1],N[5],0], [E[2],N[5],0], [E[3],N[5],0],
    [E[0],N[6],0], [E[1],N[6],0], [E[2],N[6],0], [E[3],N[6],0],
    [E[0],N[7],0], [E[1],N[7],0], [E[2],N[7],0], [E[3],N[7],0],
])

prms = {
    'loc': ('44:31:24.88',  '11:38:45.56'), # Medicina, Italy
    'antpos':
      [[ -11.69,  -46.29,   11.89],
       [ -11.69,  -26.68,   11.89],
       [ -11.69,  -85.50,   11.89],
       [ -11.69,  -65.90,   11.89],
       [ -35.08,  -46.29,   35.67],
       [ -35.08,  -26.68,   35.67],
       [ -35.08,  -85.50,   35.67],
       [ -35.08,  -65.90,   35.67],
       [ -58.47,  -46.29,   59.45],
       [ -58.47,  -26.68,   59.45],
       [ -58.47,  -85.50,   59.45],
       [ -58.47,  -65.90,   59.45],
       [ -81.86,  -46.29,   83.23],
       [ -81.86,  -26.68,   83.23],
       [ -81.86,  -85.50,   83.23],
       [ -81.86,  -65.90,   83.23],
       [-105.25,  -46.29,  107.01],
       [-105.25,  -26.68,  107.01],
       [-105.25,  -85.50,  107.01],
       [-105.25,  -65.90,  107.01],
       [-128.64,  -46.29,  130.80],
       [-128.64,  -26.68,  130.80],
       [-128.64,  -85.50,  130.80],
       [-128.64,  -65.90,  130.80],
       [-152.03,  -46.29,  154.58],
       [-152.03,  -26.68,  154.58],
       [-152.03,  -85.50,  154.58],
       [-152.03,  -65.90,  154.58],
       [-175.42,  -46.29,  178.36],
       [-175.42,  -26.68,  178.36],
       [-175.42,  -85.50,  178.36],
       [-175.42,  -65.90,  178.36]],
    'offsets': [
        +0.0056, -0.0038, -0.0702, -0.1977,
        +0.2140, -0.0807, -0.6969, +0.0800,
        +0.0095, +0.4879, +0.4600, +0.1400,
        +0.1720, +0.0000, +0.0003, +0.0002,
        -0.4300, -0.3300, -0.1300, -0.0040,
        -0.2354, -0.2089, -0.222,  -0.0300,
        +0.1472,  0.6089, -0.5892, -0.4080,
        -0.9120, -0.4312, -0.7206, -0.6967,
    ],
    'delays': [
        0.008,-02.53, 14.48, 14.16, 
        12.65, 05.98, 10.36, 10.92, 
        31.70, 30.12, 35.54, 31.23,
        30.96, 33.48, 33.60, 31.35,
        14.79, 17.18, 21.73, 13.62,
        19.52, 26.75, 24.25, 23.97, 
       -14.02,-12.43, 22.09, 18.84, 
        30.30, 24.30, 3.735, 6.658,
    ],
    'amps': [
        .0065, .0053, .011, .011,
        .011,  .0095,   .0097,    .011,
        .011,  .0131,   .011,    .011,
        .011,  .011,   .011,    .011,
        .011,  .011,   .011,    .011,
        .011,  .011,   .011,    .011,
        .011,  .011,   .011,    .011,
        .011,  .011,   .011,    .011,
    ],
    'bp_r': n.array([
        [80.717149179238135, -93.934293563351474, -78.819668779729952, 44.279774298456516]
    ] * 32),
    'bp_i': n.array([[1.]] * 32),
    'beam': a.fit.BeamFlat,
    'bm_prms': {},
}

def get_aa(freqs):
    '''Return the AntennaArray to be used fro simulation.'''
    location = prms['loc']
    antennas = []
    nants = len(prms['antpos'])
    assert(len(prms['delays']) == nants and len(prms['amps']) == nants \
        and len(prms['bp_r']) == nants and len(prms['bp_i']) == nants)
    for i in range(len(prms['antpos'])):
        beam = prms['beam'](freqs, nside=128, lmax=10, mmax=10, deg=7)
        try: beam.set_params(prms['bm_prms'])
        except(AttributeError): pass
        pos = prms['antpos'][i]
        dly = prms['delays'][i]
        amp = prms['amps'][i]
        bp_r = prms['bp_r'][i]
        bp_i = prms['bp_i'][i]
        off = prms['offsets'][i]
        antennas.append(
            a.fit.Antenna(pos[0],pos[1],pos[2], beam, delay=dly, offset=off,
                amp=amp, bp_r=bp_r, bp_i=bp_i)
        )
    aa = a.fit.AntennaArray(prms['loc'], antennas)
    return aa

src_prms = {
    'cas': {
        'str': [-806582.31594516593, -463.50970377839747, 23935.756753243873],
    },
}
