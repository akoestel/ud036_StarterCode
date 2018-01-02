import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A story about cool 3D effects",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_martian = media.Movie("The Martian",
                          "A story about a man left alone on Mars",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                          "https://www.youtube.com/watch?v=lQqhfq87FgY")

overwatch = media.Movie("Overwatch: The Movie",
                        "A story about Tracer",
                        "http://gamepreorders.com/wp-content/uploads/2016/03/overwatch-cover.jpg",
                        "https://www.youtube.com/watch?v=MPjt0Yeddj4")

varsity_blues = media.Movie("Varsity Blues",
                            "A story about being a badass",
                            "https://images-na.ssl-images-amazon.com/images/I/514SJHESF0L.jpg",
                            "https://www.youtube.com/watch?v=eSnkWiacUW4")

shawshank = media.Movie("The Shawshank Redemption",
                        "A story about a prison break",
                        "http://cdn3.gbtimes.com/cdn/farfuture/Mi_FbKUe9PiQ9YB26WYTS-RSe9vUEfGBxUeh0rRYXKk/mtime:1417532777/sites/default/files/styles/1280_wide/public/2014/12/02/the-shawshank-redemption.jpg?itok=1RpNyipr",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

movies = [toy_story,avatar,the_martian, overwatch, varsity_blues, shawshank]
fresh_tomatoes.open_movies_page(movies);
