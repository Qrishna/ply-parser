from ply_parser import *
import glob

if __name__ == "__main__":
    file = "cube.ply"
    parsed_object = parse_ply_file(file)
    if parsed_object:
        print("name:", parsed_object.name)
        print("total_vertices:", len(parsed_object.vertices))
        print("total_faces:", len(parsed_object.faces))
        print("total_colors:", len(parsed_object.colors))

        print("vertices:", parsed_object.vertices)
        print("faces:", parsed_object.faces)
        print("colors:", parsed_object.colors)

#bulk validator
# for ply_file in glob.glob("*.ply"):
#     print("\nThe file is: ", ply_file)
#
#     parsed_object = parse_ply_file(ply_file)
#     if parsed_object:
#         print("total_vertices:", len(parsed_object.vertices))
#         print("total_faces:", len(parsed_object.faces))
#         print("total_colors:", len(parsed_object.colors))
