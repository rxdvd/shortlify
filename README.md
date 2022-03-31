# shortlify

URL shortening website made as part of a paired code challenge.

## Installation & Usage

### Prerequisites

* You must have Python 3.9.1 installed.

### Installation

1. Clone the repo using `git clone git@github.com:rxdvd/shortlify.git`
2. Enter the repo directory `cd shortlify`
3. Create the virtual environment `pipenv --python 3.9.1`
4. Enter the virtual environment `pipenv shell`
5. Install dependencies `pipenv install --dev`

### Usage

* While inside the virtual environment:
  * `pipenv run dev` to start the app in development mode.
    * Available at `localhost:5000`.
  * `pipenv run test` to run tests.
  * `pipenv run coverage` to check test coverage.
* To remove the virtual environment from your system use `pipenv --rm`.

## Design & Implementation

### Technologies

* [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)
* [pytest](https://docs.pytest.org/en/7.1.x/)
* [MongoDB](https://www.mongodb.com/)

### Routes

| Route          | Method | Description |
| -------------- | ------ | ----------- |
| `/`            | `GET`  | Shows homepage where user can submit URLs that they want shortened. |
| `/`            | `POST` | Receives a full URL in the request body and then shows a page where the user can see the shortened URL. |
| `/<string:id>` | `GET`  | Redirects the user to the corresponding URL or the homepage if it doesn't exist. |

## Changelog

* Factored out controller logic into separate file `controllers/urls.py`.
* Created a model for the URLs with a property for the original URL and for the shortened one `models/URL.py`.
* Added validation to make sure the URL submitted is of the right format.
* Changed behaviour for submitting an invalid URL to return to home rather than show an error page.
* Add error message to homepage when redirected back due to an error.

## Bugs/Issues

- [x] Redirect controller recurses infinitely.
- [x] Error pages don't render.
- [x] Error pages don't return the correct status code.
- [x] Can't access database.

## Wins & Challenges

* Ran into a bug where the redirect function in the controller was calling itself repeatedly up to the max recursion depth. It turns out that because the controller function and the imported function from flask had the same name, it was calling itself instead of the redirect method from flask causing it to loop infinitely. This was fixed by renaming the function from `redirect` to `redirect_to`.
* The database could not be connected to at first because the network access wasn't configured properly on Mongo Atlas. Also, trying to query a collection that didn't yet exist resulted in the `pymongo` client freezing.
* Managed to implement a MVC design pattern in Python for the first time without running into any problems.
