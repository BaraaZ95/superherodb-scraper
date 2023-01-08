# Define here the models for your scraped items
#
# See documentation in=
# https=//docs.scrapy.org/en/latest/topics/items.html
import scrapy

from scrapy.item import Field
from itemloaders.processors import TakeFirst


class CharacterItem(scrapy.Item):

    Character = Field(output_processor=TakeFirst())
    Name = Field(output_processor=TakeFirst())
    Full_name = Field(output_processor=TakeFirst())
    Universe = Field(output_processor=TakeFirst())
    Creator = Field(output_processor=TakeFirst())
    Alter_Egos = Field()
    Place_of_birth = Field(output_processor=TakeFirst())
    Alignment = Field(output_processor=TakeFirst())
    Member = Field()
    Formerly = Field()
    Leader = Field()
    Gender = Field(output_processor=TakeFirst())
    Species = Field(output_processor=TakeFirst())
    Height = Field(output_processor=TakeFirst())
    Weight = Field(output_processor=TakeFirst())
    Eye_color = Field(output_processor=TakeFirst())
    Hair_color = Field(output_processor=TakeFirst())
    Base = Field()
    Relatives = Field()
    Occupation = Field()
    Collections = Field()
    Super_powers = Field()
    Equipment = Field()
    IQ = Field(output_processor=TakeFirst())
    Strength_force = Field(output_processor=TakeFirst())
    Speed_velocity = Field(output_processor=TakeFirst())
    Tier = Field(output_processor=TakeFirst())
    Intelligence = Field(output_processor=TakeFirst())
    Speed = Field(output_processor=TakeFirst())
    Strength = Field(output_processor=TakeFirst())
    Speed = Field(output_processor=TakeFirst())
    Strength = Field(output_processor=TakeFirst())
    Durability = Field(output_processor=TakeFirst())
    Power = Field(output_processor=TakeFirst())
    Combat = Field(output_processor=TakeFirst())
    Class_value = Field(output_processor=TakeFirst())
    Level = Field(output_processor=TakeFirst())
    Omnipotent = Field(output_processor=TakeFirst())
    Omniscient = Field(output_processor=TakeFirst())
    Omnipresent = Field(output_processor=TakeFirst())
