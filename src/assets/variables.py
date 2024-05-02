import panel as pn


class GeneralVariables:
    def __init__(self):
        self.dims = ["1D Plot", "2D Plot"]
        self.plots1D = {"1D Plots": ["Violin", "Histogram", "Density", "Bar", "Map"]}
        self.plots2D = {"2D Plots": ["Point", "2D Density", "Quantiles"]}
        self.datasets = [
            "DATA",
            "PDAT",
            "GNOM",
            "PGNO",
            "GENI",
            "PGEN",
            "1KGP",
            "HGDP",
            "SGDP",
            "VANU",
            "IGDP",
            "AYTA",
            "OFAR",
        ]
        self.ancestries = [
            "All",
            "Ambiguous",
            "Denisova",
            "Neanderthal",
            "Altai",
            "Vindija",
            "Chagyrskaya",
            "AmbigNean",
            "nonDAVC",
        ]
        self.regions = ["EUR", "MID", "SAS", "AFR", "EAS", "AMR", "OCE", "CAS"]
        self.disc_chrom = ["A", "X", "Xprime"]


class StaIndVariables:
    def __init__(self):
        self.plot_vars = [
            "ind",
            "sex",
            "pop",
            "reg",
            "dat",
            "oda",
            "tim",
            "lat",
            "lon",
            "chrom",
            "anc",
            "len_mea",
            "len_med",
            "len_max",
            "len_min",
            "nfr",
            "seq",
            "ancAMR",
            "ancEAS",
            "ancSAS",
            "ancAFR",
            "ancEUR",
            "ancOCE",
        ]
        self.plot_facets = ["ind", "sex", "dat", "oda", "reg", "pop", "chrom", "anc"]
        self.colors = [
            "lat",
            "lon",
            "len_mea",
            "len_med",
            "len_max",
            "len_min",
            "reg",
            "nfr",
            "seq",
            "ancAFR",
            "ancAMR",
            "ancEAS",
            "ancEUR",
            "ancOCE",
            "ancSAS",
        ]

