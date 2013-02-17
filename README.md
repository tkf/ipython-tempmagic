# Magics for temporary workspace

- `%cdtemp` -- Creates a temporary directory that is magically cleaned up
  when you exit IPython session.

- `%%with_temp_dir` -- Run Python code in a temporary directory and
  clean up it after the execution.

```text
%install_ext https://raw.github.com/tkf/ipython-tempmagic/master/tempmagic.py
```
