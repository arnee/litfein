litera
======

django site for a local independent bookstore

# General idea
The site is for a local independent bookstore that wants to build up an online strategy that intergrates the benefits and advantages of local versus online retail.

## CMS
The site itself consists of a number of pages in a rather flat hierachy. An editor should be able to select one of two templates to create a new pages. On this page the editor can upload picture or write some text.
* [One column](https://github.com/arnee/litera/blob/master/templates/page_1_column.html)
* [Two columns](https://github.com/arnee/litera/blob/master/templates/page_2_columns.html)

## Blog
The blog is rather simple. Each entry consists of a number or pictures or none and some text. There are a number of categories that an editor can create and edit. An entry can have none, one or multiple categories. There are no comments, no workflow or such functions of a more sophisticated blog system.
The blog itself should be intergrated in the navigation, like domain.org/blog. Further url designs should be "bloglike" e.g. /blog/entry-title-abc
* [Blog](https://github.com/arnee/litera/blob/master/templates/blog.html)

## Forms
There are two or three forms for registering for a newsletter and similar things. The forms can be hardcoded, no editor needed. When the form is submitted after a validation, the data should be stored in the backend so that it is readable and editable in the django admin, and sent via email to the store at a hardcoded address (maybe in the settings) and the person that submitted it.
* [Sample form](https://github.com/arnee/litera/blob/master/templates/order.html)

### Fields for the newsletter form
* email (required, type=email)
* Name (optional, type=String)

### Fields for the book list form
* email (required, type=email)
* Name (optional, type=String)
* Telephone (optional, type=String)

### Fields for the order form
* email (required, type=email)
* Free text (required, type=Text multiple lines)
* Telephone (required, type=String)
* Name (optional, type=String)

