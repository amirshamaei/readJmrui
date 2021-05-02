import numpy as np
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def read(path):
    header = {}
    f = open(path, "r")
    i=0
    for x in f:
      step_0 = x.split(':')
      if step_0[0] == 'Filename':
          header['fn']=step_0[1].strip("\n")
      elif step_0[0] == 'PointsInDataset':
          header['PointsInDataset'] =int(step_0[1])
      elif step_0[0] == 'DatasetsInFile':
          header['DatasetsInFile'] =int(step_0[1])
      elif step_0[0] == 'SamplingInterval':
          header['t'] =float(step_0[1])
      elif step_0[0] == 'TransmitterFrequency':
          header['Transfreq'] = float(step_0[1])
      elif step_0[0].startswith('sig(real)'):
          break
    re = np.zeros((header['DatasetsInFile']*header['PointsInDataset']),dtype="float32")
    imag = np.zeros((header['DatasetsInFile']*header['PointsInDataset']),dtype="float32")
    for x in f:
        if isfloat(x.split("\t")[0]):
            re[i] = float(x.split("\t")[0])
            imag[i] = float(x.split("\t")[1])
            i = i+1
    re= re.reshape((header['PointsInDataset'],header['DatasetsInFile']))
    imag= imag.reshape((header['PointsInDataset'],header['DatasetsInFile']))
    f.close()
    return header,re, imag