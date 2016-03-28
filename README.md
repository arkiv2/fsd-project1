# fsd-project1
Udacity FSD(Full Stack Developer Nanodegree) Course Requirement 

This project is a python application that renders an html output from a given movie list via their IMDB IDs.


### Version
1.0.3

### Tech

This project uses a number of open source projects to work properly:

* [OMDBAPI] - The OMDb API is a free web service to obtain movie information, all content and images on the site are contributed and maintained by our users.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [jQuery]

### Installation

```sh
$ git clone https://github.com/arkiv2/fsd-project1.git fsd-project1
$ cd fsd-project1
$ python main.py
```

### Usage
1. Edit main.py file

### Syntax
```sh
<movie_name> = Movie(<movie_list>, getIMDBInfo("<movie_imdb_id"),
                           "<movie_youtube_trailer_url>")
```

### Example
```sh
dead_pool = Movie(movies, getIMDBInfo("tt1431045"),
                          "https://www.youtube.com/watch?v=ZIM1HydF9UA")
```



### Plugins

This project is currently extended with the following python plugins

* urllib
* json
* 

And non-python plugins(web API)

* OMDB API https://omdbapi.com => IMDB querying API


Test and Implementation of OMDBapi can be found here:

* https://github.com/arkiv2/fsd-project1/tree/master/test_module/imdb_get.py
* https://github.com/arkiv2/fsd-project1/blob/master/boom_box.py


**Credits**

   [omdbapi]: <https://omdbapi.com>

