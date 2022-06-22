from dataclasses import dataclass

@dataclass
class KMLReader:

    @classmethod
    def coordinates_to_dict(cls, filepath: str):
        """Reads the coodinate of a KML file and converts
        it to a Python Dictionary.

        The valid format is the one from My Maps Google app.
        
        Args:
            filepath (str): The full path to *.kml file.
        
        Returns:
            Python dictionary with coordinates as a list and
            keys as str.
        """
        from fastkml import KML

        kml = KML()

        with open(filepath, mode='r') as kml_io:
            io_file = kml_io.read().encode('utf-8')
        
        kml.from_string(io_file)
        try:
            kml_destinations = next(kml.features())
        except StopIteration:
            StopIteration('Error while reading the kml.')

        return {
            item.name: [item.geometry.x, item.geometry.y]
            for item in kml_destinations.features()
         }