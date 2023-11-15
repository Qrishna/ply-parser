### PLY File Parser
This Python module provides a simple PLY (Polygon File Format) file parser. It includes a class PLYObject for storing PLY file data and a function parse_ply_file for reading PLY files and creating PLYObject instances.

### Requirements
`Python 3.11.x`

### Installation
```
python3 -m pip install ply_parser
```


### Usage
### PLYObject Class
The PLYObject class represents a PLY object with attributes:

`name`: Name of the PLY object.

`vertices`: List of vertex coordinates.

`faces`: List of face indices.

`colors`: List of RGB color values for vertices.


#### parse_ply_file Function
The parse_ply_file function takes a PLY file as input and returns a PLYObject instance. It reads the file, extracts vertex and face information, and handles color properties. If any inconsistencies or errors are detected in the PLY file, appropriate error messages are displayed.
```
file = "data/cube_colors.ply"
parsed_object = parse_ply_file(file)
if parsed_object:
    print("name:", parsed_object.name)
    print("total_vertices:", len(parsed_object.vertices))
    print("total_faces:", len(parsed_object.faces))
    print("total_colors:", len(parsed_object.colors))
```


### PLY File Format Support
This parser currently supports PLY files with the following characteristics:

`ASCII format`

`Vertex coordinates (X, Y, Z)`

`Face indices (triangles and quads)`

`Vertex colors`

### Testing
```
python3 -m unittest tests/test_ply_parser.py -v
```

### Limitations
The parser assumes the input PLY file follows the standard specifications.
It may not handle non-standard or corrupted PLY files gracefully.


### Contribution
Feel free to contribute by opening issues or submitting pull requests. Bug reports, suggestions, and improvements are welcome.

### License
This PLY file parser is licensed under the MIT License. See the LICENSE file for details.

### Some info on how to publish packages to pypi
Reference: https://packaging.python.org/en/latest/tutorials/packaging-projects/

```
# upgrade pip and build tools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
```

#### Build
```
python3 -m build
```

##### That command genrates two files in the dist directory that looks like this
```
dist/
├── ply_parser-1.0.0-py3-none-any.whl
└── ply_parser-1.0.0-py3.tar.gz
```

##### The tar.gz file is a source distribution whereas the .whl file is a built distribution. Newer pip versions preferentially install built distributions, but will fall back to source distributions if needed. You should always upload a source distribution and provide built distributions for the platforms your project is compatible with

### Uploading the distribution archives
```#### To upload to test and prod pypi one needs have two separate accounts and auth tokens need to be setup and stored in $HOME/.pypirc```


#### Uploading to test environment - TestPyPI - https://test.pypi.org/
```
python3 -m twine upload --repository testpypi dist/*
```

##### Once uploaded the project becomes available at
```
https://test.pypi.org/project/ply_parser
```


##### Download and test the upload locally in a virtual environment
```
python3 -m venv test_env
source test_env/bin/activate
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps ply_parser
python3
# then do some tests here
```

##### Uploading to Production. 
####  Upload to PyPI - https://pypi.org
```
twine upload dist/*
```

#### The new package then becomes available at:  https://pypi.org/project/ply-parser/ and can be installed by
```
python3 -m pip install ply_parser
```



