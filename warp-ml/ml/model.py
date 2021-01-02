from typing import List

from tensorflow import keras
from tensorflow.keras import layers
from warplane.ml.nn_components import WaveNetResidualConvBlock1D


class WaveNetRegressor(keras.Model):
    """
    A simple WaveNet-style convolutional sequence-to-sequence model.

    Builds on the architecture used in the paper:
    "Neural_Audio_Synthesis_of_Musical_Notes_with_WaveNet_Autoencoders"
    (https://www.researchgate.net/publication/315795409_Neural_Audio_Synthesis_of_
    Musical_Notes_with_WaveNet_Autoencoders/link/594b68f2458515225a83289a/download)

    Pieces inspired by impementations like:
        - https://www.kaggle.com/siavrez/wavenet-keras
        - https://github.com/magenta/magenta/blob/master/magenta/models/nsynth/wavenet/
        - https://github.com/morris-frank/nsynth-pytorch/blob/master/nsynth/encoder.py

    """

    def __init__(
        self,
        name: str = "WaveNetRegressor",
        n_filters: int = 16,
        kernel_size: int = 3,
        layer_max_dilation_factors: List[int] = [12, 8, 4, 1],
        **kwargs,
    ):
        """
        Parameters
        ----------
        name: str, optional
            Name given to the model
        n_filters: int, optional
            The base number of convolutional filters (per dilation rate) in a wavenet block. Each layer
            doubles this (this is an empirically effective heuristic).
        kernel_size: int, optional
            The size of the 1D (dilated) convolution kernels.
        layer_max_dilation_factors: list of int, optional
            The max dilation rates per layer. Specifies the number of layers implicitly. For example, if
            [12, 8] there will be two layers.  The first will use a stack of 12 1D convolutions ranging from
            stride lengths of 1 to 2^(12-1) = 2048, each with num_filters kernels. The second will use a
            stack of 8 1D convolutionsn of stride 1 to 2^(8-1) = 128, each with num_filters*2 kernels.
        """
        super(WaveNetRegressor, self).__init__(name=name, **kwargs)
        self.n_filters = n_filters
        self.kernel_size = kernel_size
        self.layer_max_dilation_factors = layer_max_dilation_factors

    def build(self, input_shape):
        """
        Constructs the model components on first call, using input_shape to
        initialise any size-dependent weights
        """
        # stack wavenet residual conv blocks to produce temporal feature maps
        self.channel_match_convs, self.wavenet_blocks = [], []
        for ix, layer_max_dilation_factor in enumerate(
            self.layer_max_dilation_factors
        ):
            # filters double per layer, starting from n_filters
            layer_filters = self.n_filters * (2 ** ix)
            # kernel-size one convolutions to transform block input sto match channel numbers
            # with residuals from wavenet blocks
            self.channel_match_convs.append(
                layers.Conv1D(layer_filters, 1, padding="same")
            )
            res_blk = WaveNetResidualConvBlock1D(
                name=f"WaveNetResidualConvBlock_{ix}",
                num_filters=self.n_filters * (2 ** ix),
                kernel_size=self.kernel_size,
                n_dilations=layer_max_dilation_factor,
            )
            self.wavenet_blocks.append(res_blk)
        # output layer produces the same number of channels as the input (1 for now?)
        self.output_layer = layers.Conv1D(input_shape[-1], 1, padding="same")

    def call(self, inputs, training=None):
        """
        Forward pass
        """
        # just one input sequence
        x = inputs
        for ix in range(len(self.wavenet_blocks)):
            x = self.channel_match_convs[ix](x)
            x = self.wavenet_blocks[ix](x)
        return self.output_layer(x)
