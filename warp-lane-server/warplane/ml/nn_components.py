from typing import Union, List, Tuple, Optional

import tensorflow as tf
keras = tf.keras
layers = tf.keras.layers


class Mish(layers.Activation):
    '''
    Mish Activation Function.

    .. math::
        mish(x) = x * tanh(softplus(x)) = x * tanh(ln(1 + e^{x}))

    Shape:
        - Input: Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis)
        when using this layer as the first layer in a model.
        - Output: Same shape as the input.

    Examples
    --------
        >>> X = Activation('Mish', name="conv1_act")(X_input)
    '''

    def __init__(self, activation, **kwargs):
        super(Mish, self).__init__(activation, **kwargs)
        self.__name__ = 'Mish'


def mish(inputs:tf.Tensor) -> tf.Tensor:
    """
    Function shortcut to Mish activation

    Parameters
    ----------
    inputs:
        A tensorflow tensor or numpy array
    """
    return inputs * tf.math.tanh(tf.math.softplus(inputs))

# update activations list to provide string alias to mish activation
keras.utils.get_custom_objects().update({'Mish': Mish(mish)})


class WaveNetResidualConvBlock1D(layers.Layer):
    """
    A Residual "WaveNet" Block. 
    
    Essentially a stack of n_dilations 1D convolutional layers, each with num_filters 
    and kernel_size. The first layer's filters resolve successive entries in the input 
    sequence, while subsequent layers resolve every 2nd, 4th, ... 2^(n_dilations-1).
    """
    def __init__(
        self, 
        name:str,
        num_filters:int,
        kernel_size:int,
        n_dilations:int,
        **kwargs
    ):
        """
        Parameters
        ----------
        name: str
            The name given to the layer
        num_filters: int
            The number of filters in each constituent 1D convolutional layer.
        kernel_size: int
            The kernel size for each convolutional layer's filters
        n_dilations: int
            The number of different dilations (ranging from stride length 1 to 2^n_dilations).
            For example n_dilations = 3 implies 3 convolutional layers are assembled with 
            stride lengths 1, 2 and 4.
        """
        super(WaveNetResidualConvBlock1D, self).__init__(name=name, **kwargs)
        self.num_filters = num_filters
        self.kernel_size = kernel_size
        self.n_dilations = n_dilations
    
    @property
    def dilation_rates(self) -> List[int]:
        """
        Returns a list of the dilation rates used as fixed by n_dilations.
        """
        return [2**i for i in range(self.n_dilations)]

    def build(self, input_shape):
        self.sigmoid_conv_layers_1d = [
            layers.Conv1D(
                self.num_filters,
                self.kernel_size,
                dilation_rate=dilation_rate,
                padding='same',
                activation='sigmoid'
            ) 
            for dilation_rate in self.dilation_rates
        ]
        self.mish_conv_layers_1d = [
            layers.Conv1D(
                self.num_filters,
                self.kernel_size,
                dilation_rate=dilation_rate,
                padding='same', activation='Mish'
            )
            for dilation_rate in self.dilation_rates
        ]
        self.conv_1d_out = layers.Conv1D(self.num_filters, 1, padding='same')

    def call(self, x):
        """
        Forward pass
        """
        for dilation_ix in range(self.n_dilations):
            l_sigmoid_conv1d = self.sigmoid_conv_layers_1d[dilation_ix](x)
            l_mish_conv1d = self.mish_conv_layers_1d[dilation_ix](x)
            residual = layers.Multiply()([l_sigmoid_conv1d, l_mish_conv1d])
            residual = self.conv_1d_out(residual)
            resid_input = layers.Add()([x, residual])
        return resid_input


