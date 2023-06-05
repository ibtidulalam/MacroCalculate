MacroCalculate: Personal Nutrition Tracker
Description
MacroCalculate is a Python-based application that helps users track their daily nutrient intake. The application makes use of the Nutritionix API to fetch detailed nutritional information about different food items. The user can enter various meals they've had throughout the day, including breakfast, lunch, dinner, and snacks. The application records the nutritional content of these meals, allowing the user to monitor their intake of various nutrients such as calories, fat, protein, carbohydrates, vitamin C, and iron.

Usage
When running the application, users are first prompted to enter their daily nutritional goals for the above-mentioned nutrients. Next, users enter the foods they've consumed for each meal. The app will search for the food item using the Nutritionix API, and then ask the user to specify the exact product and portion size.

Upon entering all the meals for the day, the application calculates the total intake for each nutrient and displays a final tally. This tally not only includes the total nutrient consumption but also compares it to the user's nutritional goals, providing an overview of the achieved percentages. This way, users can easily keep track of their nutritional intake and adjust their diets as necessary.

Dependencies
The application requires Python 3.6 or above and the following Python packages:

requests: for making HTTP requests to the Nutritionix API.
tabulate: for creating a tabular final tally of the nutritional intake.
Future Improvements
We're constantly looking to improve MacroCalculate. Future updates may include features such as saving daily data for week-over-week or month-over-month comparisons, tracking additional nutrients, and incorporating a graphical user interface for a more interactive user experience.

Contributions
We welcome contributions to MacroCalculate! If you have ideas for improvements or have found a bug, please open an issue or submit a pull request.
