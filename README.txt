This is the reportaprice.com project. 

Front End Engineer: Hillary
Back End Engineer: Stan Morrison
Full Stack Developer: Tom Morrison
Tester: Ann Morrison

Status: 
	The index.html, and price reporting pages are working. We are using python as the backend language to run query scripts on mySQL. The most important aspects to focus on include; the database architecture of the database containing price listings for every service, (ever) and a method design to input information into the database. To do's include; finishing the code to add users input to the database, checking user input to assure proper values are entered, searching the database, and displaying results. Order of priotrity:

		1. Adding inputs to database (listForm.py)
		2. Searching Database -Dad (Look into using external plugins google)
		3. Displaying search results
		4. Securities (making sure inputs are allowed(No mySQL query hacks), python db config file?)
		5. Front End Assembly -Hillary
		6. Determine name
		7. Launch

In order to view the site you will need to set up a local web server such as "apache". Apache comes pre set up on Macs for web development(Dad). You will just have to make sure the permissions and config files are properly set up. Additionally, you will need to download, install, properly set-up mySQL database locally (eventually this will be on the web).

Below is a collection of notes from the project 

This is a different input style vs button, not sure which is better 
<input type="submit" value="go" id="submit" onclick="searchListing()">

/ This is a pop up promp in jquery
//prompt("What is your name?");

// This is a java function to animate things on the screen for future use
var main = function() {
	// Select a class with jquery (login menu)
	$('.icon-menu').click(function() {
        $('.menu').animate({
            left: '0px'
        }, 200);
	    $('body').animate({
    	    left: '285px'
        }, 200);

	});
};

// Form wrapper set up 
// This is the only css style we are using.
<form class="form-wrapper">
</form>

// gitHub repository for craigslist open source code.
https://github.com/craigslist/python-clblob

// Local mySQL notes
mysql -u root -p
1234chapo
> SHOW DATABASES;
> USE database;
