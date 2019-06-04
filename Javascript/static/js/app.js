// from data.js
var tableData = data;
var tbody = d3.select("tbody");

// Populate table data
function DisplayTableRowsLooped(someData){
    var row = tbody.append("tr");
    var theKeys = Object.keys(someData);
    for (var i =0; i<theKeys.length; i=i+1){
        row.append("td").text(someData[theKeys[i]]);

    }
}
 tableData.forEach(DisplayTableRowsLooped);


// Search through date/time column to filter table 

// filter function 
function filterDate(DT) {
    return DT.datetime === trueInput
}; 
// // Select the submit button
var submit = d3.select("#filter-btn");

submit.on("click", function() {

//   // Prevent the page from refreshing
  d3.event.preventDefault();

//   // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

//   // Get the value property of the input element
  var inputValue = inputElement.property("value");

  trueInput = inputValue;


  console.log(inputValue);
  console.log(tableData);


  var filteredData = tableData.filter(person => person.datetime === trueInput);

console.log(filteredData);

tbody.text("")
filteredData.forEach(DisplayTableRowsLooped)
});


// create dropdown menu 