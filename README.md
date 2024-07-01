# Air Accidents
Eduardo da Silva


## Getting Started

1. Clone this repo  [link](https://github.com/drivedudu/Week_3_project.git).
2. Raw Data is being kept [here](https://www.kaggle.com/datasets/yassereleraky/aviation-accident-ntsb?select=AviationData.csv) within this repo.
3. The main script is [here]( )
4. Data processing/transformation/cleaning scripts are [here]( )


# Analysis of Air Accidents by Decades.

This project is a part of the bootcamp at [Ironhack](https://ironhack.com/).  

#### -- Project Status: [Completed]

## Project Intro
The project "Analysis of Air Accidents by Decades" aims to analyze historical air crash data from different time periods to see what trends and reasons for accidents emerge. 


### Methods Used
* Data Visualization
* Data exploration/descriptive statistics
* Data processing/cleaning


### Technologies
* Python
* Folium
* Geopandas, point
* Pandas, jupyter
* Matplotlib

## Project Description
The project analyzes aviation accident data from 1948 to 2022, categorized by decades. Data is sourced from the National Transportation Safety Board (NTSB), which investigates transportation accidents, including aviation incidents.

-- **Data Sources:** Data includes information on accident frequency, geographical locations of accidents, and weather conditions categorized by country.

**Table columns**
- **Event.Id:** Unique identifier assigned to each aviation accident event in the database.
- **Investigation.Type:** Type of investigation conducted for the accident, categorized as "Incident," "Accident," etc.
- **Accident.Number:** Unique identifier assigned to each aviation accident.
- **Event.Date:** Date when the accident occurred.
- **Location:** Geographical location where the accident took place, including city, state, and country.
- **Country:** Country where the accident occurred.
- **Latitude:** Geographical latitude coordinate of the accident location.
- **Longitude:** Geographical longitude coordinate of the accident location.
- **Airport.Code:** Code assigned to the airport nearest to the accident site.
- **Airport.Name:** Name of the airport nearest to the accident site.
- **Injury.Severity:** Severity of injuries sustained by individuals involved in the accident, ranging from minor to fatal.
- **Aircraft.damage:** Extent of damage sustained by the aircraft involved in the accident, categorized as minor, substantial, destroyed, etc.
- **Aircraft.Category:** Category of aircraft involved in the accident, such as airplane, helicopter, glider, etc.
- **Registration.Number:** Unique registration number assigned to the aircraft.
- **Make:** Make or manufacturer of the aircraft.
- **Model:** Model of the aircraft.
- **Amateur.Built:** Indicates whether the aircraft involved was built by amateur constructors.
- **Number.of.Engines:** Number of engines installed on the aircraft.
- **Engine.Type:** Type of engine(s) installed on the aircraft, such as reciprocating, turbojet, turboprop, etc.
- **FAR.Description:** Description of the Federal Aviation Regulation (FAR) under which the aircraft operates.
- **Schedule:** Indicates whether the flight was scheduled or unscheduled.
- **Purpose.of.flight:** Purpose of the flight at the time of the accident, such as personal, commercial, instructional, etc.
- **Air.carrier:** Air carrier associated with the flight, if applicable.
- **Total.Fatal.Injuries:** Total number of fatal injuries resulting from the accident.
- **Total.Serious.Injuries:** Total number of serious injuries resulting from the accident.
- **Total.Minor.Injuries:** Total number of minor injuries resulting from the accident.
- **Total.Uninjured:** Total number of individuals who were uninjured in the accident.
- **Weather.Condition:** Prevailing weather conditions at the time of the accident.
- **Broad.phase.of.flight:** Phase of flight during which the accident occurred, such as takeoff, climb, cruise, descent, etc.
- **Report.Status:** Status of the accident investigation report.
- **Publication.Date:** Date when the accident investigation report was published


### Questions and Hypotheses:

1.  **Temporal Trend Hypothesis:** Investigating if aviation safety has improved over time, evidenced by a decrease in accident frequency.

2. **Location Hypothesis:** Examining if certain geographic regions have a higher incidence of accidents due to factors like population density, geographical conditions, or specific climatic characteristics.
3. **Weather Factors Hypothesis:** Analyzing if adverse weather conditions correlate with increased aviation accidents, such as fog, storms, or strong winds.

- **Data Analysis and Visualization:**
Utilizing tables and graphs to analyze trends over time and geographical patterns. Statistical methods will be employed to test hypotheses, including regression analysis for temporal trends and correlation analysis for weather factors.

-- **Blockers and Challenges:**

* Ensuring data quality and consistency across decades and regions.
* Dealing with missing or incomplete data, especially in earlier years.
* Handling complex interactions between multiple variables, such as weather and geographic factors.

This project aims to assess the effectiveness of safety protocols implemented over the years and identify areas for improvement to further enhance aviation safety.

### Conclusions 

1.  **Temporal Trend Hypothesis:**

    * **Result of Hypothesis:** A decreasing trend in the number of accidents over time, with a peak in 1988-1998 followed by a subsequent decline. This suggests that aviation safety may have indeed improved over the decades.

    *  **Turning Point:** From 1988-1998, there was a significant increase in the number of accidents, followed by a decrease in the following years. This may indicate a turning point in aviation safety, where issues were identified, or measures were implemented that eventually led to a reduction in accidents.

    * **Continuous Evolution:** Although there is an overall decreasing trend, the number of accidents is still significant in the most recent years (2018-2022). This suggests that despite improvements over time, there is still room for continuous evolution in aviation safety.

    * **Need for Monitoring:** The analysis highlights the ongoing importance of monitoring and analyzing aviation safety data over time. This can help identify emerging trends, areas of concern, and opportunities for intervention and continuous improvement.


    * **List of the Safety protocols**
        1. Chicago Convention (1944): Established ICAO and international aviation regulations. It has been revised in 1959, 1963, 1969, 1975, 1980, 1997, 2000, and 2006.
        2. ICAO Safety Audit Program (USOAP): Conducts safety audits on member states.
        3. ICAO Standards and Recommended Practices (SARPs): Provides guidance for international aviation safety.
        4. Flight Safety Assessment Program (IASA): Assesses aviation safety standards in other countries.

    * **Future Analysis:**
        * Conduct in-depth investigations into specific factors contributing to the peak in accidents during 1988-1998 and the reasons behind the increase. This could involve examining specific events, changes in aviation regulations, technological advancements, or external factors.
        * Implement targeted interventions based on identified trends to further improve aviation safety.

    * **Recommendation**
        - Continue monitoring and analyzing aviation safety data to stay abreast of emerging trends and address potential safety concerns proactively.

2. **Location Hypothesis:**

    * **Result of Hypothesis:** The United States has by far the highest incidence of aviation accidents compared to other countries listed. This could support the idea that certain geographic regions, such as highly populated areas or regions with specific climatic conditions, are more prone to aviation accidents.
    
    * **Identification of High-Risk Regions:** Countries like Brazil, Canada, Mexico, and the United Kingdom also have relatively high numbers of aviation accidents compared to others on the list. This suggests that these regions may indeed have factors contributing to a higher incidence of accidents, as proposed by the hypothesis.


    * **Further Analysis**

         It would be beneficial to conduct further analysis to identify specific factors contributing to the high incidence of accidents in these regions. This could involve examining population density, geographical features, weather patterns, air traffic volume, infrastructure, and regulatory factors.
    

    * **Summary**

        * **Air Traffic Density:** The United States has one of the busiest and most complex airspaces in the world, with a dense network of airports, airways, and airspace sectors. High levels of air traffic can increase the risk of mid-air collisions, runway incursions, and other aviation incidents, especially in congested airspace around major cities and airports.

        * **Urbanization and Population Centers:** The US is home to several major metropolitan areas, including New York, Los Angeles, Chicago, and Atlanta, which have large populations and extensive aviation infrastructure. Urbanization and population density can contribute to increased air traffic volume, airspace congestion, and the proximity of airports to residential areas, all of which may impact aviation safety.

3. **Weather Factors Hypothesis:**

    * **Result of Hypothesis:** The fact that accident numbers differ in various weather conditions across countries implies that factors such as weather patterns, air infrastructure, and proficiency in managing adverse weather conditions contribute to these disparities.

    * **Number of Accidents by Country:**        The United States leads in the absolute number of accidents, suggesting influences beyond weather.
    Brazil, Canada, and Mexico also record a considerable number of accidents, albeit on a smaller scale compared to the United States.

    * **Distribution of Accidents according to Weather Conditions:**
        Countries like Argentina, Brazil, Mexico, and Venezuela have more accidents in adverse weather conditions.
        In contrast, India and Japan report fewer accidents, especially in good visibility conditions.

    * **Variation in Accident Distribution across Various Weather Conditions:**
    India and Spain exhibit a more balanced distribution of accidents across different weather conditions, suggesting more effective risk management in adverse conditions.


    * **Regional Variances:** The number of accidents in different visibility conditions varies from country to country. This may be due to differences in weather patterns, air transportation infrastructure, and the ability to deal with challenging weather conditions in each location.
    

    * Recommendations and Further analysis:

    * **Correlation between Weather and Accidents:**    Poor weather conditions may lead to more air accidents and technologies to handle these hazardous situations.

    * **Additional Safety Measures:**
    Countries with high accident rates in adverse weather should consider enhancing safety protocols. This includes improving navigation systems and pilot training.

    * **International Collaboration:**
    Global cooperation is vital in aviation safety. Sharing best practices and data can enhance safety standards worldwide.

## Featured Notebooks/Analysis/Deliverables

* [Kaggle database Aviation accidents](https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses/data?select=AviationData.csv)
* [Kaggle database Maps for Geopandas](https://www.kaggle.com/datasets/yassereleraky/aviation-accident-ntsb?select=geo+pandas+expect+.csv)
* [Presentation](link)





