# README.md

<a name="introduction"/>

## Introduction

This project was part of a submission to the [Convex 2024 Hackathon](https://convexhackathon.devpost.com/). Though, it's more of a module, since all it does is process the USDA FDC JSON data into a format (JSONL) that is compatible for loading into the Convex Database and only containing the data we needed (such as nutrition data and name). The rest of the submission code can be found on the [GitHub repo](https://github.com/mashiourcse/convex_nutriiton) for the Front End code.

<a name="table-of-contents"/>

## Table of Contents

[Introduction](#introduction)  
[Table of Contents](#table-of-contents)  
[Project Description](#project-description)  
[Usage](#usage)  
[Credits](#credits)  
[Other](#other)

<a name="project-description"/>

## Project Description

Our project required nutrition data from a large dataset of foods, so we decided to use data from the USDA FDC. We chose to work with their JSON data format since it was easier to read through and understand. After exploring the data, we decided we wanted to retain the following information (description, food category, brand owner, serving size, serving size unit, calories, protein, fat, carbohydrates, fiber, iron, sodium, cholesterol, sugars) and discard the rest, allowing us to reduce the size of the data fom 3 GB to 170 MB. After extracting and transforming the data, we needed to convert it to JSONL, which was necessary per the Convex database specifications.

This project includes an `explore.py` script to show how the data was explored and an `extract.py` script that extracts the necessary data into a JSONL file. Further instruction to load the data into the Convex database can be found in their [documentation](https://docs.convex.dev/database/import-export/import#single-table-import).

<a name="usage"/>

## Usage

Requirements:

- `Python 3.X`
- USDA FDC JSON data

Instructions:

- Fork this repo
- Load the USDA FDC JSON data into the project
- Name the data file `branded_download.json`
- Run `python3 explore.py` to see how we explored the data
- Run `python3 extract.py` to produce a `branded_data.jsonl` file

<a name="credits"/>

## Credits

Author: Joseph Armstrong  
[GitHub](https://github.com/JosephArmstrong314)  
[LinkedIn](https://www.linkedin.com/in/joseph-armstrong-31415926535897932384626/)  
[DevPost](https://devpost.com/joeagorn)

<a name="other"/>

## Other

| Important Links                                                                                              |
| ------------------------------------------------------------------------------------------------------------ |
| [ETL GitHub Repo](https://github.com/JosephArmstrong314/usda-fdc-etl)                                        |
| [Front End GitHub Repo](https://github.com/mashiourcse/convex_nutriiton)                                     |
| [USDA FDC Data](https://fdc.nal.usda.gov/)                                                                   |
| [DevPost Submission](https://devpost.com/software/nutrition-tool-using-usda-dataset)                         |
| [Convex Website](https://www.convex.dev/)                                                                    |
| [Convex 2024 Hackathon](https://convexhackathon.devpost.com/)                                                |
| [Convex CLI Import Documentation](https://docs.convex.dev/database/import-export/import#single-table-import) |
