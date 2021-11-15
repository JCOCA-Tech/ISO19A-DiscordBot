#!/bin/python
import discord, os, requests, random, json
from discord.ext import commands # Make sure to install the discord module (python -m pip install discord)
from dotenv import load_dotenv # Make sure to install the dotenv module (python -m pip install python-dotenv)
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Setup state
load_dotenv()  # load environment variables from .env
prefix='.'
client = commands.Bot(command_prefix=prefix)

# Startup handler
@client.event
async def on_ready():
    print(f"[DEBUG][on_ready]: Successfull login as \"{client.user}\"")

# Discord embed function wrapper
def embed(title="<empty>", url="", description="", color=0xFF5733):
    return discord.Embed(title=title, url=url, description=description, color=color)
"""
# Fact Command handler
@client.command(name='fact')
async def _fact(ctx, arg1="onion", arg2=1, arg3="popularity"): # channel object, topic, months into past
    fact_date_to=datetime.now().date().strftime("%Y-%m-%d")
    print(f"[DEBUG][fact]: fact_date_to is '{fact_date_to}'")

    fact_date_from=(datetime.now().date() - relativedelta(months=int(arg2))).strftime("%Y-%m-%d")
    print(f"[DEBUG][fact]: fact_date_from is '{fact_date_from}'")

    fact_topic=arg1
    print(f"[DEBUG][fact]: fact_topic is '{fact_topic}'")

    fact_api_key = os.getenv("FACT_API_KEY", "[ERROR]: getenv('FACT_API_KEY') failed")
    print(f"[DEBUG][fact]: fact_api_key is '{fact_api_key}'")

    fact_sort=str(arg3)

    titles=["You wanted it. You'll get it!","Roger Roger.","Did you know that google exists?","End my suffering...","Here's what I found:","Yooo. It's lit!","Cactus Jack sent me...","Fascinating","Go on. Read it. I dare you!"]

    title = random.choice (titles)
    request = "https://newsapi.org/v2/everything?q="+fact_topic+"&from="+fact_date_from+"&to="+fact_date_to+"&sortBy="+fact_sort+"&apiKey="+fact_api_key
    print(f"[DEBUG][fact]: request is '{request}'")

    api_data = requests.get(request)

    print(api_data.json())

    await ctx.send(embed=embed(title,request,description=api_data.json(),color=0x2211EE))
"""

@client.command(name='fact')
async def _fact(ctx, arg1="onion", arg2=1, arg3="popularity"): # channel object, topic, months into past

    titles=[
        "You wanted it. You'll get it!",
        "Roger Roger.",
        "Did you know that google exists?",
        "End my suffering...",
        "Here's what I found:",
        "Yooo. It's lit!",
        "Cactus Jack sent me...",
        "Fascinating",
        "Go on. Read it. I dare you!"
    ]

    title = random.choice(titles)

    messages = [
        """I never went to space.
        Ok. I lied. 
        Were in space right now.""",
        "If she says no answer 'sudo marry me'",
        "I don't sleep a lot.",
        "Glaciers and ice sheets hold about 69 percent of the world's freshwater.",
        "Recent droughts in Europe were the worst in 2,100 years.",
        "There are fossilized plants in Greenland under 1.4 km of ice.",
        "Whale songs can be used to map out the ocean floor.",
        "New creatures have been found in deep-sea volcanoes.",
        "Mount Everest is bigger now than the last time it was measured.",
        "Climate change is causing flowers to change color.",
        "North Korea and Cuba are the only places you can't buy Coca-Cola.",
        "The entire world's population could fit inside Los Angeles.",
        "There are more twins now than ever before.",
        "More people visit France than any other country.",
        "The world's most densely populated island is the size of two soccer fields.",
        "The Paris Agreement on climate change was signed by the largest number of countries ever in one day.",
        "The world's quietest room is located at Microsoft's headquarters in Washington state.",
        "There's only one country in the world that doesn't use the metric system.",
        "Four babies are born every second.",
        "The Earth's ozone layer will make a full recovery in 50 years.",
        "There are around 4 quadrillion quadrillion bacteria on Earth.",
        "People who are currently alive represent about 7% of the total number of people who have ever lived.",
        "Africa and Asia are home to nearly 90 percent of the world's rural population.",
        "The most expensive coin in the world was sold for more than $7 million.",
        "South Sudan is the youngest country in the world.",
        "More than 52% of the world's population is under 30 years old.",
        "People 60 years and older make up 12.3% of the global population.",
        "There are more than 24 time zones around the world.",
        "Canada has 9% of the world's forests.",
        "The red-billed quelea is the most common bird on Earth.",
        "There's a website that tracks the world's population in real time.",
        "More people speak Mandarin Chinese than any other language.",
        "Around one in every 200 men are direct descendants of Genghis Khan.",
        "Copenhagen is the most bike-friendly city in the world.",
        "There are 41 countries that recognize sign language as an official language.",
        "The global adult literacy rate is around 86%.",
        "All the ants on Earth weigh about as much as all the humans.",
        "The oceans contain almost 200,000 different viruses.",
        "New Zealanders have more pets per household than any other country.",
        "Tokyo is the world's largest city with 37 million inhabitants.",
        "Interpol was founded in 1914 when legal professionals from 24 countries got together to discuss catching fugitives.",
        "Nearly two people die each second.",
        "The global temperature on an average has increased by 0.6 to 1 degree Celsius till the 20th century.",
        "The United States constitutes 5% of the world population and contributes to 22% of the world’s carbon emission.",
        "Around 15% of the carbon released in the environment is due to deforestation and change in the use of land.",
        "The golden Toad is the first species to go extinct due to climate change.",
        "In recent times, half of all amphibians are at risk of extinction due to climate change. Many argue that extinction is a natural phenomenon, claiming about five species per year. However, some experts suggest we’re in the midst of the sixth mass extinction caused mostly by human activity.",
        "Vehicles like cars and trucks contribute to 20% of carbon emissions in the United States.",
        "Air conditions and heating elements consume 50% of electricity in America.",
        "Hurricanes, droughts and coral deaths are a few of the natural disasters caused due to climate change.",
        "Maria. Irma. Harvey. Sandy. Katrina. Andrew-hurricanes are reaching new extremes for climate change. The frequency of more intense hurricanes ranked as categories 4 and 5 has increased over the last 30 years. Increasingly destructive hurricanes are putting a growing number of people and structures at risk, and it has become immensely more difficult to escape these storms unscathed.",
        "Climate change enhances the spread of pests that causes life-threatening diseases like dengue, malaria, Lyme disease etc.",
        "The hottest years have been experienced from 1990 till 1997. The warmest years have been since 2005.",
        "20 of the warmest years on record have occurred in the last 22 years, as stated by The World Meteorological Organization (WMO), compounding the research released in the 2018 IPCC report.",
        "The world’s five warmest years have all occurred since 2015, with nine of the 10 warmest years occurring since 2005, according to scientists from NOAA’s National Centers for Environmental Information (NCEI).",
        "NASA scientists, who conducted a separate but similar analysis, concurred with NOAA’s ranking. NASA also found that 2010-2019 was the hottest decade ever recorded.",
        "Scientists from the United Kingdom Met Office determined that 2019 was one of the top three hottest years on record, and the World Meteorological Organizationoffsite link also ranked 2019 second warmest for the globe.",
        "The number of climate change-related incidents has increased fourfold between 1980 and 2010.",
        "Land use change and deforestation contribute to 15% of carbon emission every year.",
        "The climate change scenario was much stable before the industrial revolution and had been rapidly changing since then. Today the reality is that climate change is going to get worse than yesterday.",
        "A separate budget of US$ 40 million has been allotted for climate change research since 1990.",
        "Due to the greenhouse effect, the average temperature of the earth is 15 degrees rather than -18 degrees without the greenhouse effect.",
        "Carbon dioxide constitutes only 3.6 % of total greenhouse gases, out of which 0.12% is attributed to human activities.",
        "Carbon dioxide is not the only contributing gas to climate change. Other gases like methane and nitrous oxide are far more dangerous than carbon dioxide alone.",
        "The UN Intergovernmental Panel on Climate Change (IPCC) is a leading body fighting against climate change. This body is a political organization, however, and not a scientific body.",
        "The Kyoto Protocol, an organization formed to analyze and fight against climate change, will cost more than 100 trillion dollars, thus making developing and underdeveloped communities to participate.",
        "According to the World Food Program (WPF.org), by 2015, the number of people affected by climate change disasters could reach 375 million per year.",
        "Over the last 50 years, the concentration of carbon dioxide in the atmosphere has increased by 30% due to the burning of fossil fuels and greenhouse gas emissions like carbon dioxide, nitrous oxide and other gases, trapping more heat in the lower atmosphere.",
        "The rising temperatures will cause more deaths due to a result of overheating or hyperthermia and rapid spread of deadly diseases. Also, the growing number of people in cities and an increasing population of elderly have increased heat-related deaths, according to a 2018 study in The Lancet.",
        "Classic examples of climate change can be seen by the damages caused due to heavy rains and disasters like Hurricane Katrina in 2005.",
        "Tropical cyclone rainfall rates will likely increase in the future due to anthropogenic warming and accompanying an increase in atmospheric moisture content. Modeling studies on average project suggest an increase in the order of 10-15% for rainfall rates averaged within about 100 km of the storm for a 2 degree Celsius global warming scenario.",
        "Above 600000 deaths occur worldwide every year due to climate change. 95% of these deaths take place in developing countries.",
        "Climate change can have serious health impacts such as heat stress, extreme cold, which can cause major deaths due to heart diseases.",
        "In 2003, around 70,000 deaths occurred in Europe alone due to diseases caused by rising temperatures.",
        "Pollen and aeroallergen high levels also lead to rising temperatures. This can cause asthma, which affects 300 million people worldwide.",
        "Climate change is rapidly causing coastal flooding and displacement of people. Floods further cause major damages by injuring and killing people. They can even cause deadly diseases by spreading infection and vector-borne diseases.",
        "Due to water shortages, the transportation of water will cause it to contaminate and make it even more deadly by spreading diseases.",
        "Malaria, diarrhoea and malnutrition are diseases are water-borne diseases that have caused more than three million deaths since 2005; one-third of these deaths are in Africa alone.",
        "Steps to reduce greenhouse gases can help save the negative health impacts. Promoting safe public transportation and active activities like walking or use public transport can help reduce carbon emissions. This can also help to cut down traffic, air pollution, and thereby reducing cardiovascular diseases.",
        "The IPCC SR15 report found that limiting warming to 1.5°C above pre-industrial implies reaching net zero3CO2 emissions globally around 2050 and concurrent deep reductions in emissions of non-CO2 forcers, particularly methane.",
        "Various countries have taken steps to reduce greenhouse gas emissions. This has led to positive health effects. Promoting green transportation and carpooling can help to reduce carbon emissions and improve public health.",
        "Depending upon the carbon emissions, a rise in temperature from 1.1 degrees up to 6.4 degrees is expected by the end of this century.",
        "The concentration of carbon dioxide (CO2)​​​​​​​ in our atmosphere, as of May 2020, is 416 part​s per million, the highest it has been in human history, according to NOAA‘s Mauna Loa Observatory, an atmospheric baseline station in Hawaii.",
        "Over the next 20 years, global warming is expected to increase by 0.2 degrees per decade."
    ]

    message = random.choice(messages)

    await ctx.send(embed=embed(title,"",message,color=0x2211EE))

# Message handler
#@client.event
#async def on_message(message):
#    if(message.author == client.user):
#        return
#    
#    if(message.content.startswith('.hello')):
#        await message.channel.send("Hello!")

client.run(os.getenv("TOKEN", "[ERROR]: getenv('TOKEN') failed"))