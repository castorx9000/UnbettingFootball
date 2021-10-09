from os import pathsep
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


logos_paths = {

    #United Kingdom - FL Championship
    "Watford": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Watford.png',
    "Birmingham": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Birmingham.png',
    "Barnsley": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Barnsley.png',
    "Bristol City": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Bristol City.png',
    "Derby": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Derby.png',
    "Huddersfield": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Huddersfield.png',
    "Millwall": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Millwall.png',
    "QPR": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\QPR.png',
    "Coventry": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Coventry.png',
    "Nott'm Forest": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Nott m Forest.png',
    "Blackburn": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Blackburn.png',
    "Brentford": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Brentford.png',
    "Luton": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Middlesbrough.png',
    "Middlesbrough": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Middlesbrough.png',
    "Norwich": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Norwich.png',
    "Reading": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Reading.png',
    "Rotherham": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Rotherham.png',
    "Sheffield Weds": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Sheffield Weds.png',
    "Swansea": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Swansea.png',
    "Stoke": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Stoke.png',
    "Preston": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Preston.png',
    "Wycombe": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Wycombe.png',
    "Cardiff": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Cardiff.png',
    "Bournemouth": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Championship\Bournemouth.png',

    #Portugal
    "Famalicao": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Famalicao.png',
    "Guimaraes": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Guimaraes.png',
    "Nacional": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Nacional.png',
    "Porto": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Porto.png',
    "Santa Clara": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Santa Clara.png',
    "Moreirense": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Moreirense.png',
    "Tondela": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Tondela.png',
    "Portimonense": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Portimonense.png',
    "Sp Braga": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Sp Braga.png',
    "Maritimo": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Maritimo.png',
    "Benfica": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Benfica.png',
    "Boavista": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Boavista.png',
    "Farense": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Farense.png',
    "Gil Vicente": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Gil Vicente.png',
    "Pacos Ferreira": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Pacos Ferreira.png',
    "Rio Ave": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Rio Ave.png',
    "Belenenses": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Belenenses.png',
    "Sp Lisbon": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Primeira Liga\Sp Lisbon.png',
    
    #Netherlands
    "Heerenveen": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Heerenveen48x48.png',
    "Zwolle": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Zwolle48x48.png',
    "Twente": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Twente48x48.png',
    "FC Emmen": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\FC Emmen48x48.png',
    "Heracles": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Heracles48x48.png',
    "Sparta Rotterdam": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Sparta Rotterdam48x48.png',
    "Groningen": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Groningen48x48.png',
    "Waalwijk": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\WaalwijkGENERIC48x48.png',
    "VVV Venlo": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\VVV Venlo48x48.png',
    "AZ Alkmaar": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\AZ Alkmaar48x48.png',
    "Vitesse": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Vitesse48x48.png',
    "PSV Eindhoven": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\PSV Eindhoven48x48.png',
    "For Sittard": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\For Sittard48x48.png',
    "Den Haag": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Den Haag48x48.png',
    "Feyenoord": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Feyenoord48x48.png',
    "Willem II": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Willem II48x48.png',
    "Ajax": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Ajax48x48.png',
    "Utrecht": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Eredivisie\Utrecht48x48.png',

    #France
    "Bordeaux": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Bordeaux48x48.png',
    "Dijon": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Dijon48x48.png',
    "Lille": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Lille48x48.png',
    "Monaco": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Monaco48x48.png',
    "Lorient": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Lorient48x48.png',
    "Nimes": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Nimes48x48.png',
    "Nice": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Nice48x48.png',
    "Lyon": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Lyon48x48.png',
    "Rennes": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Rennes48x48.png',
    "Strasbourg": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Strasbourg48x48.png',
    "Reims": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Reims48x48.png',
    "Angers": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Angers48x48.png',
    "Metz": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Metz48x48.png',
    "Nantes": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Nantes48x48.png',
    "St Etienne": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\St Etienne48x48.png',
    "Brest": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Brest48x48.png',
    "Lens": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Lens48x48.png',
    "Montpellier": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Montpellier48x48.png',
    "Paris SG": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Paris SG48x48.png',
    "Marseille": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Ligue_1\Marseille48x48.png',

    #Spain
    "Alaves": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Alaves48x48.png',
    "Ath Bilbao": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Ath Bilbao48x48.png',
    "Ath Madrid": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Ath Madrid48x48.png',
    "Barcelona": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Barcelona48x48.png',
    "Betis": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Betis48x48.png',
    "Cadiz": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Cadiz48x48.png',
    "Celta": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Celta48x48.png',
    "Eibar": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Eibar48x48.png',
    "Elche": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Elche48x48.png',
    "Getafe": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Getafe48x48.png',
    "Granada": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Granada48x48.png',
    "Huesca": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Huesca48x48.png',
    "Levante": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Levante48x48.png',
    "Osasuna": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Osasuna48x48.png',
    "Real Madrid": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Real Madrid48x48.png',
    "Sevilla": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Sevilla48x48.png',
    "Sociedad": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Sociedad48x48.png',
    "Valencia": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Valencia48x48.png',
    "Valladolid": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Valladolid48x48.png',
    "Villarreal": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LaLiga\Villarreal48x48.png',

    #United Kingdom - EPL
    "Arsenal": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Arsenal48x48.png',
    "Aston Villa": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Aston Villa48x48.png',
    "Brighton": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Brighton48x48.png',
    "Burnley": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Burnley48x48.png',
    "Chelsea": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Chelsea48x48.png',
    "Crystal Palace": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Crystal Palace48x48.png',
    "Everton": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Everton48x48.png',
    "Fulham": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Fulham48x48.png',
    "Leeds": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Leeds48x48.png',
    "Leicester": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Leicester48x48.png',
    "Liverpool": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Liverpool48x48.png',
    "Man City": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Man City48x48.png',
    "Man United": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Man United48x48.png',
    "Newcastle": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Newcastle48x48.png',
    "Sheffield United": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Sheffield United48x48.png',
    "Southampton": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Southampton48x48.png',
    "Tottenham": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Tottenham48x48.png',
    "West Brom": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\West Brom48x48.png',
    "West Ham": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\West Ham48x48.png',
    "Wolves": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\EPL\Wolves48x48.png',

    #Italy
    "Atalanta": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Atalanta48x48.png',
    "Benevento": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Benevento48x48.png',
    "Bologna": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Bologna48x48.png',
    "Cagliari": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Cagliari48x48.png',
    "Crotone": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Crotone48x48.png',
    "Fiorentina": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Fiorentina48x48.png',
    "Genoa": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Genoa48x48.png',
    "Inter": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Inter48x48.png',
    "Juventus": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Juventus48x48.png',
    "Lazio": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Lazio48x48.png',
    "Milan": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Milan48x48.png',
    "Napoli": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Napoli48x48.png',
    "Parma": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Parma48x48.png',
    "Roma": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Roma48x48.png',
    "Sampdoria": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Sampdoria48x48.png',
    "Sassuolo": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Sassuolo48x48.png',
    "Spezia": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Spezia48x48.png',
    "Torino": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Torino48x48.png',
    "Udinese": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Udinese48x48.png',
    "Verona": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Serie_A\Verona48x48.png',

    #Germany
    "Bielefeld":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Arminia48x48.png',
    "Augsburg":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Augsburg48x48.png',
    "Bayern Munich":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Bayern_Munich48x48.png',
    "Dortmund":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Dortmund48x48.png',
    "Ein Frankfurt":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Frankfurt48x48.png',
    "Freiburg":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Freiburg48x48.png',
    "Hertha":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Hertha_Berlin48x48.png',
    "Hoffenheim":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Hoffenheim48x48.png',
    "FC Koln":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Koln48x48.png',
    "Leverkusen":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Leverkusen48x48.png',
    "Mainz":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Mainz48x48.png',
    "M'gladbach":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Monchengladbach48x48.png',
    "RB Leipzig":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\RB_Leipzig48x48.png',
    "Schalke 04":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Schalke48x48.png',
    "Stuttgart":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Stuttgart48x48.png',
    "Union Berlin":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Union_Berlin48x48.png',
    "Werder Bremen":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Werder_Bremen48x48.png',
    "Wolfsburg":r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\Bundesliga\Wolfsburg48x48.png',

    #Mexico
    "Club America": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\AME96X96.png',
    "Cruz Azul": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\CRA96X96.png',
    "Puebla": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\PUE96X96.png',
    "Mazatlan FC": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\MAZ96X96.png',
    "Toluca": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\TOL96X96.png',
    "Santos Laguna": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\SAN96X96.png',
    "Queretaro": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\QRO96X96.png',
    "U.N.A.M.- Pumas": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\PUM96X96.png',
    "Guadalajara Chivas": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\CHI96X96.png',
    "Club Leon": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\LEO96X96.png',
    "Club Tijuana": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\TIJ96X96.png',
    "Atlas": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\ATL96X96.png',
    "Pachuca": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\PAC96X96.png',
    "Monterrey": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\MON96X96.png',
    "Juarez": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\JUA96X96.png',
    "U.A.N.L.- Tigres": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\TIG96X96.png',
    "Atl. San Luis": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\ASL96X96.png',
    "Necaxa": r'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_Logos\NEC96X96.png'

}


def get_logos_path(clubs,logos_paths):

    paths = []

    for club in clubs:
        paths.append(logos_paths[club])

    return paths


if __name__ == "__main__":

    #Configuration
    file = 'Championship_2020-2021_03-06-2021.xlsx'
    league = 'Championship'
    season = '2020/2021'

    #Activities before plotting
    clubs_df = pd.read_excel(f'D:\Dropbox\La Cima del Éxito\Futbol\Clubs_performances\{file}')
    clubs_df = clubs_df[['Club','Performance','obPPM','exPPM','h_obPPM','h_exPPM','a_obPPM','a_exPPM','p_SG','p_CG','obSGPM','exSGPM','obCGPM','exCGPM']]
    clubs_df = clubs_df.sort_values(by=['Performance'], ascending=False)

    obPPM = clubs_df['obPPM'].tolist()
    exPPM = clubs_df['exPPM'].tolist()

    h_obPPM = clubs_df['h_obPPM'].tolist()
    h_exPPM = clubs_df['h_exPPM'].tolist()
    a_obPPM = clubs_df['a_obPPM'].tolist()
    a_exPPM = clubs_df['a_exPPM'].tolist()

    obSGPM = clubs_df['obSGPM'].tolist()
    exSGPM = clubs_df['exSGPM'].tolist()
    obCGPM = clubs_df['obCGPM'].tolist()
    exCGPM = clubs_df['exCGPM'].tolist()

    clubs = clubs_df['Club'].tolist()

    performances = clubs_df['Performance'].tolist()
    performances = [ i*100 for i in performances ]

    #Plotting
    
    paths = get_logos_path(clubs,logos_paths)

    fig, ax = plt.subplots()
    
    for x, y, path in zip(exPPM, obPPM, paths):
        ab = AnnotationBbox(OffsetImage(plt.imread(path), zoom=0.6), (x, y), frameon=False)
        ax.add_artist(ab)

    plt.xlim(0,3)
    plt.ylim(0,3)
    plt.xlabel('Expected Points Per Match', fontsize=15)
    plt.ylabel('Obtained Points Per Match', fontsize=15)
    fig.suptitle(f'Expected vs Obtained Points Per Match\n{league} season {season}', fontsize = 25)

    x = np.linspace(0,3,50)
    y = x

    plt.plot(x, y, color='black',linestyle='dashed')
    
    plt.style.use('fivethirtyeight')
    plt.show()
    #print(clubs_df)