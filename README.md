# extend-tmx-canvas
Extend tmx canvas size

usage:

1)
in this example.tmx, I manually updated the original size (on line 13)
old:
  <image source="townInterior" width="32" height="18"/>
old:
  <image source="townInterior" width="64" height="36"/>

2)

then, use the script to update all the layers to the new size:
```
python3 extend-tmx-canvas.py input_file output_file
```

3)
that's it, we now have a massive canvas!
