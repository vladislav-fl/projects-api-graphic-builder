class Logic:
    HTML_LOGIC: dict = {
        'TAG_DOCTYPE': '<!DOCTYPE html>',
        'TAG_OPEN_HTML': '<html>',
        'TAG_OPEN_HEAD': '<head>',
        'TAG_META': '<meta charset="utf-8" />',
        'TAG_OPEN_STYLE': '<style>',
        
        'PUT_STYLE': '*{position: absolute} .block:hover{cursor: pointer} ',

        'TAG_CLOSE_STYLE': '</style>',
        'TAG_CLOSE_HEAD': '</head>',
        'TAG_OPEN_BODY': '<body><script src="scripts/onclick_block.js"></script>',
        
        'PUT_API': [],
        'TAG_CLOSE_BODY': '</body>',
        'TAG_CLOSE_HTML': '</html>'
    }

html_logic: list = [
    Logic.HTML_LOGIC["TAG_DOCTYPE"],
    Logic.HTML_LOGIC["TAG_OPEN_HTML"],
    Logic.HTML_LOGIC["TAG_OPEN_HEAD"],
    Logic.HTML_LOGIC["TAG_META"],
    Logic.HTML_LOGIC["TAG_OPEN_STYLE"],
    Logic.HTML_LOGIC["PUT_STYLE"],
    Logic.HTML_LOGIC["TAG_CLOSE_STYLE"],
    Logic.HTML_LOGIC["TAG_CLOSE_HEAD"],
    Logic.HTML_LOGIC["TAG_OPEN_BODY"],
    Logic.HTML_LOGIC["PUT_API"],
    Logic.HTML_LOGIC["TAG_CLOSE_BODY"],
    Logic.HTML_LOGIC["TAG_CLOSE_HTML"],
]

class _Settings:
    class _Block:
        WIDTH = 50
        HEIGHT = 50

        START_X = 100
        START_Y = 100

        X = START_X
        Y = START_Y

        GAP_BETWEEN_BLOCKS_X = 150
        GAP_BETWEEN_BLOCKS_X += WIDTH

        GAP_BETWEEN_BLOCKS_Y = 50
        GAP_BETWEEN_BLOCKS_Y += HEIGHT

        BORDER_COLOR = 'black'
        BORDER_STYLE = 'solid'
        BORDER_WIDTH = '1px'

        # BACKGROUND_COLOR = 'white'

        TAG = ''
        DESCRIPTION = ''

        TYPE = ''
        URL = ''

    class _Branch:
        WIDTH = 150
        HEIGHT = 500

        START_X = 50
        START_Y = 50

        X = START_X
        Y = START_Y

        GAP_BETWEEN_BRANCHES_X = 50
        GAP_BETWEEN_BRANCHES_X += WIDTH

        BORDER_COLOR = 'black'
        BORDER_STYLE = 'solid'
        BORDER_WIDTH = '1px'

        # BACKGROUND_COLOR = 'white'

        TAG = ''
        DESCRIPTION = ''


class _Basic_Constructor:
    def __init__(self) -> None:
        _Settings._Block.Y = _Settings._Block.START_X
        _Settings._Block.X = _Settings._Block.START_Y
        _Settings._Block.TAG = ''

        self.html: str = ''


class _Tree_Costructor(_Basic_Constructor):
    def __init__(self) -> None:
        super().__init__()

    class _Objects:
        def __init__(self, ) -> None:
            self.BLOCK = f"<div onclick='show_info(this)' id='Description: {_Settings._Block.DESCRIPTION}\nType: {_Settings._Block.TYPE}\nURL: {_Settings._Block.URL}' class='block' style='left: {_Settings._Block.X}px; top: {_Settings._Block.Y}px; border: {_Settings._Block.BORDER_WIDTH} {_Settings._Block.BORDER_COLOR} {_Settings._Block.BORDER_STYLE}; width: {_Settings._Block.WIDTH}px; height: {_Settings._Block.HEIGHT}px;'>{_Settings._Block.TAG}</div>"
            self.BRANCH = f"<div id='{_Settings._Branch.DESCRIPTION}' class='branch' style='left: {_Settings._Branch.X}px; top: {_Settings._Branch.Y}px; border: {_Settings._Branch.BORDER_WIDTH} {_Settings._Branch.BORDER_COLOR} {_Settings._Branch.BORDER_STYLE}; width: {_Settings._Branch.WIDTH}px; height: {_Settings._Branch.HEIGHT}px;'>{_Settings._Branch.TAG}</div>"

    def build_html(self, structure: dict):
        for branch in structure.keys():
            _Settings._Branch.TAG = structure[branch]['tag']
            _Settings._Branch.DESCRIPTION = structure[branch]['description']

            html_logic[9].append(self._Objects().BRANCH)

            for block in structure[branch]['content']:
                _Settings._Block.TAG = structure[branch]['content'][block]['tag']
                _Settings._Block.DESCRIPTION = structure[branch]['content'][block]['description']
                _Settings._Block.TYPE = structure[branch]['content'][block]['type']
                _Settings._Block.URL = structure[branch]['content'][block]['url']

                html_logic[9].append(self._Objects().BLOCK)

                _Settings._Block.Y += _Settings._Block.GAP_BETWEEN_BLOCKS_Y

            _Settings._Branch.X += _Settings._Branch.GAP_BETWEEN_BRANCHES_X

            _Settings._Block.X += _Settings._Block.GAP_BETWEEN_BLOCKS_X
            _Settings._Block.Y = _Settings._Block.START_Y

        element_i: int = 0
        for element in html_logic:
            if element_i == 9:
                for elem_element in element:
                    self.html += elem_element
            else:
                self.html += element

            element_i += 1

        with open('doc.html', 'w') as html_file:
            html_file.write(self.html)


class _Graphs_Constructor(_Basic_Constructor):
    def __init__(self) -> None:
        super().__init__()
