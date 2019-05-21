from PyTorch.SpeechSynthesis.Tacotron2.tacotron2 import model as tacotron2
from PyTorch.SpeechSynthesis.Tacotron2.models import lstmcell_to_float
from PyTorch.Recommendation.NCF import neumf as ncf

print("|||module hubconf.py")

if __name__ == '__main__':

    model_tacotron2 = tacotron2.Tacotron2()
    model_ncf = ncf.NeuMF()
    
    print("if I'm that far then all imports succeeded!")
