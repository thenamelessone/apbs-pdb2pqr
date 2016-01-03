""" PDB2PQR exceptions

This module represents errors specific to PDB2PQR. Exists mainly to allow us to more easily
distinguish between code errors and input errors.

Copyright (c) 2002-2016, Jens Erik Nielsen, University College Dublin; Nathan A. Baker, Battelle
Memorial Institute, Developed at the Pacific Northwest National Laboratory, operated by Battelle
Memorial Institute, Pacific Northwest Division for the U.S. Department Energy; Paul Czodrowski &
Gerhard Klebe, University of Marburg.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and
  the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions
  and the following disclaimer in the documentation and/or other materials provided with the
  distribution.
* Neither the names of University College Dublin, Battelle Memorial Institute, Pacific Northwest
  National Laboratory, US Department of Energy, or University of Marburg nor the names of its
  contributors may be used to endorse or promote products derived from this software without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. """

__date__ = "2016-01-02"
__author__ = "Kyle Monson, Nathan Baker"
__version__ = "1.8"

import inspect

class PDB2PQRError(Exception):
    """ An error for the PDB2PQR software """
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.line = inspect.currentframe().f_back.f_lineno
        self.filename = inspect.currentframe().f_back.f_code.co_filename
    def __str__(self):
        return '''DEBUG INFO: {errorType} {filename}: {line}
Error encountered: {message}'''.format(message=self.message,
                                       errorType=self.__class__.__name__,
                                       line=self.line,
                                       filename=self.filename)
class PDBInternalError(PDB2PQRError):
    """ Internal error """
    pass

class PDBInputError(PDB2PQRError):
    """ Input error """
    pass

class PDB2PKAError(PDB2PQRError):
    """ PDB2PKA error """
    pass

class PDBFileParseError(PDB2PQRError):
    """ PDB parsing error """
    def __init__(self, lineno, message):
        super().__init__(message)
        self.lineno = lineno
        self.message = message
    def __str__(self):
        return 'PDB file parsing error line {lineno}: {message}'.format(lineno=self.lineno,
                                                                        message=self.message)
