from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode

t1= LeafNode("p", "This is a paragraph of text.")
t2=LeafNode("a", "Click me!", {"href": "https://www.google.com"})


print(t1.to_html())
print(t2.to_html())