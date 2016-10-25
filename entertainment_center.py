import webbrowser
import fresh_tomatoes
import media

toystory = media.Movie("Toy Story",
                       "A story of a boy whose toys came back to life",
                       "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

skyfall = media.Movie("Skyfall",
                      "Skyfall is the 23rd James Bond film produced by Eon Productions and released in 2012. "
                      "It features Daniel Craig in his third performance as James Bond",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcTSNSk0M1z_CZ1UKTnfE2nHmk4Oxqh_gKO0dAHZHwrfLX6D9Y4s",
                      "https://www.youtube.com/watch?v=6kw1UVovByw")

secretlifeofpets = media.Movie("The Secret Life of Pets",
                               "The quiet life of a terrier named Max is upended when his owner takes in Duke, "
                               "a stray whom Max instantly dislikes.",
                               "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                                "https://www.youtube.com/watch?v=eWI_Jsw9qUs")

inception = media.Movie("Inception",
                        "Inception is a 2010 science fiction heist thriller film written, co-produced, "
                        "and directed by Christopher Nolan, and co-produced by Emma Thomas.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

movies = [toystory,skyfall,secretlifeofpets,inception]
fresh_tomatoes.open_movies_page(movies)