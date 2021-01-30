from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

record = SeqIO.read("Genome.gb", "genbank")


""" Creating an empty diagram, empty track, and empty feature set (in that order)
    Will later add in all the tracks and features needed.
"""
gd_diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
gd_track = gd_diagram.new_track(1, name="Annotated Features")
gd_features = gd_track.new_set()


""" Read each gene and generate a feature for the Diagram
    The colors will alternate between red and orange
"""
for feature in record.features:
    # if this is not of type gene, skip it
    if feature.type != "gene":
        continue
    
    # alternate colors based on the number of features already in the set
    # Split into 3 colors: red, orange, aqua (in that order)
    if len(gd_features) % 3 == 0:
        color = colors.red
    elif len(gd_features) % 3 == 1:
        color = colors.orange
    else:
        color = colors.aqua
    
    gd_features.add_feature(
        feature,
        sigil="ARROW",
        color=color,
        label_position="end",
        label=True,
        label_size=15,
    )


""" The following sets all the options for drawing the diagram
    The settings are specific to create a circular diagram
    The diagram will be created in a png file
"""
gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize="A4",
    start=0,
    end=len(record),
    circle_core=0.5,
)
gd_diagram.write("TYLCV_circular.png", "PNG")
gd_diagram.write("TYLCV_circular.jpg", "JPG")
