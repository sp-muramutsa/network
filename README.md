PROJECT OVERVIEW
This project implements a social network using Python, JavaScript, HTML, and CSS. The application allows users to make posts, follow other users, and “like” posts. 


IMPLEMENTATION DETAILS
1. The project utilizes Python's Django Framework for the backend logic and database management.
2. JavaScript is used for asynchronous operations and dynamic content updates without page reloads.
3. HTML and CSS are used for structuring and styling the web pages.
4. Pagination is implemented to manage the display of posts in batches of 10, with navigation controls for accessing different pages.

   
FEATURES
1. New Post
- Users who are signed in can write and submit a new text-based post.


2. All posts
- Accessible via the "All Posts" link in the navigation bar:
- Displays all posts from all users, ordered by the most recent first.
- ach post includes the username of the poster, the post content, the date and time of posting, and the number of “likes”.

3. Profile Page
- Clicking on a username loads that user’s profile page.
- Displays the number of followers and following counts.
- Shows all posts by the user in reverse chronological order.
- Includes a “Follow” or “Unfollow” button for the current user to toggle following status (except for their own profile).

4. Following
- Accessible via the "Following" link in the navigation bar.
- Displays posts made by users that the current user follows.
- Behaves like the “All Posts” page but with a filtered set of posts.
- Only available to signed-in users.

5. Pagination
- Posts are displayed 10 per page on any page that displays posts.
- Includes “Next” and “Previous” buttons for navigation between pages of posts.

6. Edit Post
- Users can click an “Edit” button or link on any of their own posts to edit the content.
- The post content is replaced with a textarea for editing.
- Users can save the edited post without reloading the entire page, using JavaScript.
- The application ensures users cannot edit other users’ posts for security.

7. “Like” and “Unlike”
- Users can toggle the “like” status on any post.
- The server is updated asynchronously using JavaScript (via fetch calls), and the like count is updated on the page without reloading.
