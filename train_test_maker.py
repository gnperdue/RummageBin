#!/usr/bin/env python
"""
Split a file into two new files: <filename>.test and <filename>.train. Here, we
use a probability to assign events to the train and test samples (the
probability supplied defines the percentage of events going into the training
sample). Because we use a probability and not a `mod` condition, this approach
works best for very large samples.

For example:

    python train_test_maker.py -f source_file -p 0.8 -r 123
    python train_test_maker.py --file source_file
"""
from __future__ import print_function


def make_train_test(filenam, probability, rseed):
    """
    Create two new files based on the `filenam` argument with new extensions
    (.train and .test). Include events in filenam in the .train file based on
    the probability argument (the probability tells you the fraction assigned
    to the .trin file). Set the random seed with the final argument.
    """
    import random
    import os.path

    if not os.path.isfile(filenam):
        print("The raw data file, %s, does not exist." % filenam)
        return

    train_name = filenam + ".train"
    test_name = filenam + ".test"

    train_file = open(train_name, "w")
    test_file = open(test_name, "w")

    with open(filenam, "r") as f:
        for line in f:
            if random.random() > probability:
                print(line, file=test_file, end="")
            else:
                print(line, file=train_file, end="")

    train_file.close()
    test_file.close()


if __name__ == '__main__':

    from optparse import OptionParser
    parser = OptionParser(usage=__doc__)
    parser.add_option('-f', '--file', dest='filenam', default='file.dat',
                      help='File name for full data set.', metavar='FILE NAME')
    parser.add_option('-p', '--probability', dest='prob', default=0.2,
                      help='The probability for an event to be placed in the'
                      ' training sample.',
                      metavar='P(TRAINING EVENT)')
    parser.add_option('-s', '--seed', dest='rseed', default=123,
                      help='Random number seed.', metavar='RANDOM SEED')
    (options, args) = parser.parse_args()

    make_train_test(options.filenam, options.prob, options.rseed)
