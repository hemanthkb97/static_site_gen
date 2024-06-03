


class HTMLNode:
    def __init__(self,tag: str=None,value: str=None,children: list['HTMLNode'] = None,props: dict =None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props
        pass

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props==None:
            return ''
        string=''
        for key,value in self.props.items():
            string= string +"{0}=\"{1}\"".format(key,value)
        return string

    def __repr__(self):
        return "HTMLNode({0}, {1}, {2}, {3})".format(self.tag,self.value,self.children,self.props)