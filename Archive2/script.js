

// Function to get the input from the search bar.
function searchListings() {
    var x = document.getElementById("search").value;   
    document.getElementById("searchItem").innerHTML = x;
}

// Function to create a new business.
function createBusiness() {
    var u = document.getElementById("inBusinessID").value;
    document.getElementById("businessID").innerHTML = u;
    var v = document.getElementById("inName").value;
    document.getElementById("name").innerHTML = v;
    var w = document.getElementById("inService").value;
    document.getElementById("service").innerHTML = w;
    var x = document.getElementById("inPrice").value;
    document.getElementById("price").innerHTML = x;
    var y = document.getElementById("inRating").value;
    document.getElementById("rating").innerHTML = y;
    var z = document.getElementById("inURL").value;
    document.getElementById("url").innerHTML = z;
}

// Function to create a new listing.
function createListing() {
    var u = document.getElementById("inCategory").value;
    document.getElementById("category").innerHTML = u;
    var v = document.getElementById("inSubCategory").value;
    document.getElementById("subCategory").innerHTML = v;
    var w = document.getElementById("inService").value;
    document.getElementById("service").innerHTML = w;
    var x = document.getElementById("inPrice").value;
    document.getElementById("price").innerHTML = x;
    var y = document.getElementById("inRating").value;
    document.getElementById("rating").innerHTML = y;
    var z = document.getElementById("inURL").value;
    document.getElementById("url").innerHTML = z;
}