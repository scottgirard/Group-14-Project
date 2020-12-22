# ITSC-3155 Python Application: Foreign Currency Exchange

## Foreign Currency Exchange

Foreign Currency Exchange is a Python application built for the purpose of using a .csv dataset and the Plotly and Dash libraries as a basis for building a data visualization application.

## Introduction

Foreign currency exchange rates change frequently, making it difficult for traders to know when it is a good time to invest and when it is a good time to sell a currency. These rates are in constant fluctuation and it can be difficult for the investor to track various exchange rates due to the many different currencies available. In addition, travelers often have a need to convert from one currency to another, and ocasionally they need to convert several currencies at once. The Foreign Currency Exchange application is intended to support both kinds of users: foreign currency investors, and travelers. Our hope is that the foreign currency investor will find the application will support them in making informed investment decisions, and it will help the traveler to make fast, easy currency conversions.

## Description

Foreign Currency Exchange is written in Python with several components using the Plotly and Dash libraries. The application reads a .csv file into a dataframe then responds to user input via callbacks. Various data points are selected from the dataframe to generate time-series charts and the most current data in the .csv file is used for the currency conversions.

This app is a multi-page Dash app, so it also serves as an example of how to properly structure a Dash application to use multiple pages.

Our current dataset covers a time period between the year 2000 and 2019, but the application could be adapted to use a different dataset or even a combination of historical data and real-time data feeds.

The application is intended to be easy to use by both foreign currency investors as well as those who travel across borders and need to make currency conversions on the fly.

## Use Case Diagram

[Use Case Diagram](images/use-case-diagram.png)

## Installation

- Download the [MVP.zip](MVP.zip) file from this project directory.
- Unzip the file. This is the project structure:
```
MVP
├── app.py
├── assets
│   ├── custom.css
│   └── styles.css
├── callbacks.py
├── datasets
│   └── ForeignExchange.csv
├── index.py
└── layouts.py
```
- From within a Python IDE, run the index.py file to launch the application. This application was built and tested using PyCharm.
- The application runs a minimal http server on localhost; the application is accessed through a web browser.

## Live Demo Application

A live demo version of the application can be accessed running on [Heroku](https://currency-converter-group14.herokuapp.com/currency_converter).

[Click here to launch the live demo](https://currency-converter-group14.herokuapp.com/currency_converter)

Allow at least 30 seconds for the application to load and expect delays when making changes to the currency time-series graphs. We believe the delays are due to Heroku spinning up the server instance and network latency.

Additionally, again due to network latency, the currency converter functionality does not work properly in this demo. We suspect the callbacks take too long to return a response to the browser and browser gives up waiting for a response. When the app is run from localhost, the application works correctly.

The demo is, however, useful for exploring a version of the application prior to installing it locally. 

## Usage

### To Convert one currency to another:

* From the Convert tab, select a currency using the "Convert From" dropdown menu.
  * For example, If you want to convert 10 US dollars to a equivalent sum of Euros, you would select "U.S Dollar" from the dropdown menu.

* Select a currency from the "Convert To" dropdown menu and choose the currency you wish to convert to.
  * For the above example, you would select "European Union Euros"
* In the input field under "Amount", Type the amount of the currency you wish to convert.
  * In the Above example, you would type 10 into the input field.
* The application will display the result below the user selections.
* Additionally, the conversions for all currencies are shown in the large output box. These currencies are updated as each digit is entered into the "Amount" input field.

### To View the Exchange Rate changes for the Year via a visual representation:

* Click or tap the "Overview" tab at the top of the screen.
* Under the words "Foreign Exchange Rates for the Year", you should see a visual representation of the currency rates as imported from the Data.
* The chart is interactive. Use the icons on the top-right corner of the graph to modify the views. Tooltips should appear when you mouse over the top right corner of the graph.
* Note the ability to select timeframes by clicking and dragging over a section of the graph. The graph can be reset by clicking the "Reset axes" icon on the top right of the graph.
* Timeframes for the current year, decade, and all time can also be quickly accessed by using the dropdown menu below the graph.

### To view a more focused chart based on a single currency of your choosing:

* Click or tap the "Focus" tab at the top of the screen.
* Under the text "Please select a currency", in the interface, select a currency you wish to view.
* The graph above the dropdown selector will display the selected currency timeseries.
* Be sure to explore the tooltips at the top right corner of the graph.

### To view a chart focused on comparison between two currencies of your choosing:

* Click or tap the "Compare" tab at the top of the screen.
* Under the text "Please select a first country to compare", in the interface, select your first Currency
* Under the text "Please select a second country to compare", in the interface, select your second Currency
* Under the text "Please enter a year between 2000 and 2019 to filter timeframe of the graph", select a year between 2000 and 2019. This year should indicate the center of the time period you wish to represent.
* You should see your graph updated to reflect the data you entered.
* Be sure to explore the tooltips at the top right corner of the graph.

## License

MIT License

Copyright (c) 2020 Team 14

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors and Acknowledgement

This Project was created by:

Scott Girard

Benjamin Gambill

Chris Hernandez

Nilay Kabra

