## Instructions
use sakila; 
-- 1a. Display the first and last names of all actors from the table `actor`. -- 
SELECT first_name, last_name FROM actor;
-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column `Actor Name`. --
ALTER TABLE actor ADD COLUMN ActorName VARCHAR(120);
UPDATE actor SET ActorName = CONCAT( first_name, " ", last_name);

--  2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." 
-- What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = 'Joe'; 

--  2b. Find all actors whose last name contain the letters `GEN`:
SELECT * FROM actor WHERE last_name LIKE '%GEN%';

--  2c. Find all actors whose last names contain the letters `LI`. 
-- This time, order the rows by last name and first name, in that order:
SELECT * FROM actor WHERE last_name LIKE '%LI%' ORDER BY last_name, first_name;

--  2d. Using `IN`, display the `country_id` and `country` columns of the following countries:
-- Afghanistan, Bangladesh, and China:
SELECT country_id, country from country WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, 
-- so create a column in the table `actor` named `description` and use the data type `BLOB` 
ALTER TABLE actor ADD COLUMN description BLOB;

--  3b. Very quickly you realize that entering descriptions for each actor is too much effort. 
-- Delete the `description` column.
ALTER TABLE actor DROP COLUMN description;

--  4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(last_name) FROM actor group by last_name;

--  4b. List last names of actors and the number of actors who have that last name, 
-- but only for names that are shared by at least two actors -- 
SELECT last_name, COUNT(last_name) FROM actor group by last_name  having COUNT(last_name) >= 2 ;


--  4c. The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`.
-- Write a query to fix the record.
UpdATE actor SET first_name = 'HARPO' WHERE first_name = 'GROUCHO' and last_name = 'WILLIAMS';

--  4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. 
-- It turns out that `GROUCHO` was the correct name after all! In a single query, 
-- if the first name of the actor is currently `HARPO`, change it to `GROUCHO`.
UpdATE actor SET first_name = 'GROUCHO' WHERE first_name = 'HARPO';

SELECT * FROM actor;

-- 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
SHOW CREATE TABLE address;
select * from information_schema.columns where table_name = 'address';

-- 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. 
-- Use the tables `staff` and `address`:

SELECT staff.first_name, staff.last_name, address.address
FROM staff
INNER JOIN address ON staff.address_id=address.address_id;

--  6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005.
--  Use tables `staff` and `payment`.
use sakila;
SELECT staff.first_name, staff.last_name, sum(payment.amount)
FROM staff
INNER JOIN payment ON staff.staff_id=payment.staff_id
where payment.payment_date BETWEEN '2005-08-01' AND '2005-08-31'
group by staff.first_name, staff.last_name
; 

--  6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
Select film.title, count(film_actor.actor_id)
from film
inner join film_actor on film.film_id = film_actor.film_id
group by film.title;

--  6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
select film.title, count(inventory.inventory_id)
from film
inner join inventory on film.film_id=inventory.film_id
where film.title = 'Hunchback Impossible';

--  6e. Using the tables `payment` and `customer` and the `JOIN` command, 
-- list the total paid by each customer. List the customers alphabetically by last name:
use sakila;
select customer.first_name, customer.last_name, sum(payment.amount)
from customer
join payment on customer.customer_id = payment.customer_id
group by customer.first_name, customer.last_name
order by customer.last_name ASC;


--  7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
-- As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.
use sakila; 
select film.title
from film
join language on film.language_id = language.language_id
where film.title like 'K%' OR film.title like 'Q%' and language.name = 'English';


-- 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
use sakila;
select actor.first_name, actor.last_name, film.title -- try and change actor.first_name etc to just actor.ActorName
from ((film_actor
inner join actor on film_actor.actor_id = actor.actor_id
inner join film on film_actor.film_id=film.film_id))
where film.title = 'Alone Trip'
;


--  7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers.
--  Use joins to retrieve this information.

-- want to join on country, address, city, customer 
use sakila;
select country.country
from country
where country.country = 'Canada'
((select customer.first_name, customer.last_name, customer.email
from address
inner join customer on address.= country.country_id
inner join city on city.city_id=address.city_id))
;


--  7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as _family_ films.

-- film, category, film_cateogry 
use sakila;
select film.title, category.name
from ((film_category
inner join film on film_category.film_id = film.film_id
inner join category on film_category.category_id=category.category_id))
where category.name = 'Family'
;

-- 7e. Display the most frequently rented movies in descending order.



--  7f. Write a query to display how much business, in dollars, each store brought in.

--  7g. Write a query to display for each store its store ID, city, and country.

--  7h. List the top five genres in gross revenue in descending order. 
-- (**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)

--  8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

-- 8b. How would you display the view that you created in 8a?

-- 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
