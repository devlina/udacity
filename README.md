# Movie Trailer Website #
This website renders movie trailers. `movie` is a class defined in `media.py`. All movies are `movie` objects.
All movie instances are stored in a list in `entertainment_center.py` which in turn is used by `open_movies_page(movies)`
function defined in fresh_tomatoes.py

### To download the code
```
git clone https://github.com/devlina/udacity/movie_trailor.git
```

### To run the application (to open the website) 
Go to the code repository you have downloaded using above command, and open a python shell. 
Execute following command.
```python
>>>import fresh_tomotoes, entertainment_center.py
>>>fresh_tomatoes.open_movies_page(entertainment_center.movies)
```
