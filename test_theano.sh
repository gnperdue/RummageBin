#!/bin/bash

# time nice python -c "import numpy; numpy.test()" &> >(tee -a numpy_test.log) 2> >(tee stderr.log >&2)
nice python -c "import numpy; numpy.test()" &> >(tee -a numpy_test.log)
nice python -c "import scipy; scipy.test()" &> >(tee -a scipy_test.log)
nice python -c "import theano; theano.test()" &> >(tee -a theano_test.log)

