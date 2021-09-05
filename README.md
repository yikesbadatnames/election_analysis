# election_analysis

<br>

## Overview of Election Analysis

<br>

<p>The purpose of this analysis was to provide an aduit of each candidate's votes, percentages, and most importantly: who won this congressional election election.

Secondary goals included auditing the registered voters in each county, as well as the breakdown of registered voters in each county by percentages. </p>

<br>

## Election-Audit Results

<br>


* <p> There were a total of 369,711 votes. This is identified as easily as counting the number of rows in the CSV </p>
* <p> Denver county had 306,055 votes, making up 82.8% of the votes
* <p> Jefferson county had 38,855 votes, making up 10.5% of the votes. </p>
* <p> Arapahoe county had 24,801 votes, making up 6.7% of the votes.
* <p> Denver county had the largest amount of votes. 

<br>

> <p> Evidence for these findings in the code can be found below: </p>


<br>

![county_code](/images/county_breakdown_code.png)

<br>

* <p> Raymon Anthony Doane came in 3rd with 85,213, making up 3.1% of the votes.</p>
* <p> Charles Casper Stockham came in 2nd with 85,213 votes, making up 23.0% of the votes.</p>
* <p> And the winner... by a extremely the extremely wide margin with 272,892, making up 73.8% of the votes... is ... DIANA DEGETTE!!! </p>

> <p> Evidence for these findings in the code can be found below </p>


<br>

![candidate_code](/images/candidate_breakdown_code.png)

<br>

## Election-Audit Summary:

<br>

<p> This election audit script  can be used for any election with these modifications. First, in the for loop that reads the rows in the CSV the variables for candidate name and county name can be associated to new row indexes that would correspond to where this new CSV contains that data. Secondly, more logic can be added to the block of code that dictates the winner so that if two candidates get the same amount of votes, it will print and write that there was a tie. Additional logic could be written so that if two candidates are within a certain percentage point of votes, the votes can be recounted and submitted again in a different CSV. </p>