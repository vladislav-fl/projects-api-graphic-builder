from builder import Tree

display = Tree()

# Добавить настройки (типо display.settings), где можно будет вводить тип изображения (дерево, графы) и так далее
# хотя может не надо, так как у меня отдельный класс Tree только под дерево (короче подумать)!!!

# сделать так чтобы были свои независимые настройки у каждого дерева 
# (то есть у каждого свой x y длина ширина и так далее), чтобы можно было удобно 
# к ним обращаться и в любой последовательности добавлять элементы к разным деревам 
# (нужна ли разная последовательность?)

# Сделать возможность сразу загружать готовый json файлик

# Поменять добавление элемента, чтобы в одной функции можно было добавить несколько типов (GET, POST и так далее) к одному URL

# Обводить один URL с разными типами в еще один div

branch_id = display.create_branch('main domen', 'site for texting', 'https://site.com')
display.add_element(
    branch_id=branch_id,
    tag='main',
    description='Main page of site where you can see all information',
    url='https://site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)
display.add_element(
    branch_id=branch_id,
    tag='main',
    description='Main page of site where you can see all information',
    url='https://site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)
display.add_element(
    branch_id=branch_id,
    tag='main',
    description='Main page of site where you can see all information',
    url='https://site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)
display.add_element(
    branch_id=branch_id,
    tag='mdsfain',
    description='Main page of site where you can see all information',
    url='https://site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)
display.add_element(
    branch_id=branch_id,
    tag='mdsfain',
    description='Main page of site where you can see all information',
    url='https://site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)
display.add_element(
    branch_id=branch_id,
    tag='mdsfain',
    description='Main page of site where you can see all information',
    url='https://site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)
display.add_element(
    branch_id=branch_id,
    tag='mdsffsdfain',
    description='Main page of site where you can see all information',
    url='https://site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)


branch_id = display.create_branch('second domen', 'second site for texting', 'https://second.site.com')
display.add_element(
    branch_id=branch_id,
    tag='main',
    description='Main page of second site',
    url='https://second.site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)


branch_id = display.create_branch('3 domen', 'second site for texting', 'https://third.site.com')
display.add_element(
    branch_id=branch_id,
    tag='maifsfdsfdfsdfn',
    description='Main page of second site',
    url='https://third.site.com/',
    type='GET',
    links_from=[], # нужно убрать либо links_from, либо links_to
    links_to=[]
)





display.build()
