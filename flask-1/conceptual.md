### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript? 
Python is used for more backend and general purpose programming while javascript is used for front end and acting as a middle man between the two.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  key in dict

  try:
    dict['key']
  except:
    return 'missing key'

- What is a unit test?
  a test of an individual function. Similar to a lock in a door

- What is an integration test?
  a test that combines multiple functions or parts together. Similar to opening a door after locking it.

- What is the role of web application framework, like Flask?
  simplifying and interconnecting different tools such as Jinja

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    '/foods/pretzel' would be better if there were multiple pages with a template of '/foods/pretzel' or an entire page dedicated to pretzels. 

    'foods?type=pretzel' would be better for finding information about food and allowing the option/type of pretzel. The type tag can be used for better filtering.

- How do you collect data from a URL placeholder parameter using Flask?
  By placing the parameter in the url in arrows <> and then passing the placeholder into the following function.

- How do you collect data from the query string using Flask?
  by using request.args and placing the return in a local variable

- How do you collect data from the body of the request using Flask?
  request.form['data']
  (not sure if I understand the question)

- What is a cookie and what kinds of things are they commonly used for?
  a dictionary that is kept in the browser that the server uses to relay information. Often times the information is reminded between the two

- What is the session object in Flask?
  a "magical dictionary" that stores the keys we use within the server itself, allowing the information to carry across the website

- What does Flask's `jsonify()` do?
  A function that turns string or lists into valid json
