import json
from graphic import _Tree_Costructor, _Graphs_Constructor

class Structure:
    STRUCTURE_PATH: str = 'structure/structure.json'
    STRUCTURE = {
        
    }

    def update():
        with open(Structure.STRUCTURE_PATH, 'w') as structure_json:
            json.dump(Structure.STRUCTURE, structure_json)

            structure_json.close()


class Tree:
    def __init__(self, )  -> None:
        self._graphic_constructor = _Tree_Costructor()
        self.branch_id = 0
        self.element_id = 0

    def create_branch(self, tag: str, description: str, url: str) -> int:
        # self.tag: str = tag
        # self.description = description
        # self.url = url

        Structure.STRUCTURE[self.branch_id] = {'tag': tag, 'description': description, 'url': url, 'content': {}}

        self.branch_id += 1
        return self.branch_id - 1

    def add_element(self, branch_id: int, tag: str, description: str, url: str, type: str, links_from: list, links_to: list):
        if branch_id in Structure.STRUCTURE.keys():
            Structure.STRUCTURE[branch_id]['content'][self.element_id] = {'tag': tag, 'description': description, 'url': url, 'type': type, 'links_from': links_from, 'links_to': links_to}

            self.element_id += 1

        else:
            return Exception

    def build(self, ):
        Structure.update()
        self._graphic_constructor.build_html(Structure.STRUCTURE)
