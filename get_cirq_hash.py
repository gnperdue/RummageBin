'''
get the Git hash for a module (here, 'cirq') if we `pip install -e`'d the
module; if we installed via `pip` or `conda` directly (and `git describe`
fails), just get the dunder version.
'''
import os
import subprocess
import importlib
mod = importlib.import_module('cirq')

cwd = os.getcwd()
os.chdir(os.path.dirname(mod.__file__))
result = subprocess.run('git describe --abbrev=12 --dirty --always',
                        shell=True, stdout=subprocess.PIPE,
                        stderr=subprocess.DEVNULL)
hash = result.stdout.decode('utf-8').strip()
if hash == '':
  hash = mod.__version__
print(hash)
os.chdir(cwd)
