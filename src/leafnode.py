from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self,tag: str=None,value: str=None,props: dict =None):
        super().__init__(tag,value,None,props)
        pass

    def to_html(self):
        if(self.value==None):
            raise ValueError
        if(self.tag==None):
            return self.value
        props=''
        if(self.props!=None):
            props= " " + self.props_to_html()
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        