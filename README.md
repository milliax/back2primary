These python codes are written for DTES in Shanhua, Tainan.

# Enable utf-8 encoding

Owing to the lack of python support in Chinese we used in code. You will have to do some additional steps to enable it.

```bash
python3.7 -X utf8 <file name>
```

or setting the global environment variable directly

```bash
export PYTHONUTF8=1  # linux / macOS
```

```bash
set PYTHONUTF8=1 # windows
```