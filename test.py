from requests import post

print(post('http://localhost:5000/api/jobs',
           json={'job': 'Заголовок',
                 'work_size': '11',
                 'collaborators': "1, 2",
                 'is_finished': False}).json())