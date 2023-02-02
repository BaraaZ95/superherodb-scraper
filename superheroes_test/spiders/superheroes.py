from urllib.parse import urljoin
import scrapy
import json
from itemloaders import ItemLoader
import re
from ..items import CharacterItem
import pandas as pd


class SuperheroSpider(scrapy.Spider):
    name = 'superhero'
    handle_httpstatus_list = [301, 403, 404, 521]
    #allowed_domains = ["superherodb.com"]
    # generate URLs for all pages
    start_urls = [
        f"https://www.superherodb.com/characters/?page_nr={i}" for i in range(1, 151)]

    def parse(self, response):

        cards = response.css('ul[class = "list list-md"] > li')

        for card in cards:
            loader = ItemLoader(item=CharacterItem())

            Character = card.css('a::text').get(default="")
            
            Name = card.css(
                'a>span[class = "suffix level-1"]::text').get(default="")
            Universe = card.css(
                'a>span[class = "suffix level-2"]::text').get(default="")

            loader.add_value(
                'Character', Character)
            loader.add_value(
                'Name', Name)
            loader.add_value(
                'Universe', Universe)
            
            url = urljoin(response.url, card.css('a::attr(href)').get())       
        
            
    def parse_info(self, response):
        try:
            stats_json = [json.loads(x) for x in re.findall(
                r'{"stats":[^;]+', response.text)]  # Stats can only be accessed via JSON. shdb stats index [0], user stats, indexed [1]
        except json.JSONDecodeError:
            stats_json = None

        loader = ItemLoader(response.meta['item'], response=response)

        if stats_json != None: #If stats exist

            IQ = stats_json[0]["stats"]['int']

            Speed_velocity = stats_json[0]["stats"]['spe']

            Strength_force = stats_json[0]["stats"]['str']

            Tier = stats_json[0]["stats"]["tie"]

            Intelligence = stats_json[0]["bars"]["int"]

            Strength = stats_json[0]["bars"]["str"]

            Speed = stats_json[0]["bars"]["spe"]

            Durability = stats_json[0]["bars"]["dur"]

            Power = stats_json[0]["bars"]["pow"]

            Combat = stats_json[0]["bars"]["com"]

            Class_value = stats_json[0]["shdbclass"]['value']

            try:  

                Level = stats_json[0]["shdbclass"]['level']

            except KeyError:
                Level = 0

            Omnipotent = stats_json[0]["specials"]["omnipotent"]

            Omniscient = stats_json[0]["specials"]["omniscient"]

            Omnipresent = stats_json[0]["specials"]["omnipresent"]

            # If default stats don't exist, parse user-given stats instead

        if all([0== i for i in [Strength, Speed, Strength, Durability, Intelligence, Power, Combat, Tier]]): #If official entries don't exist, check for unofficial user entries

            IQ = stats_json[1]["stats"]['int']

            Strength_force = stats_json[1]["stats"]['str']

            Speed_velocity = stats_json[1]["stats"]['spe']

            Tier = stats_json[1]["stats"]["tie"]

            Intelligence = stats_json[1]["bars"]["int"]

            Strength = stats_json[1]["bars"]["str"]

            Speed = stats_json[1]["bars"]["spe"]

            Strength = stats_json[1]["bars"]["str"]

            Durability = stats_json[1]["bars"]["dur"]

            Power = stats_json[1]["bars"]["pow"]

            Combat = stats_json[1]["bars"]["com"]

            Class_value = stats_json[1]["shdbclass"]['value']

            try:

                Level = stats_json[1]["shdbclass"]['level']

            except KeyError:

                Level = 0

            Omnipotent = stats_json[1]["specials"]["omnipotent"]

            Omniscient = stats_json[1]["specials"]["omniscient"]

            Omnipresent = stats_json[1]["specials"]["omnipresent"]

        # If official or user-given stats are available, parse additional character info

        if any([0!= i for i in [Strength, Speed, Strength, Durability, Intelligence, Power, Combat, Tier]]):

            Full_name = response.xpath(
                '//td[contains(text(), "Full name")]/following-sibling::td/text()').get(default="None")

            loader.add_value('Full_name', Full_name)

            Creator = response.css(
                'a[class= "chip publisher"]::text').get(default="None")

            loader.add_value('Creator', Creator)

            Alter_Egos = response.css(
                'div[class="shdbcard3-holder"]> div[class="shdbcard3 cat-10 card-xs"]> a::attr(title)').getall() or "None"

            loader.add_value('Alter_Egos', Alter_Egos)

            Place_of_birth = response.xpath(
                '//td[contains(text(), "Place of birth")]/following-sibling::td/text()').get(default="None")

            loader.add_value('Place_of_birth', Place_of_birth)

            Alignment = response.xpath(
                '//td[contains(text(), "Alignment")]/following-sibling::td/text()').get(default="None")

            loader.add_value('Alignment', Alignment)

            Formerly = response.xpath(
                '//i[contains(text(), "Formerly")]/following-sibling::a/text()').getall() or ["None"]

            loader.add_value('Formerly', Formerly)

            Member_ = response.xpath(
                '//td[contains(text(), "Teams")]/following-sibling::td/a/text()').getall() or ["None"]

            Member = Member_ or response.xpath(
                '//i[contains(text(), "Member")]/following-sibling::a/text()').getall()  # Two formats for Team member

            Member = [i for i in Member if i in Formerly]

            loader.add_value('Member', Member)

            Leader = response.xpath(
                '//i[contains(text(), "Leader")]/following-sibling::a/text()').getall() or ["None"]

            Leader = [i for i in Leader if i not in list(
                Member + Formerly)]

            loader.add_value('Leader', Leader)

            Gender = response.xpath(
                '//td[contains(text(), "Gender")]/following-sibling::td/text()').get(default="None")

            loader.add_value('Gender', Gender)

            Species_ = response.xpath(
                '//td[contains(text(), "Species // Type")]/following-sibling::td/a/text()').get(default="None")

            Species = Species_ or response.xpath(
                '//td[contains(text(), "Species // Type")]/following-sibling::td/text()').get(default="None")

            loader.add_value("Species", Species)

            Height = response.xpath(
                '//td[contains(text(), "Height")]/following-sibling::td/text()').get(default="None")

            loader.add_value('Height', Height)

            Weight = response.xpath(
                '//td[contains(text(), "Weight")]/following-sibling::td/text()').get(default="None")

            loader.add_value('Weight', Weight)

            Eye_color = response.xpath(
                '//td[contains(text(), "Eye color")]/following-sibling::td/text()').get(default="None")

            loader.add_value('Eye_color', Eye_color)

            Hair_color = response.xpath(
                '//td[contains(text(), "Hair color")]/following-sibling::td/text()').get(default="None")

            loader.add_value('Hair_color', Hair_color)

            Base = response.xpath(
                '//td[contains(text(), "Base")]/following-sibling::td/text()').getall() or "None"

            loader.add_value('Base', Base)

            Relatives = response.xpath(
                '//td[contains(text(), "Relatives")]/following-sibling::td/text()').getall() or "None"

            loader.add_value('Relatives', Relatives)

            Occupation = response.xpath(
                '//td[contains(text(), "Occupation")]/following-sibling::td/text()').getall() or "None"

            loader.add_value('Occupation', Occupation)

            Collections = response.xpath(
                '//h3[contains(text(), "Collections")]/following-sibling::a/text()').getall() or "None"

            loader.add_value('IQ', IQ)

            loader.add_value('Strength_force', Strength_force)

            loader.add_value('Speed_velocity', Speed_velocity)

            loader.add_value('Tier', Tier)

            loader.add_value('Collections', Collections)

            loader.add_value('Intelligence', Intelligence)

            loader.add_value('Strength', Strength)

            loader.add_value('Speed', Speed)

            loader.add_value('Durability', Durability)

            loader.add_value('Power', Power)

            loader.add_value('Combat', Combat)

            loader.add_value('Class_value', Class_value)

            loader.add_value('Level', Level)

            loader.add_value('Omniscient', Omniscient)

            loader.add_value('Omnipotent', Omnipotent)

            loader.add_value('Omnipresent', Omnipresent)

            Super_powers = response.xpath(
                '//h3[contains(text(), "Super Powers")]/following-sibling::a/text()').getall() or "None"

            loader.add_value('Super_powers', Super_powers)

            equipment_url = response.url + "equipment/"
            
            history_url = urljoin(response.url, "history/")
            
            
            yield response.follow(history_url, callback = self.parse_history,  meta={"item": loader.load_item()})

            yield response.follow(equipment_url, callback=self.parse_equipment, meta={"item": loader.load_item()})

        # Do not parse additional info if there are no user stats
        else:
            return

    def parse_history(self, response):
        
        loader = ItemLoader(response.meta['item'], response=response)
        
        history_text =  response.css('div[class="column col-12 text-columns-2"]::text').getall()
        
        if history_text:
            
            history = ' '.join(history_text)
            
            loader.add_value('History', history.strip())
            
    
    def parse_equipment(self, response):

        loader = ItemLoader(response.meta['item'], response=response)

        Equipment = response.css(
            'div[class="column col-4 col-md-12"] > p> a::text').getall()

        loader.add_value('Equipment', Equipment)

        yield loader.load_item()
