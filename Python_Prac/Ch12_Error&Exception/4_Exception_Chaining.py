#Example 1
try:
    open("Nofile.txt")
except OSError:
    raise RuntimeError("unable to handle error")

#Example 2
try:
    open("nofile.txt")
except OSError as exc:
    raise RuntimeError from exc