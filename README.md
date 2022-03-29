# e-commerce
eBay-like e-commerce auction site that allows users to:

- Post auction listings
- Place bids on listings
- Comment on those listings
- Add listings to a “watchlist.
# Framework:
Django
# Specification
## Models:
The application has three models in addition to the User model: 
- Listing
- Bid
- Comment

## Create Listing:
- Users are able to visit a page to create a new listing. 
- They are able to specify a title for the listing, a text-based description, and what the starting bid should be. 
- Users also have the option to add an image URL for the listing

## Active Listings Page:
- The default route of the application lets the users view all of the currently active auction listings. 
- For each active listing, the page displays the title, description, current price, photo (if one exists for the listing) and the publisher username.

## Listing Page
Clicking on a listing will take users to a page specific to that listing. On that page, users will be able to view all details about the listing, including the current price for the listing.
- If the user is signed in, the user is able to add the item to their “Watchlist.” If the item is already on the watchlist, the user will be able to remove it.
- If the user is signed in, the user will be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user will be presented with an error.
- If the user is signed in and is the one who created the listing, the user will have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
- Users who are signed in will be able to add comments to the listing page. The listing page will display all comments that have been made on the listing.

## Watchlist: 
Users who are signed in will be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.
## Django Admin Interface: 
Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.

