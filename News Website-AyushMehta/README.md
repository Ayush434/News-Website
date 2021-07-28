# NEWSITA
#### Video Demo: https://www.youtube.com/watch?v=Mhn1bcR2a8k
#### Description:
My website is called Newsita. The main purpose of this website is to provide users with the news.
The users have the option to subscribe to my channel but if they choose not to, they can simply go on the website and still be able to see
the news. If they do subscribe to my channel, they will recieve an automatic welcome email from my website. I also wanted to
add the functionality of giving daily news update but i wasn't able to figure it out.

The website have a nav bar which consists of 3 buttons which are Home, Subscribe and Login/Logout. The rest of the website simply
provides the new's title, brief description, published date and a button which takes them to the full news.

The tools/languages used to this website are:
-Flask framework
-Python
-Javascript
-SQLite
-HTML
-CSS
-Bootstrap

#### Design Choices:
The design that i used to build my web application is eye catching. I made separate blocks for each news which consists of 3 details
about the news and a link to the original resource. I used the bootstrap to produce the blocks and if you look into each block,
you will see another block for a title. Bootstrap really heloped me to get those nice blocks and colors for the text. Bootstrap is
also really great for the nav bar because i was able to make my nav bar dynamic by making buttons highlighted when hovered over.
I used the CSS a little like for the purple background, adjusting the text font, positioning the blocks and margins, and many other small
things. This was my first time designing the website from scrath and it was hard but once you get hand of it, you can imagine a picture
of the website and just build it.

#### Information about the files:
The main file of the project is called application.py, which has all the functions that helps to run the website.
The first function is called index which grabs all the news articles using another function called news_articles().
The news can be displayed by using the feed.enteries which helps you access the different enteries like description, published date
or link. Once all the news are grabbed from the RSS feed successfully, the function returns it to the index.html which simply
displays all the news on the home page of the website.

Third function is called subscribe() which basically validates the users credentials. To validate the user's credentials

Once it is validated, it will insert
the credentials into the database. Then it will use their email to send the welcome email to that user.

Next function is called send_mail() which is called in the subscribe() which basically grabs the user's email and sends them
the welcome email.

Then comes the Login() which validates the user's credentials by checking in the database. Once it is validated the user will be
loged in. But now the nav bar will only show two options, one is Home and other is Logout.

The last function is called logout which simply logs the current user out.
