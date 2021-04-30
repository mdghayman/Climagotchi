# https://www.ipcc.ch/site/assets/uploads/2018/02/SYR_AR5_FINAL_full.pdf
# Page 2

class ocean:
    def __init__(self, temp, el_nino, pH, salinity, sea_level):
        self.temp = temp
        self.el_nino = el_nino
        self.pH = pH
        self.sea_level = sea_level
        self.ice_sheets = ice_sheets

def sea_temp():
    min_year = 1880
    max_year = 2012
    if el_nino == True:
        min_change = -0.05
        avg_change = 0.05
        max_change = 0.15
    else:
        min_change = 0.65
        avg_change = 0.85
        max_change = 1.06

def el_nino():
    if el_nino == True:
        pass
    else:
        pass

def pH():
    total_change_pH = 0.1
    total_change_perc = 0.26

def sea_level():
    pass

def ice_sheets():
    min_change = -0.0
    min_year = 1992
    max_year = 2011

class ice_sheets:
    def __init__(self):
        pass

class permafrost:
    def __init__(self):
        pass

class land_surface:
    def __init__(self):
        pass

class forests:
    def __init__(self):
        pass
