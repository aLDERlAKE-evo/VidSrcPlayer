# **VidSrcPlayer**

[VidSrc](https://vidsrc.to/) is a publically available API which provides you with links to watch your desired shows. 

The process involves gathering the ID of the show you wish to see either from [IMDb](https://www.imdb.com/) or from [TMDB](https://www.themoviedb.org/),
After which you attach the ID to the end of the base url depending on whether its a Tv-Show or a Movie along with some optional parameters,
The concatenated link when entered as a URL in a browser, Plays the requested media in an online player but it has some "Forced redirect ads" for which you will need
an Ab Blocker such as the [Ublock Origin](https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) which i use personally, But any other 
Good Ad blockware should work aswell.

### <ins> Work Flow </ins>
This code allows you to skip all that hassle, and directly get the final link by just using a Command Line Interface.
You just enter the name of your show, it should show you a list of shows which involves the said name from where you select the option you were looking for (Hopefully its there ＞﹏＜).
From there you just enter its serial number and it will automatically open the link in you default browser.

### <ins> Forseable Updates </ins>  
The Second version primarily looks upto the addition of:  
* Fuzzy Search results.  
* A more intuitive GUI.  
* Faster List loading.  
