# FashionPlace
FashionPlace is an e-commerce website built with Django, where users can browse and purchase fashion products. It provides features such as product listings, search functionality, user registration, user authentication, and a secure payment option using Flutterwave. It also leverages Django Ajax for dynamic page reloading and utilizes Django sessions to enable users to add items to their cart without requiring them to log in.

# Features

* Product Listings: Display a list of products with their details, including name, price, and an option to add them to the cart.

* Category View: View products based on their category, allowing users to browse specific types of fashion products.

* Search: Search for products based on keywords, providing relevant search results.

* User Registration: Allow users to create an account to access additional features, such as the ability to make purchases and view order history.

* User Authentication: Provide secure login functionality for registered users, ensuring their account information is protected.

* Cart: Enable users to add products to their cart while browsing and proceed to checkout when ready to purchase.

* Payment Integration: Integrate Flutterwave payment gateway to securely process payments for user purchases.

# Installation
* Clone the repository:
   git clone https://github.com/dolapur/fashionplace_ecommerce.git

* Navigate to the project directory:
   
   cd fashionplace_ecommerce

* Create and activate a virtual environment:

   python3 -m venv env
   
   source env/bin/activate  (Linux/macOS)
   
   env\Scripts\activate  (Windows)

* Install the project dependencies:
  
   pip install -r requirements.txt

* Apply database migrations:

   python3 manage.py migrate

* Start the development server:

   python3 manage.py runserver

* Access the website at http://localhost:8000.

# Usage

* Browse the website to view available products, categorized by different fashion categories.

* Use the search functionality to find specific products based on keywords.

* Add products to the cart while browsing and proceed to checkout to complete the purchase.

* During the checkout process, you will be redirected to register or login to proceed shopping. Register an account to access additional features such as making purchases and viewing order history. 

* During payment, you will be redirected to the secure payment page powered by Flutterwave (e.g., credit/debit card, bank transfer, mobile wallet) to complete the payment.

* After successful payment, you will receive a confirmation message


# Contributing
  Contributions to FashionPlace are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

# License
  The FashionPlace_Ecommerce project is licensed under the MIT License.


# THANKS FOR VISITING



