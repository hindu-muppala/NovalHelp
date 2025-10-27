# NovalHelp: Navy Module

## Overview

The **Navy** folder is a core part of the NovalHelp project, focused on maritime dataset handling, surveillance logs, and analytics tools for naval domain applications. It offers components for data extraction, conversion, and analytics relevant to maritime surveillance and operational tasks.

## Folder Structure

- **Navy/**  
  Main directory, containing modules and scripts for maritime analytics and file processing.

  - **novelHack_Data/novelHack/**  
    Data files and scripts related to the novelHack project components for advanced analytics and prototyping.

  - **pdf_files/**  
    Collection of maritime-related PDF documents, such as "indian-navy-air-defense-exercise-areas_01-25.md.pdf", containing real-world surveillance data and military zone information.

  - **pdf_to_md/**  
    Scripts and outputs for converting PDF files to Markdown, simplifying downstream data analysis and processing tasks.

  - **set.py**  
    Python script for custom data operations or utility functions relating to the contents of this folder.

  - **NavyAnalytics/**  
    Contains source code for Django-based analytics tools, including:
    - NavyAnalytics (project settings)
    - mapApi (Django app)
    - db.sqlite3 (database)
    - manage.py (management script)

## Key Data Files

- **maritime-dataset-v1.md / maritime-dataset-surveillance-logs_01-15.md**  
  Markdown files with samples of patrol reports, reconnaissance notes, and communication logs from naval activities. Useful for data modeling, analysis, and research in maritime security.[10]

## Usage

- Navigate the folder to find surveillance logs, zone definitions, and scripts for converting and analyzing maritime datasets.
- Leverage the Django project `NavyAnalytics` for geospatial analytics, mapping, and reporting.
- Use the file conversion tools to translate PDF documents into workable Markdown for further analysis.

## Notes

For details on the dataset and surveillance zone definitions, refer to the Markdown files in the root (`maritime-dataset-v1.md`, etc.) for information on patrol logs and geographical zones.

***

