from collections import OrderedDict

class BuildingSurfaceDetailed(object):
    """ Corresponds to IDD object `BuildingSurface:Detailed`
        Allows for detailed entry of building heat transfer surfaces.  Does not include subsurfaces such as windows or doors.
    """
    internal_name = "BuildingSurface:Detailed"
    field_count = 370

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `BuildingSurface:Detailed`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Type"] = None
        self._data["Construction Name"] = None
        self._data["Zone Name"] = None
        self._data["Outside Boundary Condition"] = None
        self._data["Outside Boundary Condition Object"] = None
        self._data["Sun Exposure"] = None
        self._data["Wind Exposure"] = None
        self._data["View Factor to Ground"] = None
        self._data["Number of Vertices"] = None
        self._data["Vertex 1 X-coordinate"] = None
        self._data["Vertex 1 Y-coordinate"] = None
        self._data["Vertex 1 Z-coordinate"] = None
        self._data["Vertex 2 X-coordinate"] = None
        self._data["Vertex 2 Y-coordinate"] = None
        self._data["Vertex 2 Z-coordinate"] = None
        self._data["Vertex 3 X-coordinate"] = None
        self._data["Vertex 3 Y-coordinate"] = None
        self._data["Vertex 3 Z-coordinate"] = None
        self._data["Vertex 4 X-coordinate"] = None
        self._data["Vertex 4 Y-coordinate"] = None
        self._data["Vertex 4 Z-coordinate"] = None
        self._data["Vertex 5 X-coordinate"] = None
        self._data["Vertex 5 Y-coordinate"] = None
        self._data["Vertex 5 Z-coordinate"] = None
        self._data["Vertex 6 X-coordinate"] = None
        self._data["Vertex 6 Y-coordinate"] = None
        self._data["Vertex 6 Z-coordinate"] = None
        self._data["Vertex 7 X-coordinate"] = None
        self._data["Vertex 7 Y-coordinate"] = None
        self._data["Vertex 7 Z-coordinate"] = None
        self._data["Vertex 8 X-coordinate"] = None
        self._data["Vertex 8 Y-coordinate"] = None
        self._data["Vertex 8 Z-coordinate"] = None
        self._data["Vertex 9 X-coordinate"] = None
        self._data["Vertex 9 Y-coordinate"] = None
        self._data["Vertex 9 Z-coordinate"] = None
        self._data["Vertex 10 X-coordinate"] = None
        self._data["Vertex 10 Y-coordinate"] = None
        self._data["Vertex 10 Z-coordinate"] = None
        self._data["Vertex 11 X-coordinate"] = None
        self._data["Vertex 11 Y-coordinate"] = None
        self._data["Vertex 11 Z-coordinate"] = None
        self._data["Vertex 12 X-coordinate"] = None
        self._data["Vertex 12 Y-coordinate"] = None
        self._data["Vertex 12 Z-coordinate"] = None
        self._data["Vertex 13 X-coordinate"] = None
        self._data["Vertex 13 Y-coordinate"] = None
        self._data["Vertex 13 Z-coordinate"] = None
        self._data["Vertex 14 X-coordinate"] = None
        self._data["Vertex 14 Y-coordinate"] = None
        self._data["Vertex 14 Z-coordinate"] = None
        self._data["Vertex 15 X-coordinate"] = None
        self._data["Vertex 15 Y-coordinate"] = None
        self._data["Vertex 15 Z-coordinate"] = None
        self._data["Vertex 16 X-coordinate"] = None
        self._data["Vertex 16 Y-coordinate"] = None
        self._data["Vertex 16 Z-coordinate"] = None
        self._data["Vertex 17 X-coordinate"] = None
        self._data["Vertex 17 Y-coordinate"] = None
        self._data["Vertex 17 Z-coordinate"] = None
        self._data["Vertex 18 X-coordinate"] = None
        self._data["Vertex 18 Y-coordinate"] = None
        self._data["Vertex 18 Z-coordinate"] = None
        self._data["Vertex 19 X-coordinate"] = None
        self._data["Vertex 19 Y-coordinate"] = None
        self._data["Vertex 19 Z-coordinate"] = None
        self._data["Vertex 20 X-coordinate"] = None
        self._data["Vertex 20 Y-coordinate"] = None
        self._data["Vertex 20 Z-coordinate"] = None
        self._data["Vertex 21 X-coordinate"] = None
        self._data["Vertex 21 Y-coordinate"] = None
        self._data["Vertex 21 Z-coordinate"] = None
        self._data["Vertex 22 X-coordinate"] = None
        self._data["Vertex 22 Y-coordinate"] = None
        self._data["Vertex 22 Z-coordinate"] = None
        self._data["Vertex 23 X-coordinate"] = None
        self._data["Vertex 23 Y-coordinate"] = None
        self._data["Vertex 23 Z-coordinate"] = None
        self._data["Vertex 24 X-coordinate"] = None
        self._data["Vertex 24 Y-coordinate"] = None
        self._data["Vertex 24 Z-coordinate"] = None
        self._data["Vertex 25 X-coordinate"] = None
        self._data["Vertex 25 Y-coordinate"] = None
        self._data["Vertex 25 Z-coordinate"] = None
        self._data["Vertex 26 X-coordinate"] = None
        self._data["Vertex 26 Y-coordinate"] = None
        self._data["Vertex 26 Z-coordinate"] = None
        self._data["Vertex 27 X-coordinate"] = None
        self._data["Vertex 27 Y-coordinate"] = None
        self._data["Vertex 27 Z-coordinate"] = None
        self._data["Vertex 28 X-coordinate"] = None
        self._data["Vertex 28 Y-coordinate"] = None
        self._data["Vertex 28 Z-coordinate"] = None
        self._data["Vertex 29 X-coordinate"] = None
        self._data["Vertex 29 Y-coordinate"] = None
        self._data["Vertex 29 Z-coordinate"] = None
        self._data["Vertex 30 X-coordinate"] = None
        self._data["Vertex 30 Y-coordinate"] = None
        self._data["Vertex 30 Z-coordinate"] = None
        self._data["Vertex 31 X-coordinate"] = None
        self._data["Vertex 31 Y-coordinate"] = None
        self._data["Vertex 31 Z-coordinate"] = None
        self._data["Vertex 32 X-coordinate"] = None
        self._data["Vertex 32 Y-coordinate"] = None
        self._data["Vertex 32 Z-coordinate"] = None
        self._data["Vertex 33 X-coordinate"] = None
        self._data["Vertex 33 Y-coordinate"] = None
        self._data["Vertex 33 Z-coordinate"] = None
        self._data["Vertex 34 X-coordinate"] = None
        self._data["Vertex 34 Y-coordinate"] = None
        self._data["Vertex 34 Z-coordinate"] = None
        self._data["Vertex 35 X-coordinate"] = None
        self._data["Vertex 35 Y-coordinate"] = None
        self._data["Vertex 35 Z-coordinate"] = None
        self._data["Vertex 36 X-coordinate"] = None
        self._data["Vertex 36 Y-coordinate"] = None
        self._data["Vertex 36 Z-coordinate"] = None
        self._data["Vertex 37 X-coordinate"] = None
        self._data["Vertex 37 Y-coordinate"] = None
        self._data["Vertex 37 Z-coordinate"] = None
        self._data["Vertex 38 X-coordinate"] = None
        self._data["Vertex 38 Y-coordinate"] = None
        self._data["Vertex 38 Z-coordinate"] = None
        self._data["Vertex 39 X-coordinate"] = None
        self._data["Vertex 39 Y-coordinate"] = None
        self._data["Vertex 39 Z-coordinate"] = None
        self._data["Vertex 40 X-coordinate"] = None
        self._data["Vertex 40 Y-coordinate"] = None
        self._data["Vertex 40 Z-coordinate"] = None
        self._data["Vertex 41 X-coordinate"] = None
        self._data["Vertex 41 Y-coordinate"] = None
        self._data["Vertex 41 Z-coordinate"] = None
        self._data["Vertex 42 X-coordinate"] = None
        self._data["Vertex 42 Y-coordinate"] = None
        self._data["Vertex 42 Z-coordinate"] = None
        self._data["Vertex 43 X-coordinate"] = None
        self._data["Vertex 43 Y-coordinate"] = None
        self._data["Vertex 43 Z-coordinate"] = None
        self._data["Vertex 44 X-coordinate"] = None
        self._data["Vertex 44 Y-coordinate"] = None
        self._data["Vertex 44 Z-coordinate"] = None
        self._data["Vertex 45 X-coordinate"] = None
        self._data["Vertex 45 Y-coordinate"] = None
        self._data["Vertex 45 Z-coordinate"] = None
        self._data["Vertex 46 X-coordinate"] = None
        self._data["Vertex 46 Y-coordinate"] = None
        self._data["Vertex 46 Z-coordinate"] = None
        self._data["Vertex 47 X-coordinate"] = None
        self._data["Vertex 47 Y-coordinate"] = None
        self._data["Vertex 47 Z-coordinate"] = None
        self._data["Vertex 48 X-coordinate"] = None
        self._data["Vertex 48 Y-coordinate"] = None
        self._data["Vertex 48 Z-coordinate"] = None
        self._data["Vertex 49 X-coordinate"] = None
        self._data["Vertex 49 Y-coordinate"] = None
        self._data["Vertex 49 Z-coordinate"] = None
        self._data["Vertex 50 X-coordinate"] = None
        self._data["Vertex 50 Y-coordinate"] = None
        self._data["Vertex 50 Z-coordinate"] = None
        self._data["Vertex 51 X-coordinate"] = None
        self._data["Vertex 51 Y-coordinate"] = None
        self._data["Vertex 51 Z-coordinate"] = None
        self._data["Vertex 52 X-coordinate"] = None
        self._data["Vertex 52 Y-coordinate"] = None
        self._data["Vertex 52 Z-coordinate"] = None
        self._data["Vertex 53 X-coordinate"] = None
        self._data["Vertex 53 Y-coordinate"] = None
        self._data["Vertex 53 Z-coordinate"] = None
        self._data["Vertex 54 X-coordinate"] = None
        self._data["Vertex 54 Y-coordinate"] = None
        self._data["Vertex 54 Z-coordinate"] = None
        self._data["Vertex 55 X-coordinate"] = None
        self._data["Vertex 55 Y-coordinate"] = None
        self._data["Vertex 55 Z-coordinate"] = None
        self._data["Vertex 56 X-coordinate"] = None
        self._data["Vertex 56 Y-coordinate"] = None
        self._data["Vertex 56 Z-coordinate"] = None
        self._data["Vertex 57 X-coordinate"] = None
        self._data["Vertex 57 Y-coordinate"] = None
        self._data["Vertex 57 Z-coordinate"] = None
        self._data["Vertex 58 X-coordinate"] = None
        self._data["Vertex 58 Y-coordinate"] = None
        self._data["Vertex 58 Z-coordinate"] = None
        self._data["Vertex 59 X-coordinate"] = None
        self._data["Vertex 59 Y-coordinate"] = None
        self._data["Vertex 59 Z-coordinate"] = None
        self._data["Vertex 60 X-coordinate"] = None
        self._data["Vertex 60 Y-coordinate"] = None
        self._data["Vertex 60 Z-coordinate"] = None
        self._data["Vertex 61 X-coordinate"] = None
        self._data["Vertex 61 Y-coordinate"] = None
        self._data["Vertex 61 Z-coordinate"] = None
        self._data["Vertex 62 X-coordinate"] = None
        self._data["Vertex 62 Y-coordinate"] = None
        self._data["Vertex 62 Z-coordinate"] = None
        self._data["Vertex 63 X-coordinate"] = None
        self._data["Vertex 63 Y-coordinate"] = None
        self._data["Vertex 63 Z-coordinate"] = None
        self._data["Vertex 64 X-coordinate"] = None
        self._data["Vertex 64 Y-coordinate"] = None
        self._data["Vertex 64 Z-coordinate"] = None
        self._data["Vertex 65 X-coordinate"] = None
        self._data["Vertex 65 Y-coordinate"] = None
        self._data["Vertex 65 Z-coordinate"] = None
        self._data["Vertex 66 X-coordinate"] = None
        self._data["Vertex 66 Y-coordinate"] = None
        self._data["Vertex 66 Z-coordinate"] = None
        self._data["Vertex 67 X-coordinate"] = None
        self._data["Vertex 67 Y-coordinate"] = None
        self._data["Vertex 67 Z-coordinate"] = None
        self._data["Vertex 68 X-coordinate"] = None
        self._data["Vertex 68 Y-coordinate"] = None
        self._data["Vertex 68 Z-coordinate"] = None
        self._data["Vertex 69 X-coordinate"] = None
        self._data["Vertex 69 Y-coordinate"] = None
        self._data["Vertex 69 Z-coordinate"] = None
        self._data["Vertex 70 X-coordinate"] = None
        self._data["Vertex 70 Y-coordinate"] = None
        self._data["Vertex 70 Z-coordinate"] = None
        self._data["Vertex 71 X-coordinate"] = None
        self._data["Vertex 71 Y-coordinate"] = None
        self._data["Vertex 71 Z-coordinate"] = None
        self._data["Vertex 72 X-coordinate"] = None
        self._data["Vertex 72 Y-coordinate"] = None
        self._data["Vertex 72 Z-coordinate"] = None
        self._data["Vertex 73 X-coordinate"] = None
        self._data["Vertex 73 Y-coordinate"] = None
        self._data["Vertex 73 Z-coordinate"] = None
        self._data["Vertex 74 X-coordinate"] = None
        self._data["Vertex 74 Y-coordinate"] = None
        self._data["Vertex 74 Z-coordinate"] = None
        self._data["Vertex 75 X-coordinate"] = None
        self._data["Vertex 75 Y-coordinate"] = None
        self._data["Vertex 75 Z-coordinate"] = None
        self._data["Vertex 76 X-coordinate"] = None
        self._data["Vertex 76 Y-coordinate"] = None
        self._data["Vertex 76 Z-coordinate"] = None
        self._data["Vertex 77 X-coordinate"] = None
        self._data["Vertex 77 Y-coordinate"] = None
        self._data["Vertex 77 Z-coordinate"] = None
        self._data["Vertex 78 X-coordinate"] = None
        self._data["Vertex 78 Y-coordinate"] = None
        self._data["Vertex 78 Z-coordinate"] = None
        self._data["Vertex 79 X-coordinate"] = None
        self._data["Vertex 79 Y-coordinate"] = None
        self._data["Vertex 79 Z-coordinate"] = None
        self._data["Vertex 80 X-coordinate"] = None
        self._data["Vertex 80 Y-coordinate"] = None
        self._data["Vertex 80 Z-coordinate"] = None
        self._data["Vertex 81 X-coordinate"] = None
        self._data["Vertex 81 Y-coordinate"] = None
        self._data["Vertex 81 Z-coordinate"] = None
        self._data["Vertex 82 X-coordinate"] = None
        self._data["Vertex 82 Y-coordinate"] = None
        self._data["Vertex 82 Z-coordinate"] = None
        self._data["Vertex 83 X-coordinate"] = None
        self._data["Vertex 83 Y-coordinate"] = None
        self._data["Vertex 83 Z-coordinate"] = None
        self._data["Vertex 84 X-coordinate"] = None
        self._data["Vertex 84 Y-coordinate"] = None
        self._data["Vertex 84 Z-coordinate"] = None
        self._data["Vertex 85 X-coordinate"] = None
        self._data["Vertex 85 Y-coordinate"] = None
        self._data["Vertex 85 Z-coordinate"] = None
        self._data["Vertex 86 X-coordinate"] = None
        self._data["Vertex 86 Y-coordinate"] = None
        self._data["Vertex 86 Z-coordinate"] = None
        self._data["Vertex 87 X-coordinate"] = None
        self._data["Vertex 87 Y-coordinate"] = None
        self._data["Vertex 87 Z-coordinate"] = None
        self._data["Vertex 88 X-coordinate"] = None
        self._data["Vertex 88 Y-coordinate"] = None
        self._data["Vertex 88 Z-coordinate"] = None
        self._data["Vertex 89 X-coordinate"] = None
        self._data["Vertex 89 Y-coordinate"] = None
        self._data["Vertex 89 Z-coordinate"] = None
        self._data["Vertex 90 X-coordinate"] = None
        self._data["Vertex 90 Y-coordinate"] = None
        self._data["Vertex 90 Z-coordinate"] = None
        self._data["Vertex 91 X-coordinate"] = None
        self._data["Vertex 91 Y-coordinate"] = None
        self._data["Vertex 91 Z-coordinate"] = None
        self._data["Vertex 92 X-coordinate"] = None
        self._data["Vertex 92 Y-coordinate"] = None
        self._data["Vertex 92 Z-coordinate"] = None
        self._data["Vertex 93 X-coordinate"] = None
        self._data["Vertex 93 Y-coordinate"] = None
        self._data["Vertex 93 Z-coordinate"] = None
        self._data["Vertex 94 X-coordinate"] = None
        self._data["Vertex 94 Y-coordinate"] = None
        self._data["Vertex 94 Z-coordinate"] = None
        self._data["Vertex 95 X-coordinate"] = None
        self._data["Vertex 95 Y-coordinate"] = None
        self._data["Vertex 95 Z-coordinate"] = None
        self._data["Vertex 96 X-coordinate"] = None
        self._data["Vertex 96 Y-coordinate"] = None
        self._data["Vertex 96 Z-coordinate"] = None
        self._data["Vertex 97 X-coordinate"] = None
        self._data["Vertex 97 Y-coordinate"] = None
        self._data["Vertex 97 Z-coordinate"] = None
        self._data["Vertex 98 X-coordinate"] = None
        self._data["Vertex 98 Y-coordinate"] = None
        self._data["Vertex 98 Z-coordinate"] = None
        self._data["Vertex 99 X-coordinate"] = None
        self._data["Vertex 99 Y-coordinate"] = None
        self._data["Vertex 99 Z-coordinate"] = None
        self._data["Vertex 100 X-coordinate"] = None
        self._data["Vertex 100 Y-coordinate"] = None
        self._data["Vertex 100 Z-coordinate"] = None
        self._data["Vertex 101 X-coordinate"] = None
        self._data["Vertex 101 Y-coordinate"] = None
        self._data["Vertex 101 Z-coordinate"] = None
        self._data["Vertex 102 X-coordinate"] = None
        self._data["Vertex 102 Y-coordinate"] = None
        self._data["Vertex 102 Z-coordinate"] = None
        self._data["Vertex 103 X-coordinate"] = None
        self._data["Vertex 103 Y-coordinate"] = None
        self._data["Vertex 103 Z-coordinate"] = None
        self._data["Vertex 104 X-coordinate"] = None
        self._data["Vertex 104 Y-coordinate"] = None
        self._data["Vertex 104 Z-coordinate"] = None
        self._data["Vertex 105 X-coordinate"] = None
        self._data["Vertex 105 Y-coordinate"] = None
        self._data["Vertex 105 Z-coordinate"] = None
        self._data["Vertex 106 X-coordinate"] = None
        self._data["Vertex 106 Y-coordinate"] = None
        self._data["Vertex 106 Z-coordinate"] = None
        self._data["Vertex 107 X-coordinate"] = None
        self._data["Vertex 107 Y-coordinate"] = None
        self._data["Vertex 107 Z-coordinate"] = None
        self._data["Vertex 108 X-coordinate"] = None
        self._data["Vertex 108 Y-coordinate"] = None
        self._data["Vertex 108 Z-coordinate"] = None
        self._data["Vertex 109 X-coordinate"] = None
        self._data["Vertex 109 Y-coordinate"] = None
        self._data["Vertex 109 Z-coordinate"] = None
        self._data["Vertex 110 X-coordinate"] = None
        self._data["Vertex 110 Y-coordinate"] = None
        self._data["Vertex 110 Z-coordinate"] = None
        self._data["Vertex 111 X-coordinate"] = None
        self._data["Vertex 111 Y-coordinate"] = None
        self._data["Vertex 111 Z-coordinate"] = None
        self._data["Vertex 112 X-coordinate"] = None
        self._data["Vertex 112 Y-coordinate"] = None
        self._data["Vertex 112 Z-coordinate"] = None
        self._data["Vertex 113 X-coordinate"] = None
        self._data["Vertex 113 Y-coordinate"] = None
        self._data["Vertex 113 Z-coordinate"] = None
        self._data["Vertex 114 X-coordinate"] = None
        self._data["Vertex 114 Y-coordinate"] = None
        self._data["Vertex 114 Z-coordinate"] = None
        self._data["Vertex 115 X-coordinate"] = None
        self._data["Vertex 115 Y-coordinate"] = None
        self._data["Vertex 115 Z-coordinate"] = None
        self._data["Vertex 116 X-coordinate"] = None
        self._data["Vertex 116 Y-coordinate"] = None
        self._data["Vertex 116 Z-coordinate"] = None
        self._data["Vertex 117 X-coordinate"] = None
        self._data["Vertex 117 Y-coordinate"] = None
        self._data["Vertex 117 Z-coordinate"] = None
        self._data["Vertex 118 X-coordinate"] = None
        self._data["Vertex 118 Y-coordinate"] = None
        self._data["Vertex 118 Z-coordinate"] = None
        self._data["Vertex 119 X-coordinate"] = None
        self._data["Vertex 119 Y-coordinate"] = None
        self._data["Vertex 119 Z-coordinate"] = None
        self._data["Vertex 120 X-coordinate"] = None
        self._data["Vertex 120 Y-coordinate"] = None
        self._data["Vertex 120 Z-coordinate"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_type = None
        else:
            self.surface_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_boundary_condition = None
        else:
            self.outside_boundary_condition = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_boundary_condition_object = None
        else:
            self.outside_boundary_condition_object = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.sun_exposure = None
        else:
            self.sun_exposure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.wind_exposure = None
        else:
            self.wind_exposure = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_to_ground = None
        else:
            self.view_factor_to_ground = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_vertices = None
        else:
            self.number_of_vertices = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_1_xcoordinate = None
        else:
            self.vertex_1_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_1_ycoordinate = None
        else:
            self.vertex_1_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_1_zcoordinate = None
        else:
            self.vertex_1_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_2_xcoordinate = None
        else:
            self.vertex_2_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_2_ycoordinate = None
        else:
            self.vertex_2_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_2_zcoordinate = None
        else:
            self.vertex_2_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_3_xcoordinate = None
        else:
            self.vertex_3_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_3_ycoordinate = None
        else:
            self.vertex_3_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_3_zcoordinate = None
        else:
            self.vertex_3_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_4_xcoordinate = None
        else:
            self.vertex_4_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_4_ycoordinate = None
        else:
            self.vertex_4_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_4_zcoordinate = None
        else:
            self.vertex_4_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_5_xcoordinate = None
        else:
            self.vertex_5_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_5_ycoordinate = None
        else:
            self.vertex_5_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_5_zcoordinate = None
        else:
            self.vertex_5_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_6_xcoordinate = None
        else:
            self.vertex_6_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_6_ycoordinate = None
        else:
            self.vertex_6_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_6_zcoordinate = None
        else:
            self.vertex_6_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_7_xcoordinate = None
        else:
            self.vertex_7_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_7_ycoordinate = None
        else:
            self.vertex_7_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_7_zcoordinate = None
        else:
            self.vertex_7_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_8_xcoordinate = None
        else:
            self.vertex_8_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_8_ycoordinate = None
        else:
            self.vertex_8_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_8_zcoordinate = None
        else:
            self.vertex_8_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_9_xcoordinate = None
        else:
            self.vertex_9_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_9_ycoordinate = None
        else:
            self.vertex_9_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_9_zcoordinate = None
        else:
            self.vertex_9_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_10_xcoordinate = None
        else:
            self.vertex_10_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_10_ycoordinate = None
        else:
            self.vertex_10_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_10_zcoordinate = None
        else:
            self.vertex_10_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_11_xcoordinate = None
        else:
            self.vertex_11_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_11_ycoordinate = None
        else:
            self.vertex_11_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_11_zcoordinate = None
        else:
            self.vertex_11_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_12_xcoordinate = None
        else:
            self.vertex_12_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_12_ycoordinate = None
        else:
            self.vertex_12_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_12_zcoordinate = None
        else:
            self.vertex_12_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_13_xcoordinate = None
        else:
            self.vertex_13_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_13_ycoordinate = None
        else:
            self.vertex_13_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_13_zcoordinate = None
        else:
            self.vertex_13_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_14_xcoordinate = None
        else:
            self.vertex_14_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_14_ycoordinate = None
        else:
            self.vertex_14_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_14_zcoordinate = None
        else:
            self.vertex_14_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_15_xcoordinate = None
        else:
            self.vertex_15_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_15_ycoordinate = None
        else:
            self.vertex_15_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_15_zcoordinate = None
        else:
            self.vertex_15_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_16_xcoordinate = None
        else:
            self.vertex_16_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_16_ycoordinate = None
        else:
            self.vertex_16_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_16_zcoordinate = None
        else:
            self.vertex_16_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_17_xcoordinate = None
        else:
            self.vertex_17_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_17_ycoordinate = None
        else:
            self.vertex_17_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_17_zcoordinate = None
        else:
            self.vertex_17_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_18_xcoordinate = None
        else:
            self.vertex_18_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_18_ycoordinate = None
        else:
            self.vertex_18_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_18_zcoordinate = None
        else:
            self.vertex_18_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_19_xcoordinate = None
        else:
            self.vertex_19_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_19_ycoordinate = None
        else:
            self.vertex_19_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_19_zcoordinate = None
        else:
            self.vertex_19_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_20_xcoordinate = None
        else:
            self.vertex_20_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_20_ycoordinate = None
        else:
            self.vertex_20_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_20_zcoordinate = None
        else:
            self.vertex_20_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_21_xcoordinate = None
        else:
            self.vertex_21_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_21_ycoordinate = None
        else:
            self.vertex_21_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_21_zcoordinate = None
        else:
            self.vertex_21_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_22_xcoordinate = None
        else:
            self.vertex_22_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_22_ycoordinate = None
        else:
            self.vertex_22_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_22_zcoordinate = None
        else:
            self.vertex_22_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_23_xcoordinate = None
        else:
            self.vertex_23_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_23_ycoordinate = None
        else:
            self.vertex_23_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_23_zcoordinate = None
        else:
            self.vertex_23_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_24_xcoordinate = None
        else:
            self.vertex_24_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_24_ycoordinate = None
        else:
            self.vertex_24_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_24_zcoordinate = None
        else:
            self.vertex_24_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_25_xcoordinate = None
        else:
            self.vertex_25_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_25_ycoordinate = None
        else:
            self.vertex_25_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_25_zcoordinate = None
        else:
            self.vertex_25_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_26_xcoordinate = None
        else:
            self.vertex_26_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_26_ycoordinate = None
        else:
            self.vertex_26_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_26_zcoordinate = None
        else:
            self.vertex_26_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_27_xcoordinate = None
        else:
            self.vertex_27_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_27_ycoordinate = None
        else:
            self.vertex_27_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_27_zcoordinate = None
        else:
            self.vertex_27_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_28_xcoordinate = None
        else:
            self.vertex_28_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_28_ycoordinate = None
        else:
            self.vertex_28_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_28_zcoordinate = None
        else:
            self.vertex_28_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_29_xcoordinate = None
        else:
            self.vertex_29_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_29_ycoordinate = None
        else:
            self.vertex_29_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_29_zcoordinate = None
        else:
            self.vertex_29_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_30_xcoordinate = None
        else:
            self.vertex_30_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_30_ycoordinate = None
        else:
            self.vertex_30_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_30_zcoordinate = None
        else:
            self.vertex_30_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_31_xcoordinate = None
        else:
            self.vertex_31_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_31_ycoordinate = None
        else:
            self.vertex_31_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_31_zcoordinate = None
        else:
            self.vertex_31_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_32_xcoordinate = None
        else:
            self.vertex_32_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_32_ycoordinate = None
        else:
            self.vertex_32_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_32_zcoordinate = None
        else:
            self.vertex_32_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_33_xcoordinate = None
        else:
            self.vertex_33_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_33_ycoordinate = None
        else:
            self.vertex_33_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_33_zcoordinate = None
        else:
            self.vertex_33_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_34_xcoordinate = None
        else:
            self.vertex_34_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_34_ycoordinate = None
        else:
            self.vertex_34_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_34_zcoordinate = None
        else:
            self.vertex_34_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_35_xcoordinate = None
        else:
            self.vertex_35_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_35_ycoordinate = None
        else:
            self.vertex_35_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_35_zcoordinate = None
        else:
            self.vertex_35_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_36_xcoordinate = None
        else:
            self.vertex_36_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_36_ycoordinate = None
        else:
            self.vertex_36_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_36_zcoordinate = None
        else:
            self.vertex_36_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_37_xcoordinate = None
        else:
            self.vertex_37_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_37_ycoordinate = None
        else:
            self.vertex_37_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_37_zcoordinate = None
        else:
            self.vertex_37_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_38_xcoordinate = None
        else:
            self.vertex_38_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_38_ycoordinate = None
        else:
            self.vertex_38_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_38_zcoordinate = None
        else:
            self.vertex_38_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_39_xcoordinate = None
        else:
            self.vertex_39_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_39_ycoordinate = None
        else:
            self.vertex_39_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_39_zcoordinate = None
        else:
            self.vertex_39_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_40_xcoordinate = None
        else:
            self.vertex_40_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_40_ycoordinate = None
        else:
            self.vertex_40_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_40_zcoordinate = None
        else:
            self.vertex_40_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_41_xcoordinate = None
        else:
            self.vertex_41_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_41_ycoordinate = None
        else:
            self.vertex_41_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_41_zcoordinate = None
        else:
            self.vertex_41_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_42_xcoordinate = None
        else:
            self.vertex_42_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_42_ycoordinate = None
        else:
            self.vertex_42_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_42_zcoordinate = None
        else:
            self.vertex_42_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_43_xcoordinate = None
        else:
            self.vertex_43_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_43_ycoordinate = None
        else:
            self.vertex_43_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_43_zcoordinate = None
        else:
            self.vertex_43_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_44_xcoordinate = None
        else:
            self.vertex_44_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_44_ycoordinate = None
        else:
            self.vertex_44_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_44_zcoordinate = None
        else:
            self.vertex_44_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_45_xcoordinate = None
        else:
            self.vertex_45_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_45_ycoordinate = None
        else:
            self.vertex_45_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_45_zcoordinate = None
        else:
            self.vertex_45_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_46_xcoordinate = None
        else:
            self.vertex_46_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_46_ycoordinate = None
        else:
            self.vertex_46_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_46_zcoordinate = None
        else:
            self.vertex_46_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_47_xcoordinate = None
        else:
            self.vertex_47_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_47_ycoordinate = None
        else:
            self.vertex_47_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_47_zcoordinate = None
        else:
            self.vertex_47_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_48_xcoordinate = None
        else:
            self.vertex_48_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_48_ycoordinate = None
        else:
            self.vertex_48_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_48_zcoordinate = None
        else:
            self.vertex_48_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_49_xcoordinate = None
        else:
            self.vertex_49_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_49_ycoordinate = None
        else:
            self.vertex_49_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_49_zcoordinate = None
        else:
            self.vertex_49_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_50_xcoordinate = None
        else:
            self.vertex_50_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_50_ycoordinate = None
        else:
            self.vertex_50_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_50_zcoordinate = None
        else:
            self.vertex_50_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_51_xcoordinate = None
        else:
            self.vertex_51_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_51_ycoordinate = None
        else:
            self.vertex_51_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_51_zcoordinate = None
        else:
            self.vertex_51_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_52_xcoordinate = None
        else:
            self.vertex_52_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_52_ycoordinate = None
        else:
            self.vertex_52_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_52_zcoordinate = None
        else:
            self.vertex_52_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_53_xcoordinate = None
        else:
            self.vertex_53_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_53_ycoordinate = None
        else:
            self.vertex_53_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_53_zcoordinate = None
        else:
            self.vertex_53_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_54_xcoordinate = None
        else:
            self.vertex_54_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_54_ycoordinate = None
        else:
            self.vertex_54_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_54_zcoordinate = None
        else:
            self.vertex_54_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_55_xcoordinate = None
        else:
            self.vertex_55_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_55_ycoordinate = None
        else:
            self.vertex_55_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_55_zcoordinate = None
        else:
            self.vertex_55_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_56_xcoordinate = None
        else:
            self.vertex_56_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_56_ycoordinate = None
        else:
            self.vertex_56_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_56_zcoordinate = None
        else:
            self.vertex_56_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_57_xcoordinate = None
        else:
            self.vertex_57_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_57_ycoordinate = None
        else:
            self.vertex_57_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_57_zcoordinate = None
        else:
            self.vertex_57_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_58_xcoordinate = None
        else:
            self.vertex_58_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_58_ycoordinate = None
        else:
            self.vertex_58_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_58_zcoordinate = None
        else:
            self.vertex_58_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_59_xcoordinate = None
        else:
            self.vertex_59_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_59_ycoordinate = None
        else:
            self.vertex_59_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_59_zcoordinate = None
        else:
            self.vertex_59_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_60_xcoordinate = None
        else:
            self.vertex_60_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_60_ycoordinate = None
        else:
            self.vertex_60_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_60_zcoordinate = None
        else:
            self.vertex_60_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_61_xcoordinate = None
        else:
            self.vertex_61_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_61_ycoordinate = None
        else:
            self.vertex_61_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_61_zcoordinate = None
        else:
            self.vertex_61_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_62_xcoordinate = None
        else:
            self.vertex_62_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_62_ycoordinate = None
        else:
            self.vertex_62_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_62_zcoordinate = None
        else:
            self.vertex_62_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_63_xcoordinate = None
        else:
            self.vertex_63_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_63_ycoordinate = None
        else:
            self.vertex_63_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_63_zcoordinate = None
        else:
            self.vertex_63_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_64_xcoordinate = None
        else:
            self.vertex_64_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_64_ycoordinate = None
        else:
            self.vertex_64_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_64_zcoordinate = None
        else:
            self.vertex_64_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_65_xcoordinate = None
        else:
            self.vertex_65_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_65_ycoordinate = None
        else:
            self.vertex_65_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_65_zcoordinate = None
        else:
            self.vertex_65_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_66_xcoordinate = None
        else:
            self.vertex_66_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_66_ycoordinate = None
        else:
            self.vertex_66_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_66_zcoordinate = None
        else:
            self.vertex_66_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_67_xcoordinate = None
        else:
            self.vertex_67_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_67_ycoordinate = None
        else:
            self.vertex_67_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_67_zcoordinate = None
        else:
            self.vertex_67_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_68_xcoordinate = None
        else:
            self.vertex_68_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_68_ycoordinate = None
        else:
            self.vertex_68_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_68_zcoordinate = None
        else:
            self.vertex_68_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_69_xcoordinate = None
        else:
            self.vertex_69_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_69_ycoordinate = None
        else:
            self.vertex_69_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_69_zcoordinate = None
        else:
            self.vertex_69_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_70_xcoordinate = None
        else:
            self.vertex_70_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_70_ycoordinate = None
        else:
            self.vertex_70_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_70_zcoordinate = None
        else:
            self.vertex_70_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_71_xcoordinate = None
        else:
            self.vertex_71_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_71_ycoordinate = None
        else:
            self.vertex_71_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_71_zcoordinate = None
        else:
            self.vertex_71_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_72_xcoordinate = None
        else:
            self.vertex_72_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_72_ycoordinate = None
        else:
            self.vertex_72_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_72_zcoordinate = None
        else:
            self.vertex_72_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_73_xcoordinate = None
        else:
            self.vertex_73_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_73_ycoordinate = None
        else:
            self.vertex_73_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_73_zcoordinate = None
        else:
            self.vertex_73_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_74_xcoordinate = None
        else:
            self.vertex_74_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_74_ycoordinate = None
        else:
            self.vertex_74_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_74_zcoordinate = None
        else:
            self.vertex_74_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_75_xcoordinate = None
        else:
            self.vertex_75_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_75_ycoordinate = None
        else:
            self.vertex_75_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_75_zcoordinate = None
        else:
            self.vertex_75_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_76_xcoordinate = None
        else:
            self.vertex_76_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_76_ycoordinate = None
        else:
            self.vertex_76_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_76_zcoordinate = None
        else:
            self.vertex_76_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_77_xcoordinate = None
        else:
            self.vertex_77_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_77_ycoordinate = None
        else:
            self.vertex_77_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_77_zcoordinate = None
        else:
            self.vertex_77_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_78_xcoordinate = None
        else:
            self.vertex_78_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_78_ycoordinate = None
        else:
            self.vertex_78_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_78_zcoordinate = None
        else:
            self.vertex_78_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_79_xcoordinate = None
        else:
            self.vertex_79_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_79_ycoordinate = None
        else:
            self.vertex_79_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_79_zcoordinate = None
        else:
            self.vertex_79_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_80_xcoordinate = None
        else:
            self.vertex_80_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_80_ycoordinate = None
        else:
            self.vertex_80_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_80_zcoordinate = None
        else:
            self.vertex_80_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_81_xcoordinate = None
        else:
            self.vertex_81_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_81_ycoordinate = None
        else:
            self.vertex_81_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_81_zcoordinate = None
        else:
            self.vertex_81_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_82_xcoordinate = None
        else:
            self.vertex_82_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_82_ycoordinate = None
        else:
            self.vertex_82_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_82_zcoordinate = None
        else:
            self.vertex_82_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_83_xcoordinate = None
        else:
            self.vertex_83_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_83_ycoordinate = None
        else:
            self.vertex_83_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_83_zcoordinate = None
        else:
            self.vertex_83_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_84_xcoordinate = None
        else:
            self.vertex_84_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_84_ycoordinate = None
        else:
            self.vertex_84_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_84_zcoordinate = None
        else:
            self.vertex_84_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_85_xcoordinate = None
        else:
            self.vertex_85_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_85_ycoordinate = None
        else:
            self.vertex_85_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_85_zcoordinate = None
        else:
            self.vertex_85_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_86_xcoordinate = None
        else:
            self.vertex_86_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_86_ycoordinate = None
        else:
            self.vertex_86_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_86_zcoordinate = None
        else:
            self.vertex_86_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_87_xcoordinate = None
        else:
            self.vertex_87_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_87_ycoordinate = None
        else:
            self.vertex_87_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_87_zcoordinate = None
        else:
            self.vertex_87_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_88_xcoordinate = None
        else:
            self.vertex_88_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_88_ycoordinate = None
        else:
            self.vertex_88_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_88_zcoordinate = None
        else:
            self.vertex_88_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_89_xcoordinate = None
        else:
            self.vertex_89_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_89_ycoordinate = None
        else:
            self.vertex_89_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_89_zcoordinate = None
        else:
            self.vertex_89_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_90_xcoordinate = None
        else:
            self.vertex_90_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_90_ycoordinate = None
        else:
            self.vertex_90_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_90_zcoordinate = None
        else:
            self.vertex_90_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_91_xcoordinate = None
        else:
            self.vertex_91_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_91_ycoordinate = None
        else:
            self.vertex_91_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_91_zcoordinate = None
        else:
            self.vertex_91_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_92_xcoordinate = None
        else:
            self.vertex_92_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_92_ycoordinate = None
        else:
            self.vertex_92_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_92_zcoordinate = None
        else:
            self.vertex_92_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_93_xcoordinate = None
        else:
            self.vertex_93_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_93_ycoordinate = None
        else:
            self.vertex_93_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_93_zcoordinate = None
        else:
            self.vertex_93_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_94_xcoordinate = None
        else:
            self.vertex_94_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_94_ycoordinate = None
        else:
            self.vertex_94_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_94_zcoordinate = None
        else:
            self.vertex_94_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_95_xcoordinate = None
        else:
            self.vertex_95_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_95_ycoordinate = None
        else:
            self.vertex_95_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_95_zcoordinate = None
        else:
            self.vertex_95_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_96_xcoordinate = None
        else:
            self.vertex_96_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_96_ycoordinate = None
        else:
            self.vertex_96_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_96_zcoordinate = None
        else:
            self.vertex_96_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_97_xcoordinate = None
        else:
            self.vertex_97_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_97_ycoordinate = None
        else:
            self.vertex_97_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_97_zcoordinate = None
        else:
            self.vertex_97_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_98_xcoordinate = None
        else:
            self.vertex_98_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_98_ycoordinate = None
        else:
            self.vertex_98_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_98_zcoordinate = None
        else:
            self.vertex_98_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_99_xcoordinate = None
        else:
            self.vertex_99_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_99_ycoordinate = None
        else:
            self.vertex_99_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_99_zcoordinate = None
        else:
            self.vertex_99_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_100_xcoordinate = None
        else:
            self.vertex_100_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_100_ycoordinate = None
        else:
            self.vertex_100_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_100_zcoordinate = None
        else:
            self.vertex_100_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_101_xcoordinate = None
        else:
            self.vertex_101_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_101_ycoordinate = None
        else:
            self.vertex_101_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_101_zcoordinate = None
        else:
            self.vertex_101_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_102_xcoordinate = None
        else:
            self.vertex_102_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_102_ycoordinate = None
        else:
            self.vertex_102_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_102_zcoordinate = None
        else:
            self.vertex_102_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_103_xcoordinate = None
        else:
            self.vertex_103_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_103_ycoordinate = None
        else:
            self.vertex_103_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_103_zcoordinate = None
        else:
            self.vertex_103_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_104_xcoordinate = None
        else:
            self.vertex_104_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_104_ycoordinate = None
        else:
            self.vertex_104_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_104_zcoordinate = None
        else:
            self.vertex_104_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_105_xcoordinate = None
        else:
            self.vertex_105_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_105_ycoordinate = None
        else:
            self.vertex_105_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_105_zcoordinate = None
        else:
            self.vertex_105_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_106_xcoordinate = None
        else:
            self.vertex_106_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_106_ycoordinate = None
        else:
            self.vertex_106_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_106_zcoordinate = None
        else:
            self.vertex_106_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_107_xcoordinate = None
        else:
            self.vertex_107_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_107_ycoordinate = None
        else:
            self.vertex_107_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_107_zcoordinate = None
        else:
            self.vertex_107_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_108_xcoordinate = None
        else:
            self.vertex_108_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_108_ycoordinate = None
        else:
            self.vertex_108_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_108_zcoordinate = None
        else:
            self.vertex_108_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_109_xcoordinate = None
        else:
            self.vertex_109_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_109_ycoordinate = None
        else:
            self.vertex_109_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_109_zcoordinate = None
        else:
            self.vertex_109_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_110_xcoordinate = None
        else:
            self.vertex_110_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_110_ycoordinate = None
        else:
            self.vertex_110_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_110_zcoordinate = None
        else:
            self.vertex_110_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_111_xcoordinate = None
        else:
            self.vertex_111_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_111_ycoordinate = None
        else:
            self.vertex_111_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_111_zcoordinate = None
        else:
            self.vertex_111_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_112_xcoordinate = None
        else:
            self.vertex_112_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_112_ycoordinate = None
        else:
            self.vertex_112_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_112_zcoordinate = None
        else:
            self.vertex_112_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_113_xcoordinate = None
        else:
            self.vertex_113_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_113_ycoordinate = None
        else:
            self.vertex_113_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_113_zcoordinate = None
        else:
            self.vertex_113_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_114_xcoordinate = None
        else:
            self.vertex_114_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_114_ycoordinate = None
        else:
            self.vertex_114_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_114_zcoordinate = None
        else:
            self.vertex_114_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_115_xcoordinate = None
        else:
            self.vertex_115_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_115_ycoordinate = None
        else:
            self.vertex_115_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_115_zcoordinate = None
        else:
            self.vertex_115_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_116_xcoordinate = None
        else:
            self.vertex_116_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_116_ycoordinate = None
        else:
            self.vertex_116_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_116_zcoordinate = None
        else:
            self.vertex_116_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_117_xcoordinate = None
        else:
            self.vertex_117_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_117_ycoordinate = None
        else:
            self.vertex_117_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_117_zcoordinate = None
        else:
            self.vertex_117_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_118_xcoordinate = None
        else:
            self.vertex_118_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_118_ycoordinate = None
        else:
            self.vertex_118_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_118_zcoordinate = None
        else:
            self.vertex_118_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_119_xcoordinate = None
        else:
            self.vertex_119_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_119_ycoordinate = None
        else:
            self.vertex_119_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_119_zcoordinate = None
        else:
            self.vertex_119_zcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_120_xcoordinate = None
        else:
            self.vertex_120_xcoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_120_ycoordinate = None
        else:
            self.vertex_120_ycoordinate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.vertex_120_zcoordinate = None
        else:
            self.vertex_120_zcoordinate = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def surface_type(self):
        """Get surface_type

        Returns:
            str: the value of `surface_type` or None if not set
        """
        return self._data["Surface Type"]

    @surface_type.setter
    def surface_type(self, value=None):
        """  Corresponds to IDD Field `surface_type`

        Args:
            value (str): value for IDD Field `surface_type`
                Accepted values are:
                      - Floor
                      - Wall
                      - Ceiling
                      - Roof
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_type`')
            vals = set()
            vals.add("Floor")
            vals.add("Wall")
            vals.add("Ceiling")
            vals.add("Roof")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `surface_type`'.format(value))

        self._data["Surface Type"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`
        To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `construction_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Zone the surface is a part of

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def outside_boundary_condition(self):
        """Get outside_boundary_condition

        Returns:
            str: the value of `outside_boundary_condition` or None if not set
        """
        return self._data["Outside Boundary Condition"]

    @outside_boundary_condition.setter
    def outside_boundary_condition(self, value=None):
        """  Corresponds to IDD Field `outside_boundary_condition`

        Args:
            value (str): value for IDD Field `outside_boundary_condition`
                Accepted values are:
                      - Adiabatic
                      - Surface
                      - Zone
                      - Outdoors
                      - Ground
                      - GroundFCfactorMethod
                      - OtherSideCoefficients
                      - OtherSideConditionsModel
                      - GroundSlabPreprocessorAverage
                      - GroundSlabPreprocessorCore
                      - GroundSlabPreprocessorPerimeter
                      - GroundBasementPreprocessorAverageWall
                      - GroundBasementPreprocessorAverageFloor
                      - GroundBasementPreprocessorUpperWall
                      - GroundBasementPreprocessorLowerWall
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outside_boundary_condition`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_boundary_condition`')
            vals = set()
            vals.add("Adiabatic")
            vals.add("Surface")
            vals.add("Zone")
            vals.add("Outdoors")
            vals.add("Ground")
            vals.add("GroundFCfactorMethod")
            vals.add("OtherSideCoefficients")
            vals.add("OtherSideConditionsModel")
            vals.add("GroundSlabPreprocessorAverage")
            vals.add("GroundSlabPreprocessorCore")
            vals.add("GroundSlabPreprocessorPerimeter")
            vals.add("GroundBasementPreprocessorAverageWall")
            vals.add("GroundBasementPreprocessorAverageFloor")
            vals.add("GroundBasementPreprocessorUpperWall")
            vals.add("GroundBasementPreprocessorLowerWall")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outside_boundary_condition`'.format(value))

        self._data["Outside Boundary Condition"] = value

    @property
    def outside_boundary_condition_object(self):
        """Get outside_boundary_condition_object

        Returns:
            str: the value of `outside_boundary_condition_object` or None if not set
        """
        return self._data["Outside Boundary Condition Object"]

    @outside_boundary_condition_object.setter
    def outside_boundary_condition_object(self, value=None):
        """  Corresponds to IDD Field `outside_boundary_condition_object`
        Non-blank only if the field Outside Boundary Condition is Surface,
        Zone, OtherSideCoefficients or OtherSideConditionsModel
        If Surface, specify name of corresponding surface in adjacent zone or
        specify current surface name for internal partition separating like zones
        If Zone, specify the name of the corresponding zone and
        the program will generate the corresponding interzone surface
        If OtherSideCoefficients, specify name of SurfaceProperty:OtherSideCoefficients
        If OtherSideConditionsModel, specify name of SurfaceProperty:OtherSideConditionsModel

        Args:
            value (str): value for IDD Field `outside_boundary_condition_object`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outside_boundary_condition_object`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_boundary_condition_object`')

        self._data["Outside Boundary Condition Object"] = value

    @property
    def sun_exposure(self):
        """Get sun_exposure

        Returns:
            str: the value of `sun_exposure` or None if not set
        """
        return self._data["Sun Exposure"]

    @sun_exposure.setter
    def sun_exposure(self, value="SunExposed"):
        """  Corresponds to IDD Field `sun_exposure`

        Args:
            value (str): value for IDD Field `sun_exposure`
                Accepted values are:
                      - SunExposed
                      - NoSun
                Default value: SunExposed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `sun_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sun_exposure`')
            vals = set()
            vals.add("SunExposed")
            vals.add("NoSun")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `sun_exposure`'.format(value))

        self._data["Sun Exposure"] = value

    @property
    def wind_exposure(self):
        """Get wind_exposure

        Returns:
            str: the value of `wind_exposure` or None if not set
        """
        return self._data["Wind Exposure"]

    @wind_exposure.setter
    def wind_exposure(self, value="WindExposed"):
        """  Corresponds to IDD Field `wind_exposure`

        Args:
            value (str): value for IDD Field `wind_exposure`
                Accepted values are:
                      - WindExposed
                      - NoWind
                Default value: WindExposed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `wind_exposure`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `wind_exposure`')
            vals = set()
            vals.add("WindExposed")
            vals.add("NoWind")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `wind_exposure`'.format(value))

        self._data["Wind Exposure"] = value

    @property
    def view_factor_to_ground(self):
        """Get view_factor_to_ground

        Returns:
            float: the value of `view_factor_to_ground` or None if not set
        """
        return self._data["View Factor to Ground"]

    @view_factor_to_ground.setter
    def view_factor_to_ground(self, value=None):
        """  Corresponds to IDD Field `view_factor_to_ground`
        From the exterior of the surface
        Unused if one uses the "reflections" options in Solar Distribution in Building input
        unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been specified.
        autocalculate will automatically calculate this value from the tilt of the surface

        Args:
            value (float): value for IDD Field `view_factor_to_ground`
                value >= 0.0
                value <= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `view_factor_to_ground`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `view_factor_to_ground`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_to_ground`')

        self._data["View Factor to Ground"] = value

    @property
    def number_of_vertices(self):
        """Get number_of_vertices

        Returns:
            float: the value of `number_of_vertices` or None if not set
        """
        return self._data["Number of Vertices"]

    @number_of_vertices.setter
    def number_of_vertices(self, value=None):
        """  Corresponds to IDD Field `number_of_vertices`
        shown with 120 vertex coordinates -- extensible object
        "extensible" -- duplicate last set of x,y,z coordinates (last 3 fields),
        remembering to remove ; from "inner" fields.
        for clarity in any error messages, renumber the fields as well.
        (and changing z terminator to a comma "," for all but last one which needs a semi-colon ";")
        vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates
        are "relative" to the Zone Origin.  If world, then building and zone origins are used
        for some internal calculations, but all coordinates are given in an "absolute" system.

        Args:
            value (float): value for IDD Field `number_of_vertices`
                value >= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_vertices`'.format(value))
            if value < 3.0:
                raise ValueError('value need to be greater or equal 3.0 '
                                 'for field `number_of_vertices`')

        self._data["Number of Vertices"] = value

    @property
    def vertex_1_xcoordinate(self):
        """Get vertex_1_xcoordinate

        Returns:
            float: the value of `vertex_1_xcoordinate` or None if not set
        """
        return self._data["Vertex 1 X-coordinate"]

    @vertex_1_xcoordinate.setter
    def vertex_1_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_1_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_1_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_1_xcoordinate`'.format(value))

        self._data["Vertex 1 X-coordinate"] = value

    @property
    def vertex_1_ycoordinate(self):
        """Get vertex_1_ycoordinate

        Returns:
            float: the value of `vertex_1_ycoordinate` or None if not set
        """
        return self._data["Vertex 1 Y-coordinate"]

    @vertex_1_ycoordinate.setter
    def vertex_1_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_1_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_1_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_1_ycoordinate`'.format(value))

        self._data["Vertex 1 Y-coordinate"] = value

    @property
    def vertex_1_zcoordinate(self):
        """Get vertex_1_zcoordinate

        Returns:
            float: the value of `vertex_1_zcoordinate` or None if not set
        """
        return self._data["Vertex 1 Z-coordinate"]

    @vertex_1_zcoordinate.setter
    def vertex_1_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_1_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_1_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_1_zcoordinate`'.format(value))

        self._data["Vertex 1 Z-coordinate"] = value

    @property
    def vertex_2_xcoordinate(self):
        """Get vertex_2_xcoordinate

        Returns:
            float: the value of `vertex_2_xcoordinate` or None if not set
        """
        return self._data["Vertex 2 X-coordinate"]

    @vertex_2_xcoordinate.setter
    def vertex_2_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_2_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_2_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_2_xcoordinate`'.format(value))

        self._data["Vertex 2 X-coordinate"] = value

    @property
    def vertex_2_ycoordinate(self):
        """Get vertex_2_ycoordinate

        Returns:
            float: the value of `vertex_2_ycoordinate` or None if not set
        """
        return self._data["Vertex 2 Y-coordinate"]

    @vertex_2_ycoordinate.setter
    def vertex_2_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_2_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_2_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_2_ycoordinate`'.format(value))

        self._data["Vertex 2 Y-coordinate"] = value

    @property
    def vertex_2_zcoordinate(self):
        """Get vertex_2_zcoordinate

        Returns:
            float: the value of `vertex_2_zcoordinate` or None if not set
        """
        return self._data["Vertex 2 Z-coordinate"]

    @vertex_2_zcoordinate.setter
    def vertex_2_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_2_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_2_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_2_zcoordinate`'.format(value))

        self._data["Vertex 2 Z-coordinate"] = value

    @property
    def vertex_3_xcoordinate(self):
        """Get vertex_3_xcoordinate

        Returns:
            float: the value of `vertex_3_xcoordinate` or None if not set
        """
        return self._data["Vertex 3 X-coordinate"]

    @vertex_3_xcoordinate.setter
    def vertex_3_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_3_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_3_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_3_xcoordinate`'.format(value))

        self._data["Vertex 3 X-coordinate"] = value

    @property
    def vertex_3_ycoordinate(self):
        """Get vertex_3_ycoordinate

        Returns:
            float: the value of `vertex_3_ycoordinate` or None if not set
        """
        return self._data["Vertex 3 Y-coordinate"]

    @vertex_3_ycoordinate.setter
    def vertex_3_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_3_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_3_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_3_ycoordinate`'.format(value))

        self._data["Vertex 3 Y-coordinate"] = value

    @property
    def vertex_3_zcoordinate(self):
        """Get vertex_3_zcoordinate

        Returns:
            float: the value of `vertex_3_zcoordinate` or None if not set
        """
        return self._data["Vertex 3 Z-coordinate"]

    @vertex_3_zcoordinate.setter
    def vertex_3_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_3_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_3_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_3_zcoordinate`'.format(value))

        self._data["Vertex 3 Z-coordinate"] = value

    @property
    def vertex_4_xcoordinate(self):
        """Get vertex_4_xcoordinate

        Returns:
            float: the value of `vertex_4_xcoordinate` or None if not set
        """
        return self._data["Vertex 4 X-coordinate"]

    @vertex_4_xcoordinate.setter
    def vertex_4_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_4_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_4_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_4_xcoordinate`'.format(value))

        self._data["Vertex 4 X-coordinate"] = value

    @property
    def vertex_4_ycoordinate(self):
        """Get vertex_4_ycoordinate

        Returns:
            float: the value of `vertex_4_ycoordinate` or None if not set
        """
        return self._data["Vertex 4 Y-coordinate"]

    @vertex_4_ycoordinate.setter
    def vertex_4_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_4_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_4_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_4_ycoordinate`'.format(value))

        self._data["Vertex 4 Y-coordinate"] = value

    @property
    def vertex_4_zcoordinate(self):
        """Get vertex_4_zcoordinate

        Returns:
            float: the value of `vertex_4_zcoordinate` or None if not set
        """
        return self._data["Vertex 4 Z-coordinate"]

    @vertex_4_zcoordinate.setter
    def vertex_4_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_4_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_4_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_4_zcoordinate`'.format(value))

        self._data["Vertex 4 Z-coordinate"] = value

    @property
    def vertex_5_xcoordinate(self):
        """Get vertex_5_xcoordinate

        Returns:
            float: the value of `vertex_5_xcoordinate` or None if not set
        """
        return self._data["Vertex 5 X-coordinate"]

    @vertex_5_xcoordinate.setter
    def vertex_5_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_5_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_5_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_5_xcoordinate`'.format(value))

        self._data["Vertex 5 X-coordinate"] = value

    @property
    def vertex_5_ycoordinate(self):
        """Get vertex_5_ycoordinate

        Returns:
            float: the value of `vertex_5_ycoordinate` or None if not set
        """
        return self._data["Vertex 5 Y-coordinate"]

    @vertex_5_ycoordinate.setter
    def vertex_5_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_5_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_5_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_5_ycoordinate`'.format(value))

        self._data["Vertex 5 Y-coordinate"] = value

    @property
    def vertex_5_zcoordinate(self):
        """Get vertex_5_zcoordinate

        Returns:
            float: the value of `vertex_5_zcoordinate` or None if not set
        """
        return self._data["Vertex 5 Z-coordinate"]

    @vertex_5_zcoordinate.setter
    def vertex_5_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_5_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_5_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_5_zcoordinate`'.format(value))

        self._data["Vertex 5 Z-coordinate"] = value

    @property
    def vertex_6_xcoordinate(self):
        """Get vertex_6_xcoordinate

        Returns:
            float: the value of `vertex_6_xcoordinate` or None if not set
        """
        return self._data["Vertex 6 X-coordinate"]

    @vertex_6_xcoordinate.setter
    def vertex_6_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_6_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_6_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_6_xcoordinate`'.format(value))

        self._data["Vertex 6 X-coordinate"] = value

    @property
    def vertex_6_ycoordinate(self):
        """Get vertex_6_ycoordinate

        Returns:
            float: the value of `vertex_6_ycoordinate` or None if not set
        """
        return self._data["Vertex 6 Y-coordinate"]

    @vertex_6_ycoordinate.setter
    def vertex_6_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_6_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_6_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_6_ycoordinate`'.format(value))

        self._data["Vertex 6 Y-coordinate"] = value

    @property
    def vertex_6_zcoordinate(self):
        """Get vertex_6_zcoordinate

        Returns:
            float: the value of `vertex_6_zcoordinate` or None if not set
        """
        return self._data["Vertex 6 Z-coordinate"]

    @vertex_6_zcoordinate.setter
    def vertex_6_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_6_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_6_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_6_zcoordinate`'.format(value))

        self._data["Vertex 6 Z-coordinate"] = value

    @property
    def vertex_7_xcoordinate(self):
        """Get vertex_7_xcoordinate

        Returns:
            float: the value of `vertex_7_xcoordinate` or None if not set
        """
        return self._data["Vertex 7 X-coordinate"]

    @vertex_7_xcoordinate.setter
    def vertex_7_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_7_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_7_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_7_xcoordinate`'.format(value))

        self._data["Vertex 7 X-coordinate"] = value

    @property
    def vertex_7_ycoordinate(self):
        """Get vertex_7_ycoordinate

        Returns:
            float: the value of `vertex_7_ycoordinate` or None if not set
        """
        return self._data["Vertex 7 Y-coordinate"]

    @vertex_7_ycoordinate.setter
    def vertex_7_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_7_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_7_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_7_ycoordinate`'.format(value))

        self._data["Vertex 7 Y-coordinate"] = value

    @property
    def vertex_7_zcoordinate(self):
        """Get vertex_7_zcoordinate

        Returns:
            float: the value of `vertex_7_zcoordinate` or None if not set
        """
        return self._data["Vertex 7 Z-coordinate"]

    @vertex_7_zcoordinate.setter
    def vertex_7_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_7_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_7_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_7_zcoordinate`'.format(value))

        self._data["Vertex 7 Z-coordinate"] = value

    @property
    def vertex_8_xcoordinate(self):
        """Get vertex_8_xcoordinate

        Returns:
            float: the value of `vertex_8_xcoordinate` or None if not set
        """
        return self._data["Vertex 8 X-coordinate"]

    @vertex_8_xcoordinate.setter
    def vertex_8_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_8_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_8_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_8_xcoordinate`'.format(value))

        self._data["Vertex 8 X-coordinate"] = value

    @property
    def vertex_8_ycoordinate(self):
        """Get vertex_8_ycoordinate

        Returns:
            float: the value of `vertex_8_ycoordinate` or None if not set
        """
        return self._data["Vertex 8 Y-coordinate"]

    @vertex_8_ycoordinate.setter
    def vertex_8_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_8_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_8_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_8_ycoordinate`'.format(value))

        self._data["Vertex 8 Y-coordinate"] = value

    @property
    def vertex_8_zcoordinate(self):
        """Get vertex_8_zcoordinate

        Returns:
            float: the value of `vertex_8_zcoordinate` or None if not set
        """
        return self._data["Vertex 8 Z-coordinate"]

    @vertex_8_zcoordinate.setter
    def vertex_8_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_8_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_8_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_8_zcoordinate`'.format(value))

        self._data["Vertex 8 Z-coordinate"] = value

    @property
    def vertex_9_xcoordinate(self):
        """Get vertex_9_xcoordinate

        Returns:
            float: the value of `vertex_9_xcoordinate` or None if not set
        """
        return self._data["Vertex 9 X-coordinate"]

    @vertex_9_xcoordinate.setter
    def vertex_9_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_9_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_9_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_9_xcoordinate`'.format(value))

        self._data["Vertex 9 X-coordinate"] = value

    @property
    def vertex_9_ycoordinate(self):
        """Get vertex_9_ycoordinate

        Returns:
            float: the value of `vertex_9_ycoordinate` or None if not set
        """
        return self._data["Vertex 9 Y-coordinate"]

    @vertex_9_ycoordinate.setter
    def vertex_9_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_9_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_9_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_9_ycoordinate`'.format(value))

        self._data["Vertex 9 Y-coordinate"] = value

    @property
    def vertex_9_zcoordinate(self):
        """Get vertex_9_zcoordinate

        Returns:
            float: the value of `vertex_9_zcoordinate` or None if not set
        """
        return self._data["Vertex 9 Z-coordinate"]

    @vertex_9_zcoordinate.setter
    def vertex_9_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_9_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_9_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_9_zcoordinate`'.format(value))

        self._data["Vertex 9 Z-coordinate"] = value

    @property
    def vertex_10_xcoordinate(self):
        """Get vertex_10_xcoordinate

        Returns:
            float: the value of `vertex_10_xcoordinate` or None if not set
        """
        return self._data["Vertex 10 X-coordinate"]

    @vertex_10_xcoordinate.setter
    def vertex_10_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_10_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_10_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_10_xcoordinate`'.format(value))

        self._data["Vertex 10 X-coordinate"] = value

    @property
    def vertex_10_ycoordinate(self):
        """Get vertex_10_ycoordinate

        Returns:
            float: the value of `vertex_10_ycoordinate` or None if not set
        """
        return self._data["Vertex 10 Y-coordinate"]

    @vertex_10_ycoordinate.setter
    def vertex_10_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_10_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_10_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_10_ycoordinate`'.format(value))

        self._data["Vertex 10 Y-coordinate"] = value

    @property
    def vertex_10_zcoordinate(self):
        """Get vertex_10_zcoordinate

        Returns:
            float: the value of `vertex_10_zcoordinate` or None if not set
        """
        return self._data["Vertex 10 Z-coordinate"]

    @vertex_10_zcoordinate.setter
    def vertex_10_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_10_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_10_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_10_zcoordinate`'.format(value))

        self._data["Vertex 10 Z-coordinate"] = value

    @property
    def vertex_11_xcoordinate(self):
        """Get vertex_11_xcoordinate

        Returns:
            float: the value of `vertex_11_xcoordinate` or None if not set
        """
        return self._data["Vertex 11 X-coordinate"]

    @vertex_11_xcoordinate.setter
    def vertex_11_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_11_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_11_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_11_xcoordinate`'.format(value))

        self._data["Vertex 11 X-coordinate"] = value

    @property
    def vertex_11_ycoordinate(self):
        """Get vertex_11_ycoordinate

        Returns:
            float: the value of `vertex_11_ycoordinate` or None if not set
        """
        return self._data["Vertex 11 Y-coordinate"]

    @vertex_11_ycoordinate.setter
    def vertex_11_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_11_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_11_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_11_ycoordinate`'.format(value))

        self._data["Vertex 11 Y-coordinate"] = value

    @property
    def vertex_11_zcoordinate(self):
        """Get vertex_11_zcoordinate

        Returns:
            float: the value of `vertex_11_zcoordinate` or None if not set
        """
        return self._data["Vertex 11 Z-coordinate"]

    @vertex_11_zcoordinate.setter
    def vertex_11_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_11_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_11_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_11_zcoordinate`'.format(value))

        self._data["Vertex 11 Z-coordinate"] = value

    @property
    def vertex_12_xcoordinate(self):
        """Get vertex_12_xcoordinate

        Returns:
            float: the value of `vertex_12_xcoordinate` or None if not set
        """
        return self._data["Vertex 12 X-coordinate"]

    @vertex_12_xcoordinate.setter
    def vertex_12_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_12_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_12_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_12_xcoordinate`'.format(value))

        self._data["Vertex 12 X-coordinate"] = value

    @property
    def vertex_12_ycoordinate(self):
        """Get vertex_12_ycoordinate

        Returns:
            float: the value of `vertex_12_ycoordinate` or None if not set
        """
        return self._data["Vertex 12 Y-coordinate"]

    @vertex_12_ycoordinate.setter
    def vertex_12_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_12_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_12_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_12_ycoordinate`'.format(value))

        self._data["Vertex 12 Y-coordinate"] = value

    @property
    def vertex_12_zcoordinate(self):
        """Get vertex_12_zcoordinate

        Returns:
            float: the value of `vertex_12_zcoordinate` or None if not set
        """
        return self._data["Vertex 12 Z-coordinate"]

    @vertex_12_zcoordinate.setter
    def vertex_12_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_12_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_12_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_12_zcoordinate`'.format(value))

        self._data["Vertex 12 Z-coordinate"] = value

    @property
    def vertex_13_xcoordinate(self):
        """Get vertex_13_xcoordinate

        Returns:
            float: the value of `vertex_13_xcoordinate` or None if not set
        """
        return self._data["Vertex 13 X-coordinate"]

    @vertex_13_xcoordinate.setter
    def vertex_13_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_13_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_13_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_13_xcoordinate`'.format(value))

        self._data["Vertex 13 X-coordinate"] = value

    @property
    def vertex_13_ycoordinate(self):
        """Get vertex_13_ycoordinate

        Returns:
            float: the value of `vertex_13_ycoordinate` or None if not set
        """
        return self._data["Vertex 13 Y-coordinate"]

    @vertex_13_ycoordinate.setter
    def vertex_13_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_13_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_13_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_13_ycoordinate`'.format(value))

        self._data["Vertex 13 Y-coordinate"] = value

    @property
    def vertex_13_zcoordinate(self):
        """Get vertex_13_zcoordinate

        Returns:
            float: the value of `vertex_13_zcoordinate` or None if not set
        """
        return self._data["Vertex 13 Z-coordinate"]

    @vertex_13_zcoordinate.setter
    def vertex_13_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_13_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_13_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_13_zcoordinate`'.format(value))

        self._data["Vertex 13 Z-coordinate"] = value

    @property
    def vertex_14_xcoordinate(self):
        """Get vertex_14_xcoordinate

        Returns:
            float: the value of `vertex_14_xcoordinate` or None if not set
        """
        return self._data["Vertex 14 X-coordinate"]

    @vertex_14_xcoordinate.setter
    def vertex_14_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_14_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_14_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_14_xcoordinate`'.format(value))

        self._data["Vertex 14 X-coordinate"] = value

    @property
    def vertex_14_ycoordinate(self):
        """Get vertex_14_ycoordinate

        Returns:
            float: the value of `vertex_14_ycoordinate` or None if not set
        """
        return self._data["Vertex 14 Y-coordinate"]

    @vertex_14_ycoordinate.setter
    def vertex_14_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_14_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_14_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_14_ycoordinate`'.format(value))

        self._data["Vertex 14 Y-coordinate"] = value

    @property
    def vertex_14_zcoordinate(self):
        """Get vertex_14_zcoordinate

        Returns:
            float: the value of `vertex_14_zcoordinate` or None if not set
        """
        return self._data["Vertex 14 Z-coordinate"]

    @vertex_14_zcoordinate.setter
    def vertex_14_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_14_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_14_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_14_zcoordinate`'.format(value))

        self._data["Vertex 14 Z-coordinate"] = value

    @property
    def vertex_15_xcoordinate(self):
        """Get vertex_15_xcoordinate

        Returns:
            float: the value of `vertex_15_xcoordinate` or None if not set
        """
        return self._data["Vertex 15 X-coordinate"]

    @vertex_15_xcoordinate.setter
    def vertex_15_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_15_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_15_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_15_xcoordinate`'.format(value))

        self._data["Vertex 15 X-coordinate"] = value

    @property
    def vertex_15_ycoordinate(self):
        """Get vertex_15_ycoordinate

        Returns:
            float: the value of `vertex_15_ycoordinate` or None if not set
        """
        return self._data["Vertex 15 Y-coordinate"]

    @vertex_15_ycoordinate.setter
    def vertex_15_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_15_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_15_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_15_ycoordinate`'.format(value))

        self._data["Vertex 15 Y-coordinate"] = value

    @property
    def vertex_15_zcoordinate(self):
        """Get vertex_15_zcoordinate

        Returns:
            float: the value of `vertex_15_zcoordinate` or None if not set
        """
        return self._data["Vertex 15 Z-coordinate"]

    @vertex_15_zcoordinate.setter
    def vertex_15_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_15_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_15_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_15_zcoordinate`'.format(value))

        self._data["Vertex 15 Z-coordinate"] = value

    @property
    def vertex_16_xcoordinate(self):
        """Get vertex_16_xcoordinate

        Returns:
            float: the value of `vertex_16_xcoordinate` or None if not set
        """
        return self._data["Vertex 16 X-coordinate"]

    @vertex_16_xcoordinate.setter
    def vertex_16_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_16_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_16_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_16_xcoordinate`'.format(value))

        self._data["Vertex 16 X-coordinate"] = value

    @property
    def vertex_16_ycoordinate(self):
        """Get vertex_16_ycoordinate

        Returns:
            float: the value of `vertex_16_ycoordinate` or None if not set
        """
        return self._data["Vertex 16 Y-coordinate"]

    @vertex_16_ycoordinate.setter
    def vertex_16_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_16_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_16_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_16_ycoordinate`'.format(value))

        self._data["Vertex 16 Y-coordinate"] = value

    @property
    def vertex_16_zcoordinate(self):
        """Get vertex_16_zcoordinate

        Returns:
            float: the value of `vertex_16_zcoordinate` or None if not set
        """
        return self._data["Vertex 16 Z-coordinate"]

    @vertex_16_zcoordinate.setter
    def vertex_16_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_16_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_16_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_16_zcoordinate`'.format(value))

        self._data["Vertex 16 Z-coordinate"] = value

    @property
    def vertex_17_xcoordinate(self):
        """Get vertex_17_xcoordinate

        Returns:
            float: the value of `vertex_17_xcoordinate` or None if not set
        """
        return self._data["Vertex 17 X-coordinate"]

    @vertex_17_xcoordinate.setter
    def vertex_17_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_17_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_17_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_17_xcoordinate`'.format(value))

        self._data["Vertex 17 X-coordinate"] = value

    @property
    def vertex_17_ycoordinate(self):
        """Get vertex_17_ycoordinate

        Returns:
            float: the value of `vertex_17_ycoordinate` or None if not set
        """
        return self._data["Vertex 17 Y-coordinate"]

    @vertex_17_ycoordinate.setter
    def vertex_17_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_17_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_17_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_17_ycoordinate`'.format(value))

        self._data["Vertex 17 Y-coordinate"] = value

    @property
    def vertex_17_zcoordinate(self):
        """Get vertex_17_zcoordinate

        Returns:
            float: the value of `vertex_17_zcoordinate` or None if not set
        """
        return self._data["Vertex 17 Z-coordinate"]

    @vertex_17_zcoordinate.setter
    def vertex_17_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_17_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_17_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_17_zcoordinate`'.format(value))

        self._data["Vertex 17 Z-coordinate"] = value

    @property
    def vertex_18_xcoordinate(self):
        """Get vertex_18_xcoordinate

        Returns:
            float: the value of `vertex_18_xcoordinate` or None if not set
        """
        return self._data["Vertex 18 X-coordinate"]

    @vertex_18_xcoordinate.setter
    def vertex_18_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_18_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_18_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_18_xcoordinate`'.format(value))

        self._data["Vertex 18 X-coordinate"] = value

    @property
    def vertex_18_ycoordinate(self):
        """Get vertex_18_ycoordinate

        Returns:
            float: the value of `vertex_18_ycoordinate` or None if not set
        """
        return self._data["Vertex 18 Y-coordinate"]

    @vertex_18_ycoordinate.setter
    def vertex_18_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_18_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_18_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_18_ycoordinate`'.format(value))

        self._data["Vertex 18 Y-coordinate"] = value

    @property
    def vertex_18_zcoordinate(self):
        """Get vertex_18_zcoordinate

        Returns:
            float: the value of `vertex_18_zcoordinate` or None if not set
        """
        return self._data["Vertex 18 Z-coordinate"]

    @vertex_18_zcoordinate.setter
    def vertex_18_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_18_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_18_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_18_zcoordinate`'.format(value))

        self._data["Vertex 18 Z-coordinate"] = value

    @property
    def vertex_19_xcoordinate(self):
        """Get vertex_19_xcoordinate

        Returns:
            float: the value of `vertex_19_xcoordinate` or None if not set
        """
        return self._data["Vertex 19 X-coordinate"]

    @vertex_19_xcoordinate.setter
    def vertex_19_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_19_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_19_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_19_xcoordinate`'.format(value))

        self._data["Vertex 19 X-coordinate"] = value

    @property
    def vertex_19_ycoordinate(self):
        """Get vertex_19_ycoordinate

        Returns:
            float: the value of `vertex_19_ycoordinate` or None if not set
        """
        return self._data["Vertex 19 Y-coordinate"]

    @vertex_19_ycoordinate.setter
    def vertex_19_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_19_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_19_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_19_ycoordinate`'.format(value))

        self._data["Vertex 19 Y-coordinate"] = value

    @property
    def vertex_19_zcoordinate(self):
        """Get vertex_19_zcoordinate

        Returns:
            float: the value of `vertex_19_zcoordinate` or None if not set
        """
        return self._data["Vertex 19 Z-coordinate"]

    @vertex_19_zcoordinate.setter
    def vertex_19_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_19_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_19_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_19_zcoordinate`'.format(value))

        self._data["Vertex 19 Z-coordinate"] = value

    @property
    def vertex_20_xcoordinate(self):
        """Get vertex_20_xcoordinate

        Returns:
            float: the value of `vertex_20_xcoordinate` or None if not set
        """
        return self._data["Vertex 20 X-coordinate"]

    @vertex_20_xcoordinate.setter
    def vertex_20_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_20_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_20_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_20_xcoordinate`'.format(value))

        self._data["Vertex 20 X-coordinate"] = value

    @property
    def vertex_20_ycoordinate(self):
        """Get vertex_20_ycoordinate

        Returns:
            float: the value of `vertex_20_ycoordinate` or None if not set
        """
        return self._data["Vertex 20 Y-coordinate"]

    @vertex_20_ycoordinate.setter
    def vertex_20_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_20_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_20_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_20_ycoordinate`'.format(value))

        self._data["Vertex 20 Y-coordinate"] = value

    @property
    def vertex_20_zcoordinate(self):
        """Get vertex_20_zcoordinate

        Returns:
            float: the value of `vertex_20_zcoordinate` or None if not set
        """
        return self._data["Vertex 20 Z-coordinate"]

    @vertex_20_zcoordinate.setter
    def vertex_20_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_20_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_20_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_20_zcoordinate`'.format(value))

        self._data["Vertex 20 Z-coordinate"] = value

    @property
    def vertex_21_xcoordinate(self):
        """Get vertex_21_xcoordinate

        Returns:
            float: the value of `vertex_21_xcoordinate` or None if not set
        """
        return self._data["Vertex 21 X-coordinate"]

    @vertex_21_xcoordinate.setter
    def vertex_21_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_21_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_21_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_21_xcoordinate`'.format(value))

        self._data["Vertex 21 X-coordinate"] = value

    @property
    def vertex_21_ycoordinate(self):
        """Get vertex_21_ycoordinate

        Returns:
            float: the value of `vertex_21_ycoordinate` or None if not set
        """
        return self._data["Vertex 21 Y-coordinate"]

    @vertex_21_ycoordinate.setter
    def vertex_21_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_21_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_21_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_21_ycoordinate`'.format(value))

        self._data["Vertex 21 Y-coordinate"] = value

    @property
    def vertex_21_zcoordinate(self):
        """Get vertex_21_zcoordinate

        Returns:
            float: the value of `vertex_21_zcoordinate` or None if not set
        """
        return self._data["Vertex 21 Z-coordinate"]

    @vertex_21_zcoordinate.setter
    def vertex_21_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_21_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_21_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_21_zcoordinate`'.format(value))

        self._data["Vertex 21 Z-coordinate"] = value

    @property
    def vertex_22_xcoordinate(self):
        """Get vertex_22_xcoordinate

        Returns:
            float: the value of `vertex_22_xcoordinate` or None if not set
        """
        return self._data["Vertex 22 X-coordinate"]

    @vertex_22_xcoordinate.setter
    def vertex_22_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_22_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_22_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_22_xcoordinate`'.format(value))

        self._data["Vertex 22 X-coordinate"] = value

    @property
    def vertex_22_ycoordinate(self):
        """Get vertex_22_ycoordinate

        Returns:
            float: the value of `vertex_22_ycoordinate` or None if not set
        """
        return self._data["Vertex 22 Y-coordinate"]

    @vertex_22_ycoordinate.setter
    def vertex_22_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_22_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_22_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_22_ycoordinate`'.format(value))

        self._data["Vertex 22 Y-coordinate"] = value

    @property
    def vertex_22_zcoordinate(self):
        """Get vertex_22_zcoordinate

        Returns:
            float: the value of `vertex_22_zcoordinate` or None if not set
        """
        return self._data["Vertex 22 Z-coordinate"]

    @vertex_22_zcoordinate.setter
    def vertex_22_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_22_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_22_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_22_zcoordinate`'.format(value))

        self._data["Vertex 22 Z-coordinate"] = value

    @property
    def vertex_23_xcoordinate(self):
        """Get vertex_23_xcoordinate

        Returns:
            float: the value of `vertex_23_xcoordinate` or None if not set
        """
        return self._data["Vertex 23 X-coordinate"]

    @vertex_23_xcoordinate.setter
    def vertex_23_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_23_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_23_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_23_xcoordinate`'.format(value))

        self._data["Vertex 23 X-coordinate"] = value

    @property
    def vertex_23_ycoordinate(self):
        """Get vertex_23_ycoordinate

        Returns:
            float: the value of `vertex_23_ycoordinate` or None if not set
        """
        return self._data["Vertex 23 Y-coordinate"]

    @vertex_23_ycoordinate.setter
    def vertex_23_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_23_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_23_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_23_ycoordinate`'.format(value))

        self._data["Vertex 23 Y-coordinate"] = value

    @property
    def vertex_23_zcoordinate(self):
        """Get vertex_23_zcoordinate

        Returns:
            float: the value of `vertex_23_zcoordinate` or None if not set
        """
        return self._data["Vertex 23 Z-coordinate"]

    @vertex_23_zcoordinate.setter
    def vertex_23_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_23_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_23_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_23_zcoordinate`'.format(value))

        self._data["Vertex 23 Z-coordinate"] = value

    @property
    def vertex_24_xcoordinate(self):
        """Get vertex_24_xcoordinate

        Returns:
            float: the value of `vertex_24_xcoordinate` or None if not set
        """
        return self._data["Vertex 24 X-coordinate"]

    @vertex_24_xcoordinate.setter
    def vertex_24_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_24_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_24_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_24_xcoordinate`'.format(value))

        self._data["Vertex 24 X-coordinate"] = value

    @property
    def vertex_24_ycoordinate(self):
        """Get vertex_24_ycoordinate

        Returns:
            float: the value of `vertex_24_ycoordinate` or None if not set
        """
        return self._data["Vertex 24 Y-coordinate"]

    @vertex_24_ycoordinate.setter
    def vertex_24_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_24_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_24_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_24_ycoordinate`'.format(value))

        self._data["Vertex 24 Y-coordinate"] = value

    @property
    def vertex_24_zcoordinate(self):
        """Get vertex_24_zcoordinate

        Returns:
            float: the value of `vertex_24_zcoordinate` or None if not set
        """
        return self._data["Vertex 24 Z-coordinate"]

    @vertex_24_zcoordinate.setter
    def vertex_24_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_24_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_24_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_24_zcoordinate`'.format(value))

        self._data["Vertex 24 Z-coordinate"] = value

    @property
    def vertex_25_xcoordinate(self):
        """Get vertex_25_xcoordinate

        Returns:
            float: the value of `vertex_25_xcoordinate` or None if not set
        """
        return self._data["Vertex 25 X-coordinate"]

    @vertex_25_xcoordinate.setter
    def vertex_25_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_25_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_25_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_25_xcoordinate`'.format(value))

        self._data["Vertex 25 X-coordinate"] = value

    @property
    def vertex_25_ycoordinate(self):
        """Get vertex_25_ycoordinate

        Returns:
            float: the value of `vertex_25_ycoordinate` or None if not set
        """
        return self._data["Vertex 25 Y-coordinate"]

    @vertex_25_ycoordinate.setter
    def vertex_25_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_25_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_25_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_25_ycoordinate`'.format(value))

        self._data["Vertex 25 Y-coordinate"] = value

    @property
    def vertex_25_zcoordinate(self):
        """Get vertex_25_zcoordinate

        Returns:
            float: the value of `vertex_25_zcoordinate` or None if not set
        """
        return self._data["Vertex 25 Z-coordinate"]

    @vertex_25_zcoordinate.setter
    def vertex_25_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_25_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_25_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_25_zcoordinate`'.format(value))

        self._data["Vertex 25 Z-coordinate"] = value

    @property
    def vertex_26_xcoordinate(self):
        """Get vertex_26_xcoordinate

        Returns:
            float: the value of `vertex_26_xcoordinate` or None if not set
        """
        return self._data["Vertex 26 X-coordinate"]

    @vertex_26_xcoordinate.setter
    def vertex_26_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_26_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_26_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_26_xcoordinate`'.format(value))

        self._data["Vertex 26 X-coordinate"] = value

    @property
    def vertex_26_ycoordinate(self):
        """Get vertex_26_ycoordinate

        Returns:
            float: the value of `vertex_26_ycoordinate` or None if not set
        """
        return self._data["Vertex 26 Y-coordinate"]

    @vertex_26_ycoordinate.setter
    def vertex_26_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_26_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_26_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_26_ycoordinate`'.format(value))

        self._data["Vertex 26 Y-coordinate"] = value

    @property
    def vertex_26_zcoordinate(self):
        """Get vertex_26_zcoordinate

        Returns:
            float: the value of `vertex_26_zcoordinate` or None if not set
        """
        return self._data["Vertex 26 Z-coordinate"]

    @vertex_26_zcoordinate.setter
    def vertex_26_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_26_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_26_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_26_zcoordinate`'.format(value))

        self._data["Vertex 26 Z-coordinate"] = value

    @property
    def vertex_27_xcoordinate(self):
        """Get vertex_27_xcoordinate

        Returns:
            float: the value of `vertex_27_xcoordinate` or None if not set
        """
        return self._data["Vertex 27 X-coordinate"]

    @vertex_27_xcoordinate.setter
    def vertex_27_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_27_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_27_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_27_xcoordinate`'.format(value))

        self._data["Vertex 27 X-coordinate"] = value

    @property
    def vertex_27_ycoordinate(self):
        """Get vertex_27_ycoordinate

        Returns:
            float: the value of `vertex_27_ycoordinate` or None if not set
        """
        return self._data["Vertex 27 Y-coordinate"]

    @vertex_27_ycoordinate.setter
    def vertex_27_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_27_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_27_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_27_ycoordinate`'.format(value))

        self._data["Vertex 27 Y-coordinate"] = value

    @property
    def vertex_27_zcoordinate(self):
        """Get vertex_27_zcoordinate

        Returns:
            float: the value of `vertex_27_zcoordinate` or None if not set
        """
        return self._data["Vertex 27 Z-coordinate"]

    @vertex_27_zcoordinate.setter
    def vertex_27_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_27_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_27_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_27_zcoordinate`'.format(value))

        self._data["Vertex 27 Z-coordinate"] = value

    @property
    def vertex_28_xcoordinate(self):
        """Get vertex_28_xcoordinate

        Returns:
            float: the value of `vertex_28_xcoordinate` or None if not set
        """
        return self._data["Vertex 28 X-coordinate"]

    @vertex_28_xcoordinate.setter
    def vertex_28_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_28_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_28_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_28_xcoordinate`'.format(value))

        self._data["Vertex 28 X-coordinate"] = value

    @property
    def vertex_28_ycoordinate(self):
        """Get vertex_28_ycoordinate

        Returns:
            float: the value of `vertex_28_ycoordinate` or None if not set
        """
        return self._data["Vertex 28 Y-coordinate"]

    @vertex_28_ycoordinate.setter
    def vertex_28_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_28_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_28_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_28_ycoordinate`'.format(value))

        self._data["Vertex 28 Y-coordinate"] = value

    @property
    def vertex_28_zcoordinate(self):
        """Get vertex_28_zcoordinate

        Returns:
            float: the value of `vertex_28_zcoordinate` or None if not set
        """
        return self._data["Vertex 28 Z-coordinate"]

    @vertex_28_zcoordinate.setter
    def vertex_28_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_28_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_28_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_28_zcoordinate`'.format(value))

        self._data["Vertex 28 Z-coordinate"] = value

    @property
    def vertex_29_xcoordinate(self):
        """Get vertex_29_xcoordinate

        Returns:
            float: the value of `vertex_29_xcoordinate` or None if not set
        """
        return self._data["Vertex 29 X-coordinate"]

    @vertex_29_xcoordinate.setter
    def vertex_29_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_29_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_29_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_29_xcoordinate`'.format(value))

        self._data["Vertex 29 X-coordinate"] = value

    @property
    def vertex_29_ycoordinate(self):
        """Get vertex_29_ycoordinate

        Returns:
            float: the value of `vertex_29_ycoordinate` or None if not set
        """
        return self._data["Vertex 29 Y-coordinate"]

    @vertex_29_ycoordinate.setter
    def vertex_29_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_29_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_29_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_29_ycoordinate`'.format(value))

        self._data["Vertex 29 Y-coordinate"] = value

    @property
    def vertex_29_zcoordinate(self):
        """Get vertex_29_zcoordinate

        Returns:
            float: the value of `vertex_29_zcoordinate` or None if not set
        """
        return self._data["Vertex 29 Z-coordinate"]

    @vertex_29_zcoordinate.setter
    def vertex_29_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_29_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_29_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_29_zcoordinate`'.format(value))

        self._data["Vertex 29 Z-coordinate"] = value

    @property
    def vertex_30_xcoordinate(self):
        """Get vertex_30_xcoordinate

        Returns:
            float: the value of `vertex_30_xcoordinate` or None if not set
        """
        return self._data["Vertex 30 X-coordinate"]

    @vertex_30_xcoordinate.setter
    def vertex_30_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_30_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_30_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_30_xcoordinate`'.format(value))

        self._data["Vertex 30 X-coordinate"] = value

    @property
    def vertex_30_ycoordinate(self):
        """Get vertex_30_ycoordinate

        Returns:
            float: the value of `vertex_30_ycoordinate` or None if not set
        """
        return self._data["Vertex 30 Y-coordinate"]

    @vertex_30_ycoordinate.setter
    def vertex_30_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_30_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_30_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_30_ycoordinate`'.format(value))

        self._data["Vertex 30 Y-coordinate"] = value

    @property
    def vertex_30_zcoordinate(self):
        """Get vertex_30_zcoordinate

        Returns:
            float: the value of `vertex_30_zcoordinate` or None if not set
        """
        return self._data["Vertex 30 Z-coordinate"]

    @vertex_30_zcoordinate.setter
    def vertex_30_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_30_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_30_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_30_zcoordinate`'.format(value))

        self._data["Vertex 30 Z-coordinate"] = value

    @property
    def vertex_31_xcoordinate(self):
        """Get vertex_31_xcoordinate

        Returns:
            float: the value of `vertex_31_xcoordinate` or None if not set
        """
        return self._data["Vertex 31 X-coordinate"]

    @vertex_31_xcoordinate.setter
    def vertex_31_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_31_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_31_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_31_xcoordinate`'.format(value))

        self._data["Vertex 31 X-coordinate"] = value

    @property
    def vertex_31_ycoordinate(self):
        """Get vertex_31_ycoordinate

        Returns:
            float: the value of `vertex_31_ycoordinate` or None if not set
        """
        return self._data["Vertex 31 Y-coordinate"]

    @vertex_31_ycoordinate.setter
    def vertex_31_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_31_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_31_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_31_ycoordinate`'.format(value))

        self._data["Vertex 31 Y-coordinate"] = value

    @property
    def vertex_31_zcoordinate(self):
        """Get vertex_31_zcoordinate

        Returns:
            float: the value of `vertex_31_zcoordinate` or None if not set
        """
        return self._data["Vertex 31 Z-coordinate"]

    @vertex_31_zcoordinate.setter
    def vertex_31_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_31_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_31_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_31_zcoordinate`'.format(value))

        self._data["Vertex 31 Z-coordinate"] = value

    @property
    def vertex_32_xcoordinate(self):
        """Get vertex_32_xcoordinate

        Returns:
            float: the value of `vertex_32_xcoordinate` or None if not set
        """
        return self._data["Vertex 32 X-coordinate"]

    @vertex_32_xcoordinate.setter
    def vertex_32_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_32_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_32_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_32_xcoordinate`'.format(value))

        self._data["Vertex 32 X-coordinate"] = value

    @property
    def vertex_32_ycoordinate(self):
        """Get vertex_32_ycoordinate

        Returns:
            float: the value of `vertex_32_ycoordinate` or None if not set
        """
        return self._data["Vertex 32 Y-coordinate"]

    @vertex_32_ycoordinate.setter
    def vertex_32_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_32_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_32_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_32_ycoordinate`'.format(value))

        self._data["Vertex 32 Y-coordinate"] = value

    @property
    def vertex_32_zcoordinate(self):
        """Get vertex_32_zcoordinate

        Returns:
            float: the value of `vertex_32_zcoordinate` or None if not set
        """
        return self._data["Vertex 32 Z-coordinate"]

    @vertex_32_zcoordinate.setter
    def vertex_32_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_32_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_32_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_32_zcoordinate`'.format(value))

        self._data["Vertex 32 Z-coordinate"] = value

    @property
    def vertex_33_xcoordinate(self):
        """Get vertex_33_xcoordinate

        Returns:
            float: the value of `vertex_33_xcoordinate` or None if not set
        """
        return self._data["Vertex 33 X-coordinate"]

    @vertex_33_xcoordinate.setter
    def vertex_33_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_33_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_33_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_33_xcoordinate`'.format(value))

        self._data["Vertex 33 X-coordinate"] = value

    @property
    def vertex_33_ycoordinate(self):
        """Get vertex_33_ycoordinate

        Returns:
            float: the value of `vertex_33_ycoordinate` or None if not set
        """
        return self._data["Vertex 33 Y-coordinate"]

    @vertex_33_ycoordinate.setter
    def vertex_33_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_33_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_33_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_33_ycoordinate`'.format(value))

        self._data["Vertex 33 Y-coordinate"] = value

    @property
    def vertex_33_zcoordinate(self):
        """Get vertex_33_zcoordinate

        Returns:
            float: the value of `vertex_33_zcoordinate` or None if not set
        """
        return self._data["Vertex 33 Z-coordinate"]

    @vertex_33_zcoordinate.setter
    def vertex_33_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_33_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_33_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_33_zcoordinate`'.format(value))

        self._data["Vertex 33 Z-coordinate"] = value

    @property
    def vertex_34_xcoordinate(self):
        """Get vertex_34_xcoordinate

        Returns:
            float: the value of `vertex_34_xcoordinate` or None if not set
        """
        return self._data["Vertex 34 X-coordinate"]

    @vertex_34_xcoordinate.setter
    def vertex_34_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_34_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_34_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_34_xcoordinate`'.format(value))

        self._data["Vertex 34 X-coordinate"] = value

    @property
    def vertex_34_ycoordinate(self):
        """Get vertex_34_ycoordinate

        Returns:
            float: the value of `vertex_34_ycoordinate` or None if not set
        """
        return self._data["Vertex 34 Y-coordinate"]

    @vertex_34_ycoordinate.setter
    def vertex_34_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_34_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_34_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_34_ycoordinate`'.format(value))

        self._data["Vertex 34 Y-coordinate"] = value

    @property
    def vertex_34_zcoordinate(self):
        """Get vertex_34_zcoordinate

        Returns:
            float: the value of `vertex_34_zcoordinate` or None if not set
        """
        return self._data["Vertex 34 Z-coordinate"]

    @vertex_34_zcoordinate.setter
    def vertex_34_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_34_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_34_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_34_zcoordinate`'.format(value))

        self._data["Vertex 34 Z-coordinate"] = value

    @property
    def vertex_35_xcoordinate(self):
        """Get vertex_35_xcoordinate

        Returns:
            float: the value of `vertex_35_xcoordinate` or None if not set
        """
        return self._data["Vertex 35 X-coordinate"]

    @vertex_35_xcoordinate.setter
    def vertex_35_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_35_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_35_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_35_xcoordinate`'.format(value))

        self._data["Vertex 35 X-coordinate"] = value

    @property
    def vertex_35_ycoordinate(self):
        """Get vertex_35_ycoordinate

        Returns:
            float: the value of `vertex_35_ycoordinate` or None if not set
        """
        return self._data["Vertex 35 Y-coordinate"]

    @vertex_35_ycoordinate.setter
    def vertex_35_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_35_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_35_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_35_ycoordinate`'.format(value))

        self._data["Vertex 35 Y-coordinate"] = value

    @property
    def vertex_35_zcoordinate(self):
        """Get vertex_35_zcoordinate

        Returns:
            float: the value of `vertex_35_zcoordinate` or None if not set
        """
        return self._data["Vertex 35 Z-coordinate"]

    @vertex_35_zcoordinate.setter
    def vertex_35_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_35_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_35_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_35_zcoordinate`'.format(value))

        self._data["Vertex 35 Z-coordinate"] = value

    @property
    def vertex_36_xcoordinate(self):
        """Get vertex_36_xcoordinate

        Returns:
            float: the value of `vertex_36_xcoordinate` or None if not set
        """
        return self._data["Vertex 36 X-coordinate"]

    @vertex_36_xcoordinate.setter
    def vertex_36_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_36_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_36_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_36_xcoordinate`'.format(value))

        self._data["Vertex 36 X-coordinate"] = value

    @property
    def vertex_36_ycoordinate(self):
        """Get vertex_36_ycoordinate

        Returns:
            float: the value of `vertex_36_ycoordinate` or None if not set
        """
        return self._data["Vertex 36 Y-coordinate"]

    @vertex_36_ycoordinate.setter
    def vertex_36_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_36_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_36_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_36_ycoordinate`'.format(value))

        self._data["Vertex 36 Y-coordinate"] = value

    @property
    def vertex_36_zcoordinate(self):
        """Get vertex_36_zcoordinate

        Returns:
            float: the value of `vertex_36_zcoordinate` or None if not set
        """
        return self._data["Vertex 36 Z-coordinate"]

    @vertex_36_zcoordinate.setter
    def vertex_36_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_36_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_36_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_36_zcoordinate`'.format(value))

        self._data["Vertex 36 Z-coordinate"] = value

    @property
    def vertex_37_xcoordinate(self):
        """Get vertex_37_xcoordinate

        Returns:
            float: the value of `vertex_37_xcoordinate` or None if not set
        """
        return self._data["Vertex 37 X-coordinate"]

    @vertex_37_xcoordinate.setter
    def vertex_37_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_37_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_37_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_37_xcoordinate`'.format(value))

        self._data["Vertex 37 X-coordinate"] = value

    @property
    def vertex_37_ycoordinate(self):
        """Get vertex_37_ycoordinate

        Returns:
            float: the value of `vertex_37_ycoordinate` or None if not set
        """
        return self._data["Vertex 37 Y-coordinate"]

    @vertex_37_ycoordinate.setter
    def vertex_37_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_37_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_37_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_37_ycoordinate`'.format(value))

        self._data["Vertex 37 Y-coordinate"] = value

    @property
    def vertex_37_zcoordinate(self):
        """Get vertex_37_zcoordinate

        Returns:
            float: the value of `vertex_37_zcoordinate` or None if not set
        """
        return self._data["Vertex 37 Z-coordinate"]

    @vertex_37_zcoordinate.setter
    def vertex_37_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_37_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_37_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_37_zcoordinate`'.format(value))

        self._data["Vertex 37 Z-coordinate"] = value

    @property
    def vertex_38_xcoordinate(self):
        """Get vertex_38_xcoordinate

        Returns:
            float: the value of `vertex_38_xcoordinate` or None if not set
        """
        return self._data["Vertex 38 X-coordinate"]

    @vertex_38_xcoordinate.setter
    def vertex_38_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_38_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_38_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_38_xcoordinate`'.format(value))

        self._data["Vertex 38 X-coordinate"] = value

    @property
    def vertex_38_ycoordinate(self):
        """Get vertex_38_ycoordinate

        Returns:
            float: the value of `vertex_38_ycoordinate` or None if not set
        """
        return self._data["Vertex 38 Y-coordinate"]

    @vertex_38_ycoordinate.setter
    def vertex_38_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_38_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_38_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_38_ycoordinate`'.format(value))

        self._data["Vertex 38 Y-coordinate"] = value

    @property
    def vertex_38_zcoordinate(self):
        """Get vertex_38_zcoordinate

        Returns:
            float: the value of `vertex_38_zcoordinate` or None if not set
        """
        return self._data["Vertex 38 Z-coordinate"]

    @vertex_38_zcoordinate.setter
    def vertex_38_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_38_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_38_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_38_zcoordinate`'.format(value))

        self._data["Vertex 38 Z-coordinate"] = value

    @property
    def vertex_39_xcoordinate(self):
        """Get vertex_39_xcoordinate

        Returns:
            float: the value of `vertex_39_xcoordinate` or None if not set
        """
        return self._data["Vertex 39 X-coordinate"]

    @vertex_39_xcoordinate.setter
    def vertex_39_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_39_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_39_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_39_xcoordinate`'.format(value))

        self._data["Vertex 39 X-coordinate"] = value

    @property
    def vertex_39_ycoordinate(self):
        """Get vertex_39_ycoordinate

        Returns:
            float: the value of `vertex_39_ycoordinate` or None if not set
        """
        return self._data["Vertex 39 Y-coordinate"]

    @vertex_39_ycoordinate.setter
    def vertex_39_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_39_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_39_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_39_ycoordinate`'.format(value))

        self._data["Vertex 39 Y-coordinate"] = value

    @property
    def vertex_39_zcoordinate(self):
        """Get vertex_39_zcoordinate

        Returns:
            float: the value of `vertex_39_zcoordinate` or None if not set
        """
        return self._data["Vertex 39 Z-coordinate"]

    @vertex_39_zcoordinate.setter
    def vertex_39_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_39_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_39_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_39_zcoordinate`'.format(value))

        self._data["Vertex 39 Z-coordinate"] = value

    @property
    def vertex_40_xcoordinate(self):
        """Get vertex_40_xcoordinate

        Returns:
            float: the value of `vertex_40_xcoordinate` or None if not set
        """
        return self._data["Vertex 40 X-coordinate"]

    @vertex_40_xcoordinate.setter
    def vertex_40_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_40_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_40_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_40_xcoordinate`'.format(value))

        self._data["Vertex 40 X-coordinate"] = value

    @property
    def vertex_40_ycoordinate(self):
        """Get vertex_40_ycoordinate

        Returns:
            float: the value of `vertex_40_ycoordinate` or None if not set
        """
        return self._data["Vertex 40 Y-coordinate"]

    @vertex_40_ycoordinate.setter
    def vertex_40_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_40_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_40_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_40_ycoordinate`'.format(value))

        self._data["Vertex 40 Y-coordinate"] = value

    @property
    def vertex_40_zcoordinate(self):
        """Get vertex_40_zcoordinate

        Returns:
            float: the value of `vertex_40_zcoordinate` or None if not set
        """
        return self._data["Vertex 40 Z-coordinate"]

    @vertex_40_zcoordinate.setter
    def vertex_40_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_40_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_40_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_40_zcoordinate`'.format(value))

        self._data["Vertex 40 Z-coordinate"] = value

    @property
    def vertex_41_xcoordinate(self):
        """Get vertex_41_xcoordinate

        Returns:
            float: the value of `vertex_41_xcoordinate` or None if not set
        """
        return self._data["Vertex 41 X-coordinate"]

    @vertex_41_xcoordinate.setter
    def vertex_41_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_41_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_41_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_41_xcoordinate`'.format(value))

        self._data["Vertex 41 X-coordinate"] = value

    @property
    def vertex_41_ycoordinate(self):
        """Get vertex_41_ycoordinate

        Returns:
            float: the value of `vertex_41_ycoordinate` or None if not set
        """
        return self._data["Vertex 41 Y-coordinate"]

    @vertex_41_ycoordinate.setter
    def vertex_41_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_41_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_41_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_41_ycoordinate`'.format(value))

        self._data["Vertex 41 Y-coordinate"] = value

    @property
    def vertex_41_zcoordinate(self):
        """Get vertex_41_zcoordinate

        Returns:
            float: the value of `vertex_41_zcoordinate` or None if not set
        """
        return self._data["Vertex 41 Z-coordinate"]

    @vertex_41_zcoordinate.setter
    def vertex_41_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_41_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_41_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_41_zcoordinate`'.format(value))

        self._data["Vertex 41 Z-coordinate"] = value

    @property
    def vertex_42_xcoordinate(self):
        """Get vertex_42_xcoordinate

        Returns:
            float: the value of `vertex_42_xcoordinate` or None if not set
        """
        return self._data["Vertex 42 X-coordinate"]

    @vertex_42_xcoordinate.setter
    def vertex_42_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_42_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_42_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_42_xcoordinate`'.format(value))

        self._data["Vertex 42 X-coordinate"] = value

    @property
    def vertex_42_ycoordinate(self):
        """Get vertex_42_ycoordinate

        Returns:
            float: the value of `vertex_42_ycoordinate` or None if not set
        """
        return self._data["Vertex 42 Y-coordinate"]

    @vertex_42_ycoordinate.setter
    def vertex_42_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_42_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_42_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_42_ycoordinate`'.format(value))

        self._data["Vertex 42 Y-coordinate"] = value

    @property
    def vertex_42_zcoordinate(self):
        """Get vertex_42_zcoordinate

        Returns:
            float: the value of `vertex_42_zcoordinate` or None if not set
        """
        return self._data["Vertex 42 Z-coordinate"]

    @vertex_42_zcoordinate.setter
    def vertex_42_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_42_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_42_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_42_zcoordinate`'.format(value))

        self._data["Vertex 42 Z-coordinate"] = value

    @property
    def vertex_43_xcoordinate(self):
        """Get vertex_43_xcoordinate

        Returns:
            float: the value of `vertex_43_xcoordinate` or None if not set
        """
        return self._data["Vertex 43 X-coordinate"]

    @vertex_43_xcoordinate.setter
    def vertex_43_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_43_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_43_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_43_xcoordinate`'.format(value))

        self._data["Vertex 43 X-coordinate"] = value

    @property
    def vertex_43_ycoordinate(self):
        """Get vertex_43_ycoordinate

        Returns:
            float: the value of `vertex_43_ycoordinate` or None if not set
        """
        return self._data["Vertex 43 Y-coordinate"]

    @vertex_43_ycoordinate.setter
    def vertex_43_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_43_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_43_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_43_ycoordinate`'.format(value))

        self._data["Vertex 43 Y-coordinate"] = value

    @property
    def vertex_43_zcoordinate(self):
        """Get vertex_43_zcoordinate

        Returns:
            float: the value of `vertex_43_zcoordinate` or None if not set
        """
        return self._data["Vertex 43 Z-coordinate"]

    @vertex_43_zcoordinate.setter
    def vertex_43_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_43_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_43_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_43_zcoordinate`'.format(value))

        self._data["Vertex 43 Z-coordinate"] = value

    @property
    def vertex_44_xcoordinate(self):
        """Get vertex_44_xcoordinate

        Returns:
            float: the value of `vertex_44_xcoordinate` or None if not set
        """
        return self._data["Vertex 44 X-coordinate"]

    @vertex_44_xcoordinate.setter
    def vertex_44_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_44_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_44_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_44_xcoordinate`'.format(value))

        self._data["Vertex 44 X-coordinate"] = value

    @property
    def vertex_44_ycoordinate(self):
        """Get vertex_44_ycoordinate

        Returns:
            float: the value of `vertex_44_ycoordinate` or None if not set
        """
        return self._data["Vertex 44 Y-coordinate"]

    @vertex_44_ycoordinate.setter
    def vertex_44_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_44_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_44_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_44_ycoordinate`'.format(value))

        self._data["Vertex 44 Y-coordinate"] = value

    @property
    def vertex_44_zcoordinate(self):
        """Get vertex_44_zcoordinate

        Returns:
            float: the value of `vertex_44_zcoordinate` or None if not set
        """
        return self._data["Vertex 44 Z-coordinate"]

    @vertex_44_zcoordinate.setter
    def vertex_44_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_44_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_44_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_44_zcoordinate`'.format(value))

        self._data["Vertex 44 Z-coordinate"] = value

    @property
    def vertex_45_xcoordinate(self):
        """Get vertex_45_xcoordinate

        Returns:
            float: the value of `vertex_45_xcoordinate` or None if not set
        """
        return self._data["Vertex 45 X-coordinate"]

    @vertex_45_xcoordinate.setter
    def vertex_45_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_45_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_45_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_45_xcoordinate`'.format(value))

        self._data["Vertex 45 X-coordinate"] = value

    @property
    def vertex_45_ycoordinate(self):
        """Get vertex_45_ycoordinate

        Returns:
            float: the value of `vertex_45_ycoordinate` or None if not set
        """
        return self._data["Vertex 45 Y-coordinate"]

    @vertex_45_ycoordinate.setter
    def vertex_45_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_45_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_45_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_45_ycoordinate`'.format(value))

        self._data["Vertex 45 Y-coordinate"] = value

    @property
    def vertex_45_zcoordinate(self):
        """Get vertex_45_zcoordinate

        Returns:
            float: the value of `vertex_45_zcoordinate` or None if not set
        """
        return self._data["Vertex 45 Z-coordinate"]

    @vertex_45_zcoordinate.setter
    def vertex_45_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_45_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_45_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_45_zcoordinate`'.format(value))

        self._data["Vertex 45 Z-coordinate"] = value

    @property
    def vertex_46_xcoordinate(self):
        """Get vertex_46_xcoordinate

        Returns:
            float: the value of `vertex_46_xcoordinate` or None if not set
        """
        return self._data["Vertex 46 X-coordinate"]

    @vertex_46_xcoordinate.setter
    def vertex_46_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_46_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_46_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_46_xcoordinate`'.format(value))

        self._data["Vertex 46 X-coordinate"] = value

    @property
    def vertex_46_ycoordinate(self):
        """Get vertex_46_ycoordinate

        Returns:
            float: the value of `vertex_46_ycoordinate` or None if not set
        """
        return self._data["Vertex 46 Y-coordinate"]

    @vertex_46_ycoordinate.setter
    def vertex_46_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_46_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_46_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_46_ycoordinate`'.format(value))

        self._data["Vertex 46 Y-coordinate"] = value

    @property
    def vertex_46_zcoordinate(self):
        """Get vertex_46_zcoordinate

        Returns:
            float: the value of `vertex_46_zcoordinate` or None if not set
        """
        return self._data["Vertex 46 Z-coordinate"]

    @vertex_46_zcoordinate.setter
    def vertex_46_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_46_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_46_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_46_zcoordinate`'.format(value))

        self._data["Vertex 46 Z-coordinate"] = value

    @property
    def vertex_47_xcoordinate(self):
        """Get vertex_47_xcoordinate

        Returns:
            float: the value of `vertex_47_xcoordinate` or None if not set
        """
        return self._data["Vertex 47 X-coordinate"]

    @vertex_47_xcoordinate.setter
    def vertex_47_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_47_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_47_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_47_xcoordinate`'.format(value))

        self._data["Vertex 47 X-coordinate"] = value

    @property
    def vertex_47_ycoordinate(self):
        """Get vertex_47_ycoordinate

        Returns:
            float: the value of `vertex_47_ycoordinate` or None if not set
        """
        return self._data["Vertex 47 Y-coordinate"]

    @vertex_47_ycoordinate.setter
    def vertex_47_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_47_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_47_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_47_ycoordinate`'.format(value))

        self._data["Vertex 47 Y-coordinate"] = value

    @property
    def vertex_47_zcoordinate(self):
        """Get vertex_47_zcoordinate

        Returns:
            float: the value of `vertex_47_zcoordinate` or None if not set
        """
        return self._data["Vertex 47 Z-coordinate"]

    @vertex_47_zcoordinate.setter
    def vertex_47_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_47_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_47_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_47_zcoordinate`'.format(value))

        self._data["Vertex 47 Z-coordinate"] = value

    @property
    def vertex_48_xcoordinate(self):
        """Get vertex_48_xcoordinate

        Returns:
            float: the value of `vertex_48_xcoordinate` or None if not set
        """
        return self._data["Vertex 48 X-coordinate"]

    @vertex_48_xcoordinate.setter
    def vertex_48_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_48_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_48_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_48_xcoordinate`'.format(value))

        self._data["Vertex 48 X-coordinate"] = value

    @property
    def vertex_48_ycoordinate(self):
        """Get vertex_48_ycoordinate

        Returns:
            float: the value of `vertex_48_ycoordinate` or None if not set
        """
        return self._data["Vertex 48 Y-coordinate"]

    @vertex_48_ycoordinate.setter
    def vertex_48_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_48_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_48_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_48_ycoordinate`'.format(value))

        self._data["Vertex 48 Y-coordinate"] = value

    @property
    def vertex_48_zcoordinate(self):
        """Get vertex_48_zcoordinate

        Returns:
            float: the value of `vertex_48_zcoordinate` or None if not set
        """
        return self._data["Vertex 48 Z-coordinate"]

    @vertex_48_zcoordinate.setter
    def vertex_48_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_48_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_48_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_48_zcoordinate`'.format(value))

        self._data["Vertex 48 Z-coordinate"] = value

    @property
    def vertex_49_xcoordinate(self):
        """Get vertex_49_xcoordinate

        Returns:
            float: the value of `vertex_49_xcoordinate` or None if not set
        """
        return self._data["Vertex 49 X-coordinate"]

    @vertex_49_xcoordinate.setter
    def vertex_49_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_49_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_49_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_49_xcoordinate`'.format(value))

        self._data["Vertex 49 X-coordinate"] = value

    @property
    def vertex_49_ycoordinate(self):
        """Get vertex_49_ycoordinate

        Returns:
            float: the value of `vertex_49_ycoordinate` or None if not set
        """
        return self._data["Vertex 49 Y-coordinate"]

    @vertex_49_ycoordinate.setter
    def vertex_49_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_49_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_49_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_49_ycoordinate`'.format(value))

        self._data["Vertex 49 Y-coordinate"] = value

    @property
    def vertex_49_zcoordinate(self):
        """Get vertex_49_zcoordinate

        Returns:
            float: the value of `vertex_49_zcoordinate` or None if not set
        """
        return self._data["Vertex 49 Z-coordinate"]

    @vertex_49_zcoordinate.setter
    def vertex_49_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_49_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_49_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_49_zcoordinate`'.format(value))

        self._data["Vertex 49 Z-coordinate"] = value

    @property
    def vertex_50_xcoordinate(self):
        """Get vertex_50_xcoordinate

        Returns:
            float: the value of `vertex_50_xcoordinate` or None if not set
        """
        return self._data["Vertex 50 X-coordinate"]

    @vertex_50_xcoordinate.setter
    def vertex_50_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_50_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_50_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_50_xcoordinate`'.format(value))

        self._data["Vertex 50 X-coordinate"] = value

    @property
    def vertex_50_ycoordinate(self):
        """Get vertex_50_ycoordinate

        Returns:
            float: the value of `vertex_50_ycoordinate` or None if not set
        """
        return self._data["Vertex 50 Y-coordinate"]

    @vertex_50_ycoordinate.setter
    def vertex_50_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_50_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_50_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_50_ycoordinate`'.format(value))

        self._data["Vertex 50 Y-coordinate"] = value

    @property
    def vertex_50_zcoordinate(self):
        """Get vertex_50_zcoordinate

        Returns:
            float: the value of `vertex_50_zcoordinate` or None if not set
        """
        return self._data["Vertex 50 Z-coordinate"]

    @vertex_50_zcoordinate.setter
    def vertex_50_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_50_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_50_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_50_zcoordinate`'.format(value))

        self._data["Vertex 50 Z-coordinate"] = value

    @property
    def vertex_51_xcoordinate(self):
        """Get vertex_51_xcoordinate

        Returns:
            float: the value of `vertex_51_xcoordinate` or None if not set
        """
        return self._data["Vertex 51 X-coordinate"]

    @vertex_51_xcoordinate.setter
    def vertex_51_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_51_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_51_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_51_xcoordinate`'.format(value))

        self._data["Vertex 51 X-coordinate"] = value

    @property
    def vertex_51_ycoordinate(self):
        """Get vertex_51_ycoordinate

        Returns:
            float: the value of `vertex_51_ycoordinate` or None if not set
        """
        return self._data["Vertex 51 Y-coordinate"]

    @vertex_51_ycoordinate.setter
    def vertex_51_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_51_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_51_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_51_ycoordinate`'.format(value))

        self._data["Vertex 51 Y-coordinate"] = value

    @property
    def vertex_51_zcoordinate(self):
        """Get vertex_51_zcoordinate

        Returns:
            float: the value of `vertex_51_zcoordinate` or None if not set
        """
        return self._data["Vertex 51 Z-coordinate"]

    @vertex_51_zcoordinate.setter
    def vertex_51_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_51_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_51_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_51_zcoordinate`'.format(value))

        self._data["Vertex 51 Z-coordinate"] = value

    @property
    def vertex_52_xcoordinate(self):
        """Get vertex_52_xcoordinate

        Returns:
            float: the value of `vertex_52_xcoordinate` or None if not set
        """
        return self._data["Vertex 52 X-coordinate"]

    @vertex_52_xcoordinate.setter
    def vertex_52_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_52_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_52_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_52_xcoordinate`'.format(value))

        self._data["Vertex 52 X-coordinate"] = value

    @property
    def vertex_52_ycoordinate(self):
        """Get vertex_52_ycoordinate

        Returns:
            float: the value of `vertex_52_ycoordinate` or None if not set
        """
        return self._data["Vertex 52 Y-coordinate"]

    @vertex_52_ycoordinate.setter
    def vertex_52_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_52_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_52_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_52_ycoordinate`'.format(value))

        self._data["Vertex 52 Y-coordinate"] = value

    @property
    def vertex_52_zcoordinate(self):
        """Get vertex_52_zcoordinate

        Returns:
            float: the value of `vertex_52_zcoordinate` or None if not set
        """
        return self._data["Vertex 52 Z-coordinate"]

    @vertex_52_zcoordinate.setter
    def vertex_52_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_52_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_52_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_52_zcoordinate`'.format(value))

        self._data["Vertex 52 Z-coordinate"] = value

    @property
    def vertex_53_xcoordinate(self):
        """Get vertex_53_xcoordinate

        Returns:
            float: the value of `vertex_53_xcoordinate` or None if not set
        """
        return self._data["Vertex 53 X-coordinate"]

    @vertex_53_xcoordinate.setter
    def vertex_53_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_53_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_53_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_53_xcoordinate`'.format(value))

        self._data["Vertex 53 X-coordinate"] = value

    @property
    def vertex_53_ycoordinate(self):
        """Get vertex_53_ycoordinate

        Returns:
            float: the value of `vertex_53_ycoordinate` or None if not set
        """
        return self._data["Vertex 53 Y-coordinate"]

    @vertex_53_ycoordinate.setter
    def vertex_53_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_53_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_53_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_53_ycoordinate`'.format(value))

        self._data["Vertex 53 Y-coordinate"] = value

    @property
    def vertex_53_zcoordinate(self):
        """Get vertex_53_zcoordinate

        Returns:
            float: the value of `vertex_53_zcoordinate` or None if not set
        """
        return self._data["Vertex 53 Z-coordinate"]

    @vertex_53_zcoordinate.setter
    def vertex_53_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_53_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_53_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_53_zcoordinate`'.format(value))

        self._data["Vertex 53 Z-coordinate"] = value

    @property
    def vertex_54_xcoordinate(self):
        """Get vertex_54_xcoordinate

        Returns:
            float: the value of `vertex_54_xcoordinate` or None if not set
        """
        return self._data["Vertex 54 X-coordinate"]

    @vertex_54_xcoordinate.setter
    def vertex_54_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_54_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_54_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_54_xcoordinate`'.format(value))

        self._data["Vertex 54 X-coordinate"] = value

    @property
    def vertex_54_ycoordinate(self):
        """Get vertex_54_ycoordinate

        Returns:
            float: the value of `vertex_54_ycoordinate` or None if not set
        """
        return self._data["Vertex 54 Y-coordinate"]

    @vertex_54_ycoordinate.setter
    def vertex_54_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_54_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_54_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_54_ycoordinate`'.format(value))

        self._data["Vertex 54 Y-coordinate"] = value

    @property
    def vertex_54_zcoordinate(self):
        """Get vertex_54_zcoordinate

        Returns:
            float: the value of `vertex_54_zcoordinate` or None if not set
        """
        return self._data["Vertex 54 Z-coordinate"]

    @vertex_54_zcoordinate.setter
    def vertex_54_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_54_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_54_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_54_zcoordinate`'.format(value))

        self._data["Vertex 54 Z-coordinate"] = value

    @property
    def vertex_55_xcoordinate(self):
        """Get vertex_55_xcoordinate

        Returns:
            float: the value of `vertex_55_xcoordinate` or None if not set
        """
        return self._data["Vertex 55 X-coordinate"]

    @vertex_55_xcoordinate.setter
    def vertex_55_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_55_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_55_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_55_xcoordinate`'.format(value))

        self._data["Vertex 55 X-coordinate"] = value

    @property
    def vertex_55_ycoordinate(self):
        """Get vertex_55_ycoordinate

        Returns:
            float: the value of `vertex_55_ycoordinate` or None if not set
        """
        return self._data["Vertex 55 Y-coordinate"]

    @vertex_55_ycoordinate.setter
    def vertex_55_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_55_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_55_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_55_ycoordinate`'.format(value))

        self._data["Vertex 55 Y-coordinate"] = value

    @property
    def vertex_55_zcoordinate(self):
        """Get vertex_55_zcoordinate

        Returns:
            float: the value of `vertex_55_zcoordinate` or None if not set
        """
        return self._data["Vertex 55 Z-coordinate"]

    @vertex_55_zcoordinate.setter
    def vertex_55_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_55_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_55_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_55_zcoordinate`'.format(value))

        self._data["Vertex 55 Z-coordinate"] = value

    @property
    def vertex_56_xcoordinate(self):
        """Get vertex_56_xcoordinate

        Returns:
            float: the value of `vertex_56_xcoordinate` or None if not set
        """
        return self._data["Vertex 56 X-coordinate"]

    @vertex_56_xcoordinate.setter
    def vertex_56_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_56_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_56_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_56_xcoordinate`'.format(value))

        self._data["Vertex 56 X-coordinate"] = value

    @property
    def vertex_56_ycoordinate(self):
        """Get vertex_56_ycoordinate

        Returns:
            float: the value of `vertex_56_ycoordinate` or None if not set
        """
        return self._data["Vertex 56 Y-coordinate"]

    @vertex_56_ycoordinate.setter
    def vertex_56_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_56_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_56_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_56_ycoordinate`'.format(value))

        self._data["Vertex 56 Y-coordinate"] = value

    @property
    def vertex_56_zcoordinate(self):
        """Get vertex_56_zcoordinate

        Returns:
            float: the value of `vertex_56_zcoordinate` or None if not set
        """
        return self._data["Vertex 56 Z-coordinate"]

    @vertex_56_zcoordinate.setter
    def vertex_56_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_56_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_56_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_56_zcoordinate`'.format(value))

        self._data["Vertex 56 Z-coordinate"] = value

    @property
    def vertex_57_xcoordinate(self):
        """Get vertex_57_xcoordinate

        Returns:
            float: the value of `vertex_57_xcoordinate` or None if not set
        """
        return self._data["Vertex 57 X-coordinate"]

    @vertex_57_xcoordinate.setter
    def vertex_57_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_57_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_57_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_57_xcoordinate`'.format(value))

        self._data["Vertex 57 X-coordinate"] = value

    @property
    def vertex_57_ycoordinate(self):
        """Get vertex_57_ycoordinate

        Returns:
            float: the value of `vertex_57_ycoordinate` or None if not set
        """
        return self._data["Vertex 57 Y-coordinate"]

    @vertex_57_ycoordinate.setter
    def vertex_57_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_57_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_57_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_57_ycoordinate`'.format(value))

        self._data["Vertex 57 Y-coordinate"] = value

    @property
    def vertex_57_zcoordinate(self):
        """Get vertex_57_zcoordinate

        Returns:
            float: the value of `vertex_57_zcoordinate` or None if not set
        """
        return self._data["Vertex 57 Z-coordinate"]

    @vertex_57_zcoordinate.setter
    def vertex_57_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_57_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_57_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_57_zcoordinate`'.format(value))

        self._data["Vertex 57 Z-coordinate"] = value

    @property
    def vertex_58_xcoordinate(self):
        """Get vertex_58_xcoordinate

        Returns:
            float: the value of `vertex_58_xcoordinate` or None if not set
        """
        return self._data["Vertex 58 X-coordinate"]

    @vertex_58_xcoordinate.setter
    def vertex_58_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_58_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_58_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_58_xcoordinate`'.format(value))

        self._data["Vertex 58 X-coordinate"] = value

    @property
    def vertex_58_ycoordinate(self):
        """Get vertex_58_ycoordinate

        Returns:
            float: the value of `vertex_58_ycoordinate` or None if not set
        """
        return self._data["Vertex 58 Y-coordinate"]

    @vertex_58_ycoordinate.setter
    def vertex_58_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_58_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_58_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_58_ycoordinate`'.format(value))

        self._data["Vertex 58 Y-coordinate"] = value

    @property
    def vertex_58_zcoordinate(self):
        """Get vertex_58_zcoordinate

        Returns:
            float: the value of `vertex_58_zcoordinate` or None if not set
        """
        return self._data["Vertex 58 Z-coordinate"]

    @vertex_58_zcoordinate.setter
    def vertex_58_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_58_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_58_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_58_zcoordinate`'.format(value))

        self._data["Vertex 58 Z-coordinate"] = value

    @property
    def vertex_59_xcoordinate(self):
        """Get vertex_59_xcoordinate

        Returns:
            float: the value of `vertex_59_xcoordinate` or None if not set
        """
        return self._data["Vertex 59 X-coordinate"]

    @vertex_59_xcoordinate.setter
    def vertex_59_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_59_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_59_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_59_xcoordinate`'.format(value))

        self._data["Vertex 59 X-coordinate"] = value

    @property
    def vertex_59_ycoordinate(self):
        """Get vertex_59_ycoordinate

        Returns:
            float: the value of `vertex_59_ycoordinate` or None if not set
        """
        return self._data["Vertex 59 Y-coordinate"]

    @vertex_59_ycoordinate.setter
    def vertex_59_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_59_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_59_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_59_ycoordinate`'.format(value))

        self._data["Vertex 59 Y-coordinate"] = value

    @property
    def vertex_59_zcoordinate(self):
        """Get vertex_59_zcoordinate

        Returns:
            float: the value of `vertex_59_zcoordinate` or None if not set
        """
        return self._data["Vertex 59 Z-coordinate"]

    @vertex_59_zcoordinate.setter
    def vertex_59_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_59_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_59_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_59_zcoordinate`'.format(value))

        self._data["Vertex 59 Z-coordinate"] = value

    @property
    def vertex_60_xcoordinate(self):
        """Get vertex_60_xcoordinate

        Returns:
            float: the value of `vertex_60_xcoordinate` or None if not set
        """
        return self._data["Vertex 60 X-coordinate"]

    @vertex_60_xcoordinate.setter
    def vertex_60_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_60_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_60_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_60_xcoordinate`'.format(value))

        self._data["Vertex 60 X-coordinate"] = value

    @property
    def vertex_60_ycoordinate(self):
        """Get vertex_60_ycoordinate

        Returns:
            float: the value of `vertex_60_ycoordinate` or None if not set
        """
        return self._data["Vertex 60 Y-coordinate"]

    @vertex_60_ycoordinate.setter
    def vertex_60_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_60_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_60_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_60_ycoordinate`'.format(value))

        self._data["Vertex 60 Y-coordinate"] = value

    @property
    def vertex_60_zcoordinate(self):
        """Get vertex_60_zcoordinate

        Returns:
            float: the value of `vertex_60_zcoordinate` or None if not set
        """
        return self._data["Vertex 60 Z-coordinate"]

    @vertex_60_zcoordinate.setter
    def vertex_60_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_60_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_60_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_60_zcoordinate`'.format(value))

        self._data["Vertex 60 Z-coordinate"] = value

    @property
    def vertex_61_xcoordinate(self):
        """Get vertex_61_xcoordinate

        Returns:
            float: the value of `vertex_61_xcoordinate` or None if not set
        """
        return self._data["Vertex 61 X-coordinate"]

    @vertex_61_xcoordinate.setter
    def vertex_61_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_61_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_61_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_61_xcoordinate`'.format(value))

        self._data["Vertex 61 X-coordinate"] = value

    @property
    def vertex_61_ycoordinate(self):
        """Get vertex_61_ycoordinate

        Returns:
            float: the value of `vertex_61_ycoordinate` or None if not set
        """
        return self._data["Vertex 61 Y-coordinate"]

    @vertex_61_ycoordinate.setter
    def vertex_61_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_61_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_61_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_61_ycoordinate`'.format(value))

        self._data["Vertex 61 Y-coordinate"] = value

    @property
    def vertex_61_zcoordinate(self):
        """Get vertex_61_zcoordinate

        Returns:
            float: the value of `vertex_61_zcoordinate` or None if not set
        """
        return self._data["Vertex 61 Z-coordinate"]

    @vertex_61_zcoordinate.setter
    def vertex_61_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_61_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_61_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_61_zcoordinate`'.format(value))

        self._data["Vertex 61 Z-coordinate"] = value

    @property
    def vertex_62_xcoordinate(self):
        """Get vertex_62_xcoordinate

        Returns:
            float: the value of `vertex_62_xcoordinate` or None if not set
        """
        return self._data["Vertex 62 X-coordinate"]

    @vertex_62_xcoordinate.setter
    def vertex_62_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_62_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_62_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_62_xcoordinate`'.format(value))

        self._data["Vertex 62 X-coordinate"] = value

    @property
    def vertex_62_ycoordinate(self):
        """Get vertex_62_ycoordinate

        Returns:
            float: the value of `vertex_62_ycoordinate` or None if not set
        """
        return self._data["Vertex 62 Y-coordinate"]

    @vertex_62_ycoordinate.setter
    def vertex_62_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_62_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_62_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_62_ycoordinate`'.format(value))

        self._data["Vertex 62 Y-coordinate"] = value

    @property
    def vertex_62_zcoordinate(self):
        """Get vertex_62_zcoordinate

        Returns:
            float: the value of `vertex_62_zcoordinate` or None if not set
        """
        return self._data["Vertex 62 Z-coordinate"]

    @vertex_62_zcoordinate.setter
    def vertex_62_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_62_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_62_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_62_zcoordinate`'.format(value))

        self._data["Vertex 62 Z-coordinate"] = value

    @property
    def vertex_63_xcoordinate(self):
        """Get vertex_63_xcoordinate

        Returns:
            float: the value of `vertex_63_xcoordinate` or None if not set
        """
        return self._data["Vertex 63 X-coordinate"]

    @vertex_63_xcoordinate.setter
    def vertex_63_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_63_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_63_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_63_xcoordinate`'.format(value))

        self._data["Vertex 63 X-coordinate"] = value

    @property
    def vertex_63_ycoordinate(self):
        """Get vertex_63_ycoordinate

        Returns:
            float: the value of `vertex_63_ycoordinate` or None if not set
        """
        return self._data["Vertex 63 Y-coordinate"]

    @vertex_63_ycoordinate.setter
    def vertex_63_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_63_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_63_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_63_ycoordinate`'.format(value))

        self._data["Vertex 63 Y-coordinate"] = value

    @property
    def vertex_63_zcoordinate(self):
        """Get vertex_63_zcoordinate

        Returns:
            float: the value of `vertex_63_zcoordinate` or None if not set
        """
        return self._data["Vertex 63 Z-coordinate"]

    @vertex_63_zcoordinate.setter
    def vertex_63_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_63_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_63_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_63_zcoordinate`'.format(value))

        self._data["Vertex 63 Z-coordinate"] = value

    @property
    def vertex_64_xcoordinate(self):
        """Get vertex_64_xcoordinate

        Returns:
            float: the value of `vertex_64_xcoordinate` or None if not set
        """
        return self._data["Vertex 64 X-coordinate"]

    @vertex_64_xcoordinate.setter
    def vertex_64_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_64_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_64_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_64_xcoordinate`'.format(value))

        self._data["Vertex 64 X-coordinate"] = value

    @property
    def vertex_64_ycoordinate(self):
        """Get vertex_64_ycoordinate

        Returns:
            float: the value of `vertex_64_ycoordinate` or None if not set
        """
        return self._data["Vertex 64 Y-coordinate"]

    @vertex_64_ycoordinate.setter
    def vertex_64_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_64_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_64_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_64_ycoordinate`'.format(value))

        self._data["Vertex 64 Y-coordinate"] = value

    @property
    def vertex_64_zcoordinate(self):
        """Get vertex_64_zcoordinate

        Returns:
            float: the value of `vertex_64_zcoordinate` or None if not set
        """
        return self._data["Vertex 64 Z-coordinate"]

    @vertex_64_zcoordinate.setter
    def vertex_64_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_64_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_64_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_64_zcoordinate`'.format(value))

        self._data["Vertex 64 Z-coordinate"] = value

    @property
    def vertex_65_xcoordinate(self):
        """Get vertex_65_xcoordinate

        Returns:
            float: the value of `vertex_65_xcoordinate` or None if not set
        """
        return self._data["Vertex 65 X-coordinate"]

    @vertex_65_xcoordinate.setter
    def vertex_65_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_65_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_65_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_65_xcoordinate`'.format(value))

        self._data["Vertex 65 X-coordinate"] = value

    @property
    def vertex_65_ycoordinate(self):
        """Get vertex_65_ycoordinate

        Returns:
            float: the value of `vertex_65_ycoordinate` or None if not set
        """
        return self._data["Vertex 65 Y-coordinate"]

    @vertex_65_ycoordinate.setter
    def vertex_65_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_65_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_65_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_65_ycoordinate`'.format(value))

        self._data["Vertex 65 Y-coordinate"] = value

    @property
    def vertex_65_zcoordinate(self):
        """Get vertex_65_zcoordinate

        Returns:
            float: the value of `vertex_65_zcoordinate` or None if not set
        """
        return self._data["Vertex 65 Z-coordinate"]

    @vertex_65_zcoordinate.setter
    def vertex_65_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_65_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_65_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_65_zcoordinate`'.format(value))

        self._data["Vertex 65 Z-coordinate"] = value

    @property
    def vertex_66_xcoordinate(self):
        """Get vertex_66_xcoordinate

        Returns:
            float: the value of `vertex_66_xcoordinate` or None if not set
        """
        return self._data["Vertex 66 X-coordinate"]

    @vertex_66_xcoordinate.setter
    def vertex_66_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_66_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_66_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_66_xcoordinate`'.format(value))

        self._data["Vertex 66 X-coordinate"] = value

    @property
    def vertex_66_ycoordinate(self):
        """Get vertex_66_ycoordinate

        Returns:
            float: the value of `vertex_66_ycoordinate` or None if not set
        """
        return self._data["Vertex 66 Y-coordinate"]

    @vertex_66_ycoordinate.setter
    def vertex_66_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_66_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_66_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_66_ycoordinate`'.format(value))

        self._data["Vertex 66 Y-coordinate"] = value

    @property
    def vertex_66_zcoordinate(self):
        """Get vertex_66_zcoordinate

        Returns:
            float: the value of `vertex_66_zcoordinate` or None if not set
        """
        return self._data["Vertex 66 Z-coordinate"]

    @vertex_66_zcoordinate.setter
    def vertex_66_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_66_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_66_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_66_zcoordinate`'.format(value))

        self._data["Vertex 66 Z-coordinate"] = value

    @property
    def vertex_67_xcoordinate(self):
        """Get vertex_67_xcoordinate

        Returns:
            float: the value of `vertex_67_xcoordinate` or None if not set
        """
        return self._data["Vertex 67 X-coordinate"]

    @vertex_67_xcoordinate.setter
    def vertex_67_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_67_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_67_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_67_xcoordinate`'.format(value))

        self._data["Vertex 67 X-coordinate"] = value

    @property
    def vertex_67_ycoordinate(self):
        """Get vertex_67_ycoordinate

        Returns:
            float: the value of `vertex_67_ycoordinate` or None if not set
        """
        return self._data["Vertex 67 Y-coordinate"]

    @vertex_67_ycoordinate.setter
    def vertex_67_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_67_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_67_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_67_ycoordinate`'.format(value))

        self._data["Vertex 67 Y-coordinate"] = value

    @property
    def vertex_67_zcoordinate(self):
        """Get vertex_67_zcoordinate

        Returns:
            float: the value of `vertex_67_zcoordinate` or None if not set
        """
        return self._data["Vertex 67 Z-coordinate"]

    @vertex_67_zcoordinate.setter
    def vertex_67_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_67_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_67_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_67_zcoordinate`'.format(value))

        self._data["Vertex 67 Z-coordinate"] = value

    @property
    def vertex_68_xcoordinate(self):
        """Get vertex_68_xcoordinate

        Returns:
            float: the value of `vertex_68_xcoordinate` or None if not set
        """
        return self._data["Vertex 68 X-coordinate"]

    @vertex_68_xcoordinate.setter
    def vertex_68_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_68_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_68_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_68_xcoordinate`'.format(value))

        self._data["Vertex 68 X-coordinate"] = value

    @property
    def vertex_68_ycoordinate(self):
        """Get vertex_68_ycoordinate

        Returns:
            float: the value of `vertex_68_ycoordinate` or None if not set
        """
        return self._data["Vertex 68 Y-coordinate"]

    @vertex_68_ycoordinate.setter
    def vertex_68_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_68_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_68_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_68_ycoordinate`'.format(value))

        self._data["Vertex 68 Y-coordinate"] = value

    @property
    def vertex_68_zcoordinate(self):
        """Get vertex_68_zcoordinate

        Returns:
            float: the value of `vertex_68_zcoordinate` or None if not set
        """
        return self._data["Vertex 68 Z-coordinate"]

    @vertex_68_zcoordinate.setter
    def vertex_68_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_68_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_68_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_68_zcoordinate`'.format(value))

        self._data["Vertex 68 Z-coordinate"] = value

    @property
    def vertex_69_xcoordinate(self):
        """Get vertex_69_xcoordinate

        Returns:
            float: the value of `vertex_69_xcoordinate` or None if not set
        """
        return self._data["Vertex 69 X-coordinate"]

    @vertex_69_xcoordinate.setter
    def vertex_69_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_69_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_69_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_69_xcoordinate`'.format(value))

        self._data["Vertex 69 X-coordinate"] = value

    @property
    def vertex_69_ycoordinate(self):
        """Get vertex_69_ycoordinate

        Returns:
            float: the value of `vertex_69_ycoordinate` or None if not set
        """
        return self._data["Vertex 69 Y-coordinate"]

    @vertex_69_ycoordinate.setter
    def vertex_69_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_69_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_69_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_69_ycoordinate`'.format(value))

        self._data["Vertex 69 Y-coordinate"] = value

    @property
    def vertex_69_zcoordinate(self):
        """Get vertex_69_zcoordinate

        Returns:
            float: the value of `vertex_69_zcoordinate` or None if not set
        """
        return self._data["Vertex 69 Z-coordinate"]

    @vertex_69_zcoordinate.setter
    def vertex_69_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_69_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_69_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_69_zcoordinate`'.format(value))

        self._data["Vertex 69 Z-coordinate"] = value

    @property
    def vertex_70_xcoordinate(self):
        """Get vertex_70_xcoordinate

        Returns:
            float: the value of `vertex_70_xcoordinate` or None if not set
        """
        return self._data["Vertex 70 X-coordinate"]

    @vertex_70_xcoordinate.setter
    def vertex_70_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_70_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_70_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_70_xcoordinate`'.format(value))

        self._data["Vertex 70 X-coordinate"] = value

    @property
    def vertex_70_ycoordinate(self):
        """Get vertex_70_ycoordinate

        Returns:
            float: the value of `vertex_70_ycoordinate` or None if not set
        """
        return self._data["Vertex 70 Y-coordinate"]

    @vertex_70_ycoordinate.setter
    def vertex_70_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_70_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_70_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_70_ycoordinate`'.format(value))

        self._data["Vertex 70 Y-coordinate"] = value

    @property
    def vertex_70_zcoordinate(self):
        """Get vertex_70_zcoordinate

        Returns:
            float: the value of `vertex_70_zcoordinate` or None if not set
        """
        return self._data["Vertex 70 Z-coordinate"]

    @vertex_70_zcoordinate.setter
    def vertex_70_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_70_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_70_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_70_zcoordinate`'.format(value))

        self._data["Vertex 70 Z-coordinate"] = value

    @property
    def vertex_71_xcoordinate(self):
        """Get vertex_71_xcoordinate

        Returns:
            float: the value of `vertex_71_xcoordinate` or None if not set
        """
        return self._data["Vertex 71 X-coordinate"]

    @vertex_71_xcoordinate.setter
    def vertex_71_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_71_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_71_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_71_xcoordinate`'.format(value))

        self._data["Vertex 71 X-coordinate"] = value

    @property
    def vertex_71_ycoordinate(self):
        """Get vertex_71_ycoordinate

        Returns:
            float: the value of `vertex_71_ycoordinate` or None if not set
        """
        return self._data["Vertex 71 Y-coordinate"]

    @vertex_71_ycoordinate.setter
    def vertex_71_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_71_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_71_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_71_ycoordinate`'.format(value))

        self._data["Vertex 71 Y-coordinate"] = value

    @property
    def vertex_71_zcoordinate(self):
        """Get vertex_71_zcoordinate

        Returns:
            float: the value of `vertex_71_zcoordinate` or None if not set
        """
        return self._data["Vertex 71 Z-coordinate"]

    @vertex_71_zcoordinate.setter
    def vertex_71_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_71_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_71_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_71_zcoordinate`'.format(value))

        self._data["Vertex 71 Z-coordinate"] = value

    @property
    def vertex_72_xcoordinate(self):
        """Get vertex_72_xcoordinate

        Returns:
            float: the value of `vertex_72_xcoordinate` or None if not set
        """
        return self._data["Vertex 72 X-coordinate"]

    @vertex_72_xcoordinate.setter
    def vertex_72_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_72_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_72_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_72_xcoordinate`'.format(value))

        self._data["Vertex 72 X-coordinate"] = value

    @property
    def vertex_72_ycoordinate(self):
        """Get vertex_72_ycoordinate

        Returns:
            float: the value of `vertex_72_ycoordinate` or None if not set
        """
        return self._data["Vertex 72 Y-coordinate"]

    @vertex_72_ycoordinate.setter
    def vertex_72_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_72_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_72_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_72_ycoordinate`'.format(value))

        self._data["Vertex 72 Y-coordinate"] = value

    @property
    def vertex_72_zcoordinate(self):
        """Get vertex_72_zcoordinate

        Returns:
            float: the value of `vertex_72_zcoordinate` or None if not set
        """
        return self._data["Vertex 72 Z-coordinate"]

    @vertex_72_zcoordinate.setter
    def vertex_72_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_72_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_72_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_72_zcoordinate`'.format(value))

        self._data["Vertex 72 Z-coordinate"] = value

    @property
    def vertex_73_xcoordinate(self):
        """Get vertex_73_xcoordinate

        Returns:
            float: the value of `vertex_73_xcoordinate` or None if not set
        """
        return self._data["Vertex 73 X-coordinate"]

    @vertex_73_xcoordinate.setter
    def vertex_73_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_73_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_73_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_73_xcoordinate`'.format(value))

        self._data["Vertex 73 X-coordinate"] = value

    @property
    def vertex_73_ycoordinate(self):
        """Get vertex_73_ycoordinate

        Returns:
            float: the value of `vertex_73_ycoordinate` or None if not set
        """
        return self._data["Vertex 73 Y-coordinate"]

    @vertex_73_ycoordinate.setter
    def vertex_73_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_73_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_73_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_73_ycoordinate`'.format(value))

        self._data["Vertex 73 Y-coordinate"] = value

    @property
    def vertex_73_zcoordinate(self):
        """Get vertex_73_zcoordinate

        Returns:
            float: the value of `vertex_73_zcoordinate` or None if not set
        """
        return self._data["Vertex 73 Z-coordinate"]

    @vertex_73_zcoordinate.setter
    def vertex_73_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_73_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_73_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_73_zcoordinate`'.format(value))

        self._data["Vertex 73 Z-coordinate"] = value

    @property
    def vertex_74_xcoordinate(self):
        """Get vertex_74_xcoordinate

        Returns:
            float: the value of `vertex_74_xcoordinate` or None if not set
        """
        return self._data["Vertex 74 X-coordinate"]

    @vertex_74_xcoordinate.setter
    def vertex_74_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_74_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_74_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_74_xcoordinate`'.format(value))

        self._data["Vertex 74 X-coordinate"] = value

    @property
    def vertex_74_ycoordinate(self):
        """Get vertex_74_ycoordinate

        Returns:
            float: the value of `vertex_74_ycoordinate` or None if not set
        """
        return self._data["Vertex 74 Y-coordinate"]

    @vertex_74_ycoordinate.setter
    def vertex_74_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_74_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_74_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_74_ycoordinate`'.format(value))

        self._data["Vertex 74 Y-coordinate"] = value

    @property
    def vertex_74_zcoordinate(self):
        """Get vertex_74_zcoordinate

        Returns:
            float: the value of `vertex_74_zcoordinate` or None if not set
        """
        return self._data["Vertex 74 Z-coordinate"]

    @vertex_74_zcoordinate.setter
    def vertex_74_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_74_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_74_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_74_zcoordinate`'.format(value))

        self._data["Vertex 74 Z-coordinate"] = value

    @property
    def vertex_75_xcoordinate(self):
        """Get vertex_75_xcoordinate

        Returns:
            float: the value of `vertex_75_xcoordinate` or None if not set
        """
        return self._data["Vertex 75 X-coordinate"]

    @vertex_75_xcoordinate.setter
    def vertex_75_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_75_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_75_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_75_xcoordinate`'.format(value))

        self._data["Vertex 75 X-coordinate"] = value

    @property
    def vertex_75_ycoordinate(self):
        """Get vertex_75_ycoordinate

        Returns:
            float: the value of `vertex_75_ycoordinate` or None if not set
        """
        return self._data["Vertex 75 Y-coordinate"]

    @vertex_75_ycoordinate.setter
    def vertex_75_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_75_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_75_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_75_ycoordinate`'.format(value))

        self._data["Vertex 75 Y-coordinate"] = value

    @property
    def vertex_75_zcoordinate(self):
        """Get vertex_75_zcoordinate

        Returns:
            float: the value of `vertex_75_zcoordinate` or None if not set
        """
        return self._data["Vertex 75 Z-coordinate"]

    @vertex_75_zcoordinate.setter
    def vertex_75_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_75_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_75_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_75_zcoordinate`'.format(value))

        self._data["Vertex 75 Z-coordinate"] = value

    @property
    def vertex_76_xcoordinate(self):
        """Get vertex_76_xcoordinate

        Returns:
            float: the value of `vertex_76_xcoordinate` or None if not set
        """
        return self._data["Vertex 76 X-coordinate"]

    @vertex_76_xcoordinate.setter
    def vertex_76_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_76_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_76_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_76_xcoordinate`'.format(value))

        self._data["Vertex 76 X-coordinate"] = value

    @property
    def vertex_76_ycoordinate(self):
        """Get vertex_76_ycoordinate

        Returns:
            float: the value of `vertex_76_ycoordinate` or None if not set
        """
        return self._data["Vertex 76 Y-coordinate"]

    @vertex_76_ycoordinate.setter
    def vertex_76_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_76_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_76_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_76_ycoordinate`'.format(value))

        self._data["Vertex 76 Y-coordinate"] = value

    @property
    def vertex_76_zcoordinate(self):
        """Get vertex_76_zcoordinate

        Returns:
            float: the value of `vertex_76_zcoordinate` or None if not set
        """
        return self._data["Vertex 76 Z-coordinate"]

    @vertex_76_zcoordinate.setter
    def vertex_76_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_76_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_76_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_76_zcoordinate`'.format(value))

        self._data["Vertex 76 Z-coordinate"] = value

    @property
    def vertex_77_xcoordinate(self):
        """Get vertex_77_xcoordinate

        Returns:
            float: the value of `vertex_77_xcoordinate` or None if not set
        """
        return self._data["Vertex 77 X-coordinate"]

    @vertex_77_xcoordinate.setter
    def vertex_77_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_77_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_77_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_77_xcoordinate`'.format(value))

        self._data["Vertex 77 X-coordinate"] = value

    @property
    def vertex_77_ycoordinate(self):
        """Get vertex_77_ycoordinate

        Returns:
            float: the value of `vertex_77_ycoordinate` or None if not set
        """
        return self._data["Vertex 77 Y-coordinate"]

    @vertex_77_ycoordinate.setter
    def vertex_77_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_77_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_77_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_77_ycoordinate`'.format(value))

        self._data["Vertex 77 Y-coordinate"] = value

    @property
    def vertex_77_zcoordinate(self):
        """Get vertex_77_zcoordinate

        Returns:
            float: the value of `vertex_77_zcoordinate` or None if not set
        """
        return self._data["Vertex 77 Z-coordinate"]

    @vertex_77_zcoordinate.setter
    def vertex_77_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_77_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_77_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_77_zcoordinate`'.format(value))

        self._data["Vertex 77 Z-coordinate"] = value

    @property
    def vertex_78_xcoordinate(self):
        """Get vertex_78_xcoordinate

        Returns:
            float: the value of `vertex_78_xcoordinate` or None if not set
        """
        return self._data["Vertex 78 X-coordinate"]

    @vertex_78_xcoordinate.setter
    def vertex_78_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_78_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_78_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_78_xcoordinate`'.format(value))

        self._data["Vertex 78 X-coordinate"] = value

    @property
    def vertex_78_ycoordinate(self):
        """Get vertex_78_ycoordinate

        Returns:
            float: the value of `vertex_78_ycoordinate` or None if not set
        """
        return self._data["Vertex 78 Y-coordinate"]

    @vertex_78_ycoordinate.setter
    def vertex_78_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_78_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_78_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_78_ycoordinate`'.format(value))

        self._data["Vertex 78 Y-coordinate"] = value

    @property
    def vertex_78_zcoordinate(self):
        """Get vertex_78_zcoordinate

        Returns:
            float: the value of `vertex_78_zcoordinate` or None if not set
        """
        return self._data["Vertex 78 Z-coordinate"]

    @vertex_78_zcoordinate.setter
    def vertex_78_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_78_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_78_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_78_zcoordinate`'.format(value))

        self._data["Vertex 78 Z-coordinate"] = value

    @property
    def vertex_79_xcoordinate(self):
        """Get vertex_79_xcoordinate

        Returns:
            float: the value of `vertex_79_xcoordinate` or None if not set
        """
        return self._data["Vertex 79 X-coordinate"]

    @vertex_79_xcoordinate.setter
    def vertex_79_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_79_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_79_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_79_xcoordinate`'.format(value))

        self._data["Vertex 79 X-coordinate"] = value

    @property
    def vertex_79_ycoordinate(self):
        """Get vertex_79_ycoordinate

        Returns:
            float: the value of `vertex_79_ycoordinate` or None if not set
        """
        return self._data["Vertex 79 Y-coordinate"]

    @vertex_79_ycoordinate.setter
    def vertex_79_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_79_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_79_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_79_ycoordinate`'.format(value))

        self._data["Vertex 79 Y-coordinate"] = value

    @property
    def vertex_79_zcoordinate(self):
        """Get vertex_79_zcoordinate

        Returns:
            float: the value of `vertex_79_zcoordinate` or None if not set
        """
        return self._data["Vertex 79 Z-coordinate"]

    @vertex_79_zcoordinate.setter
    def vertex_79_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_79_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_79_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_79_zcoordinate`'.format(value))

        self._data["Vertex 79 Z-coordinate"] = value

    @property
    def vertex_80_xcoordinate(self):
        """Get vertex_80_xcoordinate

        Returns:
            float: the value of `vertex_80_xcoordinate` or None if not set
        """
        return self._data["Vertex 80 X-coordinate"]

    @vertex_80_xcoordinate.setter
    def vertex_80_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_80_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_80_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_80_xcoordinate`'.format(value))

        self._data["Vertex 80 X-coordinate"] = value

    @property
    def vertex_80_ycoordinate(self):
        """Get vertex_80_ycoordinate

        Returns:
            float: the value of `vertex_80_ycoordinate` or None if not set
        """
        return self._data["Vertex 80 Y-coordinate"]

    @vertex_80_ycoordinate.setter
    def vertex_80_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_80_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_80_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_80_ycoordinate`'.format(value))

        self._data["Vertex 80 Y-coordinate"] = value

    @property
    def vertex_80_zcoordinate(self):
        """Get vertex_80_zcoordinate

        Returns:
            float: the value of `vertex_80_zcoordinate` or None if not set
        """
        return self._data["Vertex 80 Z-coordinate"]

    @vertex_80_zcoordinate.setter
    def vertex_80_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_80_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_80_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_80_zcoordinate`'.format(value))

        self._data["Vertex 80 Z-coordinate"] = value

    @property
    def vertex_81_xcoordinate(self):
        """Get vertex_81_xcoordinate

        Returns:
            float: the value of `vertex_81_xcoordinate` or None if not set
        """
        return self._data["Vertex 81 X-coordinate"]

    @vertex_81_xcoordinate.setter
    def vertex_81_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_81_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_81_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_81_xcoordinate`'.format(value))

        self._data["Vertex 81 X-coordinate"] = value

    @property
    def vertex_81_ycoordinate(self):
        """Get vertex_81_ycoordinate

        Returns:
            float: the value of `vertex_81_ycoordinate` or None if not set
        """
        return self._data["Vertex 81 Y-coordinate"]

    @vertex_81_ycoordinate.setter
    def vertex_81_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_81_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_81_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_81_ycoordinate`'.format(value))

        self._data["Vertex 81 Y-coordinate"] = value

    @property
    def vertex_81_zcoordinate(self):
        """Get vertex_81_zcoordinate

        Returns:
            float: the value of `vertex_81_zcoordinate` or None if not set
        """
        return self._data["Vertex 81 Z-coordinate"]

    @vertex_81_zcoordinate.setter
    def vertex_81_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_81_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_81_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_81_zcoordinate`'.format(value))

        self._data["Vertex 81 Z-coordinate"] = value

    @property
    def vertex_82_xcoordinate(self):
        """Get vertex_82_xcoordinate

        Returns:
            float: the value of `vertex_82_xcoordinate` or None if not set
        """
        return self._data["Vertex 82 X-coordinate"]

    @vertex_82_xcoordinate.setter
    def vertex_82_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_82_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_82_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_82_xcoordinate`'.format(value))

        self._data["Vertex 82 X-coordinate"] = value

    @property
    def vertex_82_ycoordinate(self):
        """Get vertex_82_ycoordinate

        Returns:
            float: the value of `vertex_82_ycoordinate` or None if not set
        """
        return self._data["Vertex 82 Y-coordinate"]

    @vertex_82_ycoordinate.setter
    def vertex_82_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_82_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_82_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_82_ycoordinate`'.format(value))

        self._data["Vertex 82 Y-coordinate"] = value

    @property
    def vertex_82_zcoordinate(self):
        """Get vertex_82_zcoordinate

        Returns:
            float: the value of `vertex_82_zcoordinate` or None if not set
        """
        return self._data["Vertex 82 Z-coordinate"]

    @vertex_82_zcoordinate.setter
    def vertex_82_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_82_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_82_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_82_zcoordinate`'.format(value))

        self._data["Vertex 82 Z-coordinate"] = value

    @property
    def vertex_83_xcoordinate(self):
        """Get vertex_83_xcoordinate

        Returns:
            float: the value of `vertex_83_xcoordinate` or None if not set
        """
        return self._data["Vertex 83 X-coordinate"]

    @vertex_83_xcoordinate.setter
    def vertex_83_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_83_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_83_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_83_xcoordinate`'.format(value))

        self._data["Vertex 83 X-coordinate"] = value

    @property
    def vertex_83_ycoordinate(self):
        """Get vertex_83_ycoordinate

        Returns:
            float: the value of `vertex_83_ycoordinate` or None if not set
        """
        return self._data["Vertex 83 Y-coordinate"]

    @vertex_83_ycoordinate.setter
    def vertex_83_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_83_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_83_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_83_ycoordinate`'.format(value))

        self._data["Vertex 83 Y-coordinate"] = value

    @property
    def vertex_83_zcoordinate(self):
        """Get vertex_83_zcoordinate

        Returns:
            float: the value of `vertex_83_zcoordinate` or None if not set
        """
        return self._data["Vertex 83 Z-coordinate"]

    @vertex_83_zcoordinate.setter
    def vertex_83_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_83_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_83_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_83_zcoordinate`'.format(value))

        self._data["Vertex 83 Z-coordinate"] = value

    @property
    def vertex_84_xcoordinate(self):
        """Get vertex_84_xcoordinate

        Returns:
            float: the value of `vertex_84_xcoordinate` or None if not set
        """
        return self._data["Vertex 84 X-coordinate"]

    @vertex_84_xcoordinate.setter
    def vertex_84_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_84_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_84_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_84_xcoordinate`'.format(value))

        self._data["Vertex 84 X-coordinate"] = value

    @property
    def vertex_84_ycoordinate(self):
        """Get vertex_84_ycoordinate

        Returns:
            float: the value of `vertex_84_ycoordinate` or None if not set
        """
        return self._data["Vertex 84 Y-coordinate"]

    @vertex_84_ycoordinate.setter
    def vertex_84_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_84_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_84_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_84_ycoordinate`'.format(value))

        self._data["Vertex 84 Y-coordinate"] = value

    @property
    def vertex_84_zcoordinate(self):
        """Get vertex_84_zcoordinate

        Returns:
            float: the value of `vertex_84_zcoordinate` or None if not set
        """
        return self._data["Vertex 84 Z-coordinate"]

    @vertex_84_zcoordinate.setter
    def vertex_84_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_84_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_84_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_84_zcoordinate`'.format(value))

        self._data["Vertex 84 Z-coordinate"] = value

    @property
    def vertex_85_xcoordinate(self):
        """Get vertex_85_xcoordinate

        Returns:
            float: the value of `vertex_85_xcoordinate` or None if not set
        """
        return self._data["Vertex 85 X-coordinate"]

    @vertex_85_xcoordinate.setter
    def vertex_85_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_85_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_85_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_85_xcoordinate`'.format(value))

        self._data["Vertex 85 X-coordinate"] = value

    @property
    def vertex_85_ycoordinate(self):
        """Get vertex_85_ycoordinate

        Returns:
            float: the value of `vertex_85_ycoordinate` or None if not set
        """
        return self._data["Vertex 85 Y-coordinate"]

    @vertex_85_ycoordinate.setter
    def vertex_85_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_85_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_85_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_85_ycoordinate`'.format(value))

        self._data["Vertex 85 Y-coordinate"] = value

    @property
    def vertex_85_zcoordinate(self):
        """Get vertex_85_zcoordinate

        Returns:
            float: the value of `vertex_85_zcoordinate` or None if not set
        """
        return self._data["Vertex 85 Z-coordinate"]

    @vertex_85_zcoordinate.setter
    def vertex_85_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_85_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_85_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_85_zcoordinate`'.format(value))

        self._data["Vertex 85 Z-coordinate"] = value

    @property
    def vertex_86_xcoordinate(self):
        """Get vertex_86_xcoordinate

        Returns:
            float: the value of `vertex_86_xcoordinate` or None if not set
        """
        return self._data["Vertex 86 X-coordinate"]

    @vertex_86_xcoordinate.setter
    def vertex_86_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_86_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_86_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_86_xcoordinate`'.format(value))

        self._data["Vertex 86 X-coordinate"] = value

    @property
    def vertex_86_ycoordinate(self):
        """Get vertex_86_ycoordinate

        Returns:
            float: the value of `vertex_86_ycoordinate` or None if not set
        """
        return self._data["Vertex 86 Y-coordinate"]

    @vertex_86_ycoordinate.setter
    def vertex_86_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_86_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_86_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_86_ycoordinate`'.format(value))

        self._data["Vertex 86 Y-coordinate"] = value

    @property
    def vertex_86_zcoordinate(self):
        """Get vertex_86_zcoordinate

        Returns:
            float: the value of `vertex_86_zcoordinate` or None if not set
        """
        return self._data["Vertex 86 Z-coordinate"]

    @vertex_86_zcoordinate.setter
    def vertex_86_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_86_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_86_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_86_zcoordinate`'.format(value))

        self._data["Vertex 86 Z-coordinate"] = value

    @property
    def vertex_87_xcoordinate(self):
        """Get vertex_87_xcoordinate

        Returns:
            float: the value of `vertex_87_xcoordinate` or None if not set
        """
        return self._data["Vertex 87 X-coordinate"]

    @vertex_87_xcoordinate.setter
    def vertex_87_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_87_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_87_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_87_xcoordinate`'.format(value))

        self._data["Vertex 87 X-coordinate"] = value

    @property
    def vertex_87_ycoordinate(self):
        """Get vertex_87_ycoordinate

        Returns:
            float: the value of `vertex_87_ycoordinate` or None if not set
        """
        return self._data["Vertex 87 Y-coordinate"]

    @vertex_87_ycoordinate.setter
    def vertex_87_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_87_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_87_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_87_ycoordinate`'.format(value))

        self._data["Vertex 87 Y-coordinate"] = value

    @property
    def vertex_87_zcoordinate(self):
        """Get vertex_87_zcoordinate

        Returns:
            float: the value of `vertex_87_zcoordinate` or None if not set
        """
        return self._data["Vertex 87 Z-coordinate"]

    @vertex_87_zcoordinate.setter
    def vertex_87_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_87_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_87_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_87_zcoordinate`'.format(value))

        self._data["Vertex 87 Z-coordinate"] = value

    @property
    def vertex_88_xcoordinate(self):
        """Get vertex_88_xcoordinate

        Returns:
            float: the value of `vertex_88_xcoordinate` or None if not set
        """
        return self._data["Vertex 88 X-coordinate"]

    @vertex_88_xcoordinate.setter
    def vertex_88_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_88_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_88_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_88_xcoordinate`'.format(value))

        self._data["Vertex 88 X-coordinate"] = value

    @property
    def vertex_88_ycoordinate(self):
        """Get vertex_88_ycoordinate

        Returns:
            float: the value of `vertex_88_ycoordinate` or None if not set
        """
        return self._data["Vertex 88 Y-coordinate"]

    @vertex_88_ycoordinate.setter
    def vertex_88_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_88_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_88_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_88_ycoordinate`'.format(value))

        self._data["Vertex 88 Y-coordinate"] = value

    @property
    def vertex_88_zcoordinate(self):
        """Get vertex_88_zcoordinate

        Returns:
            float: the value of `vertex_88_zcoordinate` or None if not set
        """
        return self._data["Vertex 88 Z-coordinate"]

    @vertex_88_zcoordinate.setter
    def vertex_88_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_88_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_88_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_88_zcoordinate`'.format(value))

        self._data["Vertex 88 Z-coordinate"] = value

    @property
    def vertex_89_xcoordinate(self):
        """Get vertex_89_xcoordinate

        Returns:
            float: the value of `vertex_89_xcoordinate` or None if not set
        """
        return self._data["Vertex 89 X-coordinate"]

    @vertex_89_xcoordinate.setter
    def vertex_89_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_89_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_89_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_89_xcoordinate`'.format(value))

        self._data["Vertex 89 X-coordinate"] = value

    @property
    def vertex_89_ycoordinate(self):
        """Get vertex_89_ycoordinate

        Returns:
            float: the value of `vertex_89_ycoordinate` or None if not set
        """
        return self._data["Vertex 89 Y-coordinate"]

    @vertex_89_ycoordinate.setter
    def vertex_89_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_89_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_89_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_89_ycoordinate`'.format(value))

        self._data["Vertex 89 Y-coordinate"] = value

    @property
    def vertex_89_zcoordinate(self):
        """Get vertex_89_zcoordinate

        Returns:
            float: the value of `vertex_89_zcoordinate` or None if not set
        """
        return self._data["Vertex 89 Z-coordinate"]

    @vertex_89_zcoordinate.setter
    def vertex_89_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_89_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_89_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_89_zcoordinate`'.format(value))

        self._data["Vertex 89 Z-coordinate"] = value

    @property
    def vertex_90_xcoordinate(self):
        """Get vertex_90_xcoordinate

        Returns:
            float: the value of `vertex_90_xcoordinate` or None if not set
        """
        return self._data["Vertex 90 X-coordinate"]

    @vertex_90_xcoordinate.setter
    def vertex_90_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_90_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_90_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_90_xcoordinate`'.format(value))

        self._data["Vertex 90 X-coordinate"] = value

    @property
    def vertex_90_ycoordinate(self):
        """Get vertex_90_ycoordinate

        Returns:
            float: the value of `vertex_90_ycoordinate` or None if not set
        """
        return self._data["Vertex 90 Y-coordinate"]

    @vertex_90_ycoordinate.setter
    def vertex_90_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_90_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_90_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_90_ycoordinate`'.format(value))

        self._data["Vertex 90 Y-coordinate"] = value

    @property
    def vertex_90_zcoordinate(self):
        """Get vertex_90_zcoordinate

        Returns:
            float: the value of `vertex_90_zcoordinate` or None if not set
        """
        return self._data["Vertex 90 Z-coordinate"]

    @vertex_90_zcoordinate.setter
    def vertex_90_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_90_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_90_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_90_zcoordinate`'.format(value))

        self._data["Vertex 90 Z-coordinate"] = value

    @property
    def vertex_91_xcoordinate(self):
        """Get vertex_91_xcoordinate

        Returns:
            float: the value of `vertex_91_xcoordinate` or None if not set
        """
        return self._data["Vertex 91 X-coordinate"]

    @vertex_91_xcoordinate.setter
    def vertex_91_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_91_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_91_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_91_xcoordinate`'.format(value))

        self._data["Vertex 91 X-coordinate"] = value

    @property
    def vertex_91_ycoordinate(self):
        """Get vertex_91_ycoordinate

        Returns:
            float: the value of `vertex_91_ycoordinate` or None if not set
        """
        return self._data["Vertex 91 Y-coordinate"]

    @vertex_91_ycoordinate.setter
    def vertex_91_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_91_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_91_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_91_ycoordinate`'.format(value))

        self._data["Vertex 91 Y-coordinate"] = value

    @property
    def vertex_91_zcoordinate(self):
        """Get vertex_91_zcoordinate

        Returns:
            float: the value of `vertex_91_zcoordinate` or None if not set
        """
        return self._data["Vertex 91 Z-coordinate"]

    @vertex_91_zcoordinate.setter
    def vertex_91_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_91_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_91_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_91_zcoordinate`'.format(value))

        self._data["Vertex 91 Z-coordinate"] = value

    @property
    def vertex_92_xcoordinate(self):
        """Get vertex_92_xcoordinate

        Returns:
            float: the value of `vertex_92_xcoordinate` or None if not set
        """
        return self._data["Vertex 92 X-coordinate"]

    @vertex_92_xcoordinate.setter
    def vertex_92_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_92_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_92_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_92_xcoordinate`'.format(value))

        self._data["Vertex 92 X-coordinate"] = value

    @property
    def vertex_92_ycoordinate(self):
        """Get vertex_92_ycoordinate

        Returns:
            float: the value of `vertex_92_ycoordinate` or None if not set
        """
        return self._data["Vertex 92 Y-coordinate"]

    @vertex_92_ycoordinate.setter
    def vertex_92_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_92_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_92_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_92_ycoordinate`'.format(value))

        self._data["Vertex 92 Y-coordinate"] = value

    @property
    def vertex_92_zcoordinate(self):
        """Get vertex_92_zcoordinate

        Returns:
            float: the value of `vertex_92_zcoordinate` or None if not set
        """
        return self._data["Vertex 92 Z-coordinate"]

    @vertex_92_zcoordinate.setter
    def vertex_92_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_92_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_92_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_92_zcoordinate`'.format(value))

        self._data["Vertex 92 Z-coordinate"] = value

    @property
    def vertex_93_xcoordinate(self):
        """Get vertex_93_xcoordinate

        Returns:
            float: the value of `vertex_93_xcoordinate` or None if not set
        """
        return self._data["Vertex 93 X-coordinate"]

    @vertex_93_xcoordinate.setter
    def vertex_93_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_93_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_93_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_93_xcoordinate`'.format(value))

        self._data["Vertex 93 X-coordinate"] = value

    @property
    def vertex_93_ycoordinate(self):
        """Get vertex_93_ycoordinate

        Returns:
            float: the value of `vertex_93_ycoordinate` or None if not set
        """
        return self._data["Vertex 93 Y-coordinate"]

    @vertex_93_ycoordinate.setter
    def vertex_93_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_93_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_93_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_93_ycoordinate`'.format(value))

        self._data["Vertex 93 Y-coordinate"] = value

    @property
    def vertex_93_zcoordinate(self):
        """Get vertex_93_zcoordinate

        Returns:
            float: the value of `vertex_93_zcoordinate` or None if not set
        """
        return self._data["Vertex 93 Z-coordinate"]

    @vertex_93_zcoordinate.setter
    def vertex_93_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_93_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_93_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_93_zcoordinate`'.format(value))

        self._data["Vertex 93 Z-coordinate"] = value

    @property
    def vertex_94_xcoordinate(self):
        """Get vertex_94_xcoordinate

        Returns:
            float: the value of `vertex_94_xcoordinate` or None if not set
        """
        return self._data["Vertex 94 X-coordinate"]

    @vertex_94_xcoordinate.setter
    def vertex_94_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_94_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_94_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_94_xcoordinate`'.format(value))

        self._data["Vertex 94 X-coordinate"] = value

    @property
    def vertex_94_ycoordinate(self):
        """Get vertex_94_ycoordinate

        Returns:
            float: the value of `vertex_94_ycoordinate` or None if not set
        """
        return self._data["Vertex 94 Y-coordinate"]

    @vertex_94_ycoordinate.setter
    def vertex_94_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_94_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_94_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_94_ycoordinate`'.format(value))

        self._data["Vertex 94 Y-coordinate"] = value

    @property
    def vertex_94_zcoordinate(self):
        """Get vertex_94_zcoordinate

        Returns:
            float: the value of `vertex_94_zcoordinate` or None if not set
        """
        return self._data["Vertex 94 Z-coordinate"]

    @vertex_94_zcoordinate.setter
    def vertex_94_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_94_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_94_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_94_zcoordinate`'.format(value))

        self._data["Vertex 94 Z-coordinate"] = value

    @property
    def vertex_95_xcoordinate(self):
        """Get vertex_95_xcoordinate

        Returns:
            float: the value of `vertex_95_xcoordinate` or None if not set
        """
        return self._data["Vertex 95 X-coordinate"]

    @vertex_95_xcoordinate.setter
    def vertex_95_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_95_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_95_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_95_xcoordinate`'.format(value))

        self._data["Vertex 95 X-coordinate"] = value

    @property
    def vertex_95_ycoordinate(self):
        """Get vertex_95_ycoordinate

        Returns:
            float: the value of `vertex_95_ycoordinate` or None if not set
        """
        return self._data["Vertex 95 Y-coordinate"]

    @vertex_95_ycoordinate.setter
    def vertex_95_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_95_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_95_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_95_ycoordinate`'.format(value))

        self._data["Vertex 95 Y-coordinate"] = value

    @property
    def vertex_95_zcoordinate(self):
        """Get vertex_95_zcoordinate

        Returns:
            float: the value of `vertex_95_zcoordinate` or None if not set
        """
        return self._data["Vertex 95 Z-coordinate"]

    @vertex_95_zcoordinate.setter
    def vertex_95_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_95_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_95_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_95_zcoordinate`'.format(value))

        self._data["Vertex 95 Z-coordinate"] = value

    @property
    def vertex_96_xcoordinate(self):
        """Get vertex_96_xcoordinate

        Returns:
            float: the value of `vertex_96_xcoordinate` or None if not set
        """
        return self._data["Vertex 96 X-coordinate"]

    @vertex_96_xcoordinate.setter
    def vertex_96_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_96_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_96_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_96_xcoordinate`'.format(value))

        self._data["Vertex 96 X-coordinate"] = value

    @property
    def vertex_96_ycoordinate(self):
        """Get vertex_96_ycoordinate

        Returns:
            float: the value of `vertex_96_ycoordinate` or None if not set
        """
        return self._data["Vertex 96 Y-coordinate"]

    @vertex_96_ycoordinate.setter
    def vertex_96_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_96_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_96_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_96_ycoordinate`'.format(value))

        self._data["Vertex 96 Y-coordinate"] = value

    @property
    def vertex_96_zcoordinate(self):
        """Get vertex_96_zcoordinate

        Returns:
            float: the value of `vertex_96_zcoordinate` or None if not set
        """
        return self._data["Vertex 96 Z-coordinate"]

    @vertex_96_zcoordinate.setter
    def vertex_96_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_96_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_96_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_96_zcoordinate`'.format(value))

        self._data["Vertex 96 Z-coordinate"] = value

    @property
    def vertex_97_xcoordinate(self):
        """Get vertex_97_xcoordinate

        Returns:
            float: the value of `vertex_97_xcoordinate` or None if not set
        """
        return self._data["Vertex 97 X-coordinate"]

    @vertex_97_xcoordinate.setter
    def vertex_97_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_97_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_97_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_97_xcoordinate`'.format(value))

        self._data["Vertex 97 X-coordinate"] = value

    @property
    def vertex_97_ycoordinate(self):
        """Get vertex_97_ycoordinate

        Returns:
            float: the value of `vertex_97_ycoordinate` or None if not set
        """
        return self._data["Vertex 97 Y-coordinate"]

    @vertex_97_ycoordinate.setter
    def vertex_97_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_97_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_97_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_97_ycoordinate`'.format(value))

        self._data["Vertex 97 Y-coordinate"] = value

    @property
    def vertex_97_zcoordinate(self):
        """Get vertex_97_zcoordinate

        Returns:
            float: the value of `vertex_97_zcoordinate` or None if not set
        """
        return self._data["Vertex 97 Z-coordinate"]

    @vertex_97_zcoordinate.setter
    def vertex_97_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_97_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_97_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_97_zcoordinate`'.format(value))

        self._data["Vertex 97 Z-coordinate"] = value

    @property
    def vertex_98_xcoordinate(self):
        """Get vertex_98_xcoordinate

        Returns:
            float: the value of `vertex_98_xcoordinate` or None if not set
        """
        return self._data["Vertex 98 X-coordinate"]

    @vertex_98_xcoordinate.setter
    def vertex_98_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_98_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_98_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_98_xcoordinate`'.format(value))

        self._data["Vertex 98 X-coordinate"] = value

    @property
    def vertex_98_ycoordinate(self):
        """Get vertex_98_ycoordinate

        Returns:
            float: the value of `vertex_98_ycoordinate` or None if not set
        """
        return self._data["Vertex 98 Y-coordinate"]

    @vertex_98_ycoordinate.setter
    def vertex_98_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_98_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_98_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_98_ycoordinate`'.format(value))

        self._data["Vertex 98 Y-coordinate"] = value

    @property
    def vertex_98_zcoordinate(self):
        """Get vertex_98_zcoordinate

        Returns:
            float: the value of `vertex_98_zcoordinate` or None if not set
        """
        return self._data["Vertex 98 Z-coordinate"]

    @vertex_98_zcoordinate.setter
    def vertex_98_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_98_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_98_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_98_zcoordinate`'.format(value))

        self._data["Vertex 98 Z-coordinate"] = value

    @property
    def vertex_99_xcoordinate(self):
        """Get vertex_99_xcoordinate

        Returns:
            float: the value of `vertex_99_xcoordinate` or None if not set
        """
        return self._data["Vertex 99 X-coordinate"]

    @vertex_99_xcoordinate.setter
    def vertex_99_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_99_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_99_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_99_xcoordinate`'.format(value))

        self._data["Vertex 99 X-coordinate"] = value

    @property
    def vertex_99_ycoordinate(self):
        """Get vertex_99_ycoordinate

        Returns:
            float: the value of `vertex_99_ycoordinate` or None if not set
        """
        return self._data["Vertex 99 Y-coordinate"]

    @vertex_99_ycoordinate.setter
    def vertex_99_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_99_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_99_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_99_ycoordinate`'.format(value))

        self._data["Vertex 99 Y-coordinate"] = value

    @property
    def vertex_99_zcoordinate(self):
        """Get vertex_99_zcoordinate

        Returns:
            float: the value of `vertex_99_zcoordinate` or None if not set
        """
        return self._data["Vertex 99 Z-coordinate"]

    @vertex_99_zcoordinate.setter
    def vertex_99_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_99_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_99_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_99_zcoordinate`'.format(value))

        self._data["Vertex 99 Z-coordinate"] = value

    @property
    def vertex_100_xcoordinate(self):
        """Get vertex_100_xcoordinate

        Returns:
            float: the value of `vertex_100_xcoordinate` or None if not set
        """
        return self._data["Vertex 100 X-coordinate"]

    @vertex_100_xcoordinate.setter
    def vertex_100_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_100_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_100_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_100_xcoordinate`'.format(value))

        self._data["Vertex 100 X-coordinate"] = value

    @property
    def vertex_100_ycoordinate(self):
        """Get vertex_100_ycoordinate

        Returns:
            float: the value of `vertex_100_ycoordinate` or None if not set
        """
        return self._data["Vertex 100 Y-coordinate"]

    @vertex_100_ycoordinate.setter
    def vertex_100_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_100_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_100_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_100_ycoordinate`'.format(value))

        self._data["Vertex 100 Y-coordinate"] = value

    @property
    def vertex_100_zcoordinate(self):
        """Get vertex_100_zcoordinate

        Returns:
            float: the value of `vertex_100_zcoordinate` or None if not set
        """
        return self._data["Vertex 100 Z-coordinate"]

    @vertex_100_zcoordinate.setter
    def vertex_100_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_100_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_100_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_100_zcoordinate`'.format(value))

        self._data["Vertex 100 Z-coordinate"] = value

    @property
    def vertex_101_xcoordinate(self):
        """Get vertex_101_xcoordinate

        Returns:
            float: the value of `vertex_101_xcoordinate` or None if not set
        """
        return self._data["Vertex 101 X-coordinate"]

    @vertex_101_xcoordinate.setter
    def vertex_101_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_101_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_101_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_101_xcoordinate`'.format(value))

        self._data["Vertex 101 X-coordinate"] = value

    @property
    def vertex_101_ycoordinate(self):
        """Get vertex_101_ycoordinate

        Returns:
            float: the value of `vertex_101_ycoordinate` or None if not set
        """
        return self._data["Vertex 101 Y-coordinate"]

    @vertex_101_ycoordinate.setter
    def vertex_101_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_101_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_101_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_101_ycoordinate`'.format(value))

        self._data["Vertex 101 Y-coordinate"] = value

    @property
    def vertex_101_zcoordinate(self):
        """Get vertex_101_zcoordinate

        Returns:
            float: the value of `vertex_101_zcoordinate` or None if not set
        """
        return self._data["Vertex 101 Z-coordinate"]

    @vertex_101_zcoordinate.setter
    def vertex_101_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_101_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_101_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_101_zcoordinate`'.format(value))

        self._data["Vertex 101 Z-coordinate"] = value

    @property
    def vertex_102_xcoordinate(self):
        """Get vertex_102_xcoordinate

        Returns:
            float: the value of `vertex_102_xcoordinate` or None if not set
        """
        return self._data["Vertex 102 X-coordinate"]

    @vertex_102_xcoordinate.setter
    def vertex_102_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_102_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_102_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_102_xcoordinate`'.format(value))

        self._data["Vertex 102 X-coordinate"] = value

    @property
    def vertex_102_ycoordinate(self):
        """Get vertex_102_ycoordinate

        Returns:
            float: the value of `vertex_102_ycoordinate` or None if not set
        """
        return self._data["Vertex 102 Y-coordinate"]

    @vertex_102_ycoordinate.setter
    def vertex_102_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_102_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_102_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_102_ycoordinate`'.format(value))

        self._data["Vertex 102 Y-coordinate"] = value

    @property
    def vertex_102_zcoordinate(self):
        """Get vertex_102_zcoordinate

        Returns:
            float: the value of `vertex_102_zcoordinate` or None if not set
        """
        return self._data["Vertex 102 Z-coordinate"]

    @vertex_102_zcoordinate.setter
    def vertex_102_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_102_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_102_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_102_zcoordinate`'.format(value))

        self._data["Vertex 102 Z-coordinate"] = value

    @property
    def vertex_103_xcoordinate(self):
        """Get vertex_103_xcoordinate

        Returns:
            float: the value of `vertex_103_xcoordinate` or None if not set
        """
        return self._data["Vertex 103 X-coordinate"]

    @vertex_103_xcoordinate.setter
    def vertex_103_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_103_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_103_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_103_xcoordinate`'.format(value))

        self._data["Vertex 103 X-coordinate"] = value

    @property
    def vertex_103_ycoordinate(self):
        """Get vertex_103_ycoordinate

        Returns:
            float: the value of `vertex_103_ycoordinate` or None if not set
        """
        return self._data["Vertex 103 Y-coordinate"]

    @vertex_103_ycoordinate.setter
    def vertex_103_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_103_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_103_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_103_ycoordinate`'.format(value))

        self._data["Vertex 103 Y-coordinate"] = value

    @property
    def vertex_103_zcoordinate(self):
        """Get vertex_103_zcoordinate

        Returns:
            float: the value of `vertex_103_zcoordinate` or None if not set
        """
        return self._data["Vertex 103 Z-coordinate"]

    @vertex_103_zcoordinate.setter
    def vertex_103_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_103_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_103_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_103_zcoordinate`'.format(value))

        self._data["Vertex 103 Z-coordinate"] = value

    @property
    def vertex_104_xcoordinate(self):
        """Get vertex_104_xcoordinate

        Returns:
            float: the value of `vertex_104_xcoordinate` or None if not set
        """
        return self._data["Vertex 104 X-coordinate"]

    @vertex_104_xcoordinate.setter
    def vertex_104_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_104_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_104_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_104_xcoordinate`'.format(value))

        self._data["Vertex 104 X-coordinate"] = value

    @property
    def vertex_104_ycoordinate(self):
        """Get vertex_104_ycoordinate

        Returns:
            float: the value of `vertex_104_ycoordinate` or None if not set
        """
        return self._data["Vertex 104 Y-coordinate"]

    @vertex_104_ycoordinate.setter
    def vertex_104_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_104_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_104_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_104_ycoordinate`'.format(value))

        self._data["Vertex 104 Y-coordinate"] = value

    @property
    def vertex_104_zcoordinate(self):
        """Get vertex_104_zcoordinate

        Returns:
            float: the value of `vertex_104_zcoordinate` or None if not set
        """
        return self._data["Vertex 104 Z-coordinate"]

    @vertex_104_zcoordinate.setter
    def vertex_104_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_104_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_104_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_104_zcoordinate`'.format(value))

        self._data["Vertex 104 Z-coordinate"] = value

    @property
    def vertex_105_xcoordinate(self):
        """Get vertex_105_xcoordinate

        Returns:
            float: the value of `vertex_105_xcoordinate` or None if not set
        """
        return self._data["Vertex 105 X-coordinate"]

    @vertex_105_xcoordinate.setter
    def vertex_105_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_105_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_105_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_105_xcoordinate`'.format(value))

        self._data["Vertex 105 X-coordinate"] = value

    @property
    def vertex_105_ycoordinate(self):
        """Get vertex_105_ycoordinate

        Returns:
            float: the value of `vertex_105_ycoordinate` or None if not set
        """
        return self._data["Vertex 105 Y-coordinate"]

    @vertex_105_ycoordinate.setter
    def vertex_105_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_105_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_105_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_105_ycoordinate`'.format(value))

        self._data["Vertex 105 Y-coordinate"] = value

    @property
    def vertex_105_zcoordinate(self):
        """Get vertex_105_zcoordinate

        Returns:
            float: the value of `vertex_105_zcoordinate` or None if not set
        """
        return self._data["Vertex 105 Z-coordinate"]

    @vertex_105_zcoordinate.setter
    def vertex_105_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_105_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_105_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_105_zcoordinate`'.format(value))

        self._data["Vertex 105 Z-coordinate"] = value

    @property
    def vertex_106_xcoordinate(self):
        """Get vertex_106_xcoordinate

        Returns:
            float: the value of `vertex_106_xcoordinate` or None if not set
        """
        return self._data["Vertex 106 X-coordinate"]

    @vertex_106_xcoordinate.setter
    def vertex_106_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_106_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_106_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_106_xcoordinate`'.format(value))

        self._data["Vertex 106 X-coordinate"] = value

    @property
    def vertex_106_ycoordinate(self):
        """Get vertex_106_ycoordinate

        Returns:
            float: the value of `vertex_106_ycoordinate` or None if not set
        """
        return self._data["Vertex 106 Y-coordinate"]

    @vertex_106_ycoordinate.setter
    def vertex_106_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_106_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_106_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_106_ycoordinate`'.format(value))

        self._data["Vertex 106 Y-coordinate"] = value

    @property
    def vertex_106_zcoordinate(self):
        """Get vertex_106_zcoordinate

        Returns:
            float: the value of `vertex_106_zcoordinate` or None if not set
        """
        return self._data["Vertex 106 Z-coordinate"]

    @vertex_106_zcoordinate.setter
    def vertex_106_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_106_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_106_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_106_zcoordinate`'.format(value))

        self._data["Vertex 106 Z-coordinate"] = value

    @property
    def vertex_107_xcoordinate(self):
        """Get vertex_107_xcoordinate

        Returns:
            float: the value of `vertex_107_xcoordinate` or None if not set
        """
        return self._data["Vertex 107 X-coordinate"]

    @vertex_107_xcoordinate.setter
    def vertex_107_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_107_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_107_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_107_xcoordinate`'.format(value))

        self._data["Vertex 107 X-coordinate"] = value

    @property
    def vertex_107_ycoordinate(self):
        """Get vertex_107_ycoordinate

        Returns:
            float: the value of `vertex_107_ycoordinate` or None if not set
        """
        return self._data["Vertex 107 Y-coordinate"]

    @vertex_107_ycoordinate.setter
    def vertex_107_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_107_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_107_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_107_ycoordinate`'.format(value))

        self._data["Vertex 107 Y-coordinate"] = value

    @property
    def vertex_107_zcoordinate(self):
        """Get vertex_107_zcoordinate

        Returns:
            float: the value of `vertex_107_zcoordinate` or None if not set
        """
        return self._data["Vertex 107 Z-coordinate"]

    @vertex_107_zcoordinate.setter
    def vertex_107_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_107_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_107_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_107_zcoordinate`'.format(value))

        self._data["Vertex 107 Z-coordinate"] = value

    @property
    def vertex_108_xcoordinate(self):
        """Get vertex_108_xcoordinate

        Returns:
            float: the value of `vertex_108_xcoordinate` or None if not set
        """
        return self._data["Vertex 108 X-coordinate"]

    @vertex_108_xcoordinate.setter
    def vertex_108_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_108_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_108_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_108_xcoordinate`'.format(value))

        self._data["Vertex 108 X-coordinate"] = value

    @property
    def vertex_108_ycoordinate(self):
        """Get vertex_108_ycoordinate

        Returns:
            float: the value of `vertex_108_ycoordinate` or None if not set
        """
        return self._data["Vertex 108 Y-coordinate"]

    @vertex_108_ycoordinate.setter
    def vertex_108_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_108_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_108_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_108_ycoordinate`'.format(value))

        self._data["Vertex 108 Y-coordinate"] = value

    @property
    def vertex_108_zcoordinate(self):
        """Get vertex_108_zcoordinate

        Returns:
            float: the value of `vertex_108_zcoordinate` or None if not set
        """
        return self._data["Vertex 108 Z-coordinate"]

    @vertex_108_zcoordinate.setter
    def vertex_108_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_108_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_108_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_108_zcoordinate`'.format(value))

        self._data["Vertex 108 Z-coordinate"] = value

    @property
    def vertex_109_xcoordinate(self):
        """Get vertex_109_xcoordinate

        Returns:
            float: the value of `vertex_109_xcoordinate` or None if not set
        """
        return self._data["Vertex 109 X-coordinate"]

    @vertex_109_xcoordinate.setter
    def vertex_109_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_109_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_109_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_109_xcoordinate`'.format(value))

        self._data["Vertex 109 X-coordinate"] = value

    @property
    def vertex_109_ycoordinate(self):
        """Get vertex_109_ycoordinate

        Returns:
            float: the value of `vertex_109_ycoordinate` or None if not set
        """
        return self._data["Vertex 109 Y-coordinate"]

    @vertex_109_ycoordinate.setter
    def vertex_109_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_109_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_109_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_109_ycoordinate`'.format(value))

        self._data["Vertex 109 Y-coordinate"] = value

    @property
    def vertex_109_zcoordinate(self):
        """Get vertex_109_zcoordinate

        Returns:
            float: the value of `vertex_109_zcoordinate` or None if not set
        """
        return self._data["Vertex 109 Z-coordinate"]

    @vertex_109_zcoordinate.setter
    def vertex_109_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_109_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_109_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_109_zcoordinate`'.format(value))

        self._data["Vertex 109 Z-coordinate"] = value

    @property
    def vertex_110_xcoordinate(self):
        """Get vertex_110_xcoordinate

        Returns:
            float: the value of `vertex_110_xcoordinate` or None if not set
        """
        return self._data["Vertex 110 X-coordinate"]

    @vertex_110_xcoordinate.setter
    def vertex_110_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_110_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_110_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_110_xcoordinate`'.format(value))

        self._data["Vertex 110 X-coordinate"] = value

    @property
    def vertex_110_ycoordinate(self):
        """Get vertex_110_ycoordinate

        Returns:
            float: the value of `vertex_110_ycoordinate` or None if not set
        """
        return self._data["Vertex 110 Y-coordinate"]

    @vertex_110_ycoordinate.setter
    def vertex_110_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_110_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_110_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_110_ycoordinate`'.format(value))

        self._data["Vertex 110 Y-coordinate"] = value

    @property
    def vertex_110_zcoordinate(self):
        """Get vertex_110_zcoordinate

        Returns:
            float: the value of `vertex_110_zcoordinate` or None if not set
        """
        return self._data["Vertex 110 Z-coordinate"]

    @vertex_110_zcoordinate.setter
    def vertex_110_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_110_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_110_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_110_zcoordinate`'.format(value))

        self._data["Vertex 110 Z-coordinate"] = value

    @property
    def vertex_111_xcoordinate(self):
        """Get vertex_111_xcoordinate

        Returns:
            float: the value of `vertex_111_xcoordinate` or None if not set
        """
        return self._data["Vertex 111 X-coordinate"]

    @vertex_111_xcoordinate.setter
    def vertex_111_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_111_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_111_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_111_xcoordinate`'.format(value))

        self._data["Vertex 111 X-coordinate"] = value

    @property
    def vertex_111_ycoordinate(self):
        """Get vertex_111_ycoordinate

        Returns:
            float: the value of `vertex_111_ycoordinate` or None if not set
        """
        return self._data["Vertex 111 Y-coordinate"]

    @vertex_111_ycoordinate.setter
    def vertex_111_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_111_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_111_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_111_ycoordinate`'.format(value))

        self._data["Vertex 111 Y-coordinate"] = value

    @property
    def vertex_111_zcoordinate(self):
        """Get vertex_111_zcoordinate

        Returns:
            float: the value of `vertex_111_zcoordinate` or None if not set
        """
        return self._data["Vertex 111 Z-coordinate"]

    @vertex_111_zcoordinate.setter
    def vertex_111_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_111_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_111_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_111_zcoordinate`'.format(value))

        self._data["Vertex 111 Z-coordinate"] = value

    @property
    def vertex_112_xcoordinate(self):
        """Get vertex_112_xcoordinate

        Returns:
            float: the value of `vertex_112_xcoordinate` or None if not set
        """
        return self._data["Vertex 112 X-coordinate"]

    @vertex_112_xcoordinate.setter
    def vertex_112_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_112_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_112_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_112_xcoordinate`'.format(value))

        self._data["Vertex 112 X-coordinate"] = value

    @property
    def vertex_112_ycoordinate(self):
        """Get vertex_112_ycoordinate

        Returns:
            float: the value of `vertex_112_ycoordinate` or None if not set
        """
        return self._data["Vertex 112 Y-coordinate"]

    @vertex_112_ycoordinate.setter
    def vertex_112_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_112_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_112_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_112_ycoordinate`'.format(value))

        self._data["Vertex 112 Y-coordinate"] = value

    @property
    def vertex_112_zcoordinate(self):
        """Get vertex_112_zcoordinate

        Returns:
            float: the value of `vertex_112_zcoordinate` or None if not set
        """
        return self._data["Vertex 112 Z-coordinate"]

    @vertex_112_zcoordinate.setter
    def vertex_112_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_112_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_112_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_112_zcoordinate`'.format(value))

        self._data["Vertex 112 Z-coordinate"] = value

    @property
    def vertex_113_xcoordinate(self):
        """Get vertex_113_xcoordinate

        Returns:
            float: the value of `vertex_113_xcoordinate` or None if not set
        """
        return self._data["Vertex 113 X-coordinate"]

    @vertex_113_xcoordinate.setter
    def vertex_113_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_113_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_113_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_113_xcoordinate`'.format(value))

        self._data["Vertex 113 X-coordinate"] = value

    @property
    def vertex_113_ycoordinate(self):
        """Get vertex_113_ycoordinate

        Returns:
            float: the value of `vertex_113_ycoordinate` or None if not set
        """
        return self._data["Vertex 113 Y-coordinate"]

    @vertex_113_ycoordinate.setter
    def vertex_113_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_113_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_113_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_113_ycoordinate`'.format(value))

        self._data["Vertex 113 Y-coordinate"] = value

    @property
    def vertex_113_zcoordinate(self):
        """Get vertex_113_zcoordinate

        Returns:
            float: the value of `vertex_113_zcoordinate` or None if not set
        """
        return self._data["Vertex 113 Z-coordinate"]

    @vertex_113_zcoordinate.setter
    def vertex_113_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_113_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_113_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_113_zcoordinate`'.format(value))

        self._data["Vertex 113 Z-coordinate"] = value

    @property
    def vertex_114_xcoordinate(self):
        """Get vertex_114_xcoordinate

        Returns:
            float: the value of `vertex_114_xcoordinate` or None if not set
        """
        return self._data["Vertex 114 X-coordinate"]

    @vertex_114_xcoordinate.setter
    def vertex_114_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_114_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_114_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_114_xcoordinate`'.format(value))

        self._data["Vertex 114 X-coordinate"] = value

    @property
    def vertex_114_ycoordinate(self):
        """Get vertex_114_ycoordinate

        Returns:
            float: the value of `vertex_114_ycoordinate` or None if not set
        """
        return self._data["Vertex 114 Y-coordinate"]

    @vertex_114_ycoordinate.setter
    def vertex_114_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_114_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_114_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_114_ycoordinate`'.format(value))

        self._data["Vertex 114 Y-coordinate"] = value

    @property
    def vertex_114_zcoordinate(self):
        """Get vertex_114_zcoordinate

        Returns:
            float: the value of `vertex_114_zcoordinate` or None if not set
        """
        return self._data["Vertex 114 Z-coordinate"]

    @vertex_114_zcoordinate.setter
    def vertex_114_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_114_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_114_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_114_zcoordinate`'.format(value))

        self._data["Vertex 114 Z-coordinate"] = value

    @property
    def vertex_115_xcoordinate(self):
        """Get vertex_115_xcoordinate

        Returns:
            float: the value of `vertex_115_xcoordinate` or None if not set
        """
        return self._data["Vertex 115 X-coordinate"]

    @vertex_115_xcoordinate.setter
    def vertex_115_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_115_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_115_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_115_xcoordinate`'.format(value))

        self._data["Vertex 115 X-coordinate"] = value

    @property
    def vertex_115_ycoordinate(self):
        """Get vertex_115_ycoordinate

        Returns:
            float: the value of `vertex_115_ycoordinate` or None if not set
        """
        return self._data["Vertex 115 Y-coordinate"]

    @vertex_115_ycoordinate.setter
    def vertex_115_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_115_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_115_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_115_ycoordinate`'.format(value))

        self._data["Vertex 115 Y-coordinate"] = value

    @property
    def vertex_115_zcoordinate(self):
        """Get vertex_115_zcoordinate

        Returns:
            float: the value of `vertex_115_zcoordinate` or None if not set
        """
        return self._data["Vertex 115 Z-coordinate"]

    @vertex_115_zcoordinate.setter
    def vertex_115_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_115_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_115_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_115_zcoordinate`'.format(value))

        self._data["Vertex 115 Z-coordinate"] = value

    @property
    def vertex_116_xcoordinate(self):
        """Get vertex_116_xcoordinate

        Returns:
            float: the value of `vertex_116_xcoordinate` or None if not set
        """
        return self._data["Vertex 116 X-coordinate"]

    @vertex_116_xcoordinate.setter
    def vertex_116_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_116_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_116_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_116_xcoordinate`'.format(value))

        self._data["Vertex 116 X-coordinate"] = value

    @property
    def vertex_116_ycoordinate(self):
        """Get vertex_116_ycoordinate

        Returns:
            float: the value of `vertex_116_ycoordinate` or None if not set
        """
        return self._data["Vertex 116 Y-coordinate"]

    @vertex_116_ycoordinate.setter
    def vertex_116_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_116_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_116_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_116_ycoordinate`'.format(value))

        self._data["Vertex 116 Y-coordinate"] = value

    @property
    def vertex_116_zcoordinate(self):
        """Get vertex_116_zcoordinate

        Returns:
            float: the value of `vertex_116_zcoordinate` or None if not set
        """
        return self._data["Vertex 116 Z-coordinate"]

    @vertex_116_zcoordinate.setter
    def vertex_116_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_116_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_116_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_116_zcoordinate`'.format(value))

        self._data["Vertex 116 Z-coordinate"] = value

    @property
    def vertex_117_xcoordinate(self):
        """Get vertex_117_xcoordinate

        Returns:
            float: the value of `vertex_117_xcoordinate` or None if not set
        """
        return self._data["Vertex 117 X-coordinate"]

    @vertex_117_xcoordinate.setter
    def vertex_117_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_117_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_117_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_117_xcoordinate`'.format(value))

        self._data["Vertex 117 X-coordinate"] = value

    @property
    def vertex_117_ycoordinate(self):
        """Get vertex_117_ycoordinate

        Returns:
            float: the value of `vertex_117_ycoordinate` or None if not set
        """
        return self._data["Vertex 117 Y-coordinate"]

    @vertex_117_ycoordinate.setter
    def vertex_117_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_117_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_117_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_117_ycoordinate`'.format(value))

        self._data["Vertex 117 Y-coordinate"] = value

    @property
    def vertex_117_zcoordinate(self):
        """Get vertex_117_zcoordinate

        Returns:
            float: the value of `vertex_117_zcoordinate` or None if not set
        """
        return self._data["Vertex 117 Z-coordinate"]

    @vertex_117_zcoordinate.setter
    def vertex_117_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_117_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_117_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_117_zcoordinate`'.format(value))

        self._data["Vertex 117 Z-coordinate"] = value

    @property
    def vertex_118_xcoordinate(self):
        """Get vertex_118_xcoordinate

        Returns:
            float: the value of `vertex_118_xcoordinate` or None if not set
        """
        return self._data["Vertex 118 X-coordinate"]

    @vertex_118_xcoordinate.setter
    def vertex_118_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_118_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_118_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_118_xcoordinate`'.format(value))

        self._data["Vertex 118 X-coordinate"] = value

    @property
    def vertex_118_ycoordinate(self):
        """Get vertex_118_ycoordinate

        Returns:
            float: the value of `vertex_118_ycoordinate` or None if not set
        """
        return self._data["Vertex 118 Y-coordinate"]

    @vertex_118_ycoordinate.setter
    def vertex_118_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_118_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_118_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_118_ycoordinate`'.format(value))

        self._data["Vertex 118 Y-coordinate"] = value

    @property
    def vertex_118_zcoordinate(self):
        """Get vertex_118_zcoordinate

        Returns:
            float: the value of `vertex_118_zcoordinate` or None if not set
        """
        return self._data["Vertex 118 Z-coordinate"]

    @vertex_118_zcoordinate.setter
    def vertex_118_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_118_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_118_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_118_zcoordinate`'.format(value))

        self._data["Vertex 118 Z-coordinate"] = value

    @property
    def vertex_119_xcoordinate(self):
        """Get vertex_119_xcoordinate

        Returns:
            float: the value of `vertex_119_xcoordinate` or None if not set
        """
        return self._data["Vertex 119 X-coordinate"]

    @vertex_119_xcoordinate.setter
    def vertex_119_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_119_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_119_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_119_xcoordinate`'.format(value))

        self._data["Vertex 119 X-coordinate"] = value

    @property
    def vertex_119_ycoordinate(self):
        """Get vertex_119_ycoordinate

        Returns:
            float: the value of `vertex_119_ycoordinate` or None if not set
        """
        return self._data["Vertex 119 Y-coordinate"]

    @vertex_119_ycoordinate.setter
    def vertex_119_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_119_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_119_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_119_ycoordinate`'.format(value))

        self._data["Vertex 119 Y-coordinate"] = value

    @property
    def vertex_119_zcoordinate(self):
        """Get vertex_119_zcoordinate

        Returns:
            float: the value of `vertex_119_zcoordinate` or None if not set
        """
        return self._data["Vertex 119 Z-coordinate"]

    @vertex_119_zcoordinate.setter
    def vertex_119_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_119_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_119_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_119_zcoordinate`'.format(value))

        self._data["Vertex 119 Z-coordinate"] = value

    @property
    def vertex_120_xcoordinate(self):
        """Get vertex_120_xcoordinate

        Returns:
            float: the value of `vertex_120_xcoordinate` or None if not set
        """
        return self._data["Vertex 120 X-coordinate"]

    @vertex_120_xcoordinate.setter
    def vertex_120_xcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_120_xcoordinate`

        Args:
            value (float): value for IDD Field `vertex_120_xcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_120_xcoordinate`'.format(value))

        self._data["Vertex 120 X-coordinate"] = value

    @property
    def vertex_120_ycoordinate(self):
        """Get vertex_120_ycoordinate

        Returns:
            float: the value of `vertex_120_ycoordinate` or None if not set
        """
        return self._data["Vertex 120 Y-coordinate"]

    @vertex_120_ycoordinate.setter
    def vertex_120_ycoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_120_ycoordinate`

        Args:
            value (float): value for IDD Field `vertex_120_ycoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_120_ycoordinate`'.format(value))

        self._data["Vertex 120 Y-coordinate"] = value

    @property
    def vertex_120_zcoordinate(self):
        """Get vertex_120_zcoordinate

        Returns:
            float: the value of `vertex_120_zcoordinate` or None if not set
        """
        return self._data["Vertex 120 Z-coordinate"]

    @vertex_120_zcoordinate.setter
    def vertex_120_zcoordinate(self, value=None):
        """  Corresponds to IDD Field `vertex_120_zcoordinate`

        Args:
            value (float): value for IDD Field `vertex_120_zcoordinate`
                Unit: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `vertex_120_zcoordinate`'.format(value))

        self._data["Vertex 120 Z-coordinate"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.surface_type))
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.outside_boundary_condition))
        out.append(self._to_str(self.outside_boundary_condition_object))
        out.append(self._to_str(self.sun_exposure))
        out.append(self._to_str(self.wind_exposure))
        out.append(self._to_str(self.view_factor_to_ground))
        out.append(self._to_str(self.number_of_vertices))
        out.append(self._to_str(self.vertex_1_xcoordinate))
        out.append(self._to_str(self.vertex_1_ycoordinate))
        out.append(self._to_str(self.vertex_1_zcoordinate))
        out.append(self._to_str(self.vertex_2_xcoordinate))
        out.append(self._to_str(self.vertex_2_ycoordinate))
        out.append(self._to_str(self.vertex_2_zcoordinate))
        out.append(self._to_str(self.vertex_3_xcoordinate))
        out.append(self._to_str(self.vertex_3_ycoordinate))
        out.append(self._to_str(self.vertex_3_zcoordinate))
        out.append(self._to_str(self.vertex_4_xcoordinate))
        out.append(self._to_str(self.vertex_4_ycoordinate))
        out.append(self._to_str(self.vertex_4_zcoordinate))
        out.append(self._to_str(self.vertex_5_xcoordinate))
        out.append(self._to_str(self.vertex_5_ycoordinate))
        out.append(self._to_str(self.vertex_5_zcoordinate))
        out.append(self._to_str(self.vertex_6_xcoordinate))
        out.append(self._to_str(self.vertex_6_ycoordinate))
        out.append(self._to_str(self.vertex_6_zcoordinate))
        out.append(self._to_str(self.vertex_7_xcoordinate))
        out.append(self._to_str(self.vertex_7_ycoordinate))
        out.append(self._to_str(self.vertex_7_zcoordinate))
        out.append(self._to_str(self.vertex_8_xcoordinate))
        out.append(self._to_str(self.vertex_8_ycoordinate))
        out.append(self._to_str(self.vertex_8_zcoordinate))
        out.append(self._to_str(self.vertex_9_xcoordinate))
        out.append(self._to_str(self.vertex_9_ycoordinate))
        out.append(self._to_str(self.vertex_9_zcoordinate))
        out.append(self._to_str(self.vertex_10_xcoordinate))
        out.append(self._to_str(self.vertex_10_ycoordinate))
        out.append(self._to_str(self.vertex_10_zcoordinate))
        out.append(self._to_str(self.vertex_11_xcoordinate))
        out.append(self._to_str(self.vertex_11_ycoordinate))
        out.append(self._to_str(self.vertex_11_zcoordinate))
        out.append(self._to_str(self.vertex_12_xcoordinate))
        out.append(self._to_str(self.vertex_12_ycoordinate))
        out.append(self._to_str(self.vertex_12_zcoordinate))
        out.append(self._to_str(self.vertex_13_xcoordinate))
        out.append(self._to_str(self.vertex_13_ycoordinate))
        out.append(self._to_str(self.vertex_13_zcoordinate))
        out.append(self._to_str(self.vertex_14_xcoordinate))
        out.append(self._to_str(self.vertex_14_ycoordinate))
        out.append(self._to_str(self.vertex_14_zcoordinate))
        out.append(self._to_str(self.vertex_15_xcoordinate))
        out.append(self._to_str(self.vertex_15_ycoordinate))
        out.append(self._to_str(self.vertex_15_zcoordinate))
        out.append(self._to_str(self.vertex_16_xcoordinate))
        out.append(self._to_str(self.vertex_16_ycoordinate))
        out.append(self._to_str(self.vertex_16_zcoordinate))
        out.append(self._to_str(self.vertex_17_xcoordinate))
        out.append(self._to_str(self.vertex_17_ycoordinate))
        out.append(self._to_str(self.vertex_17_zcoordinate))
        out.append(self._to_str(self.vertex_18_xcoordinate))
        out.append(self._to_str(self.vertex_18_ycoordinate))
        out.append(self._to_str(self.vertex_18_zcoordinate))
        out.append(self._to_str(self.vertex_19_xcoordinate))
        out.append(self._to_str(self.vertex_19_ycoordinate))
        out.append(self._to_str(self.vertex_19_zcoordinate))
        out.append(self._to_str(self.vertex_20_xcoordinate))
        out.append(self._to_str(self.vertex_20_ycoordinate))
        out.append(self._to_str(self.vertex_20_zcoordinate))
        out.append(self._to_str(self.vertex_21_xcoordinate))
        out.append(self._to_str(self.vertex_21_ycoordinate))
        out.append(self._to_str(self.vertex_21_zcoordinate))
        out.append(self._to_str(self.vertex_22_xcoordinate))
        out.append(self._to_str(self.vertex_22_ycoordinate))
        out.append(self._to_str(self.vertex_22_zcoordinate))
        out.append(self._to_str(self.vertex_23_xcoordinate))
        out.append(self._to_str(self.vertex_23_ycoordinate))
        out.append(self._to_str(self.vertex_23_zcoordinate))
        out.append(self._to_str(self.vertex_24_xcoordinate))
        out.append(self._to_str(self.vertex_24_ycoordinate))
        out.append(self._to_str(self.vertex_24_zcoordinate))
        out.append(self._to_str(self.vertex_25_xcoordinate))
        out.append(self._to_str(self.vertex_25_ycoordinate))
        out.append(self._to_str(self.vertex_25_zcoordinate))
        out.append(self._to_str(self.vertex_26_xcoordinate))
        out.append(self._to_str(self.vertex_26_ycoordinate))
        out.append(self._to_str(self.vertex_26_zcoordinate))
        out.append(self._to_str(self.vertex_27_xcoordinate))
        out.append(self._to_str(self.vertex_27_ycoordinate))
        out.append(self._to_str(self.vertex_27_zcoordinate))
        out.append(self._to_str(self.vertex_28_xcoordinate))
        out.append(self._to_str(self.vertex_28_ycoordinate))
        out.append(self._to_str(self.vertex_28_zcoordinate))
        out.append(self._to_str(self.vertex_29_xcoordinate))
        out.append(self._to_str(self.vertex_29_ycoordinate))
        out.append(self._to_str(self.vertex_29_zcoordinate))
        out.append(self._to_str(self.vertex_30_xcoordinate))
        out.append(self._to_str(self.vertex_30_ycoordinate))
        out.append(self._to_str(self.vertex_30_zcoordinate))
        out.append(self._to_str(self.vertex_31_xcoordinate))
        out.append(self._to_str(self.vertex_31_ycoordinate))
        out.append(self._to_str(self.vertex_31_zcoordinate))
        out.append(self._to_str(self.vertex_32_xcoordinate))
        out.append(self._to_str(self.vertex_32_ycoordinate))
        out.append(self._to_str(self.vertex_32_zcoordinate))
        out.append(self._to_str(self.vertex_33_xcoordinate))
        out.append(self._to_str(self.vertex_33_ycoordinate))
        out.append(self._to_str(self.vertex_33_zcoordinate))
        out.append(self._to_str(self.vertex_34_xcoordinate))
        out.append(self._to_str(self.vertex_34_ycoordinate))
        out.append(self._to_str(self.vertex_34_zcoordinate))
        out.append(self._to_str(self.vertex_35_xcoordinate))
        out.append(self._to_str(self.vertex_35_ycoordinate))
        out.append(self._to_str(self.vertex_35_zcoordinate))
        out.append(self._to_str(self.vertex_36_xcoordinate))
        out.append(self._to_str(self.vertex_36_ycoordinate))
        out.append(self._to_str(self.vertex_36_zcoordinate))
        out.append(self._to_str(self.vertex_37_xcoordinate))
        out.append(self._to_str(self.vertex_37_ycoordinate))
        out.append(self._to_str(self.vertex_37_zcoordinate))
        out.append(self._to_str(self.vertex_38_xcoordinate))
        out.append(self._to_str(self.vertex_38_ycoordinate))
        out.append(self._to_str(self.vertex_38_zcoordinate))
        out.append(self._to_str(self.vertex_39_xcoordinate))
        out.append(self._to_str(self.vertex_39_ycoordinate))
        out.append(self._to_str(self.vertex_39_zcoordinate))
        out.append(self._to_str(self.vertex_40_xcoordinate))
        out.append(self._to_str(self.vertex_40_ycoordinate))
        out.append(self._to_str(self.vertex_40_zcoordinate))
        out.append(self._to_str(self.vertex_41_xcoordinate))
        out.append(self._to_str(self.vertex_41_ycoordinate))
        out.append(self._to_str(self.vertex_41_zcoordinate))
        out.append(self._to_str(self.vertex_42_xcoordinate))
        out.append(self._to_str(self.vertex_42_ycoordinate))
        out.append(self._to_str(self.vertex_42_zcoordinate))
        out.append(self._to_str(self.vertex_43_xcoordinate))
        out.append(self._to_str(self.vertex_43_ycoordinate))
        out.append(self._to_str(self.vertex_43_zcoordinate))
        out.append(self._to_str(self.vertex_44_xcoordinate))
        out.append(self._to_str(self.vertex_44_ycoordinate))
        out.append(self._to_str(self.vertex_44_zcoordinate))
        out.append(self._to_str(self.vertex_45_xcoordinate))
        out.append(self._to_str(self.vertex_45_ycoordinate))
        out.append(self._to_str(self.vertex_45_zcoordinate))
        out.append(self._to_str(self.vertex_46_xcoordinate))
        out.append(self._to_str(self.vertex_46_ycoordinate))
        out.append(self._to_str(self.vertex_46_zcoordinate))
        out.append(self._to_str(self.vertex_47_xcoordinate))
        out.append(self._to_str(self.vertex_47_ycoordinate))
        out.append(self._to_str(self.vertex_47_zcoordinate))
        out.append(self._to_str(self.vertex_48_xcoordinate))
        out.append(self._to_str(self.vertex_48_ycoordinate))
        out.append(self._to_str(self.vertex_48_zcoordinate))
        out.append(self._to_str(self.vertex_49_xcoordinate))
        out.append(self._to_str(self.vertex_49_ycoordinate))
        out.append(self._to_str(self.vertex_49_zcoordinate))
        out.append(self._to_str(self.vertex_50_xcoordinate))
        out.append(self._to_str(self.vertex_50_ycoordinate))
        out.append(self._to_str(self.vertex_50_zcoordinate))
        out.append(self._to_str(self.vertex_51_xcoordinate))
        out.append(self._to_str(self.vertex_51_ycoordinate))
        out.append(self._to_str(self.vertex_51_zcoordinate))
        out.append(self._to_str(self.vertex_52_xcoordinate))
        out.append(self._to_str(self.vertex_52_ycoordinate))
        out.append(self._to_str(self.vertex_52_zcoordinate))
        out.append(self._to_str(self.vertex_53_xcoordinate))
        out.append(self._to_str(self.vertex_53_ycoordinate))
        out.append(self._to_str(self.vertex_53_zcoordinate))
        out.append(self._to_str(self.vertex_54_xcoordinate))
        out.append(self._to_str(self.vertex_54_ycoordinate))
        out.append(self._to_str(self.vertex_54_zcoordinate))
        out.append(self._to_str(self.vertex_55_xcoordinate))
        out.append(self._to_str(self.vertex_55_ycoordinate))
        out.append(self._to_str(self.vertex_55_zcoordinate))
        out.append(self._to_str(self.vertex_56_xcoordinate))
        out.append(self._to_str(self.vertex_56_ycoordinate))
        out.append(self._to_str(self.vertex_56_zcoordinate))
        out.append(self._to_str(self.vertex_57_xcoordinate))
        out.append(self._to_str(self.vertex_57_ycoordinate))
        out.append(self._to_str(self.vertex_57_zcoordinate))
        out.append(self._to_str(self.vertex_58_xcoordinate))
        out.append(self._to_str(self.vertex_58_ycoordinate))
        out.append(self._to_str(self.vertex_58_zcoordinate))
        out.append(self._to_str(self.vertex_59_xcoordinate))
        out.append(self._to_str(self.vertex_59_ycoordinate))
        out.append(self._to_str(self.vertex_59_zcoordinate))
        out.append(self._to_str(self.vertex_60_xcoordinate))
        out.append(self._to_str(self.vertex_60_ycoordinate))
        out.append(self._to_str(self.vertex_60_zcoordinate))
        out.append(self._to_str(self.vertex_61_xcoordinate))
        out.append(self._to_str(self.vertex_61_ycoordinate))
        out.append(self._to_str(self.vertex_61_zcoordinate))
        out.append(self._to_str(self.vertex_62_xcoordinate))
        out.append(self._to_str(self.vertex_62_ycoordinate))
        out.append(self._to_str(self.vertex_62_zcoordinate))
        out.append(self._to_str(self.vertex_63_xcoordinate))
        out.append(self._to_str(self.vertex_63_ycoordinate))
        out.append(self._to_str(self.vertex_63_zcoordinate))
        out.append(self._to_str(self.vertex_64_xcoordinate))
        out.append(self._to_str(self.vertex_64_ycoordinate))
        out.append(self._to_str(self.vertex_64_zcoordinate))
        out.append(self._to_str(self.vertex_65_xcoordinate))
        out.append(self._to_str(self.vertex_65_ycoordinate))
        out.append(self._to_str(self.vertex_65_zcoordinate))
        out.append(self._to_str(self.vertex_66_xcoordinate))
        out.append(self._to_str(self.vertex_66_ycoordinate))
        out.append(self._to_str(self.vertex_66_zcoordinate))
        out.append(self._to_str(self.vertex_67_xcoordinate))
        out.append(self._to_str(self.vertex_67_ycoordinate))
        out.append(self._to_str(self.vertex_67_zcoordinate))
        out.append(self._to_str(self.vertex_68_xcoordinate))
        out.append(self._to_str(self.vertex_68_ycoordinate))
        out.append(self._to_str(self.vertex_68_zcoordinate))
        out.append(self._to_str(self.vertex_69_xcoordinate))
        out.append(self._to_str(self.vertex_69_ycoordinate))
        out.append(self._to_str(self.vertex_69_zcoordinate))
        out.append(self._to_str(self.vertex_70_xcoordinate))
        out.append(self._to_str(self.vertex_70_ycoordinate))
        out.append(self._to_str(self.vertex_70_zcoordinate))
        out.append(self._to_str(self.vertex_71_xcoordinate))
        out.append(self._to_str(self.vertex_71_ycoordinate))
        out.append(self._to_str(self.vertex_71_zcoordinate))
        out.append(self._to_str(self.vertex_72_xcoordinate))
        out.append(self._to_str(self.vertex_72_ycoordinate))
        out.append(self._to_str(self.vertex_72_zcoordinate))
        out.append(self._to_str(self.vertex_73_xcoordinate))
        out.append(self._to_str(self.vertex_73_ycoordinate))
        out.append(self._to_str(self.vertex_73_zcoordinate))
        out.append(self._to_str(self.vertex_74_xcoordinate))
        out.append(self._to_str(self.vertex_74_ycoordinate))
        out.append(self._to_str(self.vertex_74_zcoordinate))
        out.append(self._to_str(self.vertex_75_xcoordinate))
        out.append(self._to_str(self.vertex_75_ycoordinate))
        out.append(self._to_str(self.vertex_75_zcoordinate))
        out.append(self._to_str(self.vertex_76_xcoordinate))
        out.append(self._to_str(self.vertex_76_ycoordinate))
        out.append(self._to_str(self.vertex_76_zcoordinate))
        out.append(self._to_str(self.vertex_77_xcoordinate))
        out.append(self._to_str(self.vertex_77_ycoordinate))
        out.append(self._to_str(self.vertex_77_zcoordinate))
        out.append(self._to_str(self.vertex_78_xcoordinate))
        out.append(self._to_str(self.vertex_78_ycoordinate))
        out.append(self._to_str(self.vertex_78_zcoordinate))
        out.append(self._to_str(self.vertex_79_xcoordinate))
        out.append(self._to_str(self.vertex_79_ycoordinate))
        out.append(self._to_str(self.vertex_79_zcoordinate))
        out.append(self._to_str(self.vertex_80_xcoordinate))
        out.append(self._to_str(self.vertex_80_ycoordinate))
        out.append(self._to_str(self.vertex_80_zcoordinate))
        out.append(self._to_str(self.vertex_81_xcoordinate))
        out.append(self._to_str(self.vertex_81_ycoordinate))
        out.append(self._to_str(self.vertex_81_zcoordinate))
        out.append(self._to_str(self.vertex_82_xcoordinate))
        out.append(self._to_str(self.vertex_82_ycoordinate))
        out.append(self._to_str(self.vertex_82_zcoordinate))
        out.append(self._to_str(self.vertex_83_xcoordinate))
        out.append(self._to_str(self.vertex_83_ycoordinate))
        out.append(self._to_str(self.vertex_83_zcoordinate))
        out.append(self._to_str(self.vertex_84_xcoordinate))
        out.append(self._to_str(self.vertex_84_ycoordinate))
        out.append(self._to_str(self.vertex_84_zcoordinate))
        out.append(self._to_str(self.vertex_85_xcoordinate))
        out.append(self._to_str(self.vertex_85_ycoordinate))
        out.append(self._to_str(self.vertex_85_zcoordinate))
        out.append(self._to_str(self.vertex_86_xcoordinate))
        out.append(self._to_str(self.vertex_86_ycoordinate))
        out.append(self._to_str(self.vertex_86_zcoordinate))
        out.append(self._to_str(self.vertex_87_xcoordinate))
        out.append(self._to_str(self.vertex_87_ycoordinate))
        out.append(self._to_str(self.vertex_87_zcoordinate))
        out.append(self._to_str(self.vertex_88_xcoordinate))
        out.append(self._to_str(self.vertex_88_ycoordinate))
        out.append(self._to_str(self.vertex_88_zcoordinate))
        out.append(self._to_str(self.vertex_89_xcoordinate))
        out.append(self._to_str(self.vertex_89_ycoordinate))
        out.append(self._to_str(self.vertex_89_zcoordinate))
        out.append(self._to_str(self.vertex_90_xcoordinate))
        out.append(self._to_str(self.vertex_90_ycoordinate))
        out.append(self._to_str(self.vertex_90_zcoordinate))
        out.append(self._to_str(self.vertex_91_xcoordinate))
        out.append(self._to_str(self.vertex_91_ycoordinate))
        out.append(self._to_str(self.vertex_91_zcoordinate))
        out.append(self._to_str(self.vertex_92_xcoordinate))
        out.append(self._to_str(self.vertex_92_ycoordinate))
        out.append(self._to_str(self.vertex_92_zcoordinate))
        out.append(self._to_str(self.vertex_93_xcoordinate))
        out.append(self._to_str(self.vertex_93_ycoordinate))
        out.append(self._to_str(self.vertex_93_zcoordinate))
        out.append(self._to_str(self.vertex_94_xcoordinate))
        out.append(self._to_str(self.vertex_94_ycoordinate))
        out.append(self._to_str(self.vertex_94_zcoordinate))
        out.append(self._to_str(self.vertex_95_xcoordinate))
        out.append(self._to_str(self.vertex_95_ycoordinate))
        out.append(self._to_str(self.vertex_95_zcoordinate))
        out.append(self._to_str(self.vertex_96_xcoordinate))
        out.append(self._to_str(self.vertex_96_ycoordinate))
        out.append(self._to_str(self.vertex_96_zcoordinate))
        out.append(self._to_str(self.vertex_97_xcoordinate))
        out.append(self._to_str(self.vertex_97_ycoordinate))
        out.append(self._to_str(self.vertex_97_zcoordinate))
        out.append(self._to_str(self.vertex_98_xcoordinate))
        out.append(self._to_str(self.vertex_98_ycoordinate))
        out.append(self._to_str(self.vertex_98_zcoordinate))
        out.append(self._to_str(self.vertex_99_xcoordinate))
        out.append(self._to_str(self.vertex_99_ycoordinate))
        out.append(self._to_str(self.vertex_99_zcoordinate))
        out.append(self._to_str(self.vertex_100_xcoordinate))
        out.append(self._to_str(self.vertex_100_ycoordinate))
        out.append(self._to_str(self.vertex_100_zcoordinate))
        out.append(self._to_str(self.vertex_101_xcoordinate))
        out.append(self._to_str(self.vertex_101_ycoordinate))
        out.append(self._to_str(self.vertex_101_zcoordinate))
        out.append(self._to_str(self.vertex_102_xcoordinate))
        out.append(self._to_str(self.vertex_102_ycoordinate))
        out.append(self._to_str(self.vertex_102_zcoordinate))
        out.append(self._to_str(self.vertex_103_xcoordinate))
        out.append(self._to_str(self.vertex_103_ycoordinate))
        out.append(self._to_str(self.vertex_103_zcoordinate))
        out.append(self._to_str(self.vertex_104_xcoordinate))
        out.append(self._to_str(self.vertex_104_ycoordinate))
        out.append(self._to_str(self.vertex_104_zcoordinate))
        out.append(self._to_str(self.vertex_105_xcoordinate))
        out.append(self._to_str(self.vertex_105_ycoordinate))
        out.append(self._to_str(self.vertex_105_zcoordinate))
        out.append(self._to_str(self.vertex_106_xcoordinate))
        out.append(self._to_str(self.vertex_106_ycoordinate))
        out.append(self._to_str(self.vertex_106_zcoordinate))
        out.append(self._to_str(self.vertex_107_xcoordinate))
        out.append(self._to_str(self.vertex_107_ycoordinate))
        out.append(self._to_str(self.vertex_107_zcoordinate))
        out.append(self._to_str(self.vertex_108_xcoordinate))
        out.append(self._to_str(self.vertex_108_ycoordinate))
        out.append(self._to_str(self.vertex_108_zcoordinate))
        out.append(self._to_str(self.vertex_109_xcoordinate))
        out.append(self._to_str(self.vertex_109_ycoordinate))
        out.append(self._to_str(self.vertex_109_zcoordinate))
        out.append(self._to_str(self.vertex_110_xcoordinate))
        out.append(self._to_str(self.vertex_110_ycoordinate))
        out.append(self._to_str(self.vertex_110_zcoordinate))
        out.append(self._to_str(self.vertex_111_xcoordinate))
        out.append(self._to_str(self.vertex_111_ycoordinate))
        out.append(self._to_str(self.vertex_111_zcoordinate))
        out.append(self._to_str(self.vertex_112_xcoordinate))
        out.append(self._to_str(self.vertex_112_ycoordinate))
        out.append(self._to_str(self.vertex_112_zcoordinate))
        out.append(self._to_str(self.vertex_113_xcoordinate))
        out.append(self._to_str(self.vertex_113_ycoordinate))
        out.append(self._to_str(self.vertex_113_zcoordinate))
        out.append(self._to_str(self.vertex_114_xcoordinate))
        out.append(self._to_str(self.vertex_114_ycoordinate))
        out.append(self._to_str(self.vertex_114_zcoordinate))
        out.append(self._to_str(self.vertex_115_xcoordinate))
        out.append(self._to_str(self.vertex_115_ycoordinate))
        out.append(self._to_str(self.vertex_115_zcoordinate))
        out.append(self._to_str(self.vertex_116_xcoordinate))
        out.append(self._to_str(self.vertex_116_ycoordinate))
        out.append(self._to_str(self.vertex_116_zcoordinate))
        out.append(self._to_str(self.vertex_117_xcoordinate))
        out.append(self._to_str(self.vertex_117_ycoordinate))
        out.append(self._to_str(self.vertex_117_zcoordinate))
        out.append(self._to_str(self.vertex_118_xcoordinate))
        out.append(self._to_str(self.vertex_118_ycoordinate))
        out.append(self._to_str(self.vertex_118_zcoordinate))
        out.append(self._to_str(self.vertex_119_xcoordinate))
        out.append(self._to_str(self.vertex_119_ycoordinate))
        out.append(self._to_str(self.vertex_119_zcoordinate))
        out.append(self._to_str(self.vertex_120_xcoordinate))
        out.append(self._to_str(self.vertex_120_ycoordinate))
        out.append(self._to_str(self.vertex_120_zcoordinate))
        return ",".join(out)