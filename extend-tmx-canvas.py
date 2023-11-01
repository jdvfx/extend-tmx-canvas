import xml.etree.ElementTree as ET
import sys

if len(sys.argv)!=3:
    print("expected syntax:\n$ python3 extend-tmx-canvas.py input_file output_file")
    quit()
input_file = sys.argv[1]
output_file = sys.argv[2]

tree = ET.parse(input_file)
root = tree.getroot()

with open(input_file,"r") as f:
    file_txt = f.read()

# get the new tile size
# wh(number of tiles)
w = int(str(root.get("width")))
h = int(str(root.get("height")))

number_of_tiles_extended = w*h
s2 = f"width={w} height={h}"

print("new size:" , number_of_tiles_extended, s2)
if number_of_tiles_extended==0:
    quit()

layers=0
for child in root:
    d  = child.find("data")
    if d is not None:
        layers+=1
        w_ = int(str(child.get("width")))
        h_ = int(str(child.get("height")))
        
        s1 = f'width="{w_}" height="{h_}"'
        file_txt = file_txt.replace(s1,s2)

        data = str(d.text)
        dd = data.replace("\n","")
        data_vec = dd.split(",")
        current_number_of_tiles = len(data_vec)

        # string of zeros with comas (,0,..,0)
        s = ","
        for i in range(number_of_tiles_extended-current_number_of_tiles):
            s+="0,"
        a = s[:-1]
        
        data = data[:-1]
        data2 = data + s[:-1]
        file_txt = file_txt.replace(data,data2)

print(f"{layers} layers updated")
with open(output_file,"w") as f:
    f.write(file_txt)
print(f"DONE, file witten: {output_file}")

