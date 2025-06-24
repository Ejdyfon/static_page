from leafnode import LeafNode
from textnode import TextNode, TextType


print("hello world")

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","",props={"src":text_node.url, "alt": text_node.text})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    temp_text_type = text_type
    nodes_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes_list.append(node)
        else:
            splited = node.text.split(delimiter)
            if len(splited) % 2 == 0:
                raise Exception(f"missing closing tag")
            i = 1
            for split in splited:
                if i % 2 != 0:
                    nodes_list.append(TextNode(split,TextType.TEXT))
                else:
                    nodes_list.append(TextNode(split, temp_text_type))
                i += 1
    
    return nodes_list



def main():
    textnode = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(textnode)

main()