# Election_Analysis

## Project Overview
  The Board of Election of Colorado employee has given me the task of doing the elction audit of a recent local congressional election.
  The purpose of this election analysis audit is defined as follows:
  * Calculate the total number of vote cast in the election.
  * Get a complete list of candidate who recieved votes.
  * Calculate the total numberof votes each candidate recieved.
  * Calculate the percentage of votes each candidate won.
  * Determine the winner of the election based on popular vote.
  * The voter turnout for each county.
  * The percentage of votes from each county out of the total count.
  * The county with the highest turnout.
 ### Resources
     * Data sources: election_results.csv
     * software: Python 3.7.6, Visual studio code 1.70.2
     
 #### Election Audit Results
     * Total votes of 369,711 were casted in this congressional election.
     * 10.5% of the total votes was casted from Jefferson County(38,855), 6.7% of the total votes was casted from Arapahoe County(24,801),while the rest of the 
       votes(82.8%) came from Denver 306,055 votes
     * Denver county had largest number of votes
     * Charles Casper Stockham got 23.0% of the total votes(85,213 votes),Diana DeGette got 73.8% of the total votes (272,892 votes)and Raymon Anthony Doane got 
       3.1% of the total votes (11,606 votes)
     * Diana DeGette won the congressional election by getting 73.8% of the total votes cast (272,892 votes).

##### Election Audit Summary
     *This analysis tool could be used for any election with minimal modifications :
     *i. Changing the row index depending on the value you are intrested in analysing for example county vote count row[1] and for cndidate vote count use row[2]
     *ii.Ensuring that election_results.csv is always populate with county in row [1] and candidate in row [2]
  
