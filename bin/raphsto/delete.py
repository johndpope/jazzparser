#!/usr/bin/env ../jazzshell
"""
Deletes a trained Raphsto model.

"""
"""
============================== License ========================================
 Copyright (C) 2008, 2010-12 University of Edinburgh, Mark Granroth-Wilding
 
 This file is part of The Jazz Parser.
 
 The Jazz Parser is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 The Jazz Parser is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with The Jazz Parser.  If not, see <http://www.gnu.org/licenses/>.

============================ End license ======================================

"""
__author__ = "Mark Granroth-Wilding <mark.granroth-wilding@ed.ac.uk>" 

import sys, os
from optparse import OptionParser

from jazzparser.misc.raphsto import RaphstoHmm, RaphstoModelLoadError

def main():
    usage = "%prog [options] <model_name>"
    description = "Deletes all the files associated with a trained Raphsto model"
    parser = OptionParser(usage=usage, description=description)
    options, arguments = parser.parse_args()
    
    if len(arguments) < 1:
        print "You must specify a model name"
        sys.exit(1)
    model_name = arguments[0]
    
    # Check the model exists
    try:
        model = RaphstoHmm.load_model(model_name)
    except RaphstoModelLoadError:
        print "Could not load model %s" % model_name
        sys.exit(1)
    model.delete()
    print "Deleted model %s" % model_name
    
if __name__ == "__main__":
    main()
