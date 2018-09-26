// from data.js
var tableData = data;

var tbody = d3.select("tbody");

// YOUR CODE HERE!

// Select the submit button
var submit = d3.select("#filter-btn");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  var filteredData = tableData.filter(tableData => tableData.date === inputValue);

  console.log(filteredData);

  filteredData.forEach((filteredData) => {
    var row = tbody.append("tr");
    Object.entries(filteredData).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });
});


//table to html
//var tbody = d3.select("tbody");
 
//data.forEach((filteredData) => {
//    var row = tbody.append("tr");
//    Object.entries(filteredData).forEach(([key, value]) => {
//      var cell = tbody.append("td");
//      cell.text(value);
//    });
//  });

//reset form button
var reset = d3.select("#reset-btn");

reset.on("click", function(){
  tbody.selectAll('td').remove()
});