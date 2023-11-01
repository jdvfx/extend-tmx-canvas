# extend-tmx-canvas
Extend tmx canvas size

usage:

1)
In this example.tmx, I manually updated the canvas size (on line 13)<br>
old: ```<image source="townInterior" width="32" height="18"/>```<br>
new: ```<image source="townInterior" width="64" height="36"/>```<br>

2)

Then, the script update all the layers to the new size:
```
python3 extend-tmx-canvas.py input_file output_file
```

3)
That's it, all the layers have the new size and the tile data has a bunch of extra zeros.
You now have a massive canvas!
