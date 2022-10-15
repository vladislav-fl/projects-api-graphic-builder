from builder import Tree

display = Tree()

# Добавить настройки (типо display.settings), где можно будет вводить тип изображения (дерево, графы) и так далее
# хотя может не надо, так как у меня отдельный класс Tree только под дерево (короче подумать)!!!

# сделать так чтобы были свои независимые настройки у каждого дерева 
# (то есть у каждого свой x y длина ширина и так далее), чтобы можно было удобно 
# к ним обращаться и в любой последовательности добавлять элементы к разным деревам 
# (нужна ли разная последовательность?)

branch_id = display.create_branch('main domen', 'site for texting', 'https://site.com')
display.add_element(
    branch_id=branch_id,
    tag='main',
    description='main page of site',
    url='https://site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)
display.add_element(
    branch_id=branch_id,
    tag='help',
    description='help page of site',
    url='https://site.com/help',
    type='GET',
    links_from=['main'],
    links_to=[]
)

# Вместо display.add_element использовать branch.add_element

branch_id = display.create_branch('secondary domen', 'site for texting', 'https://site.com')
display.add_element(
    branch_id=branch_id,
    tag='main',
    description='main page of site',
    url='https://second.site.com/',
    type='GET',
    links_from=[],
    links_to=[]
)

display.add_element(
    branch_id=branch_id,
    tag='help',
    description='help page of site',
    url='https://second.site.com/help',
    type='GET',
    links_from=[],
    links_to=[]
)

display.add_element(
    branch_id=branch_id,
    tag='help',
    description='help page of site with POST',
    url='https://second.site.com/help',
    type='POST',
    links_from=[],
    links_to=[]
)

display.add_element(
    branch_id=branch_id,
    tag='blog',
    description='blog page',
    url='https://second.site.com/blog',
    type='GET',
    links_from=[],
    links_to=[]
)

display.build()
