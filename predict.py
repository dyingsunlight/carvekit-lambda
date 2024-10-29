from carvekit.api.interface import Interface
from carvekit.ml.wrap.fba_matting import FBAMatting
from carvekit.ml.wrap.tracer_b7 import TracerUniversalB7
from carvekit.pipelines.postprocessing import MattingMethod
from carvekit.pipelines.preprocessing import PreprocessingStub
from carvekit.trimap.generator import TrimapGenerator

seg_net = TracerUniversalB7(
    device='cpu',
    batch_size=1
)
fba = FBAMatting(device='cpu',
    input_tensor_size=386,
    batch_size=1
)
trimap = TrimapGenerator()
preprocessing = PreprocessingStub()
postprocessing = MattingMethod(
    matting_module=fba,
    trimap_generator=trimap,
    device='cpu'
)
interface = Interface(
    pre_pipe=preprocessing,
    post_pipe=postprocessing,
    seg_pipe=seg_net
)

def predict(image):
    cat_wo_bg = interface([image])[0]
    return cat_wo_bg
