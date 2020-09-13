<h2>Linear Regression</h2>

<h3>Intro</h3>
<ul>
  <li>Linear Regression - approximating linear function to scatter data in order to find out the general trend.</li>
  <li>In regressing we want to predict continueous values as opposed to classification where we want to predict a classification of a case.</li>
  <li>Calculating line of regression:
    <br>
    <br>
    1. Calculating m and c coeffeicients based on the actual x and y values:
    <br>
    <br>
    <img src="images/linear_reg.JPG">
    <br>
    <br>
    2. Linear function through the predicted points for given m, c and set of x's values:
    <br>
    <br>
    <img src="images/predictions.JPG">
    <br>
    <br>
    3. We treat the distance between actal value and predicted as an error:
    <br>
    <br>
    <img src="images/error.JPG">
    <br>
    <br>
  </li>
  <li> Finding the best fit regression line with <b>gradient search</b>
    <br>
    - the main puropse on this is to reduce the error = > the smallest error, the best fit line<br>
    - performing n iterations for different m <br>
    - using different value of m we calculate the equation of <b>y = mx + c</b>
    - after every iteration, a predicted value y is being calculated using different m value <br>
    - next step is comparing distances between actual value and predicted one <br>
    - when in a current iteration the distance between the predicted value and actual one is minimum - for this iteration we take m value for the best fit line <br>
  </li>
  
</ul>
