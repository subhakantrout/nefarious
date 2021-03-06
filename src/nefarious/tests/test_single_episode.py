from nefarious.parsers.tv import TVParser
from django.test import TestCase


class TVMatch(TestCase):
    tv_single_episode_tests = []

    def setUp(self):
        # single episode tests
        self.tv_single_episode_tests = [
            ["Sonny.With.a.Chance.S02E15", "Sonny With a Chance", 2, 15],
            ["Two.and.a.Half.Me.103.720p.HDTV.X264-DIMENSION", "Two and a Half Me", 1, 3],
            ["Two.and.a.Half.Me.113.720p.HDTV.X264-DIMENSION", "Two and a Half Me", 1, 13],
            ["Two.and.a.Half.Me.1013.720p.HDTV.X264-DIMENSION", "Two and a Half Me", 10, 13],
            ["Chuck.4x05.HDTV.XviD-LOL", "Chuck", 4, 5],
            ["The.Girls.Next.Door.S03E06.DVDRip.XviD-WiDE", "The Girls Next Door", 3, 6],
            ["Degrassi.S10E27.WS.DSR.XviD-2HD", "Degrassi", 10, 27],
            ["Parenthood.2010.S02E14.HDTV.XviD-LOL", "Parenthood", 2, 14],
            ["Hawaii Five 0 S01E19 720p WEB DL DD5 1 H 264 NT", "Hawaii Five 0", 1, 19],
            ["The Event S01E14 A Message Back 720p WEB DL DD5 1 H264 SURFER", "The Event", 1, 14],
            ["Adam Hills In Gordon St Tonight S01E07 WS PDTV XviD FUtV", "Adam Hills In Gordon St Tonight", 1, 7],
            ["Adventure.Inc.S03E19.DVDRip.XviD-OSiTV", "Adventure Inc", 3, 19],
            ["S03E09 WS PDTV XviD FUtV", "", 3, 9],
            ["5x10 WS PDTV XviD FUtV", "", 5, 10],
            ["Castle.2009.S01E14.HDTV.XviD-LOL", "Castle", 1, 14],
            ["Pride.and.Prejudice.1995.S03E20.HDTV.XviD-LOL", "Pride and Prejudice", 3, 20],
            ["The.Office.S03E115.DVDRip.XviD-OSiTV", "The Office", 3, 115],
            ["Parks and Recreation - S02E21 - 94 Meetings - 720p TV.mkv", "Parks and Recreation", 2, 21],
            ["24-7 Penguins-Capitals- Road to the NHL Winter Classic - S01E03 - Episode 3.mkv", "24-7 Penguins-Capitals- Road to the NHL Winter Classic", 1, 3],
            ["Adventure.Inc.S03E19.DVDRip.\"XviD\"-OSiTV", "Adventure Inc", 3, 19],
            ["Hawaii Five-0 (2010) - 1x05 - Nalowale (Forgotten/Missing)", "Hawaii Five-0", 1, 5],
            ["Hawaii Five-0 (2010) - 1x05 - Title", "Hawaii Five-0", 1, 5],
            ["House - S06E13 - 5 to 9 [DVD]", "House", 6, 13],
            ["The Mentalist - S02E21 - 18-5-4", "The Mentalist", 2, 21],
            ["Breaking.In.S01E07.21.0.Jump.Street.720p.WEB-DL.DD5.1.h.264-KiNGS", "Breaking In", 1, 7],
            ["CSI.525", "CSI", 5, 25],
            ["King of the Hill - 10x12 - 24 Hour Propane People [SDTV]", "King of the Hill", 10, 12],
            ["Brew Masters S01E06 3 Beers For Batali DVDRip XviD SPRiNTER", "Brew Masters", 1, 6],
            ["24 7 Flyers Rangers Road to the NHL Winter Classic Part01 720p HDTV x264 ORENJI", "24 7 Flyers Rangers Road to the NHL Winter Classic", 1, 1],
            ["24 7 Flyers Rangers Road to the NHL Winter Classic Part 02 720p HDTV x264 ORENJI", "24 7 Flyers Rangers Road to the NHL Winter Classic", 1, 2],
            ["24-7 Flyers-Rangers- Road to the NHL Winter Classic - S01E01 - Part 1", "24-7 Flyers-Rangers- Road to the NHL Winter Classic", 1, 1],
            ["S6E02-Unwrapped-(Playing With Food) - [DarkData]", "", 6, 2],
            ["S06E03-Unwrapped-(Number Ones Unwrapped) - [DarkData]", "", 6, 3],
            ["The Mentalist S02E21 18 5 4 720p WEB DL DD5 1 h 264 EbP", "The Mentalist", 2, 21],
            ["01x04 - Halloween, Part 1 - 720p WEB-DL", "", 1, 4],
            ["extras.s03.e05.ws.dvdrip.xvid-m00tv", "extras", 3, 5],
            ["castle.2009.416.hdtv-lol", "castle", 4, 16],
            ["hawaii.five-0.2010.217.hdtv-lol", "hawaii five-0", 2, 17],
            ["Looney Tunes - S1936E18 - I Love to Singa", "Looney Tunes", 1936, 18],
            ["American_Dad!_-_7x6_-_The_Scarlett_Getter_[SDTV]", "American Dad!", 7, 6],
            ["Falling_Skies_-_1x1_-_Live_and_Learn_[HDTV-720p]", "Falling Skies", 1, 1],
            ["Top Gear - 07x03 - 2005.11.70", "Top Gear", 7, 3],
            ["Glee.S04E09.Swan.Song.1080p.WEB-DL.DD5.1.H.264-ECI", "Glee", 4, 9],
            ["S08E20 50-50 Carla [DVD]", "", 8, 20],
            ["Cheers S08E20 50-50 Carla [DVD]", "Cheers", 8, 20],
            ["S02E10 6-50 to SLC [SDTV]", "", 2, 10],
            ["Franklin & Bash S02E10 6-50 to SLC [SDTV]", "Franklin & Bash", 2, 10],
            ["The_Big_Bang_Theory_-_6x12_-_The_Egg_Salad_Equivalency_[HDTV-720p]", "The Big Bang Theory", 6, 12],
            ["Top_Gear.19x06.720p_HDTV_x264-FoV", "Top Gear", 19, 6],
            ["Portlandia.S03E10.Alexandra.720p.WEB-DL.AAC2.0.H.264-CROM.mkv", "Portlandia", 3, 10],
            ["(Game of Thrones s03 e - \"Game of Thrones Season 3 Episode 10\"", "Game of Thrones", 3, 10],
            ["House.Hunters.International.S05E607.720p.hdtv.x264", "House Hunters International", 5, 607],
            ["Adventure.Time.With.Finn.And.Jake.S01E20.720p.BluRay.x264-DEiMOS", "Adventure Time With Finn And Jake", 1, 20],
            ["Hostages.S01E04.2-45.PM.[HDTV-720p].mkv", "Hostages", 1, 4],
            ["S01E04", "", 1, 4],
            ["1x04", "", 1, 4],
            ["10.Things.You.Dont.Know.About.S02E04.Prohibition.HDTV.XviD-AFG", "10 Things You Dont Know About", 2, 4],
            ["30 Rock - S01E01 - Pilot.avi", "30 Rock", 1, 1],
            ["666 Park Avenue - S01E01", "666 Park Avenue", 1, 1],
            ["Warehouse 13 - S01E01", "Warehouse 13", 1, 1],
            ["Don't Trust The B---- in Apartment 23.S01E01", "Don't Trust The B---- in Apartment 23", 1, 1],
            ["Warehouse.13.S01E01", "Warehouse 13", 1, 1],
            ["Dont.Trust.The.B----.in.Apartment.23.S01E01", "Dont Trust The B---- in Apartment 23", 1, 1],
            ["24 S01E01", "24", 1, 1],
            ["24.S01E01", "24", 1, 1],
            ["Homeland - 2x12 - The Choice [HDTV-1080p].mkv", "Homeland", 2, 12],
            ["Homeland - 2x4 - New Car Smell [HDTV-1080p].mkv", "Homeland", 2, 4],
            ["Top Gear - 06x11 - 2005.08.07", "Top Gear", 6, 11],
            ["The_Voice_US_s06e19_04.28.2014_hdtv.x264.Poke.mp4", "The Voice US", 6, 19],
            ["the.100.110.hdtv-lol", "the 100", 1, 10],
            ["2009x09 [SDTV].avi", "", 2009, 9],
            ["S2009E09 [SDTV].avi", "", 2009, 9],
            ["Shark Week S2009E09 [SDTV].avi", "Shark Week", 2009, 9],
            ["St_Elsewhere_209_Aids_And_Comfort", "St Elsewhere", 2, 9],
            ["[Impatience] Locodol - 0x01 [720p][34073169].mkv", "Locodol", 0, 1],
            ["South.Park.S15.E06.City.Sushi", "South Park", 15, 6],
            ["South Park - S15 E06 - City Sushi", "South Park", 15, 6],
            ["Constantine S1-E1-WEB-DL-1080p-NZBgeek", "Constantine", 1, 1],
            ["Constantine S1E1-WEB-DL-1080p-NZBgeek", "Constantine", 1, 1],
            ["NCIS.S010E16.720p.HDTV.X264-DIMENSION", "NCIS", 10, 16],
            ["[ www.Torrenting.com ] - Revolution.2012.S02E17.720p.HDTV.X264-DIMENSION", "Revolution", 2, 17],
            ["Revolution.2012.S02E18.720p.HDTV.X264-DIMENSION.mkv", "Revolution", 2, 18],
            ["Series - Season 1 - Episode 01 (Resolution).avi", "Series", 1, 1],
            ["5x09 - 100 [720p WEB-DL].mkv", "", 5, 9],
            ["1x03 - 274 [1080p BluRay].mkv", "", 1, 3],
            ["1x03 - The 112th Congress [1080p BluRay].mkv", "", 1, 3],
            ["Revolution.2012.S02E14.720p.HDTV.X264-DIMENSION [PublicHD].mkv", "Revolution", 2, 14],
            ["Castle.2009.S06E03.720p.HDTV.X264-DIMENSION [PublicHD].mkv", "Castle", 6, 3],
            ["19-2.2014.S02E01.720p.HDTV.x264-CROOKS", "19-2", 2, 1],
            ["Community - S01E09 - Debate 109", "Community", 1, 9],
            ["Entourage - S02E02 - My Maserati Does 185", "Entourage", 2, 2],
            ["6x13 - The Family Guy 100th Episode Special", "", 6, 13],
            ["The Young And The Restless - S41 E10478 - 2014-08-15", "The Young And The Restless", 41, 10478],
            ["The Young And The Restless - S42 E10591 - 2015-01-27", "The Young And The Restless", 42, 10591],
            ["Series Title [1x05] Episode Title", "Series Title", 1, 5],
            ["Series Title [S01E05] Episode Title", "Series Title", 1, 5],
            ["Series Title Season 01 Episode 05 720p", "Series Title", 1, 5],
            ["The Young And the Restless - S42 E10713 - 2015-07-20.mp4", "The Young And the Restless", 42, 10713],
            # TODO - handle absolute episode parsing (i.e 103)
            #["quantico.103.hdtv-lol[ettv].mp4", "quantico", 1, 3],
            ["Fargo - 01x02 - The Rooster Prince - [itz_theo]", "Fargo", 1, 2],
            ["Castle (2009) - [06x16] - Room 147.mp4", "Castle", 6, 16],
            ["grp-zoos01e11-1080p", "grp-zoo", 1, 11],
            ["grp-zoo-s01e11-1080p", "grp-zoo", 1, 11],
            ["Jeopardy!.S2016E14.2016-01-20.avi", "Jeopardy!", 2016, 14],
            ["Ken.Burns.The.Civil.War.5of9.The.Universe.Of.Battle.1990.DVDRip.x264-HANDJOB", "Ken Burns The Civil War", 1, 5],
            ["Judge Judy 2016 02 25 S20E142", "Judge Judy", 20, 142],
            ["Judge Judy 2016 02 25 S20E143", "Judge Judy", 20, 143],
            ["Red Dwarf - S02 - E06 - Parallel Universe", "Red Dwarf", 2, 6],
            ["O.J.Simpson.Made.in.America.Part.Two.720p.HDTV.x264-2HD", "O J Simpson Made in America", 1, 2],
            ["The.100000.Dollar.Pyramid.2016.S01E05.720p.HDTV.x264-W4F", "The 100000 Dollar Pyramid", 1, 5],
            ["Class S01E02 (22 October 2016) HDTV 720p [Webrip]", "Class", 1, 2],
            #["this.is.not.happening.2015.0308-yestv", "this is not happening 2015", 3, 8],
            ["Jeopardy - S2016E231", "Jeopardy", 2016, 231],
            ["Jeopardy - 2016x231", "Jeopardy", 2016, 231],
            ["Shortland.Street.S26E022.HDTV.x264-FiHTV", "Shortland Street", 26, 22],
            ["Super.Potatoes.S01.Ep06.1080p.BluRay.DTS.x264-MiR", "Super Potatoes", 1, 6],
            ["Room 104 - S01E07 The Missionaries [SDTV]", "Room 104", 1, 7],
            ["11-02 The Retraction Reaction (HD).m4v", "", 11, 2],
            ["Plus belle la vie - S14E3533 FRENCH WEBRIP H.264 AAC (09.05.2018)", "Plus belle la vie", 14, 3533],
            ["The 100 - S01E02 - Earth Skills HDTV-1080p AVC DTS [EN+FR+ES+PT+DA+FI+NB+SV]", "The 100", 1, 2],
            ["Series Title - S01E01 - Day 100 [SDTV]", "Series Title", 1, 1],
        ]

    def test_tv(self):
        for name, title, season, episode in self.tv_single_episode_tests:
            parser = TVParser(name)
            self.assertTrue(parser.is_match(title, season, episode), '{} ({})'.format(name, parser.match))
