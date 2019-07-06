
    
var svgWidth = 1000;
var svgHeight = 1000;

var margin = {
top: 20,
right: 40,
bottom: 60,
left: 80
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select("#scatter")
.append("svg")
.attr("width", svgWidth)
.attr("height", svgHeight);

var chartGroup = svg.append("g")
.attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("assets/data/data.csv")
.then(function(newsData) {
      
      // Step 1: Parse Data/Cast as numbers
      // ==============================
      newsData.forEach(function(data) {
                       data.age = +data.age;
                       data.smokes = +data.smokes;
                       });
      
      // Step 2: Create scale functions
      // ==============================
      var xLinearScale = d3.scaleLinear()
      .domain([30, d3.max(newsData, d => d.age)])
      .range([0, width]);
      
      var yLinearScale = d3.scaleLinear()
      .domain([8, d3.max(newsData, d => d.smokes)])
      .range([height, 0]);
      
      // Step 3: Create axis functions
      // ==============================
      var bottomAxis = d3.axisBottom(xLinearScale);
      var leftAxis = d3.axisLeft(yLinearScale);
      
      // Step 4: Append Axes to the chart
      // ==============================
      chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);
      
      chartGroup.append("g")
      .call(leftAxis);
      
      // Step 5: Create Circles
      // ==============================
      var circlesGroup = chartGroup.selectAll("circle")
      .data(newsData)
      .enter()
      .append("circle")
      .attr("cx", d => xLinearScale(d.age))
      .attr("cy", d => yLinearScale(d.smokes))
      .attr("r", "15")
      .attr("fill", "pink")
      .attr("opacity", ".5")
      .text(function(d){
            return d.abbr;
            })
      ;
      
      // Step 6: Initialize tool tip
      // ==============================
      var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
            return (`${d.abbr}<br>Age: ${d.age}<br>Smoking Rate: ${d.smokes}`);
            });
      
      // Step 7: Create tooltip in the chart
      // ==============================
      chartGroup.call(toolTip);
      
      // Step 8: Create event listeners to display and hide the tooltip
      // ==============================
      circlesGroup.on("click", function(data) {
                      toolTip.show(data, this);
                      })
      // onmouseout event
      .on("mouseout", function(data, index) {
          toolTip.hide(data);
          });
      
      // Create axes labels
      chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Healthcare");
      
      chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("Poverty");
      });


//You need to create a scatter plot between two of the data variables such as `Healthcare vs. Poverty` or `Smokers vs. Age`.

//Using the D3 techniques we taught you in class, create a scatter plot that represents each state with circle elements. You'll code this graphic in the `app.js` file of your homework directory—make sure you pull in the data from `data.csv` by using the `d3.csv` function. Your scatter plot should ultimately appear like the image at the top of this section.

//* Include state abbreviations in the circles.

//* Create and situate your axes and labels to the left and bottom of the chart.

//* Note: You'll need to use `python -m http.server` to run the visualization. This will host the page at `localhost:8000` in your web browser.
