import os
import atexit

from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)
from IPython.utils.tempdir import TemporaryDirectory


@magics_class
class TempMagic(Magics):

    def __init__(self, *args, **kwds):
        super(TempMagic, self).__init__(*args, **kwds)
        self._temp_dirs = []
        atexit.register(self.cleanup_all)

    def cleanup_all(self):
        for td in self._temp_dirs:
            try:
                td.cleanup()
            except:
                pass
        self._temp_dirs[:] = []

    @magic_arguments()
    @argument('--suffix', '-s', default=None)
    @argument('--prefix', '-p', default=None)
    @argument('--directory', '-d', default=None)
    @line_magic
    def cdtemp(self, parameter_s=''):
        """
        Make temporal directory and change the current to there.

        The temporal directory made will be removed when the current
        IPython process terminates.

        """
        args = parse_argstring(self.cdtemp, parameter_s)
        kwds = dict(
            (k, v) for (k, v) in vars(args).iteritems() if v is not None)
        td = TemporaryDirectory(**kwds)
        self._temp_dirs.append(td)
        os.chdir(td.name)
        return td.name
