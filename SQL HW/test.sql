USE sakila;
#1a. Display the first and last names of all actors from the table actor.
SELECT first_name, last_name
FROM actor;

#1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
ALTER TABLE actor#this line is to prevent existing column error when re-running the script.
DROP COLUMN Actor_Name; #this line is to prevent existing column error when re-running the script.

ALTER TABLE actor 
ADD COLUMN Actor_Name VARCHAR(50);
    
UPDATE actor 
SET Actor_Name = CONCAT(first_name, '  ', last_name);

#2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
#What is one query would you use to obtain this information?
SELECT * from actor
WHERE first_name = 'Joe';
    
#2b. Find all actors whose last name contain the letters GEN:
select * from actor
where last_name LIKE '%GEN%';

#2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select * from actor
where last_name LIKE '%LI%'
ORDER BY last_name, first_name;

#2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT * FROM country
WHERE country IN ("Afghanistan", "Bangladesh", "China");

#3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, 
#so create a column in the table actor named description and use the data type BLOB 
#(Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).
ALTER TABLE actor
ADD COLUMN Description BLOB(50);

#3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
ALTER TABLE actor
DROP COLUMN Description;

#4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(last_name)
FROM actor
GROUP BY last_name;

#4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, COUNT(last_name)
FROM actor
GROUP BY last_name
HAVING COUNT(last_name) >= 2;

#4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor SET first_name = 'HARPO' WHERE first_name = 'GROUCHO';

#4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
UPDATE actor SET first_name = 'GROUCHO' WHERE first_name = 'HARPO';

#5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
SHOW CREATE TABLE address;

#6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT address.address, address.address2, staff.first_name, staff.last_name
FROM staff
JOIN address ON
address.address_id = staff.address_id;

#6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT
	staff.staff_id as 'Staff ID',
	staff.first_name as 'First Name',
	staff.last_name as 'Last Name',
    SUM(amount) as 'Total'
FROM payment
JOIN staff ON
staff.staff_id = payment.staff_id
WHERE payment.payment_date LIKE '2005-08%'
GROUP BY staff.staff_id;

#6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT 
	film.title as 'Title',
    COUNT(actor_id) as '# of Actors'
FROM film_actor
INNER JOIN film ON
film.film_id = film_actor.film_id
GROUP BY film.title;

#6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT 
	film.title as 'Title',
    COUNT(inventory_id) as '# of Copies'
FROM film
INNER JOIN inventory ON
film.film_id = inventory.film_id
GROUP BY film.title
HAVING film.title = 'Hunchback Impossible';

#6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT
	customer.customer_id as 'Customer ID',
	customer.first_name as 'First Name',
	customer.last_name as 'Last Name',
    SUM(amount) as 'Total Paid'
FROM customer
JOIN payment ON
customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY last_name;

#7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
#As an unintended consequence, films starting with the letters K and Q have also soared in popularity.
#Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT *
FROM film
WHERE film.title LIKE 'K%' OR 'Q%' IN
(
SELECT film.title
FROM film
WHERE film.language_id = 1
);
#7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name
FROM actor
WHERE actor_id IN
(
  SELECT actor_id
  FROM film_actor
  WHERE film_id IN
  (
   SELECT film_id
   FROM film
   WHERE title = 'Alone Trip'
  )
);

#7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
SELECT customer.first_name, customer.last_name, customer.email, country.country
FROM customer 
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id
WHERE country.country = 'Canada';

#7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.
SELECT title
FROM film
WHERE rating = 'G' OR 'PG';

#7e. Display the most frequently rented movies in descending order.
SELECT film.title as 'Film Title',
				COUNT(rental.inventory_id) as 'Times Rented'
FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY film.title
ORDER BY COUNT(rental.inventory_id) DESC;
#SELECT t1.col, t3.col 
#FROM table1 
#join table2 ON table1.primarykey = table2.foreignkey
#join table3 ON table2.primarykey = table3.foreignkey


#7f. Write a query to display how much business, in dollars, each store brought in.
SELECT store.store_id as 'Store ID',
				SUM(payment.amount) as 'Amount'
FROM payment 
JOIN rental ON payment.rental_id = rental.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN store on inventory.store_id = store.store_id
GROUP BY store.store_id;

#7g. Write a query to display for each store its store ID, city, and country.
SELECT store.store_id, city.city, country.country
FROM store 
JOIN address ON store.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id;

#7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT category.category_id as 'Category',
				SUM(payment.amount) as 'Gross Revenue'
FROM PAYMENT
JOIN rental ON payment.rental_id = rental.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film_category on inventory.film_id = film_category.film_id
JOIN category on film_category.category_id = category.category_id
GROUP BY category.category_id
ORDER BY SUM(payment.amount) DESC;

#8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
SELECT category.category_id as 'Category',
				SUM(payment.amount) as 'Gross Revenue'
FROM PAYMENT
JOIN rental ON payment.rental_id = rental.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film_category on inventory.film_id = film_category.film_id
JOIN category on film_category.category_id = category.category_id
GROUP BY category.category_id
ORDER BY SUM(payment.amount) DESC;

#8b. How would you display the view that you created in 8a?
#8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
