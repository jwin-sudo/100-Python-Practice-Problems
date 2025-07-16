'''
Exercise 85 - Data Cleaner

Question: Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 

Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or brake lines in it. The new file content should look like in the expected output.

Expected output: 

Afghanistan
Albania
Algeria
Andorra
Angola
Antigua and Barbuda
Argentina
Armenia
Aruba
Australia
Austria
Azerbaijan
Bahamas, The
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia
Bosnia and Herzegovina
Botswana
Brazil
Brunei
Bulgaria
Burkina Faso
Burma
Burundi
Cambodia
Cameroon
Canada
Cabo Verde
Central African Republic
Chad
Chile
China
Colombia
Comoros
Congo, Democratic Republic of the
Congo, Republic of the
Costa Rica
Cote d'Ivoire
Croatia
Cuba
Curacao
Cyprus
Czechia
Denmark
Djibouti
Dominica
Dominican Republic
East Timor (see Timor-Leste)
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Fiji
Finland
France
Gabon
Gambia, The
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guinea-Bissau
Guyana
Haiti
Holy See
Honduras
Hong Kong
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
Korea, North
Korea, South
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macau
Macedonia
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Mauritania
Mauritius
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Namibia
Nauru
Nepal
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
North Korea
Norway
Oman
Pakistan
Palau
Palestinian Territories
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Qatar
Romania
Russia
Rwanda
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Maarten
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Korea
South Sudan
Spain
Sri Lanka
Sudan
Suriname
Swaziland
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Tanzania
Thailand
Timor-Leste
Togo
Tonga
Trinidad and Tobago
Tunisia
Turkey
Turkmenistan
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom
Uruguay
Uzbekistan
Vanuatu
Venezuela
Vietnam
Yemen
Zambia
Zimbabwe

'''

import re
# Read the raw data from the file
with open("countries_raw.txt", "r") as file:
    raw_data = file.read() 
# Use regex to find all country names (assuming they are capitalized words)
countries = re.findall(r'\b[A-Z][a-zA-Z\s,\'-]+\b', raw_data)
# Remove duplicates and sort the list
countries = sorted(set(countries))
# Write the cleaned list to a new file
with open("countries-cleaned.txt", "w") as file:
    for country in countries:
        file.write(country + "\n")
# Print the number of countries cleaned
print(f"Number of countries cleaned: {len(countries)}")
# Print the first 10 countries as a sample output
print("Sample of cleaned countries:")
print("\n".join(countries[:10]))
# Note: Ensure that the 'countries-raw.txt' file is in the same directory as this script.   
# This code will read the raw country data, clean it, and save the cleaned list to a new file.
# The expected output is a cleaned list of country names without any additional text or line breaks.
# The code uses regular expressions to extract country names, removes duplicates, sorts them, and writes them to a new file.
# The output file will be named 'countries-cleaned.txt' and will contain the cleaned list of country names.
# The code also prints the number of countries cleaned and a sample of the first 10 countries.
# Ensure that the 'countries-raw.txt' file is in the same directory as this script.
# This code is designed to clean a list of country names from a raw text file.
# The expected output is a cleaned list of country names without any additional text or line breaks.
