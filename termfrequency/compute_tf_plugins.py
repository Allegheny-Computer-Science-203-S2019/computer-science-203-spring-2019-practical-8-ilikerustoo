"""Compute term frequencies for an input file using a plugin style"""

import sys
import configparser
import importlib.machinery


def load_plugins():
    """Load the compiled Python plugins specified in the configuration file"""
    config = configparser.ConfigParser()
    config.read("config.ini")
    # either words1.pyc or words2.pyc
    words_plugin = config.get("Plugins", "Words")
    # either frequencies1.pyc or frequencies2.pyc
    frequencies_plugin = config.get("Plugins", "Frequencies")
    # pylint: disable=global-variable-undefined
    global tfwords, tffreqs
    # pylint: disable=no-value-for-parameter
    # pylint: disable=deprecated-method
    tfwords = importlib.machinery.SourcelessFileLoader(
        "tfwords", words_plugin
    ).load_module()
    tffreqs = importlib.machinery.SourcelessFileLoader(
        "tffreqs", frequencies_plugin
    ).load_module()


if __name__ == "__main__":

    load_plugins()
    word_freqs = tffreqs.top25(tfwords.extract_words(sys.argv[1]))
    for (w, c) in word_freqs:
        print(w, " - ", c)
