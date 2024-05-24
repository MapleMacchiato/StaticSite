class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
       self.tag = tag
       self.value = value
       self.children = children
       self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html = ""
        for prop in props:
            html += " " + prop + "=" + '"' + props[prop] + '"'
        return html

    def __repr__(self)
        return f"
            HTMLNode, 
            tag={self.tag}, 
            value={self.value}, 
            children={self.children, 
            props=self.props"
